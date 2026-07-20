#!/usr/bin/env python3
"""
discovery output validator -- envelope conformance, hard-fail.

Usage:
    python3 -m src.validate check --run DIR --slug SLUG
    python3 -m src.validate selftest

Verdict is binary by operator ruling (2026-07-14): ANY violation fails the
run. No tiers, no warnings, no partial credit. Tiering is deferred until
failure classes are understood in practice.

Exit codes:
    0  PASS -- every check clean
    1  FAIL -- one or more violations
    2  ERROR -- could not run (bad args, unreadable dir)

This validates SHAPE, not TRUTH. See src/rules.py docstring.
"""

import argparse
import csv
import re
import sys
from pathlib import Path

try:
    from src import rules
except ImportError:
    import rules


VALIDATOR_VERSION = "envelope-0"


class Report:
    """Collects violations. Any violation = fail."""

    def __init__(self):
        self.violations = []
        self.checks_run = 0

    def check(self, condition, code, detail):
        """Record a check. condition True = clean."""
        self.checks_run += 1
        if not condition:
            self.violations.append((code, detail))
        return condition

    def fail(self, code, detail):
        self.checks_run += 1
        self.violations.append((code, detail))

    @property
    def passed(self):
        return not self.violations


# --- helpers ---------------------------------------------------------

TAG_RE = re.compile(r"\[([^\]]+)\]")


def read_lines(path):
    return path.read_text(encoding="utf-8").splitlines()


def find_tags(line):
    """All bracketed tokens on a line."""
    return TAG_RE.findall(line)


def normalize_tag(token):
    """Reduce a bracketed token to its base tag, or None if it isn't one.

    Fix 2026-07-14 (first real run): tags may carry an inline qualifier.
    `[mechanical: 21 matches]` is the SAME tag as `[mechanical]` -- the
    prompt requires a method clause and never says where it must live.
    Returns the base tag name, or None if the token is not a tag at all
    (e.g. `[fig:3.1]`, `[p:89]`).
    """
    t = token.strip()

    # Whole-match first: `model-knowledge, unverified` owns its comma.
    if t in rules.ALL_ACCEPTED_TAGS:
        return t

    # A compound tag keeps its first component: `[mechanical + inferred-confirmed]`
    for sep in rules.TAG_QUALIFIER_SEPARATORS:
        if sep in t:
            head = t.split(sep, 1)[0].strip()
            if head in rules.ALL_ACCEPTED_TAGS:
                return head
            # `[model-knowledge, unverified -> registry queue]`
            for legal in rules.ALL_ACCEPTED_TAGS:
                if t.startswith(legal):
                    return legal
    return None


def tag_has_method(line, token):
    """A [mechanical] tag needs its method INSIDE the bracket.

    REBUILD 2026-07-19 (v2.8): v2.5 allowed the method to live in the line's
    prose; v2.8 forbids it -- "A bare [mechanical], or one with the method in
    the line's prose, ... is a defect: method AND grade must be machine-
    extractable from the tag, not recoverable by reading the sentence"
    (discovery_prompt_v2_8.md, Provenance tags). This is why the old prose-
    fallback let TAG_MECHANICAL_NO_METHOD pass: every convention line has prose
    before its tag, so the fallback was always satisfied.

    This function enforces only that SOMETHING rides inside the bracket after
    `mechanical` (method presence). The `<method>; <grade>` grade grammar and
    the grade vocabulary are enforced separately by tag_grade() and wired into
    check_provenance_tags after this check, so a method-less tag raises
    exactly TAG_MECHANICAL_NO_METHOD (the specificity contract).
    """
    # token is the raw bracket body, e.g. "mechanical: 21 matches; sampled".
    # A method is present iff there is a qualifier separator with non-empty
    # content after it.
    for sep in (":", ",", "+"):
        if sep in token:
            after = token.split(sep, 1)[1].strip()
            if after:
                return True
    return False


