"""
Rule definitions for the discovery output validator.

Every constant here traces to an explicit line in discovery_prompt_v2_8.md.
Nothing is invented. If a rule is not written down in the prompt, it does
not appear here.

REBUILD 2026-07-19 (Session C, chunks 1-2): re-grounded v2.5 -> v2.8 and
banked all five audit-mined lints. Chunk 1 fixed the two red selftests
(TAG_ILLEGAL specificity; TAG_MECHANICAL_NO_METHOD false pass) and re-cited
constants to v2.8. Chunk 2 added the five lints: graded-tag grammar
(TAG_NO_GRADE), partial-on-universal (TAG_PARTIAL_UNIVERSAL), chunk-deferral
arithmetic (CHUNKPLAN_OVERSIZED), coverage partition (CHUNKPLAN_COVERAGE,
the P16 lint twin), and the container-keyed convention bound
(CONVENTIONS_TOO_MANY keyed via CONTAINER_CLASS_MISSING).

SCOPE (deliberate): this module validates the ENVELOPE only -- the file
family, master-doc section structure, provenance tags, forecast quarantine,
and the countable bounds. It does NOT validate the config fragment's field
names (master doc section 7). That schema boundary remains out of scope per
the P-2/P-3/P-4 sequencing flag in discovery_test_record_v1.md; v2.8 keeps it
a rule-not-copy boundary.

WHAT THIS CANNOT DO: this checks SHAPE, never TRUTH. A fabricated
[operator-decided] tag on a ruling no operator made is perfectly
well-formed and passes clean. See P-5 in the test record. Do not describe
a green verdict from this tool as provenance integrity.
"""

# --- Provenance tags -------------------------------------------------
# Source: discovery_prompt_v2_8.md "Provenance tags (mandatory on every
# convention line)". Closed world. A bare convention line is a defect by
# the prompt's own definition.

LEGAL_TAGS = frozenset({
    "operator-decided",
    "inferred-confirmed",
    "mechanical",
    "model-knowledge, unverified",
    "discovery-forecast",
    "default",
})

# --- Mechanical STRENGTH GRADES (v2.8, graded-tag lint 2026-07-19) ----
# discovery_prompt_v2_8.md, Provenance tags: a [mechanical: ...] tag must
# end in a strength grade, machine-extractable from the tag. The grade is
# the LAST ';'-delimited clause inside the bracket. Grade added v2.7;
# enforced here in chunk 2.
#
#   exhaustive -- count covers every site the claim ranges over; one
#                 counter-example would falsify it.
#   sampled    -- count covers a stated subset; holds on what was checked.
#   partial    -- count is real but does not settle the claim (proxy, or
#                 the claim ranges wider than the count). A partial grade
#                 on a universal claim is itself a defect -- checked by the
#                 partial-on-universal lint, NOT here.
LEGAL_GRADES = frozenset({"exhaustive", "sampled", "partial"})
MECHANICAL_GRADE_SEPARATOR = ";"

# --- Universal quantifiers (partial-on-universal lint, v2.8) ----------
# discovery_prompt_v2_8.md, Provenance tags: "A partial grade on a
# universal ('always', 'every', 'never') is a defect." The rappers-handbook
# audit generalized this: a claim carrying a universal, backed by a partial
# count, must carry the exception column or be downgraded to "usually/most"
# (evidence/discovery_eval_findings_rappers-handbook.md, generalizable rule).
#
# Scope is deliberately TIGHT and spec-anchored. Bare "fixed" and
# "throughout" are EXCLUDED: they appear in innocent prose (the valid
# fixture's "title case throughout" is exhaustive-graded and true), and a
# loose vocabulary would false-flag. Matched case-insensitively as whole
# words / phrases.
UNIVERSAL_QUANTIFIERS = (
    "always", "every", "never", "invariant", "fixed frame",
)

