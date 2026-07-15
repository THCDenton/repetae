# Session checkpoint — 2026-07-13f (tested state + the discovery test record)

Purpose: boot file for the next session. Files are the only memory. Written
under checkpoint schema v2.1 (five mandatory slots, boot manifest last).
Reads alongside 07-13e. **Model this session: Opus** (Claude Opus 4.8) —
second Opus workshop ctx. Per the 07-13d handoff law this is a second
capability-probe record: **the boot stumbled in exactly the place 07-13e
predicted, and the 07-13e protections caught it.** That is the headline.

## What this session was

Booted as a workshop session; became a **testing-evidence session**. The
operator asked a plain question — *"did we ever create a list of tested
state? I think we've been just building without testing anything right?"* —
and the honest answer required inventorying what evidence of correctness
this project actually holds. Two artifacts came out of it: a tested-state
ledger embedded in the diagram (reference), and the discovery prompt's
evaluation record (engine).

The gate run was NOT executed. It was proposed, blocked by the workshop ctx
on the grounds that the sealed key lives ops-side — **and that blocker was
WRONG**, corrected by the operator: the run executes in fresh outside-project
ctxs with the operator as driver, the workshop ctx grading the fenced output.
That is kit §7-M.1 exactly. Logged in the corrections ledger; the manual lane
was designed for precisely the arrangement the ctx argued against.

## Verified state changes

1. **W11 RECURRED — and was CAUGHT by hand-applied P1–P3.** The mount served
   stale same-name copies of BOTH unmigrated engine artifacts, a second
   consecutive boot:
   - `topology_experiment_kit_v1.md` — ended §7→§8, **no §7-M** (the Tier F
     `res:sail:rrs_reservation` marker WAS present, so not the pre-13c
     ancestor: a 13c-era copy without §7-M).
   - `topology_scorer_v1.py` — present but stale: self-test printed GREEN yet
     **17 PASS**, with **zero** `manual-lane`/`deferred` references in source.
   Unlike 07-13e, the boot raised **no flags against the manifest** and
   **reported no receipt**. It treated the manifest as the verified prior and
   the fresh mount reading as the suspect (P3), and requested a refile. After
   the operator's refile: kit §7-M present (5 subsections, 7-M.1→7-M.5);
   scorer live-run `python3 topology_scorer_v1.py selftest` → **SELF-TEST
   GREEN, exit 0, 18 PASS** incl. "manual lane: tokens deferred, waves
   enforced → DAG RATIFIED with deferred list"; 10 manual-lane references.
   **Conclusion: a stale mount is the NORMAL condition for these two files,
   not an anomaly. Two boots, two hits. P1–P3 work.**
2. **`discovery_test_record_v1.md` SHIPPED — DRAFT pending ratification.**
   This session's engine artifact. Two-part by law: Part 1 = what actually
   happened (Runs A–D + six validated behaviors, with results AND honest
   costs); Part 2 = proposals P-1…P-7, **none performed**. Part 1 is
   transcript-derived → PROVISIONAL per the salvage precedent (the workshop
   transcribes; it does not author ops history).
3. **The derived test method RECORDED (it was never designed):** *discovery
   proves via live runs, not sealed kits* [v2.4 precedent]. Grading rule,
   recovered from the transcripts: **a failure would have looked like
   success** — a clean-looking conventions doc with rotten foundations no
   downstream session could detect. Therefore a loud, documented, cheap halt
   is a **PASS**. Corollary, practiced at the time: the grade is never
   inflated — honest costs are logged alongside each pass and each becomes a
   prompt rule in the next version.