def tag_grade(token):
    """The strength grade of a [mechanical] tag, or None if absent/illegal.

    v2.8 (graded-tag lint, chunk 2): a [mechanical: <method>; <grade>] tag
    must end in a legal strength grade -- "method AND grade must be machine-
    extractable from the tag" (discovery_prompt_v2_8.md, Provenance tags).

    The grade is the LAST ';'-delimited clause inside the bracket. The
    method clause may itself contain ':' and ',' (e.g.
    "[mechanical: Class: = Function: = 172, exact; exhaustive]"), so the
    grade is split on ';' from the RIGHT, never on ':' or ','.

    Returns the grade string if it is one of rules.LEGAL_GRADES; otherwise
    None (covers both no-grade and illegal-grade-word -- option-1 scope).
    """
    if rules.MECHANICAL_GRADE_SEPARATOR not in token:
        return None
    candidate = token.rsplit(rules.MECHANICAL_GRADE_SEPARATOR, 1)[1].strip()
    return candidate if candidate in rules.LEGAL_GRADES else None


def parse_est_size(cell):
    """(value:int, unit:str) from an est_size cell like '1180 lines'.

    Returns (None, None) if the cell has no leading integer. The unit is
    everything after the number, stripped -- used to detect a mixed-unit
    plan, which makes the deferral comparison meaningless.
    """
    m = re.match(r"\s*(\d+)\s*(.*)$", cell or "")
    if not m:
        return (None, None)
    return (int(m.group(1)), m.group(2).strip())


def read_loc_grammar(master_path):
    """The declared loc-grammar string from the registration line, or None.

    v2.8: the run proves its own loc-grammar and states it as the final field
    of the registration line (`... | loc-grammar: <grammar>`). Coverage
    arithmetic reads the page component UNDER that declared grammar rather
    than assuming a fixed shape (F1, Session C chunk 3). Returns the grammar
    text after the prefix, or None if there is no parseable registration line.
    """
    if not master_path.exists():
        return None
    lines = [ln for ln in read_lines(master_path) if ln.strip()]
    if not lines:
        return None
    last = lines[-1].strip()
    if not last.startswith("- "):
        return None
    parts = [p.strip() for p in last[2:].split("|")]
    if not parts:
        return None
    final = parts[-1]
    if not final.startswith(rules.REGISTRATION_GRAMMAR_PREFIX):
        return None
    return final[len(rules.REGISTRATION_GRAMMAR_PREFIX):].strip()


def grammar_is_page_resolvable(grammar):
    """True if the declared grammar names a page unit we can extract from.

    Applied by the coverage lint before it trusts loc_page() output: a
    page-based grammar (page.line, `page N + §N.M`, `p<N>`) resolves to an
    integer page; anything else is reported uncertifiable, never guessed.
    """
    if not grammar:
        return False
    low = grammar.lower()
    return any(m in low for m in rules.PAGE_GRAMMAR_MARKERS)


def loc_page(cell):
    """The integer page component of a location under a page-based grammar.

    F1 (Session C chunk 3): the loc-grammar is per-source and proven, not a
    fixed `page.line`. The page is the first run of digits in the locator,
    whether written `173.4` (page.line), `p173` / `p2` (pN), or `173`. An
    optional leading `p` is tolerated. Locators with no digits return None --
    the coverage arithmetic reports them rather than guessing.
    """
    m = re.match(rules.LOC_PAGE_RE, cell or "")
    return int(m.group(1)) if m else None


def read_container_class(master_path):
    """The declared container class ('born_digital'|'scan_ocr'), or None.

    v2.8: the class is stated in the ingest read-back, known at Ingest before
    any convention is written. Read from the run's own statement, never
    inferred from file contents.

    F2 (Session C chunk 3): envelope-0 matched only the exact fixture string
    `container:` (lowercase, colon) inside ## Conventions. Both real piles
    DECLARE the class plainly but in forms that string missed -- rappers
    "Container `born_digital`" (capitalized, backtick, no colon) in its
    ## Ingest read-back, Loeliger "container `scan_ocr`" likewise. The reader
    now scans the whole master doc case-insensitively for the word
    "container" followed, within a short window, by a legal class token
    (tolerating a colon, a space, or a backtick between them). The HALT-on-
    absent behavior is unchanged: a class genuinely nowhere stated still
    returns None and raises CONTAINER_CLASS_MISSING. Only the reader widened;
    the refusal-to-guess discipline (v2.6 lesson) holds.
    """
    if not master_path.exists():
        return None
    text = master_path.read_text(encoding="utf-8")
    low = text.lower()
    for m in re.finditer(r"container", low):
        window = low[m.end():m.end() + 40]
        for cls in rules.CONTAINER_BOUNDS:
            if re.search(rf"[:`\s]+{re.escape(cls)}\b", window):
                return cls
    return None


