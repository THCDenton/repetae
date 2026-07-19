# Filing note — Loeliger TIL discovery run (v2.7), coverage status

**Filed:** Session A (2026-07-18b roadmap), clerical.
**Status of this pile:** VINDICATION EVIDENCE for discovery_prompt_v2.7 — with
one KNOWN, ALREADY-DOCKETED coverage defect. Filed as-is; not patched here
(Session A does not touch piles; the patch is Session D / roadmap p174–179).

## What this pile is evidence FOR (v2.7 held)

- **Raster-as-detector earned its keep.** The run rasterized up front and caught
  the `■`→`B` block-glyph OCR corruption that is invisible in the text layer.
  Under the old confirmer-only rule nothing would have triggered a look. (07-18
  verified-state 1, item 5.)
- **Deferral defect ABSENT.** All 85 prose section rows are page-bounded and
  under the ~1500-tok fallback; no `boundary_type: section` row exceeds the
  bound. Verified by arithmetic on `chunk_plan_loeliger-til.csv` this session.
  The dictionary is one convention row (c086) covering 172 uniform entries —
  a sanctioned convention line, not 172 IOUs.
- **Exhaustive-grade entity count.** `Class: == Function: == 172`, exact.
- **Location grammar clean.** 250 anchors; 3/3 citations resolved on first try.
- **Graded `[mechanical:]` tag works.** Every tag carries a valid grade; no
  partial-graded universal shipped (the rappers defect class did not recur).

## The known defect: coverage by silence (p174–179)

Printed pages **174–179 are covered by no chunk.** The convention row c086 ends
at p173; the next section row c054 begins at p180. Nothing spans the interval.
What is dropped: §6.2 "A Classy Cross-Reference" and §6.3 "Sum Total." Root
cause: printed p174 does double duty (dictionary end + §6.2 start) and the
plan's boundary logic assumed one page = one owner.

**This defect is CONFIRMED BY THREE INDEPENDENT METHODS:**
1. The third-ctx auditor's arithmetic (chunk rows jump p173→p180) — 07-18.
2. The 07-18 session's raster read of the pages against the binary.
3. This Session-A filing check's own coverage-partition arithmetic
   (independent re-derivation before filing).

**It is already banked**, not newly loose: drafted as
`docket_chunk_coverage_reverify_v1.md` (md5 `0d22783c4a236dc906c46d6618da4af7`),
in the repo under `evidence/` since commit `90cfab2`.

## Why the defect STRENGTHENS the vindication (do not read it as a failure)

The run predates the coverage rule. A v2.7 run shipping a silent 6-page gap is
exactly the failure mode the coverage rule (roadmap B.1 / the docket) is written
to prevent: *a page may not be dropped by silence — only by a stated,
page-checked reason.* This pile is the run that motivates that rule. Filing it
WITH the gap labeled is more faithful to the system's own provenance discipline
than filing a cleaned copy or waiting.

**Do NOT** silently patch this pile to close the gap. The patch is a Session-D
job (it needs the p174–179 chunk patch + a changelog line under the amendment
protocol). If a downstream reader wants clean coverage, they take the patched
pile from Session D, not this one.

## Second witness (cross-pile), for the coverage-rule case

The **rappers** chunk plan skips chunk-id `ch18` (rows run ch01–ch17, ch19–ch37)
after a ch17 merge ate what would have been ch18 and the id was never
renumbered. Coverage there is genuinely fine (219/219 pages) — **cosmetic**, not
a real gap — but it is the same organ (chunk-plan id/coverage integrity) and
the same class a free lint catches and no human notices, sitting in a
`ratified` artifact. (07-15b open-question 5.)

Together: one real gap (Loeliger) + one cosmetic id-skip (rappers) = two
independent witnesses that chunk-plan coverage wants a lint. Logged into
register v5 as evidence for the coverage-partition proposal.