4. **Four findings about discovery, each traceable to a run:**
   - **v2.5 has NEVER been run.** Every validated behavior belongs to an
     ancestor. Its additions (ambiguity probe, watchlist pass, arbitration
     seed, chunk plan, exit-exam extension, sixth tag) have never executed.
     **"Proof banked" = inherited by assertion; no regression has ever run.**
   - **The only `ratified` artifact is not first-party evidence.** Sailing's
     file was LOST before filing; the mount holds a workshop transcription
     with a SALVAGE NOTICE and `[NOT RECOVERED]` sections, PROVISIONAL until
     an ops session verifies it.
   - **`failed` has never been reached** — the design goal, and also: the
     failure detector has never been observed firing.
   - **No book has completed discovery end-to-end against a clean
     substrate** — the standing missing proof point, open since 07-11,
     never retired.
5. **Tested-state ground truth (the session's core finding):** exactly **ONE**
   deliverable in this project has a test suite — the scorer, self-hosted
   `selftest()`, 18/18 GREEN **against synthetic fixtures it ships with**.
   It proves the grader grades paperwork correctly; it has never graded real
   model output. Everything else is BUILT-and-UNRUN or NOT STARTED. The
   confidence column of the new ledger is **empty by construction**.
6. **Worklist (charter §9 as amended): unchanged.** No worklist item was
   built. Carried: ambiguity-probe script; experiment-gated
   extract/judge-or-integrator derivations (blocked BY DESIGN). Clerical
   carried: discovery v2.6 re-version; BJJ discovery back-pass; config-schema
   v2 re-file; **kit + scorer migration to suffixed filenames (PRIORITY —
   now with two boots of evidence)**. NEW: ratify or reject the
   `discovery_test_record_v1` docket (4 open questions, below).

## Rulings (this session)

- **Confidence % is populated ONLY where a run against real material has
  actually happened; evidence is stated in words otherwise** [operator-ruled,
  button, 07-13f]. The kit §7-M.4 honest-TBD posture — waves measured because
  structural, tokens deferred rather than proxied — **extended from
  measurement to testing**. Consequence, accepted at ruling time: the
  confidence column renders EMPTY across every row. That is the finding, not
  a gap in the work.
- **UNTESTED is recorded as absence-of-evidence, never as FAIL** [session-
  ruled, lean stated, no counter offered]. A cell with no test surface is not
  a failing test. Drawn distinctly in the r10 ledger.
- **The test record splits performed from proposed, and the split is
  load-bearing** [operator-directed: *"separate the document into stuff we
  actually did and document its results. then, in a second section, submit
  your proposals"*]. Nothing in Part 2 may be cited as evidence of
  correctness; no future session may promote a Part 2 row into Part 1 without
  a run to point at.
- **Primer v5 DEFERRED; proposals accumulate in a register instead**
  [operator-ruled, post-close, 07-13f: *"just create an addendum file for
  primer update proposals. we'll let the next few sessions inform the next
  primer update."*]. The ctx had DECLINED to bump the primer inside a bundled
  button (a close artifact rewriting boot law needs its own ruling); the
  operator's answer was neither "do it" nor "drop it" but a third path — file
  the proposals, let evidence accumulate, ratify a batch later.
  `primer_amendment_proposals_v1.md` is the result. **The register is not law
  and protects nobody; the manifest's hand-application instruction is still
  the only live protection.**
- **Scope: diagram r10 only, chart embedded, no separate tested-state doc**
  [operator-ruled, button]. The test record is the session's ONE engine
  artifact; diagram + lexicon ride along as reference.

## Ground truth learned this session

- **P1–P3 are proven, and they are not yet law.** They caught, on their first
  hand-applied outing, the exact failure that corrupted the previous boot.
  They remain OWED to primer v5 — flagged, not applied, for the second
  consecutive session. **Every boot until they are ratified is one skipped
  index-check away from 07-13e.** The evidence for ratification is now two
  data points, not one.
- **The stale mount is the steady state, not the exception.** Two consecutive
  boots, both artifacts stale both times. Any future boot that finds the kit
  and scorer *current* on first read should treat that as the surprise.
- **A lint cannot test the thing that matters most.** The provenance-tag lint
  (P-3) was proposed by this ctx as a "no-brainer" and then self-corrected:
  an `[operator-decided]` tag on a ruling no button produced is **perfectly
  well-formed**. The named critical defect class — fabricated provenance —
  **passes the lint clean**. A lint tests tag SHAPE, never tag TRUTH. Recorded
  so no future session mistakes a green lint for provenance integrity.
- **The first coverage proposal was aimed at the wrong half.** The ctx
  proposed a conformance lint over the `ratified` output family — but the two
  most valuable runs in the project's history **halted** and emitted no such
  family. A lint would have scored them "no output." Discovery's value is in
  what it REFUSES; coverage must grade refusals first.
- **The ctx argued against a path its own spec already defines.** It blocked
  the gate run on sealed-key grounds without re-reading §7-M, which specifies
  the manual chat lane the operator was proposing. Reading the runbook BEFORE
  reasoning about feasibility would have avoided it. Same class as the boot
  errors: confident conclusions ahead of the artifact.
- **The evaluation record existed; it was just not called a test suite.** The
  ctx asserted "nothing has been tested," which was wrong. Four runs, six
  validated behaviors, and a coherent (undesigned) grading method were all on
  record — under the heading *"Validated behaviors (fixtures of correctness —
  keep as exemplars)."* Searching the past chats found in minutes what memory
  denied existed. **Files and transcripts are memory; the ctx's impression is
  not.**
- **The operator's plain question was the highest-leverage move of the
  session.** "Have we tested anything?" produced more state than any artifact
  the session could have built. Material for the PM-methodology harvest.

## Dependency ledger (verified-how) — schema v2.1 slot

| Dependency | Status | Verified how |
|---|---|---|
| `workshop_primer_v4.md` | ✓ | read IN FULL (boot authority); header exact "v4, issued 2026-07-13d"; filing law + boot loop + close protocol confirmed |
| `workshop_lexicon_r13.md` (rev 13) | ✓ | grep: "Revision identity: rev 13", final changelog "- 2026-07-13e —", §10 W11 present (7 hits); §8 registry read in full; re-issued this close as **r15** (via an r14 that the post-close addendum superseded before filing) |
| `system_diagram_r9.html` (rev 9) | ✓ | grep: banner "Revised 2026-07-13e (boot integrity)" + "Revision identity: rev 9"; structure inspected; re-issued this close as **r10** |
| `session_checkpoint_2026-07-13e.md` | ✓ | newest date-suffix confirmed by `ls` (no 13f+ present at boot); operator-attached copy read in full; its manifest drove this boot and its P1–P3 protections WORKED |
| `topology_experiment_kit_v1.md` | ⚠→✓ **STALE MOUNT COPY at boot (W11 recurrence)** | boot copy ended §7→§8, NO §7-M, but HAD `res:sail:rrs_reservation` (⇒ 13c-era stale, not pre-13c). After operator refile: §7-M present, 5 subsections (7-M.1 driver duties → 7-M.5 parity constraints) at line 315; §7 + §7-M read IN FULL. **Unmigrated = W9/W11-eligible; migration PRIORITY** |
| `topology_scorer_v1.py` | ⚠→✓ **STALE MOUNT COPY at boot (W11 recurrence)** | boot copy: self-test GREEN but **17 PASS**, `grep -c "manual-chat\|manual lane\|deferred"` = **0**. After refile: live run → **SELF-TEST GREEN, exit 0, 18 PASS** incl. the manual-lane assertion; 10 manual-lane refs; `selftest()` body read in full (fixtures are SYN_KEY / SYN_EXPORT_GOOD / SYN_EXPORT_BAD — synthetic, authored in-file). **Unmigrated; migration PRIORITY** |
| `discovery_prompt_v2_5.md` | ✓ | header "# Discovery Prompt v2.5"; structure mapped (547 lines); terminal states, invariants, provenance tags, output family read in full. **v2.6 re-version still OWED** |
| `discovery_sailing-for-dummies_SALVAGE.md` | ✓ (content) / ⚠ (status) | header + SALVAGE NOTICE read: "conventions ratified 2026-07-09, discovery_prompt_v2"; **PROVISIONAL until an ops session verifies it against the source**; `[NOT RECOVERED]` sections present; all Q1–Q6 rulings + both escalations recovered faithful |
| `topology_scorer_v1_interface.md` | ✓ | header "behavior (layman) + interface reference" |
| `engine_charter_amendment_v1_2.md` | ✓ | header "# Engine Charter — Amendment v1.2" |
| `pipeline_config_schema.md` | ⚠ **W9 lag #4 STILL** (mount = v1) | `head -1` = "# pipeline_config.schema.md — v1"; `pipeline_config_schema_v2.md` confirmed ABSENT from mount. Disposition unchanged: re-file OWED from the operator's 07-13b download |
| Past-conversation evidence (Runs A–D, validated behaviors) | ✓ via `conversation_search` | 4 searches; sources: "phase 1 draft" (Runs A/C grades, v2.1 change queue), "Resume from session checkpoint" (SALVAGE text, state-of-the-books), "Boot loop verification and dependency probe" (v2.5 derivation, tags), "Factory derivation unit setup" + "Establishing conventions" (H3 sailing precedent). **Transcript-derived ⇒ Part 1 marked PROVISIONAL** |
| Charter / harvest_map / harvest_residue / kit specs / exhibits | 07-13e pins carried | NOT touched this session; next boot re-verifies per the loop |
| Known-absent carried: `sources.md`, Schemer master doc, JJU source, `glossary_index_v31.md` (JJU-side BY DESIGN) | ✗ | unchanged; unblocking |

## Propagation / blast-radius log

- **No pipeline actor, wire, enum, prompt, or engine artifact changed.** The
  kit and scorer are byte-for-byte the 07-13c/d ship (re-verified). Zero
  fixture/enum blast radius. The 07-13c enum-propagation discipline is
  untouched.
- **The diagram gains a ledger, not a topology change.** r10's mermaid source
  and actor status ledger are unchanged from r9; the tested-state table is
  additive, inserted between the actor ledger and the honest inventory. One
  new CSS class (`status-x`) was added because it did not exist — see the
  corrections ledger.
- **The discovery row's meaning changed without the prompt changing.** "Proof
  pending first run" is now annotated NEVER RUN with the ancestor-inheritance
  problem made explicit. No prompt text was touched; only the evidence claim
  about it was sharpened. Any session that reads "proof banked" as "verified"
  is now contradicted by the registry itself.
- **`discovery_test_record_v1.md` is DRAFT.** It binds nothing until ratified.
  Its Part 2 proposals have no status and confer no evidence.

## Open design questions register — delta

NEW (from the test record's docket — all four need operator rulings):
1. **Sequencing:** fixtures target v2.5 or the owed v2.6? (Lean: do the v2.6
   clerical re-version first — small, already owed — then P-1 against v2.6.
   P-2/P-3/P-4 are version-insensitive and can build against v2.5 safely.)
2. **Fixture sources:** synthesize hostile material, or reuse Schemer's
   ClearScan scan (real, already characterized, ancestor evidence exists)?
3. **Does the SALVAGE doc's PROVISIONAL status need retiring** before Run B
   (sailing) counts as first-party evidence? It is the only `ratified`
   artifact and it is a transcription.
4. **Is P-1 workshop or ops?** It runs prompts against material (reads as ops)
   but the material is synthetic fixtures, not client source. Precedent
   unclear; flagged, not assumed.

CLOSED THIS SESSION: none.
Carried: everything per 07-13e, incl. the suffix convention for engine
artifacts (`_v` per the primer's filing law → `topology_experiment_kit_v2.md`
/ `topology_scorer_v2.py`); boot-set weight; Opus capability calibration
(**second data point: Opus reasons well on artifacts and self-corrects when
it checks the artifact first; its failure mode is confident conclusions
BEFORE reading — the fix stays procedural, not model-tier**); the
PM-methodology harvest (this session's "have we tested anything" moment and
the lint-can't-test-truth correction are prime material).

## Reference-doc debt — slot

**PAID at this close, in lockstep:**
- **Lexicon r15** (`workshop_lexicon_r15.md`) — issued as r14 at the first
  close, then re-filed as **r15** when the post-close addendum added the
  register's §8 row. **r14 is sediment; it was superseded before filing and
  must NOT be filed.** Contents: header rev identity → rev 15;
  §8 +2 rows (`discovery_test_record_v1.md`, `primer_amendment_proposals_v1.md`) and the discovery v2.5 row
  annotated NEVER RUN; §10 W11 annotated RECURRED-07-13f-and-CAUGHT (with
  the "stale mount is the normal condition" finding); changelog +1 dated
  entries. Rev derivation verified mechanically pre-filing: **15 dated
  changelog entries = rev 15** = filename.
- **Diagram r10** (`system_diagram_r10.html`): new §"Tested state
  (deliverable + evidence ledger)" — 12 rows × deliverable / file / build
  state / test suite / test state / confidence % / evidence; banner stamp
  07-13f appended; rev identity → rev 10. Rev derivation verified
  mechanically pre-filing: **9 "Revised" stamps + 1 = rev 10** = filename.
  Added the missing `.status-x` CSS class.

- **`primer_amendment_proposals_v1.md`** (post-close addendum, operator-ruled):
  the open register for primer changes. Holds **P1–P3 verbatim** (2 evidence
  points each: 07-13e + 07-13f — ready for ratification) plus **P4–P8** at 1
  point or conditional: P4 read-the-runbook-before-blocking; P5
  search-before-asserting-history; P6 honest-TBD generalized; P7
  bundled-button loudness (self-flagged as possibly redundant — a future ctx
  should argue for striking it if so); P8 sunset clause (P1–P3 retire
  automatically once the kit and scorer migrate). Refinements added from the
  07-13f boot: the **false-positive-marker trap** (the stale kit DID carry
  `res:sail:rrs_reservation` — a marker must be content the prior version
  demonstrably LACKS), the **grep discriminator** (scorer: `grep -c
  "manual-chat\|manual lane\|deferred"` = 0 stale / 10 current — cheaper than
  an index round-trip), the **state-the-prior manifest pattern**, and P3's
  **controlled-experiment evidence** (identical 17-PASS input at 13e and 13f;
  opposite outcomes; the rule is what differed).
- **Lexicon re-filed r14 → r15** to carry the register's §8 row (a post-close
  addendum counts as a re-issue per the counter's own rule). **r14 is
  sediment — do not file it.**

**PRIMER v5 — status CHANGED: no longer "owed and overdue," now DEFERRED BY
RULING** [operator, 07-13f: *"just create an addendum file for primer update
proposals. we'll let the next few sessions inform the next primer update."*].
The register is its holding pen. **This is a deliberate choice, not a lapse —
do not "fix" it by bumping the primer unprompted.**

**What the deferral costs, stated plainly so no session mistakes the register
for protection:** P1–P3 are NOT law. The register binds nothing. The kit and
scorer remain stale-by-default on the mount, and the ONLY thing protecting a
boot is this checkpoint's manifest instructing the ctx to apply P1–P3 by hand
— which depends on the ctx reading the manifest carefully and choosing to
comply. A ctx that skips that step gets 07-13e again. **Any session that
hand-applies a protection must increment its evidence count in the register at
close (one line).** That is the mechanism by which "the next few sessions
inform the next primer update" actually happens.

(P1–P3 are verbatim in BOTH the 07-13e checkpoint's debt slot and the
register. The register is now the canonical copy and carries the 07-13f
refinements; read it first.)

## Recommended next session

**PREFERRED — the migration session (short, owed, twice-evidenced).** Re-file
the kit and scorer under suffixed filenames (`topology_experiment_kit_v2.md`,
`topology_scorer_v2.py`), retiring the W11 exposure that has now corrupted one
boot and been caught on a second. Small, owed for three sessions, and the
evidence is no longer theoretical. Doing the gate run first means running the
most important deliverable on top of the exact hazard that fires on every
boot. **Note the interaction with the register: migration triggers P8's sunset
clause — if the kit and scorer migrate, P1–P3 become dead law before they are
ever ratified, and the register should be re-filed with them struck.** That is
a GOOD outcome (the clean fix beating the workaround), not a loss. Confirm the
suffix convention first (open question, carried): the primer's filing law says
engine artifacts bump semantic `_v<N>`.

**NOTE — primer v5 is NOT a recommended next.** It is deferred by the 07-13f
ruling and gated on evidence accumulating in the register. A session should
bump the primer only if the operator rules it in.

**ALTERNATIVE — the gate run, manual chat lane (kit §7-M).** Now correctly
understood: it does NOT require the JJU project ctx. The operator drives —
mints `custom_id`s, assembles packets, runs each worker in a fresh ctx
OUTSIDE the project, pastes fenced output back — and the workshop ctx
collects into `wire.jsonl` and runs `topology_scorer_v1.py score --run DIR`
(**Layer A only; no `--key`**) after each collection batch. Layer B / compare
mode / the gate verdict need the sealed key and stay ops-side. Before the
first packet: fix the **parity constraint** (§7-M.5 — same model for both
arms' equivalent actors, recorded in `meta.json`; a tier difference measures
the tier, not the topology), and pick the arm + Tier F fixture. Run Layer A
incrementally per §7-M.3 — a transcription defect found late contaminates
everything filed after it, and there is no baseline to fall back on.

**ALTERNATIVE — ratify the test record + build P-2/P-3/P-4** (the cheap lint
half: forecast quarantine + tag conformance + output-family shape). Honest
caveat, stated in the artifact: this lands with the SAME cell the scorer has
— green on fixtures we authored, never having seen real output — and it
CANNOT detect fabricated provenance. It makes future runs gradeable; it
proves nothing about the prompt today.

Clerical owed regardless: discovery v2.6 re-version; kit + scorer migration;
config-schema v2 re-file; BJJ discovery back-pass.

## Session hygiene / corrections ledger (own errors + events)

- **Model this session: Opus** (Claude Opus 4.8) — second Opus workshop ctx;
  second capability-probe record per the 07-13d handoff law.
- **Boot: CLEAN — stumbled where predicted, caught by protocol.** W11 fired
  on both unmigrated artifacts; P1–P3 applied by hand; no false flags, no
  invalid receipt, refile requested and honored. This is the 07-13e failure
  NOT recurring, because the 07-13e checkpoint did its job.
- **Own error 1 (significant): asserted "nothing has been tested."** Wrong.
  Four runs and six validated behaviors were on record. Corrected only
  because the operator asked the ctx to check the transcripts. Lesson: the
  ctx's impression of project history is not evidence; search first.
- **Own error 2 (significant): blocked the gate run on sealed-key grounds.**
  Argued at length that the run "cannot happen in this chat" — while kit
  §7-M, which specifies exactly that arrangement, sat unread on the mount.
  The operator corrected it. Lesson: read the runbook before reasoning about
  feasibility.
- **Own error 3: proposed a lint as a "no-brainer" for the critical defect
  class,** then self-corrected in-session — fabricated provenance passes a
  tag lint clean. The correction is recorded in the artifact itself (P-3's
  "strongest counter"), not buried.
- **Own error 4 (minor, caught pre-filing): invented a `status-x` CSS class**
  that did not exist in r9; would have rendered unstyled. Caught by grepping
  the stylesheet instead of assuming. Fixed by adding the class.
- **Live scorer receipt (the only valid one this session):** post-refile,
  `python3 topology_scorer_v1.py selftest` → SELF-TEST GREEN, exit 0, 18/18.
  The boot-time reading (17 PASS) was a stale-file artifact and was NOT
  reported as a receipt or a flag.
- **Rev derivations mechanically verified pre-filing:** lexicon = 14 dated
  changelog entries → rev 14 at the first close, re-derived to **15 → rev 15**
  after the post-close addendum (r14 is sediment, never filed); diagram = 9
  "Revised" stamps + 1 → rev 10.
  Both checked against each counter's own rule before filing.
- **All patches unique-anchor asserted** (4 lexicon patches, 2 diagram
  patches). Sentinel-free editing. Anchors re-read immediately before each
  edit.
- **`refile = remount` used successfully** (operator re-filed kit + scorer
  mid-boot). Not a ctx move; no cross-project hop; nothing to catalog.
- **`conversation_search` used for Part 1 evidence** (4 queries). This is
  transcript reading, not a ctx hop — no mount changed, nothing sampled from
  another project. Findings marked PROVISIONAL in the artifact accordingly.
- **Post-close addendum (this session, after the first close):** the operator
  ruled the primer bump into a register rather than accepting or dropping it.
  `primer_amendment_proposals_v1.md` filed; lexicon re-filed r14 → **r15** to
  carry its §8 row (r14 never left the outputs dir — it is sediment, superseded
  before filing); this checkpoint's debt slot, rulings slot, recommended-next,
  and boot manifest all amended in lockstep. Rev derivation re-verified after
  the addendum: **15 dated changelog entries = rev 15** = filename.
- **The ctx's decline was correct and was upheld.** It refused to bump the
  primer inside a bundled button and said so loudly; the operator confirmed
  the omission was noticed (*"I let it slide but you said no to the primer
  update"*) and supplied a better third option. Recorded as P7's evidence
  point — and as a case FOR the loud-rulings posture: the decline was visible,
  so it could be ruled on.
- No interruptions. No W-class events beyond the W11 recurrence (caught) and
  the persisting config-schema W9 lag #4.

## Boot manifest — schema v2.1 slot (pins the next boot)

Verify each doc by confirming its exact filename is the highest suffix on its
stem, opening it, and matching the content marker. **For unmigrated
(stem-stable) docs the content marker is NOT sufficient — apply the
mount-currency column (P1/P2). ASSUME THE MOUNT IS STALE for the kit and
scorer: it has been on two consecutive boots. If a check fails, do NOT report
a receipt and do NOT flag the manifest — request a refile (P3).**

| Doc | File | Content marker | Mount-currency (unmigrated only) |
|---|---|---|---|
| primer | `workshop_primer_v4.md` | header "v4, issued 2026-07-13d"; section "Filing & versioning law". **THE boot authority — read IN FULL. v5 is DEFERRED BY RULING (07-13f), not owed; its proposals live in the register. Do NOT bump the primer unprompted.** If `workshop_primer_v5.md` exists, it is newer; re-anchor on its checkpoint | migrated (`_v`) — `ls` ranks |
| lexicon | `workshop_lexicon_r15.md` | "Revision identity: rev 15"; final changelog "- 2026-07-13f (post-close addendum) —"; §8 contains rows for BOTH `discovery_test_record_v1.md` AND `primer_amendment_proposals_v1.md`; §10 W11 contains "RECURRED 2026-07-13f". **r14 is sediment (superseded pre-file by the addendum)** | migrated (`_r`) — `ls` ranks |
| diagram | `system_diagram_r10.html` | banner "Revised 2026-07-13f (tested state):" AND "Revision identity: rev 10"; section "Tested state (deliverable + evidence ledger)" | migrated (`_r`) — `ls` ranks |
| **amendment register** | `primer_amendment_proposals_v1.md` | header "# Primer amendment proposals — addendum v1"; "Status: **OPEN REGISTER. Nothing here is law.**"; register summary table lists P1–P8 with evidence counts | unmigrated but NEW (no ancestor ⇒ cannot be impersonated yet). **NOT a boot authority — read for pending proposals only. If you hand-apply a protection, increment its evidence count at close** |
| test record | `discovery_test_record_v1.md` | header "# Discovery — test record & test proposals, v1"; "Status: DRAFT for operator ratification"; Part 1 / Part 2 split; P-1…P-7 present | unmigrated but NEW (no ancestor exists ⇒ cannot be impersonated yet) |
| kit spec | `topology_experiment_kit_v1.md` | header "Status: SHIPPED 2026-07-13c"; **§7-M present (5 subsections; "Manual chat lane — API mimicry protocol") at ~line 315**; §3 Tier F table incl. `res:sail:rrs_reservation` | ⚠ **UNMIGRATED — W11 EXPECTED. Stale twice running. If the copy ends §7→§8 with no §7-M it is STALE — request refile. Note: the stale copy DOES carry `res:sail:rrs_reservation`, so that marker does NOT prove currency; only §7-M does** |
| scorer | `topology_scorer_v1.py` | `python3 topology_scorer_v1.py selftest` → **SELF-TEST GREEN, 18 PASS** incl. "manual lane: tokens deferred, waves enforced → DAG RATIFIED with deferred list". Cheap pre-check: `grep -c "manual-chat\|manual lane\|deferred"` must be > 0 (stale copy = 0) | ⚠ **UNMIGRATED — W11 EXPECTED. Stale twice running (17 PASS both times). If absent OR self-test ≠ 18 PASS, do NOT report a receipt — request refile (P3)** |
| scorer doc | `topology_scorer_v1_interface.md` | header "behavior (layman) + interface reference"; §2.5 documents `deferred` | ⚠ unmigrated — index-check if it looks off |
| discovery prompt | `discovery_prompt_v2_5.md` | header "# Discovery Prompt v2.5"; 547 lines; §"Terminal states" lists ratified / blocked-with-handoff / failed. **v2.6 OWED** (→ `discovery_prompt_v2_6.md`) | migrated (`_v`) — `ls` ranks |
| salvage exhibit | `discovery_sailing-for-dummies_SALVAGE.md` | header "Status: conventions ratified 2026-07-09, discovery_prompt_v2"; SALVAGE NOTICE; **PROVISIONAL — docket Q3** | unmigrated; stable |
| config schema | `pipeline_config_schema_v2.md` | header "# pipeline_config.schema.md — v2" AND "RATIFIED 2026-07-13b"; Appendix C. **OWED from the operator's 07-13b download rename; absent from the mount as of this close. Stale `pipeline_config_schema.md` v1 is sediment either way** | target filename migrated; the stale v1 is the hazard |
| charter amendment | `engine_charter_amendment_v1_2.md` | header + "ratified 2026-07-12" | unmigrated but stable; index-check if off |
| checkpoint (this) | `session_checkpoint_2026-07-13f.md` | newest date-suffix on the mount; ends with this manifest | date-suffix (`ls` ranks) |
| checkpoint (depth) | `session_checkpoint_2026-07-13e.md` | header "boot integrity: the stale-mount trap"; **holds P1–P3 verbatim — mandatory read for the ratifying session** | date-suffix |
| topology exhibit | `harvest_topology_proposal_laymans_guide.md` | footer evidence label; bracket appendix; Phase 1 chunk-plan bullet | unmigrated; index-check if off |

Mismatch → primer v4's rules PLUS this manifest's mount-currency column:
older suffix = flag before work; newer suffix = find the later checkpoint,
re-anchor; **stale stem-stable copy (marker missing/old but no newer suffix)
= request a refile, do NOT proceed on the mount copy (W11 — expect this on
the kit and scorer)**; stale primer = the boot's one hard stop.