def line_has_universal(line):
    """True if the convention line asserts a universal quantifier.

    v2.8 / rappers-handbook audit: a universal claim ("always", "every",
    "never", "invariant", "fixed frame") backed only by a `partial` count is
    a defect -- the count did not settle the universal (the census counted
    headings; the exceptions lived in its own range). Matched case-
    insensitively as whole words; the phrase "fixed frame" as a substring.
    """
    low = line.lower()
    for q in rules.UNIVERSAL_QUANTIFIERS:
        if " " in q:
            if q in low:
                return True
        else:
            if re.search(rf"\b{re.escape(q)}\b", low):
                return True
    return False


def is_convention_line(line):
    """A convention line is a TOP-LEVEL bulleted line in the Conventions section.

    The prompt says every convention line carries exactly one tag and a bare
    line is a defect. Non-bullet prose (headers, blanks, axis titles) is not
    a convention line.

    Fix 2026-07-14 (first real run): envelope-0 counted EVERY bullet at any
    indent. Indented sub-bullets are continuations of the convention above
    them -- they elaborate a line that already carries its own tag, and
    re-tagging each one would be noise the prompt never asks for. On the
    Loeliger run this over-counted by 13 (75 -> 62) and produced 13 false
    TAG_BARE hits. An indented bullet is scoped to its parent.
    """
    if line.startswith((" ", "\t")):
        return False
    stripped = line.strip()
    return stripped.startswith("- ") and len(stripped) > 2


def section_bounds(lines, section_name):
    """Return (start, end) line indices for a '## <name>' section body."""
    start = None
    for i, line in enumerate(lines):
        if line.strip() == f"## {section_name}":
            start = i + 1
            break
    if start is None:
        return None
    for j in range(start, len(lines)):
        if lines[j].startswith("## "):
            return (start, j)
    return (start, len(lines))


# --- checks ----------------------------------------------------------

def check_file_family(run_dir, slug, rep):
    """Every file in the family present; sidecar manifest matches."""
    master = run_dir / rules.MASTER_DOC.format(slug=slug)
    rep.check(master.exists(), "FAMILY_MASTER_MISSING",
              f"{master.name} not found")

    for pattern in rules.SIDECARS:
        name = pattern.format(slug=slug)
        rep.check((run_dir / name).exists(), "FAMILY_SIDECAR_MISSING",
                  f"{name} not found")


def check_master_sections(master_path, rep):
    """Nine named sections, in order."""
    if not master_path.exists():
        return
    lines = read_lines(master_path)
    found = [ln.strip()[3:].strip() for ln in lines if ln.startswith("## ")]

    for name in rules.MASTER_SECTIONS:
        rep.check(name in found, "SECTION_MISSING",
                  f"master doc has no '## {name}'")

    # order
    present = [n for n in found if n in rules.MASTER_SECTIONS]
    expected = [n for n in rules.MASTER_SECTIONS if n in found]
    rep.check(present == expected, "SECTION_ORDER",
              f"sections out of order: {present} != {expected}")


def check_status_line(master_path, rep):
    if not master_path.exists():
        return
    lines = read_lines(master_path)
    has = any(ln.startswith(rules.STATUS_PREFIX) for ln in lines[:5])
    rep.check(has, "STATUS_LINE_MISSING",
              f"no line starting '{rules.STATUS_PREFIX}' in first 5 lines")


