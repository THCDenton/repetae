# Validator real-pile findings — Session C, chunk 3 (v2)

**Session:** roadmap Session C, chunk 3 — the real-pile shakedown, PLUS an
in-session validator repair (operator-authorized mid-session). Model: Claude
Opus (normal code/audit session, not a Fable probe).
**Supersedes:** `validator_real_pile_findings_v1.md` (the pre-fix triage). v1
recommended; the operator then authorized fixing F1–F3 in the same ctx and
re-scoping rappers as pre-v2.8. This v2 records what the fixes did against the
real piles. v1 is sediment (kept for archaeology under the filing law).
**Discipline held:** piles were NOT modified (git confirms: the only `evidence/`
change is these records). Every violation class terminates in exactly one of
{lint, prompt rule, rejected docket} per roadmap C.4. Nothing evaporates.

> **Pre-finding, recorded loudly:** roadmap C.3 assumed chunk 3 would first have
> to *build* a real-pile runner. It did not — chunk 1 already shipped the
> `check --run … --slug …` CLI and `validate_run()` resolves every family file
> by slug. The runner existed. Chunk 3 was pure shakedown from the first minute.

---

## Pile version scope (governs how each pile's reds are read)

| Pile | prompt era | vs validator (v2.8) | how reds are read |
|---|---|---|---|
| `loeliger-til` (07-18) | **v2.7** | ~current | version-current test — reds are live signal |
| `rappers-handbook` (07-15) | **v2.6** | two versions stale | pre-v2.8 — most reds are era-mismatch |

**Ruling [operator, this session]:** rappers is a pre-v2.8 pile. Rules that
postdate v2.6 (graded tags, the deferral-arithmetic machinery) judge it by a
standard it was never written to; those reds are era-mismatch (rejected docket),
NOT defects to fix in the pile. **Loeliger (v2.7) is the version-current real
test** the session leans on.

---

## Result — BEFORE fixes vs AFTER fixes

| Pile | before | after | what changed |
|---|---|---|---|
| Loeliger | RED, 2 violations | **RED, 1 violation** | 2 false positives (F1, F2) gone; the ONE real defect now fires |
| rappers | RED, 52 violations | RED, 37 violations | F1/F2/F3 false positives gone; era-mismatch + one real defect remain |

**The headline result:** after the fixes, Loeliger's single remaining violation
is the **p174–179 coverage gap** — the exact defect the validator was built to
catch, confirmed three independent ways in prior sessions, and MASKED before F1
because the loc-grammar bug short-circuited coverage. The validator now catches
it mechanically:

> `CHUNKPLAN_COVERAGE row 55: gap — pages 174..179 unassigned between chunk
> ending at 173 (row 87) and this chunk starting at 180`

This is the P16 coverage capability coming alive against real material for the
first time. It is the session's most important single line.

---

## Findings, one row per violation class (with fix disposition)

### F1 — `CHUNKPLAN_COVERAGE` rejected the proven per-source loc-grammar → **LINT BUG, FIXED**

**Was:** hardcoded `page.line`; rejected bare `pN` locators as unparseable,
halting coverage on both piles.
**Ground truth:** v2.8 line 290 — loc-grammar is *"propose a mechanically
resolvable grammar"*, per-source; line 561 — locations are *"in the proven
loc-grammar."* The run declares its grammar in the registration line. Loeliger:
`page N + §N.M[.K]`; rappers: `p<N>, N = printed page` — both page-based.
**Fix (Option A, operator-chosen):** `_check_chunk_coverage` reads the declared
grammar via `read_loc_grammar()`; if page-resolvable, `loc_page()` extracts the
first digit-run (`173.4`→173, `p173`→173, `p2`→2). Missing/malformed
registration line → coverage stays silent and defers to the registration lints
(specificity preserved). Grammar read but not page-based → uncertifiable,
reported not guessed (HALT-don't-guess).
**Result:** both piles parse. Loeliger's real p174–179 gap surfaces; rappers
coverage passes (219/219, genuinely intact).
**Terminated in:** a lint fix. ✓

### F2 — `CONTAINER_CLASS_MISSING` on piles that DO declare the class → **LINT BUG, FIXED**

**Was:** matched only the exact fixture string `container:` (lowercase, colon)
inside ## Conventions. Both piles declare the class in forms it missed —
rappers "Container `born_digital`" (capitalized, backtick, no colon) in
## Ingest; Loeliger "container `scan_ocr`" likewise.
**Fix:** `read_container_class` scans the whole master doc case-insensitively
for "container" followed within a short window by a legal class token,
tolerating colon/space/backtick between. HALT-on-genuinely-absent unchanged
(the `container_class_missing` fixture still fires).
**Result:** Loeliger reads `scan_ocr`, rappers `born_digital`. Rappers then
correctly fires `CONVENTIONS_TOO_MANY 61 > 50` — the REAL bound-blow the 07-15
run documented, previously hidden behind the false MISSING.
**Terminated in:** a lint fix. ✓

### F3 — `CHUNKPLAN_OVERSIZED` witnessed the wrong bound → **LINT BUG, HEURISTIC RETIRED**

**Was:** took the smallest `fallback_split` est_size as the ruled bound. Wrong
by construction — fallback fragments are SMALLER than the bound — so it flagged
14 rappers chapters at ≥1400 when the plan's own stated bound was 4500. Passed
the fixture only because there the smallest fallback equalled the bound.
**Deeper finding:** there is NO reliable machine-readable witness of the ruled
bound in the current chunk-plan schema. It lives in free-text notes on some
fallback rows and not others; the fixture states no number. Parsing it from
prose is the brittle narration-archaeology the coverage rule forbids.
**Fix (operator-chosen: retire now):** the heuristic is removed;
`_check_chunk_deferral` no longer raises `CHUNKPLAN_OVERSIZED`. Its surviving
live check — the mixed-unit guard (`CHUNKPLAN_SIZE_UNIT`) — is kept. The dead
`chunkplan_oversized` fixture is retired and replaced with `chunkplan_size_unit`
so the surviving check stays covered.
**Note:** independently, rappers' oversized reds were also era-mismatch (the
deferral machinery is v2.8; rappers is v2.6). Both facts → no oversized firing.
**Terminated in:** a lint change (retirement) + a docket entry (P18, below). ✓