# --- Tag QUALIFIERS (fix, 2026-07-14, first real run) -----------------
# The prompt names the tags but nowhere forbids a qualifier inside the
# bracket. The Loeliger run wrote BOTH forms and both are compliant:
#
#   [mechanical]                      method stated in the line's prose
#   [mechanical: 21 matches]          method stated inside the bracket
#   [operator-decided, 2026-07-14]    ruling plus its date
#
# envelope-0 required an EXACT string match, so every qualified tag was
# reported TAG_ILLEGAL -- 45 of 49 violations on the first real run were
# this bug. The fixture suite missed it because the fixtures were authored
# from the same misreading as the code.
#
# A tag matches if the text BEFORE the first qualifier separator is a
# legal tag. `model-knowledge, unverified` contains a comma in the tag
# itself, so it is matched whole before separator-splitting is attempted.

TAG_QUALIFIER_SEPARATORS = (":", ",", " + ", " — ", " -- ")

# Downstream only -- figure-worker output. Not emitted by discovery itself,
# but named in the prompt, so accepted rather than flagged.
DOWNSTREAM_TAGS = frozenset({"model-vision"})

ALL_ACCEPTED_TAGS = LEGAL_TAGS | DOWNSTREAM_TAGS

# --- Master doc sections ---------------------------------------------
# Source: discovery_prompt_v2_8.md "Output family" section 1. Nine sections,
# named, in this order.

MASTER_SECTIONS = (
    "Conventions",
    "Ambiguity forecast",
    "Escalations",
    "Registry queue",
    "Effort forecast",
    "Config fragment",
    "Kit nominations",
    "Sidecar manifest",
    "Changelog",
)

# --- File family ------------------------------------------------------
# Source: discovery_prompt_v2_8.md "Output family" sections 1-6.
# <slug> is substituted at check time.

MASTER_DOC = "discovery_{slug}.md"

SIDECARS = (
    "harvest_brief_{slug}.md",
    "content_mode_map_{slug}.csv",
    "loc_anchors_{slug}.csv",
    "arbitration_seed_{slug}.md",
    "chunk_plan_{slug}.csv",
)

# --- Pinned enums -----------------------------------------------------
# Source: discovery_prompt_v2_8.md section 3 -- "Pinned enum in `mode`".

CONTENT_MODES = frozenset({
    "prose",
    "tabular",
    "dialogic",
    "code_listing",
    "mixed",
})

# Source: discovery_prompt_v2_8.md section 6 -- chunk plan boundary_type.
BOUNDARY_TYPES = frozenset({
    "chapter",
    "section",
    "convention",
    "fallback_split",
})

CHUNK_PLAN_COLUMNS = (
    "chunk_id",
    "boundary_type",
    "loc_start",
    "loc_end",
    "est_size",
    "notes",
)

# --- Chunk deferral arithmetic (lint 3, v2.8) ------------------------
# Source: discovery_prompt_v2_8.md section 6 + the chunk-plan axis:
# "cut at the source's natural teaching boundary ... a size-bounded
# fallback for oversized units -- the bound is a per-source button ruling
# MEASURED against this source's layout ... never a global constant.
# Fallback splits reference the ruled per-source bound and split at the
# least-bad ruled boundary."
#
# The defect this catches: a NON-fallback boundary (chapter/section/
# convention) whose est_size exceeds the ruled bound -- it should have been
# a fallback_split, but was left as an oversized natural unit. Because the
# bound is per-source and NOT a column in the plan, the plan's own
# fallback_split rows reveal it: a fallback exists precisely BECAUSE a unit
# hit the bound, so the smallest fallback_split est_size is an upper witness
# to where the operator's ruled ceiling sits. Any non-fallback row at or
# above that witness should itself have been deferred. No global constant is
# introduced; the arithmetic is against the plan's own declared sizes.
#
# est_size grammar: "<number> <unit>" (e.g. "1180 lines"). The unit must be
# consistent across rows for the comparison to be meaningful; a mixed-unit
# plan is its own defect (CHUNKPLAN_SIZE_UNIT).
FALLBACK_BOUNDARY_TYPE = "fallback_split"
NATURAL_BOUNDARY_TYPES = frozenset({"chapter", "section", "convention"})