def check_provenance_tags(master_path, rep):
    """P-3: every convention line carries exactly one legal tag."""
    if not master_path.exists():
        return
    lines = read_lines(master_path)
    bounds = section_bounds(lines, "Conventions")
    if bounds is None:
        return
    start, end = bounds

    # A bracketed token is a CITATION (not a tag, not illegal) if it looks
    # like [p:89], [fig:3.1], [ch2], etc. Citations ride alongside tags
    # legally and, on their own, do not make a line tagged.
    def is_citation(tok):
        return tok.startswith(("fig:", "p:", "ch")) or bool(re.match(r"^\d", tok))

    for i in range(start, end):
        line = lines[i]
        if not is_convention_line(line):
            continue
        all_bracketed = find_tags(line)

        # (a) no brackets at all -> genuinely bare.
        if not all_bracketed:
            rep.fail("TAG_BARE",
                     f"line {i+1}: convention line carries no tag")
            continue

        # Map each bracketed token to a base tag (None = not a tag).
        resolved = [(tok, normalize_tag(tok)) for tok in all_bracketed]
        tag_tokens = [(tok, base) for tok, base in resolved if base]

        # No legal provenance tag on the line. Decide between ILLEGAL and BARE
        # -- REBUILD 2026-07-19: these are now MUTUALLY EXCLUSIVE. A line with
        # an illegal tag token is NOT bare (it has a tag attempt); a line whose
        # only brackets are citations IS bare (a citation is not a tag). The
        # old code fired both, failing the selftest's specificity assertion.
        if not tag_tokens:
            illegal = [tok for tok, _ in resolved if not is_citation(tok)]
            if illegal:
                # (b) at least one non-citation bracket that isn't a legal tag.
                for tok in illegal:
                    rep.fail("TAG_ILLEGAL",
                             f"line {i+1}: '[{tok}]' is not a legal "
                             f"provenance tag")
            else:
                # (c) only citations, no tag -> bare.
                rep.fail("TAG_BARE",
                         f"line {i+1}: convention line carries no "
                         f"provenance tag (only citations)")
            continue

        if len(tag_tokens) > 1:
            rep.fail("TAG_MULTIPLE",
                     f"line {i+1}: {len(tag_tokens)} provenance tags, expected 1")

        # [mechanical] requires its method inside the bracket (v2.8).
        for tok, base in tag_tokens:
            if base == "mechanical" and not tag_has_method(line, tok):
                rep.fail("TAG_MECHANICAL_NO_METHOD",
                         f"line {i+1}: [mechanical] without method clause "
                         f"inside the bracket")
                continue
            # ...and a legal strength grade as its final ';' clause (v2.8).
            # Only checked when the method is present, so a bare/method-less
            # tag raises exactly TAG_MECHANICAL_NO_METHOD, not both (the
            # selftest's one-code-per-fixture specificity contract).
            if base == "mechanical" and tag_grade(tok) is None:
                rep.fail("TAG_NO_GRADE",
                         f"line {i+1}: [mechanical] tag has no legal strength "
                         f"grade (expected final ';' clause in "
                         f"{sorted(rules.LEGAL_GRADES)})")
                continue
            # A partial-graded universal is a defect (rappers-handbook class):
            # the count did not settle the universal. Only reached when the
            # grade is legal, so this never co-fires with TAG_NO_GRADE.
            if (base == "mechanical" and tag_grade(tok) == "partial"
                    and line_has_universal(line)):
                rep.fail("TAG_PARTIAL_UNIVERSAL",
                         f"line {i+1}: universal claim carries a 'partial' "
                         f"grade -- downgrade to 'usually/most' or carry the "
                         f"exception")


