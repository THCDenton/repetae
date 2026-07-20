# Session checkpoint — 2026-07-19e (roadmap Session C, CHUNK 3: real-pile shakedown + in-session F1–F3 validator repair)

Purpose: boot file for the next session. **Files are the only memory.** Written
under checkpoint schema v2.1 (slots below, boot manifest last). Part of the
07-19* CODE sub-thread — inherits the living-doc manifest from 07-18c (primer
v4, lexicon r19, diagram r14); re-issues NEITHER lexicon nor diagram (no design
change to their domain this session, same pattern as 07-19c/d). **Model this
session: Claude Opus** — a workshop CODE session inside the claude.ai project.
NORMAL derivation/audit session, NOT a Fable capability probe; keep it out of
the Fable model series. Worked against the operator's uploaded `repetae.zip`
(git tree, commit-clean at `7049e51 closed C`), verified on disk; all scripting
ran on the on-disk unzip.

## What this session was

**Roadmap Session C, chunk 3 — the real-pile shakedown — PLUS an
operator-authorized in-session validator repair.** Two phases:
1. **Shakedown (the chunk-3 mandate):** ran the rebuilt validator (all 5 lints,
   24/24 GREEN at boot) mechanically against both real piles; recorded every
   violation as a finding; did NOT fix the piles. Filed findings v1.
2. **Repair (authorized mid-session):** the operator reviewed the v1 findings
   and authorized fixing F1–F3 in this same ctx, plus re-scoping rappers as a
   pre-v2.8 pile. Applied the three fixes, re-ran both piles, filed findings v2.

**Result:** selftest still 24/24 GREEN; Loeliger 2→1 violations (the 1 is the
real p174–179 coverage gap, now CAUGHT); rappers 52→37 (remainder = era-mismatch
+ one real section-order defect). **No pile was touched** (git-confirmed).

## Verified state changes

Baseline reproduced BEFORE any edit: selftest **24/24 GREEN** on the uploaded
tree; handshake md5s matched the 07-19d boot handshake exactly (rules.py
`cf820125`, validate.py `e462fab9`, build_invalid `73310ee3`, valid fixture
`3bd1287a`). All edits inside `tools/discovery-validator/` except the two
findings records under `evidence/`.

**F1 — loc-grammar coverage bug (CHUNKPLAN_COVERAGE) — FIXED.** Envelope-0
hardcoded `page.line` and rejected bare `pN` locators as unparseable, halting
coverage on BOTH real piles and masking the very defect it was built to catch.
Spec truth: v2.8 line 290 loc-grammar is per-source and *proven*; the run
declares it in the registration line (`loc-grammar: <grammar>`).
1. `src/rules.py`: `LOC_PAGE_RE` widened to `\s*p?\s*(\d+)` (first page integer,
   optional `p`); new `PAGE_GRAMMAR_MARKERS`. The old page.line-only comment
   block replaced with the F1 rationale.
2. `src/validate.py`: new `read_loc_grammar()` (reads the registration line's
   final field) and `grammar_is_page_resolvable()`; `loc_page()` now
   grammar-agnostic (`173.4`→173, `p173`→173, `p2`→2). `_check_chunk_coverage()`
   takes `run_dir, slug`, reads the declared grammar, and: (a) if the
   registration line is missing/malformed → SILENT, defers to the registration
   lints (specificity preserved); (b) grammar read but not page-based →
   uncertifiable, reported not guessed; (c) page-based → extract and walk.
   **Option A chosen [operator ruling]:** read the declared grammar and handle
   page-based vs non-page, do NOT build a general grammar parser off two
   examples (that would be the over-fit trap in a fancier costume).

