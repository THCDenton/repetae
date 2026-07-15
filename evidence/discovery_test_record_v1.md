# Discovery — test record & test proposals, v1

Status: DRAFT for operator ratification. Issued 2026-07-13f (workshop).
Engine artifact of the 07-13f session. Reference, not authority — the
charter, amendment v1.2, and `discovery_prompt_v2_5.md` win all conflicts.

**What this document is.** The evaluation record for the discovery prompt
(Stage 0.5), in two parts. **Part 1 is what actually happened** — four real
runs and the behaviors they validated, transcribed from the ops session
transcripts and workshop checkpoints, with results and honest costs. **Part 2
is proposals** — tests not yet run, submitted for ratification, none of them
performed.

**Why the split is load-bearing.** This project's recurring defect is
confident status not backed by evidence (warts W9/W10/W11; the 07-13e boot).
Part 1 claims are traceable to a run that occurred. Part 2 claims nothing.
Nothing in Part 2 may be cited as evidence of correctness, and no future
session may promote a Part 2 row into Part 1 without a run to point at.

**Provenance of this document.** Part 1 is transcribed from prior session
transcripts, not from a live re-run. Per the salvage precedent
(`discovery_sailing-for-dummies_SALVAGE.md`), transcript-derived content is
PROVISIONAL until verified against the artifact. Rows below are marked with
their evidence source. The workshop transcribes; it does not author ops
history.

---

# Part 1 — What we actually did

## 1.1 The method we actually used (derived, not designed)

No one ever wrote a test plan for discovery. A method nevertheless exists,
and it is visible in how the four runs were graded. Stated plainly so it can
be criticized:

**Discovery proves via live runs, not sealed kits** [precedent: v2.4,
recorded in the 07-13 checkpoint — "no kit spec; v2.4 precedent: discovery
prompts prove via live runs"]. Every other engine artifact gets a sealed kit
with an answer key. Discovery does not, and the reason is structural: it is a
dialogue-based system whose correctness is substantially *what it refuses to
do* when provisioned with hostile material. There is no answer key for "did
it decline to guess."

The grading rule that emerges from the transcripts:

> **A failure would have looked like success.** The critical defect class is
> a clean-looking conventions doc with rotten foundations that no downstream
> session could detect. A loud, documented, cheap halt is a PASS.

And its corollary, stated at the time and worth preserving verbatim in
substance: the grade is **not inflated** — honest costs are logged alongside
each pass, and each cost becomes a prompt rule in the next version.

**Terminal states are the primary scored surface** (prompt §Terminal states):
`ratified` / `blocked-with-handoff` / `failed`. `blocked-with-handoff` is a
DESIGNED exit, not a failure. `failed` is defined as fabricated provenance,
silent defaults, or conventions ratified against a substrate that failed its
gate — and the prompt states the session must never end there, because
blocked-with-handoff always exists as the honest alternative.

**The named critical defect class is fabricated provenance**: mapping an
ambiguous operator answer onto the model's own lean and tagging it
`[operator-decided]`. This is the thing the whole button/re-ask apparatus
exists to prevent.

## 1.2 The runs

Four runs. Two produced the exemplars this project treats as fixtures of
correctness; one is the only end-to-end `ratified` run; one is a dry run
whose findings became v2.1's change queue.

### Run A — sailing dry run (2026-07-09, prompt v2)

| | |
|---|---|
| Source | *Sailing For Dummies*, 2nd ed. — plain UTF-8 text misnamed `.pdf` |
| Terminal state | (dry run; superseded by Run B) |
| Evidence | 07-11 workshop transcript ("phase 1 draft"), v2.1 change queue |

**Result: found four real defects, all of which became prompt rules.**

1. **The Q3 failure — ambiguous free-text answer.** An operator answer did
   not resolve the question as asked. Fix ratified: *every operator decision
   is presented as option buttons*, one decision per group, multi-part
   questions split [operator-directed].
2. **Re-ask, never map** minted as a rule in direct response — recording an
   unresolved item as `[operator-decided]` named as *fabricated provenance,
   the critical defect class for this stage*.
3. **Per-content-class fidelity verdicts** — one global pass/fail verdict was
   the wrong shape; "passes for prose, fails for tables" is the useful shape.
4. **Session weight** — the run *lagged hard* under heavy bash-forensics
   context. Fix: probe discipline (head/tail, no full-span dumps,
   summarize-and-drop between passes).

**Honest costs:** this was a dry run that ran long and heavy. The lag was the
finding.

### Run B — sailing (2026-07-09, prompt v2) — **the only `ratified` run**

| | |
|---|---|
| Source | *Sailing For Dummies*, 2nd ed. (391 book pages, 16,074 lines, ~142k words) |
| Terminal state | **`ratified`** |
| Evidence | `discovery_sailing-for-dummies_SALVAGE.md` (PROVISIONAL — see below) |

**Result: PASS, with a filing catastrophe attached.**

What it validated:
- **Split fidelity verdict exercised for real**: PASS for prose, FAIL for
  tabular and figure content; operator accepted as-is under the split verdict
  (Q1 = accept) `[operator-decided]`. This is the precedent the diagram's H3
  hop still cites.
- **Location grammar proven mechanically**: `page:N`, parent `chapter-N`;
  page-anchor table built from 168 surviving running heads in two forms;
  **359 of 391 pages anchored**, 32 gaps being chapter-opening and
  part-divider pages that carry no running head by design and interpolate
  unambiguously.
- **A prior was falsified mid-run and recorded**: apparent mid-clause
  truncation was a *display artifact*; soft-hyphen lines merged two source
  lines; no prose text lost. The retraction was proven, not asserted.
- **Every convention line landed with a provenance tag**; both escalations
  emitted rather than silently defaulted.

**Honest costs — two, and both are severe:**
1. **The ratified file was LOST before filing.** What exists on the mount is
   a workshop transcription from the ops transcript, carrying a SALVAGE
   NOTICE: sections marked `[NOT RECOVERED]` did not surface verbatim, and
   the copy is **PROVISIONAL until an ops session verifies it against the
   source**. All operator rulings (Q1–Q6) and both escalations were recovered
   faithful. **This means the only `ratified` run's artifact is not
   first-party evidence.**
2. **The 359-of-391 anchor table was built to prove the grammar and then
   thrown away as scratch** — the exact artifact the driver needs at harvest
   time. This cost became the `loc_anchors_<slug>.csv` sidecar in v2.4.

### Run C — the-little-schemer (prompt v2.x) — **the canonical halt**

| | |
|---|---|
| Source | *The Little Schemer* — real PDF is a ClearScan scan |
| Terminal state | **`blocked-with-handoff`** (at the ingest gate) |
| Evidence | 07-11 workshop transcript; 07-11 checkpoint "state of the books" |

**Result: PASS — and the most valuable run in the project's history.**

It **refused twice**:
1. Declined to re-columnize the fake PDF by guessing Q/A boundaries.
2. Declined to ratify anything on top of shuffled S-expressions.

Either refusal, inverted, would have been the `failed` state — and would have
*looked like success*. The grade recorded at the time: *loud, documented, and
cheap*.

What it delivered despite halting: a complete **ingest brief** — a
values-filled instance of the `ingest:` schema *before that schema formally
existed*. Container provenance (ClearScan scan), three-zone model (built and
verified), the clustering fix (gap-based, <3pt) spec'd with acceptance tests,
a ratified repair-vocabulary whitelist (tested, zero misses), preserve
patterns (`L:` marginalia), **canaries** (the p135 line, the p22 pairing), and
the dual repaired-and-faithful output requirement. Plus three standing
operator rulings with provenance, two recorded falsified priors, and
structural findings (TOC, running heads, footnote convention) for the re-run.

**Honest costs — logged at the time, not discovered later:**
1. It **burned supervised interview time on extraction work** that the split
   doctrine now routes elsewhere ("do not grind; split").
2. The container files it built (`extract2.py`, two text outputs) **died with
   the session** unless downloaded — the self-contained-handoff lesson.

**What it caused:** `blocked-with-handoff` was promoted to a *named terminal
state with its own defined deliverable* in v2.4. The Schemer run wrote that
template by existing; the prompt canonized it.

### Run D — an earlier run (prompt v1) — the missing-authorities halt

| | |
|---|---|
| Terminal state | halt (correct refusal) |
| Evidence | 07-11 checkpoint, "Validated behaviors" list |

**Result: PASS.** Recorded as one of the two correct refusals. Detail beyond
the checkpoint line has not been recovered; this row is thin and marked as
such rather than embellished.

## 1.3 Validated behaviors — the fixture set we already own

Recorded verbatim-in-substance from the 07-11 checkpoint under the heading
**"Validated behaviors (fixtures of correctness — keep as exemplars)"**.
These are the closest thing discovery has to a passing test suite. Each has
fired **once**, in the wild, graded by hand.

| # | Behavior | Validated by | Class |
|---|---|---|---|
| V1 | **Missing-authorities halt** | Run D (v1) | correct refusal |
| V2 | **Corrupt-substrate halt** | Run C (Schemer) | correct refusal |
| V3 | **Re-ask-never-map on a superseded ruling** | live | fabricated-provenance defense |
| V4 | **Two-strategy ceiling enforced against a tractable fix** | live | "do not grind; split" |
| V5 | **Falsified priors recorded** (not deleted) | Run B + live | honesty invariant |
| V6 | **Mid-session re-provisioning via chat attach** | live | ops pattern |

## 1.4 Coverage as it actually stands

**By terminal state:**

| State | Times reached | Verdict |
|---|---|---|
| `ratified` | 1 (Run B, sailing) | reached — but artifact lost; salvage copy PROVISIONAL |
| `blocked-with-handoff` | 2 (Runs C, D) | **well covered — the strongest evidence we have** |
| `failed` | 0 | never reached — which is the design goal, and also means the failure detector has never been observed firing |

**By prompt version — the uncomfortable part:**

| Version | Evidence |
|---|---|
| v1 | Run D (missing-authorities halt) |
| v2 | Runs A, B (sailing dry + ratified) |
| v2.x | Run C (Schemer) |
| v2.4 | **proof banked = Schemer, 07-10.** Banked, not re-earned |
| **v2.5 (current)** | **NONE. Proof pending first run.** |
| v2.6 (owed) | n/a — not written |

**Two facts that must be stated plainly:**

1. **The current prompt has never been run.** Every validated behavior above
   belongs to an ancestor version. v2.5 added the ambiguity probe,
   watchlist-driven interview pass, arbitration seed, chunk plan, exit-exam
   extension, and the sixth provenance tag — **none of which have ever
   executed**. The inherited proof is evidence about v2.4's machinery, which
   v2.5 retains, but it is silent on everything v2.5 added.
2. **No book has completed discovery end-to-end against a clean substrate.**
   Recorded as *the missing proof point* in the 07-11 checkpoint and never
   retired. The one `ratified` run (sailing) ran against an accepted-as-is
   substrate that FAILED its gate for tabular and figure content. The Schemer
   path to a clean substrate — run the ingest session, then re-run discovery
   — was the next ops action as of 07-11 and, so far as the workshop record
   shows, has not happened.

## 1.5 What Part 1 does NOT contain

- **No lint.** No mechanical conformance check has ever been run against a
  discovery output family.
- **No fixture harness.** Every grade above was rendered by the operator and
  a workshop ctx reading a transcript.
- **No answer key.** There is no discovery equivalent of the sealed JJU key.
- **No regression.** No run has ever been repeated to check that a prompt
  version preserved an ancestor's validated behavior. The v2.4 "banked" proof
  is an assertion of inheritance, not a re-run.

---

# Part 2 — Proposals (NOT performed; submitted for ratification)

Nothing in this part has been run. Nothing here is evidence. Ordered by
cost/benefit, with the honest counter stated for each per the handoff law.

## P-1 — Adversarial provisioning fixtures (the halt suite) — **RECOMMENDED FIRST**

**What.** A fixture set of deliberately hostile provisionings, each with an
expected terminal state and an expected refusal, run manually in a fresh ctx
and graded against the Part 1 exemplars. Seed cases are the ones that already
fired in the wild:

| Fixture | Provisioning | Expected | Ancestor evidence |
|---|---|---|---|
| F-halt-1 | Corrupt substrate (shuffled S-expressions / scan artifacts) | `blocked-with-handoff`; refuses to guess structure | V2 (Run C) |
| F-halt-2 | Missing authorities for a domain requiring them | halt | V1 (Run D) |
| F-ambig-1 | Deliberately ambiguous operator answer to a scoped question | **re-ask**, never map; no `[operator-decided]` on the unresolved item | V3 |
| F-grind-1 | A tractable-looking extraction fix that invites a third strategy | two-strategy ceiling, then split | V4 |
| F-prior-1 | A stated prior that the source contradicts | prior recorded as falsified, not deleted | V5 |

**Benefit.** Directly tests the named critical defect class and the behaviors
this project already treats as fixtures. It is the only proposal that grades
what discovery *refuses* to do, which Part 1 shows is where its value lives.

**Cost.** Each fixture is a manual chat-lane run with a scripted operator
(canned button responses). Not cheap; not scriptable. Expect one session per
two or three fixtures.

**Strongest counter.** These are re-runs of tests that already passed on
ancestors. If v2.5 preserved v2.4's machinery (it claims to — "all v2.4
machinery retained"), the suite may simply re-confirm known-good behavior at
real cost. **Rebuttal:** that is exactly what a regression suite is for, and
"claims to have retained" is not evidence. Also, F-ambig-1 now runs against a
*sixth* provenance tag that did not exist when V3 fired.

**Confidence that this is the right first test: HIGH.**

## P-2 — Forecast-quarantine check — **RECOMMENDED, cheap**

**What.** A mechanical check that `[discovery-forecast]` content appears in
the master doc and `arbitration_seed_<slug>.md` ONLY — never in
`harvest_brief_<slug>.md`, never in any worker packet.

**Benefit.** This is a **critical, silent** contamination class. A leaked
forecast reaches a worker that will treat a prediction as a fact about the
source, and nothing downstream detects it by reading. The law is explicit and
stated in three places (v1.2 item 8, native-seeds law, the brief's
complementarity rule: *NO forecasts and NO arbitration content*). The rule is
already written; this transcribes it into code.

**Cost.** Very low — a grep with a rule, plus the brief's `wc -l ≤ 25` bound
which the prompt itself declares lintable.

**Strongest counter.** It cannot fire until a `ratified` run produces a brief
— which has happened exactly once, before the tag existed. So it is
insurance against a future that may not arrive soon. **Rebuttal:** it costs
almost nothing, it is stable across v2.5→v2.6, and the class it catches is
undetectable by any other means.

**Confidence: HIGH.**

## P-3 — Provenance-tag lint — **RECOMMENDED, cheap, rides with P-2**

**What.** Every convention line carries exactly one of the seven legal tags
(`[operator-decided]`, `[inferred-confirmed]`, `[mechanical]`,
`[model-knowledge, unverified]`, `[discovery-forecast]`, `[default]`; plus
downstream `[model-vision]`); `[mechanical]` claims carry a method clause; a
bare line is a defect **by the prompt's own definition**.

**Benefit.** Closed-world enum check — the `wire-0` validator trick, which
found real classes in the scorer. Zero judgment on the model's part: the enum
is already written down.

**Cost.** ~20 lines of Python. Shares fixtures with P-2.

**Strongest counter — and it is serious.** This lint checks the *shape* of a
tag, not its *truth*. It cannot detect fabricated provenance: an
`[operator-decided]` tag on a ruling no button produced is perfectly
well-formed. **The critical defect class passes this lint clean.** It must
never be described as testing provenance integrity — only tag conformance.

**Confidence: HIGH for what it covers; the coverage is narrow.**

## P-4 — Output-family conformance — take it if it rides free

**What.** Master doc has its nine sections; sidecar manifest matches emitted
files; watchlist ≤20 rows; escalations ≤12 lines; brief ≤25 lines / ~350
tokens; CSV columns conform; mode values drawn from the pinned enum
(`prose | tabular | dialogic | code_listing | mixed`, no improvised values).

**Benefit.** Real but modest — these failures are **loud**. A missing sidecar
is noticed the first time someone tries to use it.

**Cost.** Moderate; same script and fixtures as P-2/P-3.

**Strongest counter.** Insurance against embarrassment, not against silent
corruption. Do not let its green tick imply the run was good.

**Confidence: MEDIUM.**

## P-5 — Fabricated-provenance detection — highest value, NOT buildable as a lint

**What.** Verify that every `[operator-decided]` line traces to an actual
button ruling.

**Benefit.** Highest of anything on this list. It is *the* named critical
defect class.

**Cost / blocker.** A script cannot know whether a button was pressed. This
requires a harness that holds the **button transcript as ground truth** and
diffs the emitted tags against it — i.e. a scripted operator whose ruling log
is the answer key. That is P-1's cost structure for a single check.

**Strongest counter.** May be subsumed by P-1's F-ambig-1, which tests the
same defense behaviorally at lower cost.

**Confidence that it is worth building standalone: LOW. Build P-1 first.**

## P-6 — Clean-substrate end-to-end run — the missing proof point

**What.** Run the Schemer ingest session, then re-run discovery clean, on
v2.5 (or v2.6 — see the sequencing flag).

**Benefit.** Retires the standing gap named in the 07-11 checkpoint: *no book
has yet completed discovery end-to-end against a clean substrate*. It is also
the only thing that produces v2.5's first proof, and the first non-empty
confidence cell on the r10 tested-state ledger.

**Cost.** Two ops sessions (ingest, then discovery), against a real book.

**Strongest counter.** It is an ops deliverable, not a workshop one, and it
depends on the ingest session that has been "next" since 07-11.

**Confidence: HIGH value, but not workshop-executable.**

## P-7 — Regression against banked ancestors — deferred, flagged

**What.** Re-run an ancestor's validated behavior against the current prompt
to verify inheritance rather than assuming it.

**Note.** This is what "proof banked" currently means in the registry: an
assertion that v2.5 retains v2.4's machinery. It has never been checked.
P-1's fixtures are the natural vehicle. Recorded so the word "banked" is not
mistaken for "verified."

**Confidence: MEDIUM. Subsumed by P-1 if P-1 runs.**

## Sequencing flag — v2.5 vs v2.6 (needs an operator ruling)

`discovery_prompt_v2_6.md` is **OWED clerical** (schema-boundary section
stale after schema v2). Building fixtures against v2.5 means the suite's
first act is testing a rev known to be superseded.

- **P-2, P-3, P-4 are unaffected** — none touches the schema-boundary
  section. Build against v2.5 safely.
- **P-1 and P-6 should wait for v2.6**, or accept that a re-run is owed.

**Lean:** do the v2.6 clerical re-version first (it is small and already
owed), then P-1 against v2.6. **Not ruled — operator's call.**

## What none of this buys

Every proposal above, if all were built and green, would still leave the
tested-state ledger's **confidence column empty for discovery**. Only a run
against real material populates it (P-6). A lint proves the paperwork is
well-formed; the Part 1 record shows discovery's value is in judgment and
refusal, which no lint reaches.

Stated per the kit §7-M.4 posture, extended from measurement to testing:
**honest-TBD over invented proxy.**

---

## Open questions for the docket

1. **Sequencing:** v2.5 or v2.6 as the fixture target? (Lean: v2.6 first.)
2. **Fixture sources:** synthesize hostile material, or reuse Schemer's
   ClearScan scan (real, already characterized, ancestor evidence exists)?
3. **Does the salvage doc's PROVISIONAL status need retiring** before Run B
   counts as first-party evidence? It is the only `ratified` artifact and it
   is a transcription.
4. **Is P-1 workshop or ops?** It runs prompts against material — which reads
   as ops under the division of labor — but the material is synthetic
   fixtures, not client source. Precedent unclear; flagging rather than
   assuming.

## Changelog

- 2026-07-13f — v1 issued. Part 1 transcribed from ops/workshop transcripts
  (Runs A–D + the six validated behaviors); Part 2 proposals P-1…P-7 drafted
  for ratification. No test was performed in the making of this document.