### F4 — `TAG_NO_GRADE` ×33 on rappers → **ERA MISMATCH (no fix)**

Rappers is v2.6; graded tags arrived v2.7. 33 historically-correct tags judged
by a later rule. Do NOT fix the pile; do NOT weaken the live lint. Still fires
post-fix, as expected — real era signal, not a bug.
**Terminated in:** an explicitly-rejected docket entry. ✓

### F5 — `SECTION_ORDER` on rappers → **GENUINE DEFECT (confirmed, pile untouched)**

`Effort forecast` before `Ambiguity forecast`; spec canonical order per v2.8
skeleton. The known 07-15 Effort-forecast misnest, mechanically re-confirmed.
Pile NOT reordered (evidence, not input). Arguably version-neutral (section
order predates v2.6), so it stands as a real defect regardless of era scope.
**Terminated in:** confirmed-correct lint; defect already docketed. ✓

---

## New docket entry (from F3)

**DOCKET — deferral bound needs a machine-readable witness (suggested P18).**
`CHUNKPLAN_OVERSIZED` is retired, not abandoned-in-spirit: the defect it targets
(a natural boundary that should have deferred) is real, but uncheckable without
an explicit bound. Re-enable ONLY against a machine-readable bound — a
`ruled_bound` column on the chunk plan, or a pinned config field the plan echoes
— NOT a heuristic over fragment sizes. Until that schema exists, the absence of
this check is absence-of-evidence, never a pass. Recommended: fold the bound
field into the Session-B/D schema work.

---

## Cross-check against already-banked findings

- Loeliger **p174–179 gap** (`_COVERAGE_NOTE.md`, W15, P16): the validator now
  CATCHES it (post-F1). The v1 blocking dependency is cleared — F1 was the
  blocker, F1 is fixed, the P16 capability is live and demonstrated.
- Rappers **ch18 id-skip** (cosmetic; coverage 219/219): correctly NOT flagged.
  No finding. Confirmed still-clean post-fix.

---

## Terminus summary (roadmap C.4 ledger)

| Finding | Class | Terminus | Status |
|---|---|---|---|
| F1 loc-grammar | validator bug | lint fix | **DONE** — declared-grammar read |
| F2 container read-back | validator bug | lint fix | **DONE** — reader widened |
| F3 oversized witness | validator bug | lint retire + docket | **DONE** — heuristic removed, P18 filed |
| F4 ungraded tags ×33 | era mismatch | rejected docket | recorded; no code change |
| F5 section order | pile defect | confirmed | lint correct; pile untouched |

**Net code delta:** 3 lint changes (F1 fix, F2 fix, F3 retire), 1 fixture
retired + 1 added, selftest still 24/24 GREEN, both piles re-run. Loeliger 2→1
(the 1 is real); rappers 52→37 (remainder = era-mismatch + one real defect).

## Test-logging rule (roadmap C.4) — register proposal, as filed (P17)

> **Every audit finding must terminate in exactly one of: a lint, a prompt rule,
> or an explicitly-rejected docket entry. Audits mine; the validator banks. No
> finding may simply evaporate.**

This record is written under that rule — every row terminates.

---

**Ground truth, recorded plainly:** the validator was NOT trustworthy against
real piles at boot — over-fit to synthetic fixtures on three of five real-pile
checks. After the fixes it is materially better: it stopped false-firing on
legitimate per-source grammars and declared container classes, retired a
heuristic it could not compute honestly, and — the point of the exercise — now
catches the real Loeliger coverage gap it was built for and could not previously
see. That gap firing on a version-current pile, false positives gone, is the
evidence the P16 capability is real. What remains red is honest era-mismatch
(rappers, pre-v2.8) or a genuine known defect (rappers section order). No pile
was touched.