def check_forecast_quarantine(run_dir, slug, rep):
    """P-2: [discovery-forecast] appears ONLY in master doc + arbitration seed.

    Critical, silent class. A leaked forecast reaches a worker that treats a
    prediction as a fact about the source.
    """
    permitted = {p.format(slug=slug) for p in rules.FORECAST_PERMITTED_FILES}
    marker = f"[{rules.FORECAST_TAG}]"

    for path in sorted(run_dir.iterdir()):
        if not path.is_file():
            continue
        if path.name in permitted:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if marker in text:
            hits = [i + 1 for i, ln in enumerate(text.splitlines())
                    if marker in ln]
            rep.fail("FORECAST_LEAK",
                     f"{path.name}: {marker} at line(s) {hits} "
                     f"-- forecast permitted only in {sorted(permitted)}")


def check_brief_bounds(run_dir, slug, rep):
    """Brief <=25 lines. Lintable by wc -l, per the prompt."""
    path = run_dir / f"harvest_brief_{slug}.md"
    if not path.exists():
        return
    n = len(read_lines(path))
    rep.check(n <= rules.BRIEF_MAX_LINES, "BRIEF_TOO_LONG",
              f"harvest_brief: {n} lines > {rules.BRIEF_MAX_LINES}")


def check_watchlist_bound(master_path, rep):
    """Ambiguity forecast watchlist <=20 rows."""
    if not master_path.exists():
        return
    lines = read_lines(master_path)
    bounds = section_bounds(lines, "Ambiguity forecast")
    if bounds is None:
        return
    start, end = bounds
    rows = [ln for ln in lines[start:end] if is_convention_line(ln)]
    rep.check(len(rows) <= rules.WATCHLIST_MAX_ROWS, "WATCHLIST_TOO_LONG",
              f"watchlist: {len(rows)} rows > {rules.WATCHLIST_MAX_ROWS}")


def check_master_bounds(master_path, rep):
    """Master doc <=300 lines total; convention lines <= the CONTAINER-KEYED
    bound (born_digital <=50, scan_ocr <=75), read from the run's ingest
    read-back. Lint 5 (Session C chunk 2): the bound is no longer a hardcoded
    default -- it is keyed to the declared container class."""
    if not master_path.exists():
        return
    lines = read_lines(master_path)
    rep.check(len(lines) <= rules.MASTER_MAX_TOTAL_LINES, "MASTER_TOO_LONG",
              f"master doc: {len(lines)} lines > {rules.MASTER_MAX_TOTAL_LINES}")

    bounds = section_bounds(lines, "Conventions")
    if not bounds:
        return
    start, end = bounds
    conv = [ln for ln in lines[start:end] if is_convention_line(ln)]

    container = read_container_class(master_path)
    if container is None:
        # v2.8: the class is known at Ingest and MUST be stated in the
        # read-back. Absent, the validator cannot key the bound -- it says so
        # rather than silently applying the strict default (an unstated class
        # was the ambiguity v2.6 killed).
        rep.fail("CONTAINER_CLASS_MISSING",
                 "no 'container: <born_digital|scan_ocr>' read-back line in "
                 "## Conventions; cannot key the convention-line bound")
        return

    bound = rules.CONTAINER_BOUNDS[container]
    rep.check(len(conv) <= bound, "CONVENTIONS_TOO_MANY",
              f"{len(conv)} convention lines > {bound} "
              f"(container: {container})")


def check_mode_map(run_dir, slug, rep):
    """content_mode_map: pinned enum, every cell populated or '~'."""
    path = run_dir / f"content_mode_map_{slug}.csv"
    if not path.exists():
        return
    with path.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            rep.fail("MODEMAP_EMPTY", "content_mode_map is empty")
            return
        if "mode" not in reader.fieldnames:
            rep.fail("MODEMAP_NO_MODE_COL",
                     f"no 'mode' column; got {reader.fieldnames}")
            return
        for i, row in enumerate(reader, start=2):
            mode = (row.get("mode") or "").strip()
            if mode not in rules.CONTENT_MODES:
                rep.fail("MODEMAP_BAD_ENUM",
                         f"row {i}: mode '{mode}' not in "
                         f"{sorted(rules.CONTENT_MODES)}")
            for col, val in row.items():
                if val is None or val.strip() == "":
                    rep.fail("MODEMAP_EMPTY_CELL",
                             f"row {i}: column '{col}' empty (use '~')")
            if any("|" in (v or "") or (v or "").strip().startswith("#")
                   for v in row.values()):
                rep.fail("MODEMAP_MARKDOWN",
                         f"row {i}: markdown in cell")


