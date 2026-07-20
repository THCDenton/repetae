# Validator real-pile findings — Session C, chunk 3 (v1)

**Session:** roadmap Session C, chunk 3 — the real-pile shakedown. Model: Claude
Opus (normal code/audit session, not a Fable probe).
**What ran:** the rebuilt discovery validator (all 5 lints, selftest 24/24 GREEN
at boot, handshake md5s matched the 07-19d checkpoint) executed mechanically
against the two real discovery piles via its existing CLI
(`python3 -m src.validate check --run DIR --slug SLUG`).
**Discipline held:** piles were NOT modified. Every violation class below
terminates in exactly one of {lint, prompt rule, rejected docket} per roadmap
C.4. Nothing evaporates.

> **Pre-finding, recorded loudly:** roadmap C.3 assumed chunk 3 would first have
> to *build* a real-pile runner. It did not — chunk 1 already shipped the
> `check --run … --slug …` CLI and `validate_run()` resolves every family file
> by slug. The runner existed. Chunk 3 was pure shakedown from the first minute.

---

## Raw result

| Pile | prompt era | checks run | envelope | distinct classes |
|---|---|---|---|---|
| `loeliger-til` (07-18 run) | v2.7 | 30 | **RED — 2 violations** | 2 |
| `rappers-handbook` (07-15 run) | v2.6 | 79 | **RED — 52 violations** | 5 |

Both RED, exactly as roadmap C.3 predicted. But the headline is *where* the red
comes from: **of the five distinct violation classes across both piles, four
are validator defects, not pile defects.** One real book (rappers) surfaced
three separate validator bugs in one run — the same ratio the 07-14 checkpoint
recorded ("one real book found three bugs in ten minutes"). The validator was
built and fixture-tested by reasoning from the spec; the fixtures shared the
code's reading and could not catch where that reading over-fit. Real piles can.

---

## Findings, one row per violation class

### F1 — `CHUNKPLAN_COVERAGE` rejects the proven per-source loc-grammar → **LINT BUG**

**Fired on:** both piles (Loeliger row 2 `p1`; rappers row 2 `p2`).
**What the lint did:** demanded `page.line` grammar and rejected bare `pN` page
locators as unparseable, halting coverage verification.
**Ground truth:** the spec does NOT mandate `page.line`. v2.8 line 290 —
location grammar is *"propose a mechanically resolvable grammar"*, per-source;
line 561 — locations are *"in the proven loc-grammar."* The Loeliger pile
**proved `pN` as its grammar** (250 anchors, 3/3 citations resolved on first
try, per `_COVERAGE_NOTE.md`) and shipped `ratified` after a cold third-ctx
audit. The validator invented a global grammar the spec explicitly leaves to
the run.
**Severity:** highest in the session. This lint would false-RED *every*
legitimate `pN`-grammar run, and it masks the one defect it was built to catch
(the real Loeliger p174–179 coverage gap is invisible while the grammar check
short-circuits).
**Terminates in:** a **lint fix** — lint 4 must read the run's declared
loc-grammar (from the registration line / master doc) and verify coverage in
*that* grammar, not a hardcoded one. Page-only grammars partition by page.

### F2 — `CONTAINER_CLASS_MISSING` on piles that DO declare the class → **LINT BUG**

**Fired on:** both piles.
**What the lint did:** reported no container read-back, so it couldn't key the
convention-line bound.
**Ground truth:** both piles state the class plainly. Rappers line 14:
"Container `born_digital`". Loeliger line 13: "container `scan_ocr`". The lint's
`read_container_class()` only recognizes the exact string it invented for the
valid fixture (`container: born_digital`, colon form, in a specific Identity
line). It cannot see the class written with a backtick, without a colon, or
sited in the `## Ingest` block / config fragment where both real runs put it.
**This is the same failure mode as F1:** the lint hardcoded the fixture's exact
string instead of the spec's actual grammar. Green-on-fixtures meant "matches my
reading," never "matches a real run."
**Terminates in:** a **lint fix** — `read_container_class()` must recognize the
container class wherever the spec permits it to be stated (Ingest read-back OR
config fragment), tolerant of `container` with/without colon and inside code
spans. The v2.6-lesson HALT-don't-default behavior stays; only the reader
widens. *Design tension to resolve in the fix:* the checkpoint's own ruling
("absent read-back HALTS") is correct — but "absent" must mean genuinely absent,
not "present in a form my parser didn't anticipate."

### F3 — `CHUNKPLAN_OVERSIZED` witnesses the wrong bound → **LINT BUG**

**Fired on:** rappers only (14 hits, rows flagged ≥1400 tok).
**What the lint did:** took the *smallest `fallback_split` est_size* (1400) as
the witnessed ceiling and flagged every `chapter` row at or above it.
**Ground truth:** the rappers plan states its actual bound in its own notes —
row ch25: *"chapter=4903 tok exceeds ruled 4500 bound."* The ceiling is **4500**.
The value 1400 is a *post-split fragment size*, not the bound; a fallback split
produces pieces SMALLER than the bound by construction, so witnessing the bound
from the smallest fragment is guaranteed to under-read it. The lint's witness
heuristic is inverted.
**Why it passed fixtures:** the valid fixture's smallest fallback happened to
equal its bound, so the wrong heuristic gave the right answer on synthetic data.
Real data separated the two numbers and exposed it.
**Terminates in:** a **lint fix** — the witnessed bound must come from the
plan's stated bound (the `fallback_split` rows exist *because* a unit hit the
bound; the bound is the size that TRIGGERED the split, recoverable from the
pre-split chapter's stated overage, not from the fragment sizes). Until a
reliable in-band witness is specified, this lint should stay silent rather than
false-fire — a mis-set bound is the exact wart (W15-adjacent) the project keeps
warning about. *Note:* Loeliger correctly threw NO oversized violation (all 85
section rows genuinely under its fallback), so the lint is not uniformly broken
— it fails specifically when bound ≠ smallest-fragment.