# --- Coverage partition (lint 4, v2.8 -- the P16 lint twin) ----------
# Source: discovery_prompt_v2_8.md section 6 coverage rule: "every in-scope
# range appears in exactly one chunk ... walk the chunk rows in loc order
# and confirm each in-scope page lands in exactly one chunk. Any gap OR
# overlap triggers a MANDATORY re-verification." This is the author-time
# twin of the same partition check enforced on ingest (schema-lockstep).
#
# Enforced by ARITHMETIC on the loc-grammar, never on the plan's narration
# of itself. The fixtures use the `page.line` grammar; the page is the
# integer before the dot. Contiguity in loc order:
#   next.start_page == prev.end_page      -> shared boundary page (LEGAL:
#                                            v2.8 "shared-boundary case",
#                                            one page doing double duty)
#   next.start_page == prev.end_page + 1  -> clean adjacency (LEGAL)
#   next.start_page  > prev.end_page + 1  -> GAP (the Loeliger p174-179 class)
#   next.start_page  < prev.end_page      -> OVERLAP
# Gap and overlap are both hard fails; the shared-boundary touch is the one
# non-strict adjacency the spec explicitly permits.
LOC_PAGE_RE = r"^\s*(\d+)"   # leading integer of a page.line location

# --- Countable bounds -------------------------------------------------
# Every bound below is stated numerically in the prompt.

WATCHLIST_MAX_ROWS = 20          # "the reviewed watchlist (<=20 rows...)"
ESCALATION_MAX_LINES = 12        # "Escalations  <=12 lines each"
BRIEF_MAX_LINES = 25             # "Hard budget: <=25 lines / ~350 tokens"
EXHIBIT_MAX_LINES = 5            # "exhibits <=5 lines each, per axis"
# Source: discovery_prompt_v2_8.md "Bounds (re-ruled in v2.6)". The bound is
# CONTAINER-KEYED: born_digital <=50, scan_ocr <=75. v2.5's flat ~45
# "counted nothing in particular" (first real run: 88 vs 62 on one document).
#
# LINT 5 (Session C chunk 2): the validator now READS the container class
# from the master doc's ingest read-back and keys the bound to it. v2.8:
# "The container class is known at Ingest, before any convention is written,
# so the applicable bound is known too -- state it in the read-back." The
# read-back line is a convention line in the ## Conventions Identity/Ingest
# axis carrying `container: born_digital` or `container: scan_ocr`. If the
# read-back is ABSENT the validator cannot key the bound and says so
# (CONTAINER_CLASS_MISSING) rather than silently applying the strict default
# -- an unstated class was itself the ambiguity v2.6 killed. The bound is
# never guessed from file contents; it is read from the run's own statement.
MASTER_MAX_CONVENTION_LINES_BORN_DIGITAL = 50   # "born_digital sources: <=50"
MASTER_MAX_CONVENTION_LINES_SCAN_OCR = 75       # "scan_ocr sources: <=75"

# The read-back marker the validator scans for, and the class -> bound map.
CONTAINER_CLASS_MARKER = "container:"
CONTAINER_BOUNDS = {
    "born_digital": MASTER_MAX_CONVENTION_LINES_BORN_DIGITAL,
    "scan_ocr": MASTER_MAX_CONVENTION_LINES_SCAN_OCR,
}
MASTER_MAX_TOTAL_LINES = 300     # "Total master doc <=300 lines before the YAML"

# --- Forecast quarantine ----------------------------------------------
# Source: discovery_prompt_v2_8.md section 2 complementarity rule --
# "NO forecasts and NO arbitration content" in the brief; and section 5 --
# "NEVER injected into the brief or any worker packet".
#
# [discovery-forecast] content is legal in exactly two files. Anywhere
# else is a critical, silent contamination class: a leaked forecast
# reaches a worker that treats a prediction as a fact about the source,
# and nothing downstream detects it by reading.

FORECAST_TAG = "discovery-forecast"

FORECAST_PERMITTED_FILES = (
    MASTER_DOC,
    "arbitration_seed_{slug}.md",
)

# --- Status line ------------------------------------------------------
# Source: discovery_prompt_v2_8.md section 1 -- the master doc's line 2.
STATUS_PREFIX = "Status: conventions ratified"

# --- Registration line ------------------------------------------------
# Source: "Final line: the registration line for `sources.md`"
# Format: - <slug> | <type> | <title / author / year> | loc-grammar: <grammar>
REGISTRATION_FIELD_COUNT = 4
REGISTRATION_GRAMMAR_PREFIX = "loc-grammar:"