def check_chunk_plan(run_dir, slug, rep):
    """chunk_plan: declared columns, boundary_type enum, deferral arithmetic,
    coverage partition.

    Lints 3-4 (Session C chunk 2) run arithmetic across the collected rows:
      - CHUNKPLAN_OVERSIZED: a natural (non-fallback) boundary whose est_size
        meets or exceeds the ruled bound witnessed by the smallest
        fallback_split -- it should itself have been deferred.
      - CHUNKPLAN_COVERAGE: walk rows in loc order; every in-scope page in
        exactly one chunk. Gap or overlap = hard fail (the P16 lint twin).
    """
    path = run_dir / f"chunk_plan_{slug}.csv"
    if not path.exists():
        return
    rows = []
    with path.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            rep.fail("CHUNKPLAN_EMPTY", "chunk_plan is empty")
            return
        got = tuple(f.strip() for f in reader.fieldnames)
        rep.check(got == rules.CHUNK_PLAN_COLUMNS, "CHUNKPLAN_COLUMNS",
                  f"columns {got} != {rules.CHUNK_PLAN_COLUMNS}")
        for i, row in enumerate(reader, start=2):
            rows.append((i, row))
            bt = (row.get("boundary_type") or "").strip()
            if bt not in rules.BOUNDARY_TYPES:
                rep.fail("CHUNKPLAN_BAD_ENUM",
                         f"row {i}: boundary_type '{bt}' not in "
                         f"{sorted(rules.BOUNDARY_TYPES)}")
            if bt == rules.FALLBACK_BOUNDARY_TYPE:
                notes = (row.get("notes") or "").strip()
                if not notes or notes == "~":
                    rep.fail("CHUNKPLAN_NO_REASON",
                             f"row {i}: fallback_split without notes reason")

    # If the header was malformed the rows are unreliable; the columns check
    # already fired, so skip the arithmetic rather than pile on non-specific
    # noise.
    if got != rules.CHUNK_PLAN_COLUMNS:
        return

    _check_chunk_deferral(rows, rep)
    _check_chunk_coverage(rows, rep, run_dir, slug)


def _check_chunk_deferral(rows, rep):
    """Lint 3: a natural boundary over the ruled bound should have deferred.

    RETIRED WITNESS (Session C chunk 3, F3): envelope-0 witnessed the ruled
    per-source bound from the SMALLEST fallback_split est_size. That is wrong
    by construction -- a fallback split produces fragments SMALLER than the
    bound (it exists to get under it), so the smallest fragment systematically
    under-reads the ceiling. On the rappers pile it flagged 14 chapters at
    >=1400 when the plan's own stated bound was 4500; it passed the fixture
    only because there the smallest fallback happened to equal the bound.

    The honest finding: there is NO reliable machine-readable witness of the
    ruled bound in the current chunk-plan schema. The bound lives in free-text
    notes on some fallback rows ("chapter=4903 tok exceeds ruled 4500 bound")
    and not at all on others, and the fixture states no number. Parsing it out
    of prose is exactly the brittle narration-archaeology the coverage rule
    forbids ("arithmetic on the loc-grammar, never on the plan's narration").

    So this lint stays SILENT rather than compute a number it cannot trust --
    a mis-set bound firing on every run is the wart the project keeps warning
    against. The mixed-unit guard (a real, in-band, arithmetic check) is kept;
    it needs no bound. Re-enabling deferral arithmetic is docketed: it needs
    an explicit machine-readable bound (a `ruled_bound` column or a pinned
    config field), NOT a heuristic. Until that schema exists, absence of this
    check is recorded as absence-of-evidence, never as a pass.
    """
    units = set()
    for i, row in rows:
        val, unit = parse_est_size(row.get("est_size", ""))
        if val is not None and unit:
            units.add(unit)

    if len(units) > 1:
        rep.fail("CHUNKPLAN_SIZE_UNIT",
                 f"est_size units are mixed ({sorted(units)}); "
                 f"deferral arithmetic needs one unit")
        return

    # No trustworthy in-band witness of the ruled bound exists in the current
    # schema (see docstring). CHUNKPLAN_OVERSIZED is intentionally not raised
    # here; re-enable only against an explicit bound field. [F3, chunk 3]
    return