### F4 — `TAG_NO_GRADE` ×33 on the rappers pile → **ERA MISMATCH (no pile fix)**

**Fired on:** rappers only (33 hits).
**What the lint did:** required every `[mechanical]` tag to carry a strength
grade (`exhaustive|partial|sampled`); the rappers tags carry none.
**Ground truth:** the rappers pile is `discovery_prompt_v2.6` (line 2). Graded
tags were introduced in **v2.7**. The validator enforces v2.8. This is a v2.6
artifact judged by a rule that postdates it by two versions — precisely the
"span-era fragments" the checkpoint said the old piles carry. The tags were
*correct for their era*.
**Terminates in:** an **explicitly-rejected docket entry** — NOT a lint change
and NOT a pile fix. The validator is right to enforce grades going forward; the
rappers pile is simply pre-grade evidence. Recorded so a future session does not
"fix" 33 historically-correct tags or weaken the live lint to accommodate a
retired era. If the rappers pile is ever re-run, it re-runs at current-version,
which supplies grades natively.

### F5 — `SECTION_ORDER` on the rappers pile → **GENUINE PILE DEFECT (confirmed)**

**Fired on:** rappers only (1 hit).
**What the lint did:** flagged `Effort forecast` appearing before `Ambiguity
forecast`; spec canonical order (v2.8 skeleton, line 485+) is Conventions →
Ambiguity forecast → Escalations → Registry queue → Effort forecast → …
**Ground truth:** this is REAL, and already on record — the 07-15 run's own
report and the diagram r14 banner note *"an Effort forecast mis-nested INSIDE
`## Conventions`."* The rebuilt validator mechanically re-confirmed a defect
three prior human/script reads had found. This is the validator working as
intended: a free lint catching a real structural defect sitting in a `ratified`
artifact that no downstream reader would notice.
**Terminates in:** the defect is already docketed against the rappers pile;
this finding **confirms the lint is correct** and adds a mechanical witness.
Per pile-no-touch discipline, the pile is NOT reordered here. Any patch is a
Session-D-class job under the amendment protocol, if the pile is ever promoted
from evidence to input.

---

## Cross-check against already-banked findings (no double-counting)

- The Loeliger **p174–179 coverage-by-silence gap** (`_COVERAGE_NOTE.md`, wart
  W15, register P16, `docket_chunk_coverage_reverify_v1.md`) is the defect lint
  4 was BUILT to catch. This session could **not** confirm the validator catches
  it, because F1 (the loc-grammar bug) short-circuits coverage before the
  partition walk runs. **This is a blocking dependency: F1 must be fixed before
  the validator can be trusted to catch the very defect that motivated it.**
  Recorded as the session's sharpest single result.
- The rappers **ch18 id-skip** (cosmetic, coverage genuinely 219/219) is banked
  in `_COVERAGE_NOTE.md` as the cross-pile second witness. The validator did not
  flag it (correctly — coverage is intact; the gap is only in the id sequence).
  No new finding.

---

## Recommended terminus summary (roadmap C.4 ledger)

| Finding | Class | Terminus |
|---|---|---|
| F1 loc-grammar | validator bug | **lint fix** (read proven per-source grammar) |
| F2 container read-back | validator bug | **lint fix** (widen class reader) |
| F3 oversized witness | validator bug | **lint fix** (correct bound witness) |
| F4 ungraded tags ×33 | era mismatch | **rejected docket** (pre-grade evidence; no fix) |
| F5 section order | pile defect | **confirmed** (lint correct; pile untouched) |

**Net:** three lint fixes owed (F1–F3), one rejected-docket entry (F4), one
confirmed-correct lint (F5). The three lint fixes are a validator-repair session
of their own — flagged here, NOT performed this session (chunk 3 records; it
does not fix). F1 is the priority: it blocks the P16 coverage capability.

## Test-logging rule (roadmap C.4) — register proposal, as filed

Proposed for the open-design register (verbatim per roadmap C.4):

> **Every audit finding must terminate in exactly one of: a lint, a prompt rule,
> or an explicitly-rejected docket entry. Audits mine; the validator banks. No
> finding may simply evaporate.**

This findings record is the first artifact written under that rule — every row
above carries a terminus. Recommended register id: **P17** (ctx lean; ratify or
renumber on the board). Ratification belongs to the operator, not this session.

---

**Ground truth, recorded plainly:** the rebuilt validator is not yet trustworthy
against real piles. It is spec-faithful on synthetic fixtures and over-fit on
three of five real-pile checks. That is not a regression — it is the fixture
suite's known blind spot (green means "matches my reading of the spec") meeting
real data for the first time, exactly as the 07-14 and 07-15 runs predicted it
would. The validator earned its keep this session by being wrong in three
locatable, spec-anchored ways. Chunk 3's job was to find that out without
touching the piles. Done.