**F2 — container-class false-missing (CONTAINER_CLASS_MISSING) — FIXED.**
Envelope-0 matched only the exact fixture string `container:` (lowercase,
colon) inside `## Conventions`. Both piles DECLARE the class plainly in forms it
missed (rappers "Container `born_digital`", capitalized/backtick/no-colon, in
`## Ingest`; Loeliger "container `scan_ocr`").
1. `src/validate.py`: `read_container_class()` rewritten to scan the whole
   master doc case-insensitively for "container" followed within a 40-char
   window by a legal class token, tolerating `[:` `` ` `` space] between.
   HALT-on-genuinely-absent unchanged (the `container_class_missing` fixture,
   which removes the line entirely, still fires — verified).
- **Result:** Loeliger reads `scan_ocr`; rappers reads `born_digital` and then
  correctly fires `CONVENTIONS_TOO_MANY 61 > 50` — the REAL bound-blow the 07-15
  run documented, previously hidden behind the false MISSING.

**F3 — oversized-bound witness (CHUNKPLAN_OVERSIZED) — HEURISTIC RETIRED.**
Envelope-0 witnessed the ruled bound from the SMALLEST `fallback_split`
est_size — wrong by construction (fallback fragments are smaller than the bound;
it flagged 14 rappers chapters at ≥1400 vs the plan's stated 4500). Deeper
finding: **no reliable machine-readable witness of the bound exists in the
current chunk-plan schema** (it lives in free-text notes on some rows, absent
on the fixture). Parsing it from prose = the narration-archaeology the coverage
rule forbids.
1. `src/validate.py`: `_check_chunk_deferral()` no longer raises
   `CHUNKPLAN_OVERSIZED`; the mixed-unit guard (`CHUNKPLAN_SIZE_UNIT`) is kept
   (needs no bound). **Retire-now [operator ruling]**, not patch.
2. `tests/build_invalid.py`: the `CHUNKPLAN_OVERSIZED` case is retired and
   replaced with a `CHUNKPLAN_SIZE_UNIT` case (one row given a different unit),
   so the surviving live check stays covered. The stale
   `fixtures/invalid/chunkplan_oversized/` dir was removed (it is derived; the
   builder no longer creates it).
- Independently, rappers' oversized reds were ALSO era-mismatch (deferral
  machinery is v2.8; rappers is v2.6) — both facts point to no oversized firing.

**Findings records (evidence/):**
- `validator_real_pile_findings_v1.md` — the pre-fix triage (now sediment,
  kept for archaeology per the filing law).
- `validator_real_pile_findings_v2.md` — CURRENT: fixes applied, both piles
  re-run, rappers re-scoped as pre-v2.8, terminus ledger, P17 + P18 filed.

## Rulings (this session)

- **Runner already existed** [ctx finding]. Roadmap C.3 assumed chunk 3 must
  build a real-pile runner; chunk 1 already shipped the `check --run … --slug …`
  CLI. Chunk 3 was pure shakedown from minute one.
- **F1 Option A: read the declared grammar, don't build a general parser**
  [operator ruling]. The spec proves a per-source grammar but defines no grammar
  registry for the validator to interpret generically; a general parser off two
  examples is over-fit. Handle page-based vs non-page; report anything else
  uncertifiable.
- **F1 defers to the registration lints on a malformed registration line**
  [ctx call, specificity-anchored]. Coverage stays silent when the grammar is
  unreadable *because the registration line itself is broken* — that defect is
  already owned by REGISTRATION_*; co-firing would break the specificity
  contract. Coverage's own "uncertifiable" fires only on a read-but-non-page
  grammar.
- **F3 retire, do not patch** [operator ruling]. No trustworthy in-band witness
  of the bound exists; a lint that computes the wrong number is worse than one
  that stays silent. Re-enable only against an explicit machine-readable bound
  (docketed P18). Absence recorded as absence-of-evidence, never a pass.
- **Rappers is a pre-v2.8 pile** [operator ruling]. Rules postdating v2.6
  (graded tags, deferral arithmetic) judge it by a standard it never targeted;
  those reds are era-mismatch (rejected docket), NOT pile defects. Loeliger
  (v2.7) is the version-current real test.
- **F5 section-order defect left in place** [pile-no-touch discipline]. Real,
  version-neutral, already docketed; the pile is evidence not input. **Killing
  it is explicitly deferred to the next context** [operator, at close].

## Propagation / blast radius

- **P16 IS DEMONSTRATED LIVE.** The unblock condition named in findings v1 —
  F1 masks the coverage check — is cleared. The validator now catches the real
  Loeliger p174–179 gap mechanically on a version-current pile with the false
  positives gone. This is the first time the coverage capability has fired
  against real material.
- **Outputs do not exist to the next session until synced.** Ship the sources
  (2 src files, 1 generator, 2 findings records, this checkpoint) as the
  standard CLOSE PROTOCOL zip; invalid fixtures regenerate on the far side
  (including the retired oversized dir vanishing and the new size_unit dir
  appearing). Sync is a paste snippet (no `.sh`), delivered in the closing
  message.
- **NEXT SESSION = kill F5** [operator, at close]: reorder the rappers pile's
  `## Effort forecast` into its canonical slot (after Registry queue, before
  Config fragment) under the amendment protocol (changelog line; the pile moves
  from as-is evidence to a patched rev). This is the one real defect left. NOTE:
  this is a PILE PATCH — confirm the isolation rule (piles edited by a fresh
  ctx / operator per the ops-side split) before a workshop ctx touches it.