def _check_chunk_coverage(rows, rep, run_dir, slug):
    """Lint 4 (P16 twin): every in-scope page in exactly one chunk.

    Walk rows in loc order. A shared boundary page (next.start == prev.end)
    is legal per v2.8; a gap (start > prev.end + 1) or overlap
    (start < prev.end) is a hard fail.

    F1 (Session C chunk 3): the page component is read under the run's OWN
    declared loc-grammar (registration line), not a hardcoded `page.line`.
    If the declared grammar is not page-resolvable, coverage is reported
    uncertifiable once -- the same HALT-don't-guess posture lint 5 uses for
    an absent container class. If a grammar IS page-based but an individual
    row's locator carries no page integer, that row violates its own declared
    grammar and is reported (a real defect, not a validator assumption).
    """
    master = run_dir / rules.MASTER_DOC.format(slug=slug)
    grammar = read_loc_grammar(master)
    if grammar is None:
        # The registration line is missing or malformed -- that defect is
        # owned by check_registration_line (REGISTRATION_MISSING / _FIELDS /
        # _GRAMMAR). Coverage stays silent rather than co-fire; without a
        # readable registration line there is no grammar to verify against,
        # and piling on a second code would break the specificity contract.
        return
    if not grammar_is_page_resolvable(grammar):
        rep.fail("CHUNKPLAN_COVERAGE",
                 f"declared loc-grammar {grammar!r} is not page-resolvable; "
                 f"coverage cannot be verified by page arithmetic")
        return

    spans = []
    for i, row in rows:
        p_start = loc_page(row.get("loc_start", ""))
        p_end = loc_page(row.get("loc_end", ""))
        if p_start is None or p_end is None:
            rep.fail("CHUNKPLAN_COVERAGE",
                     f"row {i}: loc_start/loc_end carry no page under declared "
                     f"grammar {grammar!r} "
                     f"({row.get('loc_start')!r}, {row.get('loc_end')!r}); "
                     f"coverage cannot be verified")
            return
        if p_end < p_start:
            rep.fail("CHUNKPLAN_COVERAGE",
                     f"row {i}: loc_end page {p_end} precedes loc_start "
                     f"page {p_start}")
            return
        spans.append((p_start, p_end, i))

    spans.sort()
    for (prev_start, prev_end, prev_i), (start, end, i) in zip(spans, spans[1:]):
        if start < prev_end:
            rep.fail("CHUNKPLAN_COVERAGE",
                     f"row {i}: page {start} overlaps chunk ending at "
                     f"page {prev_end} (row {prev_i})")
            return
        if start > prev_end + 1:
            rep.fail("CHUNKPLAN_COVERAGE",
                     f"row {i}: gap -- pages {prev_end + 1}..{start - 1} "
                     f"unassigned between chunk ending at {prev_end} "
                     f"(row {prev_i}) and this chunk starting at {start}")
            return


def check_escalation_bounds(master_path, rep):
    """Escalations <=12 lines each."""
    if not master_path.exists():
        return
    lines = read_lines(master_path)
    bounds = section_bounds(lines, "Escalations")
    if bounds is None:
        return
    start, end = bounds
    block = 0
    for i in range(start, end):
        line = lines[i]
        if line.strip().startswith("### "):
            block = 0
        elif line.strip():
            block += 1
            if block > rules.ESCALATION_MAX_LINES:
                rep.fail("ESCALATION_TOO_LONG",
                         f"line {i+1}: escalation exceeds "
                         f"{rules.ESCALATION_MAX_LINES} lines")
                block = 0


