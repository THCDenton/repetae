# Docket item — chunk-plan coverage arithmetic + mandatory re-verify loop

Status: DRAFTED 2026-07-18, homes UNDECIDED (see §Homes).
Origin: Loeliger v2.7 test run + independent audit; gap confirmed by raster.
Class: NEW defect class to discovery — "coverage by silence."

---

## The finding, in one line

A chunk plan can claim to cover every in-scope page while silently dropping a
range, and nothing in the current pipeline catches it except a human doing
arithmetic by hand.

## The claim under test

The Loeliger chunk plan asserts its own coverage invariant: *"every in-scope
range in exactly one chunk."* The master doc accounted for the region by
calling printed p174 a single-page §6.2 seed exclusion.

## The evidence run against it

- **Arithmetic (the auditor's catch):** chunk rows jump from printed p173
  (c086, dictionary) to printed p180 (c054, Ch7 start). Printed p174–179 —
  six pages — appear in NO chunk. The plan's stated invariant fails its own
  arithmetic.
- **Raster (this session's confirmation — the text layer on this scan lies):**
  rasterized printed p173–180 (`pdftoppm -r 100 -gray`, file pages 188–195;
  print = file − 15) and read them by eye. Findings:
  - p173: dictionary tail (`WAIT`, `WHILE`, `XOR`).
  - **p174: dictionary ENDS (`[` literal handler) AND §6.2 "A Classy
    Cross-Reference" BEGINS — a shared boundary page.** The plan's "single-page
    seed exclusion" description is wrong on two counts: the dictionary spills
    onto 174 (contradicting c086's p103–173 range), and §6.2 is not one page.
  - p175–178: §6.2 continues — all ~150 keywords grouped by class (Memory
    Reference, Program Control, Relational, Stack, Utility, Vocabulary, …).
    Real, in-scope reference content.
  - p179: §6.2 ends; **§6.3 "Sum Total"** begins — the chapter's prose
    summary ("~150 user-available keywords… under 4K bytes").
  - p180: Ch7 "Extension Please" — the plan resumes cleanly here.

## The consequence (what a worker does wrong, concretely)

Two real artifacts are dropped from harvest entirely:
1. **§6.2 the class-organized cross-reference** — no worker ever reads it. A
   query like "which keywords are Relational?" resolves to nothing, because the
   only page answering it was never chunked.
2. **§6.3 the chapter summary** — the chapter's own conclusion, never harvested.

Neither appears in the run's own report as a problem. The plan described a
silent drop as a deliberate one-page exclusion.

## The root cause, and why it's a NEW class

The gap formed because **printed p174 does double duty** (dictionary end +
section start), and the plan's boundary logic assumed one page = one owner.
The drop happened by SILENCE — the plan did not decide to exclude 174–179; it
failed to assign them and then narrated the failure as a decision.

This is the same SHAPE as the already-docketed "defer instead of chunk"
defect: honest-sounding, well-formed, and wrong in a way invisible to anyone
reading the output — catchable only by pointing arithmetic at it. It is a NEW
class because "defer" was a chunk that named itself and didn't cut; this is a
range that no chunk names at all.

## The rule this finding proposes

> Chunk-plan coverage is verified by ARITHMETIC, not by the plan's own prose
> claim. Any gap or overlap in in-scope page coverage triggers a MANDATORY
> re-verification of the affected pages: rasterize and read them, then either
> (a) bring them into a chunk, or (b) record an EVIDENCED exclusion naming what
> is on the pages and why it is out of scope. **A page may not be dropped by
> silence; it is dropped only by a stated, page-checked reason.**

Note the shape: this is the SAME upgrade v2.7 made to the raster rule — from
confirmer ("double-check a verdict you already have") to detector ("go looking,
then re-verify against the pages"). The coverage check should hunt for the gap
and send the run back to the pages, not merely confirm a plan that looks whole.

## Homes — UNDECIDED (the reason this is a docket item, not an edit)

Two candidate homes, and the v2.7-era logic argues for BOTH (a rule that lives
only in the writer rots when the writer changes — the schema-lockstep lesson):
- **Discovery prompt** — the run must execute the coverage arithmetic + the
  re-verify loop before shipping a chunk plan. Earliest catch, author-time.
- **Engine lint** — the validator checks coverage independently on ingest,
  regardless of what discovery did. Catches it even if a future discovery
  version forgets. (Same partition check: every in-scope page covered exactly
  once; gap or overlap = hard fail.)

Deferred deliberately. Deciding homes is its own session's work, the way
schema-lockstep (P14) was.

## Confidence

- **The gap is certain** — arithmetic + raster, two independent methods, two
  independent ctxs (auditor found it, this session confirmed it against the
  binary). Not a hunch.
- **The class is one instance so far.** A second witness would be another book
  whose chunk plan drops a shared-boundary or short-section range. The
  mechanism (one page, two owners) will recur wherever a dictionary/back-matter
  section abuts a prose section — plausibly common, but unproven beyond this
  book.

## Local cleanup owed regardless of the rule

The Loeliger chunk plan needs a chunk (or evidenced exclusion) for printed
p174–179 (§6.2 + §6.3). Separate, small, and NOT done this session — captured
here so it isn't lost.