- **Then roadmap D** (freeze ruling + harvest prep), **then E** (first contact).

## Open design questions register — delta

NEW this session: **P17** (test-logging rule, roadmap C.4 — verbatim: every
audit finding terminates in exactly one of {lint, prompt rule, rejected
docket}); **P18** (deferral bound needs a machine-readable witness — a
`ruled_bound` column or pinned config field — before CHUNKPLAN_OVERSIZED can be
re-enabled; fold into Session-B/D schema work). Both UNRATIFIED, ctx-lean ids,
ratify-or-renumber on the board.
CARRIED: register pending set incl. P11 (now demonstrable, per P16 live),
P3-R/P4/P5–P7/P9/P10/P12/P13/P14→charter/P15/P16. The P13 close rider (paste
snippet, not `.sh`) still owed to register v6.

## Session hygiene / corrections ledger

- **MODEL: Claude Opus** (normal code/audit session). NOT a Fable probe.
- **Baseline-before-edit held.** 24/24 reproduced on the uploaded tree; handshake
  md5s matched 07-19d, BEFORE any edit.
- **Spec read verbatim before each fix** — surfaced the F1 fork (Option A vs a
  general parser) and the F3 depth (no in-band witness), neither visible from
  the findings one-liners.
- **A ctx triage error was caught by the operator and corrected in-session.**
  F3 was first triaged as a pure witness-logic bug; the operator's question
  ("what version did rappers run on?") surfaced that its reds are ALSO
  era-mismatch, which decoupled the F3 code decision from rappers entirely and
  re-scoped the whole rappers column. Logged loudly per the model-handoff
  discipline (calibration surface), though this is an Opus session not a first
  boot.
- **Scope held with one authorized expansion.** Chunk 3 is record-don't-fix; the
  fix phase was explicitly operator-authorized mid-session, not scope creep. No
  pile edited; no refactor beyond the three fixes + their fixture bookkeeping.
- **Filing law honored.** Findings v1 → v2 as a NEW file (immutable filed
  files); v1 kept as sediment. Living docs (lexicon r19, diagram r14, primer v4)
  UNTOUCHED and inherited — this code sub-thread re-issues neither, same as
  07-19c/d.
- **BOOT/CLOSE PROTOCOL exercised:** booted via the primer's verification loop
  against the uploaded zip verified on disk (primer v4 confirmed current — no
  hard stop; lexicon r19 / diagram r14 confirmed highest-suffix); close is the
  standard sources-only zip + paste-snippet sync + MANIFEST with two-hash fields.

## New handshake md5s (verify the merge next session)

| File | md5 | lines | expected_prior (07-19d) |
|---|---|---|---|
| `src/rules.py`        | `6996b2d962bc0cb78c167603abae535c` | 284 | `cf820125d3e704c2de2a47298ba73de0` |
| `src/validate.py`     | `7cd3bb3eae5301ae1c2c1cbf3e3cb597` | 833 | `e462fab9f64955811279b5e7bf82dddf` |
| `tests/build_invalid.py` | `069dbb7f649c9a0b7ccc03697cd1ee78` | 260 | `73310ee378082dcd881896648955ceea` |
| `fixtures/valid/sample_run/discovery_synth.md` | `3bd1287afd21a2bcdecd806840ffa014` | 47 | `-` (UNCHANGED this session) |

Invalid fixtures regenerate from the valid fixture via `build_invalid.py`
(single source of truth); their per-file md5s are derived, not shipped. The
`chunkplan_oversized` case is GONE; `chunkplan_size_unit` is NEW.

---

## Boot manifest — request list (next session = kill F5, the rappers section-order defect)

### Living-doc manifest (INHERITED from 07-18c — verify these are current)

| Doc | exact filename | content marker |
|---|---|---|
| primer | `workshop_primer_v4.md` | header "v4, issued 2026-07-13d" |
| lexicon | `workshop_lexicon_r19.md` | rev 19; last changelog 2026-07-18 |
| diagram | `system_diagram_r14.html` | banner "Revised 2026-07-18"; rev 14 |
| newest checkpoint | THIS FILE (`…07-19e.md`) | code sub-thread; inherits above |