def check_registration_line(master_path, rep):
    """Final line: - <slug> | <type> | <title/author/year> | loc-grammar: <g>"""
    if not master_path.exists():
        return
    lines = [ln for ln in read_lines(master_path) if ln.strip()]
    if not lines:
        rep.fail("REGISTRATION_MISSING", "master doc is empty")
        return
    last = lines[-1].strip()
    if not last.startswith("- "):
        rep.fail("REGISTRATION_MISSING",
                 f"final line is not a registration line: {last[:60]!r}")
        return
    parts = [p.strip() for p in last[2:].split("|")]
    rep.check(len(parts) == rules.REGISTRATION_FIELD_COUNT,
              "REGISTRATION_FIELDS",
              f"registration line has {len(parts)} fields, "
              f"expected {rules.REGISTRATION_FIELD_COUNT}")
    if len(parts) == rules.REGISTRATION_FIELD_COUNT:
        rep.check(parts[-1].startswith(rules.REGISTRATION_GRAMMAR_PREFIX),
                  "REGISTRATION_GRAMMAR",
                  f"final field missing '{rules.REGISTRATION_GRAMMAR_PREFIX}'")


def check_sidecar_manifest(master_path, run_dir, slug, rep):
    """Sidecar manifest lists the emitted family."""
    if not master_path.exists():
        return
    lines = read_lines(master_path)
    bounds = section_bounds(lines, "Sidecar manifest")
    if bounds is None:
        return
    start, end = bounds
    body = "\n".join(lines[start:end])
    for pattern in rules.SIDECARS:
        name = pattern.format(slug=slug)
        if (run_dir / name).exists():
            rep.check(name in body, "MANIFEST_OMITS_FILE",
                      f"sidecar manifest does not list {name}")


# --- driver ----------------------------------------------------------

def validate_run(run_dir, slug):
    rep = Report()
    master = run_dir / rules.MASTER_DOC.format(slug=slug)

    check_file_family(run_dir, slug, rep)
    check_status_line(master, rep)
    check_master_sections(master, rep)
    check_provenance_tags(master, rep)
    check_forecast_quarantine(run_dir, slug, rep)
    check_brief_bounds(run_dir, slug, rep)
    check_watchlist_bound(master, rep)
    check_master_bounds(master, rep)
    check_escalation_bounds(master, rep)
    check_mode_map(run_dir, slug, rep)
    check_chunk_plan(run_dir, slug, rep)
    check_registration_line(master, rep)
    check_sidecar_manifest(master, run_dir, slug, rep)

    return rep


def print_report(rep, run_dir, slug):
    print(f"discovery validator {VALIDATOR_VERSION}")
    print(f"run:  {run_dir}")
    print(f"slug: {slug}")
    print(f"checks run: {rep.checks_run}")
    print()
    if rep.passed:
        print("ENVELOPE GREEN")
        print()
        print("Certifies SHAPE only: file family, sections, tags, forecast")
        print("quarantine, bounds, enums. Does NOT certify the config")
        print("fragment's field names (out of scope, schema v2.6 owed), and")
        print("CANNOT detect fabricated provenance. A well-formed lie passes.")
        return 0

    print(f"ENVELOPE RED -- {len(rep.violations)} violation(s)")
    print()
    for code, detail in rep.violations:
        print(f"  [{code}] {detail}")
    print()
    print("Hard fail by ruling: any violation fails the run.")
    return 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd")

    p_val = sub.add_parser("check", help="validate a run directory")
    p_val.add_argument("--run", required=True, type=Path)
    p_val.add_argument("--slug", required=True)

    sub.add_parser("selftest", help="run the fixture suite")

    args = parser.parse_args(argv)

    if args.cmd == "selftest":
        from tests import selftest
        return selftest.run()

    if args.cmd != "check":
        parser.print_help()
        return 2

    if not args.run.is_dir():
        print(f"ERROR: {args.run} is not a directory", file=sys.stderr)
        return 2

    rep = validate_run(args.run, args.slug)
    return print_report(rep, args.run, args.slug)


if __name__ == "__main__":
    sys.exit(main())