### BOOT PROTOCOL (burned in until ratified — P13 rider owed to register v6)

1. **Orient.** Ask the operator to paste current repo state (`tree`, git
   hash/status), scoped to fit `xclip`. No guessing from a stale mount.
2. **Requisition, then loop.** Emit a bash requisition snippet (probe declared
   paths, print md5 + line counts, loud `MISSING:` branch, `| tee /dev/tty |
   xclip -selection clipboard`). Operator runs it, pastes back. Loop until
   complete.
3. **Attach for scripting.** Anything scripted against is ATTACHED or supplied
   as the whole-repo zip — never pasted.
4. **Then, and only then, work begins.**

### CLOSE PROTOCOL (burned in — snippet form as of 07-19d)

Deliverables travel as ONE zip; the operator places them with a PASTE SNIPPET
that verifies before it writes. NO sync `.sh` is shipped. Ship SOURCES not
derived artifacts; `MANIFEST.txt` lists each shipped file as `path · md5 ·
bytes · lines · expected_prior_md5`. Two-hash placement: place if absent; skip
if disk already equals new md5; overwrite ONLY if disk equals expected_prior;
HALT on any other difference. After placement: run `build_invalid.py` then the
selftest; a sync that doesn't end green says DO NOT commit.

---

**READ THIS FIRST.** The repo is the source of truth: `~/git/repetae`,
operator's machine (Pop!_OS, X11, GNOME; `xclip` present). **Session C is
COMPLETE, including chunk 3 and the F1–F3 repair. Selftest 24/24 GREEN; both
real piles re-run; P16 coverage capability demonstrated live on Loeliger; no
pile touched.** The NEXT session's job is narrow and named: **kill F5 — reorder
the rappers pile's `## Effort forecast` into its canonical slot under the
amendment protocol** (a PILE PATCH — honor the isolation rule; a fresh ctx /
operator edits the pile, a workshop ctx emits the patch instruction). Then
roadmap D (freeze), then E (first contact). Do NOT reopen the F1/F2 fixes or the
F3 retirement without a real finding naming one — freeze discipline arriving
early.

Requisition snippet — run in `~/git/repetae`, paste output, then ATTACH the
validator dir + the rappers pile:

```bash
cd ~/git/repetae && { echo "=== kill-F5 requisition $(date -u +%FT%TZ) ==="
req(){ [ -f "$1" ] && printf '%-52s OK md5=%s lines=%s\n' "$2" \
  "$(md5sum "$1"|cut -d' ' -f1)" "$(wc -l <"$1")" \
  || printf '%-52s MISSING: %s\n' "$2" "$1"; }
echo "--- validator (verify the F1-F3 merge took) ---"
req tools/discovery-validator/src/rules.py           "rules.py"
req tools/discovery-validator/src/validate.py        "validate.py"
req tools/discovery-validator/tests/build_invalid.py "build_invalid.py"
req tools/discovery-validator/tests/selftest.py      "selftest.py"
req tools/discovery-validator/fixtures/valid/sample_run/discovery_synth.md "valid fixture"
echo "--- the pile to patch (attach whole run dir) ---"
req evidence/rappers-handbook-run-2026-07-15/discovery_rappers-handbook.md "rappers pile (F5 target)"
echo "--- expected handshake (this session's outputs) ---"
echo "  rules.py        EXPECT 6996b2d962bc0cb78c167603abae535c"
echo "  validate.py     EXPECT 7cd3bb3eae5301ae1c2c1cbf3e3cb597"
echo "  build_invalid   EXPECT 069dbb7f649c9a0b7ccc03697cd1ee78"
echo "  valid fixture   EXPECT 3bd1287afd21a2bcdecd806840ffa014 (unchanged)"
echo "--- verify GREEN before touching the pile ---"
echo "  cd tools/discovery-validator && python3 tests/selftest.py   # EXPECT 24/24"
echo "  python3 -m src.validate check --run ../../evidence/rappers-handbook-run-2026-07-15 --slug rappers-handbook  # EXPECT SECTION_ORDER among the reds"
echo "=== end ==="; } | tee /dev/tty | xclip -selection clipboard
```

If the outputs' md5s do not match, the merge did not take — re-sync from the
07-19e zip FIRST, confirm 24/24, THEN start on F5.
