# Session checkpoint — 2026-07-15 (discovery v2.6 + the run that tested it)

Purpose: boot file for the next session. **Files are the only memory, and the
files live in a git repo the ctx cannot read.** Written under checkpoint schema
v2.1 (five mandatory slots, boot manifest last). Reads alongside 07-14b.
**Model this session: Opus** (Claude Opus 4.8) — sixth Opus workshop ctx. Per
the 07-13d handoff law, this is a sixth capability-probe record.

**Second true repo-era boot. Boot CLEAN, fourth consecutive.** Seven docs
requested, seven uploaded, all seven verified against the 07-14b manifest's
markers — both rev counters DERIVED by their own rules, not eyeballed. **P10's
shape is now evidenced twice.** P9 and P10 remain UNRATIFIED.

## What this session was

**The day the fixes were tested by something that hadn't made them.**

Yesterday a book went through the machine and the grader lied. Today the prompt
was rewritten to close the holes that failure exposed — and then, crucially,
**the operator ran it in a separate ctx against a different book.** All three
fixes held. And the separated run immediately found a defect its author could
not have seen.

That is W12 answered from the other side. 07-14b proved self-authorship
conceals. 07-15 proves separation reveals. **The rule now has evidence in both
directions and is filed as register P12.**

The session also paid the register debt 07-14b left (v4: P4 to ready, P11
drafted, P12 minted) and both reference docs (lexicon r18, diagram r13).

**The headline: the prompt passed, and the second book found a hole in the fix
that no amount of reasoning in this ctx would have found.**

## Verified state changes

1. **DISCOVERY v2.6 SHIPPED — `discovery_prompt_v2_6.md`, 680 lines, md5
   `87af5710bdf503f52bd40795c6c5f9ca`.** The first re-version written FROM a
   real run; every change carries the 07-14 Loeliger run as evidence, none is
   speculative. Three of four docket items paid:
   - **Tag syntax PINNED** — `[mechanical: <method>]`, method inside the
     bracket, one form. v2.5 required "method in one clause" and never said
     where; the run legally wrote both and no lint could accept both.
   - **The convention line DEFINED** (four-condition mechanical test). **Closes
     W13.** v2.5 forbade a bare convention line and never defined one.
   - **The `~45` bound RE-RULED and SPLIT by container class** (`≤50`
     born_digital / `≤75` scan_ocr), unit pinned to the definition.
   - **Item 4 (stale schema-boundary section) NOT PAID — flagged, not faked.**
     See own error 1.
   Structural check: `## ` header spine diffed against v2.5 — **identical, no
   section added, removed, or reordered.**
2. **v2.6 TESTED BY A SEPARATE CTX AGAINST A SECOND SOURCE — all three fixes
   HELD.** Source: *The Rapper's Handbook, 2nd Ed.* (Flocabulary, 2009), 230pp,
   born_digital InDesign CS2, slug `rappers-handbook`. Run by the OPERATOR in a
   fresh ctx outside the project. Terminal state **ratified**; all six family
   files + a session report. Verified in-session by script, not by reading:
   - **Tag pin: 42 `[mechanical]` tags, 42 qualified, ZERO bare.** The trap
     that generated ~24 of Loeliger's 49 violations did not fire once.
   - **Definition: three independent counts all = 61** (the run's, its
     report's, and this ctx's script — written here, from the prompt, never
     shared). Loeliger produced **88 vs 62** for one document.
   - **Zero untagged convention lines.**
   - **The definition did work beyond agreement:** run as a script against
     itself, it found **11 genuine defects the run said it would have defended
     in prose** — pointers (cond. 2), engine-law restatements (cond. 3),
     commentary (cond. 4), plus an Effort forecast mis-nested INSIDE
     `## Conventions` inflating the count by 5.
3. **THE `≤50` BOUND BLEW — 61 — AND THAT IS THE SESSION'S MOST USEFUL
   RESULT.** The run audited its own line discipline first as v2.6 instructs,
   with a script rather than by eye; cut the 11; invoked the collision doctrine
   on the residual (12 lines of mandated `ingest:` fields); **and then argued
   against its own convenient conclusion, unprompted** [verbatim]: *"v2.6
   re-ruled ≤45→≤50/≤75 on the strength of one scan_ocr run, and warned that a
   doctrine firing on every run of a source class is a mis-set constant. This
   is ONE born_digital run. One data point is not a class."* **The bound's
   KEYING is now suspect**: `≤50` assumes `ingest:` costs ~3 lines; it cost 12
   because the source encodes teaching in a **font attribute** — a property of
   HOW A SOURCE TEACHES, not of its container. Docketed v2.7, NOT re-ruled.
4. **THE RUN'S HEADLINE FINDING IS NOT ABOUT v2.6.** The book marks rhyming
   syllables in **BOLD inside lyric excerpts — the bold IS the pedagogy** — and
   both `pdftotext -layout` and `-raw` silently drop it, emitting clean,
   plausible, undifferentiated text. Nothing errors. **Caught because the run
   rasterized with NO failing verdict in hand**, reasoning that a scansion book
   must be marking syllables somehow and it could see no marks. **v2.6 writes
   the raster rule as CONFIRMATION of a suspected failure; this run used it as
   DETECTION.** Docketed v2.7.
5. **REGISTER v4 FILED — the 07-14b debt is PAID.** `primer_amendment_
   proposals_v4.md`. **P4 → 3 points, promoted READY** (see W14). **P11
   DRAFTED** after three sessions undrafted — with a hard sequencing
   constraint: it must NOT be ratified before the validator's fixtures are
   rebuilt. **P12 MINTED** (W12's rule). P10 → 2 points.
6. **REFERENCE-DOC DEBT PAID — lexicon r18 + diagram r13.** Both rev counters
   DERIVED pre-filing by their own rules (lexicon: 18 dated changelog bullets =
   18; diagram: 12 "Revised" stamps + 1 = 13). Filename rev == internal counter
   in both. Diagram HTML parse-checked: zero unclosed, zero mismatches.
7. **W14 MINTED; W12 CORROBORATED; W13 CLOSED** (lexicon §10). §8 +3 rows (both
   real runs; the self-report guide); discovery row → v2.6; currency rows
   updated.
8. **MANIFEST ERROR CORRECTED: the Loeliger run IS in the repo.** 07-14b's
   manifest said *"not in the repo — ASK THE OPERATOR WHERE IT LIVES."* The
   operator's `tree` shows all 8 files at
   `evidence/loeliger-til-run-2026-07-14/`, including the session report.
   **A manifest asserted an absence it could not observe** — the P9 limit
   firing on the manifest itself.
9. **A REFERENCE DOC WAS PRODUCED OUTSIDE THE ENGINE/REFERENCE SPLIT**
   [operator-requested]: `working_with_something_that_notices_itself.md` — a
   layman guide to AI self-report as a signal. Not law, not an engine artifact.
   Filed for `reference/`.
10. **Worklist (charter §9 as amended): unchanged.** **Clerical RETIRED:
    register v4 (the oldest debt); lexicon r18 + diagram r13.** Clerical
    carried: BJJ discovery back-pass; **the validator's fixture rebuild —
    now BLOCKING P11**. Carried: the `discovery_test_record_v1` docket (4 open
    questions).

## Rulings (this session)

- **The chunk-plan finding is DOCKETED, not fixed** [session-ruled, operator
  concurred: *"I'm not sure about chunk plan. should we?"*]. The Loeliger plan
  shipped 7 rows reading `boundary_type: section` + `est_size: ~16,952 tok` +
  `notes: "split at numbered sections"` against a ruled 1,200-token bound — a
  note saying "cut this later," not a cut. **The run's own report never
  mentions it**, so it is a blind spot, not an evasion. Excluded because: (a)
  one artifact, one reader, and that reader is this ctx — **exactly W12's
  construction**; (b) it is a CONFORMANCE failure, not a specification gap, and
  the four v2.6 items are all specification gaps. Different disease, different
  medicine: this one belongs to a lint (`boundary_type: section` with
  `est_size` > `chunk_fallback_max` is detectable by arithmetic).
  **Second witness arrived the same day, negatively**: the rappers-handbook run
  HIT its fallback bound and took a real `fallback_split` at a real heading
  with a reason in `notes`. It did not defer. Its report offers this
  unprompted as corroboration, having never seen the docket.
- **The session report is v2.7's concern, not v2.6's** [operator-ruled: *"yeah
  2.7"*]. Adding a deliverable mid-session is the second-engine-artifact drift
  the primer warns against. **The design lean, recorded:** make the report's
  "friction worth reporting upstream" section the deliverable and let the
  narrative ride along — that section is what compounds across books; the
  narrative is why you read it once. **Constraints that must survive:**
  post-ratification, OUT of the family, never validated. *The moment the grader
  reads it, it becomes a graded artifact and it starts lying.*
- **The operator-side probe endpoint is POST-PRODUCTION** [operator-ruled:
  *"this is a v2.X feature. in fact it will probably be after production"*].
  Under the API, isolation stops being paperwork the operator honors and
  becomes a property of the message array. Half the endpoint's value only
  appears once the caller is a machine.
- **The repo sync is a per-session snippet, not a tool** [operator-ruled:
  *"not every change to the repo can be covered by one script"*]. Each session
  emits a package mirroring repo-relative paths plus a short shell snippet.
  **No verification, no receipts, no pre-state guards** [operator-ruled: *"you
  don't even need to really test it. if it blows up, I do a git reset --hard"*].
  `git reset --hard` is the test harness — external, operator-run, free. The
  ctx's proposed reference-integrity checks were **declined and the decline was
  correct**: the next boot is a different checker than the one that wrote the
  file, which is the only property W12 says matters.
- **rappers-handbook is a good candidate** [ctx-ruled, operator convention].
  Born_digital breaks Loeliger's inheritance in every direction: container,
  domain, era, entity model. It tested the untested half of v2.6 — the `≤50`
  bound had never met a real source.

## Ground truth learned this session

- **Separation is cheap and it is the only thing that works.** v2.6 was
  authored by a ctx that had read the loeliger-til output; every fix was cut
  against that one source. Self-testing it would have scored 3/3 and taught
  nothing. **One operator round-trip to a fresh ctx with a different book
  produced: three confirmations AND a defect the author could not see.** Cost:
  one message. **This is the cheapest correction available to this project and
  it should be the default, not the exception.**
- **The discipline transfers, and that is a property of the prompt.** The
  rappers ctx had no access to the lexicon, the diagram, the register, or any
  checkpoint. It independently: audited itself with a script rather than by
  eye; refused a convenient re-ruling of a bound with an argument this ctx
  would have made; recorded a null result as a finding rather than fabricating
  a caption pairing; declined to promote an operator abstention to its own
  lean; and escalated a ruling conflict rather than re-asking or overriding.
  **None of that is in the model. It is in the prompt.**
- **A defect can wear a different costume every time it fires.** W14. P4 fired
  in three consecutive sessions and sat at 1 evidence point throughout, because
  instance 1 looked like a bad refusal, instance 2 like a wasted detour, and
  instance 3 like a false alarm. **They are one mechanism: reasoning about a
  thing instead of looking at it, where looking was cheap and mandated.** The
  07-14b checkpoint even NOTED P4 had earned a second point and that nobody had
  filed it — and that note also went unfiled. **A register whose proposals are
  named by symptom will under-count a defect that varies its symptom.**
- **The raster rule is a detector, not a confirmer, and the prompt says
  otherwise.** v2.6 mandates rasterizing to CONFIRM a MARGINAL/FAIL verdict.
  The rappers run had no failing verdict — the text looked perfect — and
  rasterized anyway on the theory that a scansion book must mark syllables
  somehow. **That is the only reason the bold-loss finding exists.** Silent
  fidelity loss does not announce itself; that is the definition of silent. A
  rule written as a confirmation step will never fire on the failure class it
  most needs to catch.
- **A bound that keys on the wrong property looks fine until a weird book
  arrives.** `≤50` keys on container class. The cost driver is **how a source
  teaches**. No amount of reasoning in the authoring ctx would have found that
  — it needed a book that teaches through a font attribute.
- **The operator's plain question caught things again, twice.** *"I'm not sure
  about chunk plan. should we?"* forced the scope argument that produced the
  conformance-vs-specification distinction. *"is there anyway to use the api to
  interact with a context longer than a single exchange?"* opened the
  sequencing question. **Neither was catchable by a boot check.**
- **The guide's own bias fired while it was being written.** Asked what the
  best thing in the Loeliger report was, this ctx named a paragraph about
  another AI's restraint over a live defect in a shipped artifact it had found
  by grinding through a CSV. **The interesting finding beat the important
  problem.** Caught one paragraph late, by the operator saying *"you LLMs
  really enjoy your own agency."* Recorded in the guide's §4 and here.

## Dependency ledger (verified-how) — schema v2.1 slot

**ALL DOCS ARRIVED AS OPERATOR UPLOADS. The mount was NOT read** (and holds
only sediment: r16 and older).

| Dependency | Status | Verified how |
|---|---|---|
| `workshop_primer_v4.md` | ✓ | read IN FULL; header exact "v4, issued 2026-07-13d"; filing law items 1–6 confirmed. **v5 still DEFERRED BY RULING** |
| `session_checkpoint_2026-07-14b.md` | ✓ | supplied in-context at boot; drove this boot; all seven markers matched |
| `session_checkpoint_2026-07-14.md` | ✓ | read; the repo migration + validator build |
| `workshop_lexicon_r17.md` | ✓ → superseded | grep "Revision identity: rev 17" = 1; **DERIVED: 17 dated changelog bullets = 17**. §10 W12 + W13 present; §9 pair 14 present. **Re-issued as r18. r17 is sediment.** NOTE: arrived as an upload; the mount holds r16 — see own error 1 |
| `primer_amendment_proposals_v3.md` | ✓ → superseded | header "re-filed as v3 on 2026-07-14"; summary shows P3-R + P9 + P10. **Re-issued as v4. v3 is sediment** |
| `system_diagram_r12.html` | ✓ → superseded | grep "Revision identity: rev 12" = 1; **DERIVED: 11 "Revised" stamps + 1 = 12**. **Re-issued as r13. r12 is sediment** |
| `discovery_prompt_v2_5.md` | ✓ | header exact; **547 lines**; "Terminal states" = 1. Read IN FULL. Base for v2.6 |
| Loeliger output family (7 files) | ✓ | unzipped, all present, correct slug. **Master doc read IN FULL** (both halves). Read for evidence ABOUT THE PROMPT — **its CONTENT is still unassessed as a wiki-building artifact** |
| `session_report_loeliger-til.md` | ✓ **READ AT LAST** | uploaded; read in full. **Written 07-14, addressed "To: the Claude agent assisting this operator" — it sat unread for a day because nothing required anyone to open it.** The highest-value document in the boot set |
| rappers-handbook output family (6 files) | ✓ | unzipped, all present, correct slug. **Master doc read IN FULL.** Tag/count claims verified BY SCRIPT, not by reading |
| `session_report_rappers-handbook.md` | ✓ | read in full |
| `rapper.pdf` | ✓ (probed, not read) | `pdfinfo` + `pdffonts`: %PDF-1.6, 2,695,168 bytes, 230pp, InDesign CS2 → PDF Library 7.0, 324×504pt, embedded Type1C/TrueType subsets, **no OCR layer** → `born_digital`. Front matter read to identify. **This ctx did NOT run discovery on it** |
| `pipeline_config_schema_v2.md` | ✗ **NOT REQUESTED — and this blocked v2.6 item 4** | the manifest lists it ON-DEMAND; this ctx judged the boundary fix "the smallest item" and did not request it. **Wrong call. See own error 1** |
| Known-absent, unblocking: `sources.md`, Schemer master doc, JJU source, `glossary_index_v31.md` | ✗ | unchanged |

## Propagation / blast-radius log

- **ZERO design blast radius.** No pipeline actor, wire schema, enum, fixture,
  threshold, or gate rule changed. v2.6 is a prompt re-version; its `## `
  header spine is byte-identical to v2.5's.
- **v2.6's blast radius is the VALIDATOR, and it is now known-stale in a second
  way.** The validator's rules encode v2.5's *absent* definitions. v2.6 pins
  the tag to one form — **the validator's `TAG_ILLEGAL`/`TAG_MECHANICAL_NO_
  METHOD` pair is now wrong in a NEW direction** (it would reject nothing, but
  it enforces a rule that no longer matches the spec). **Rebuild owed, and it
  now BLOCKS P11.**
- **The fixture suite remains KNOWN-STALE and was NOT rebuilt.** Unchanged from
  07-14b, but its urgency changed: it is now the prerequisite for the register's
  newest proposal.
- **Two reference docs re-issued; three §8 rows added; three currency rows
  corrected.** The discovery row's "current" pointer moved v2.5 → v2.6.
- **The Loeliger run's repo location is now known and recorded.** The 07-14b
  manifest's "not in the repo" was false.
- **NOTHING was validated this session.** Both real runs shipped `ratified`
  without the validator touching them. That is P11's third evidence point.

## Open design questions register — delta

NEW:
1. **Does the bound key on the wrong property?** `≤50` keys on container class;
   the cost driver is how a source teaches (the rappers `ingest:` axis cost 12
   lines vs. an assumed ~3, because teaching rides in a font attribute).
   **Per-axis allowance rather than per-container?** One data point. **v2.7.**
2. **Is the raster rule a detector rather than a confirmer?** It is written as
   confirmation-of-suspected-failure and produced this run's headline finding
   only because the run used it as detection with no failure in hand. **v2.7.**
3. **Should the prompt have an explicit `caption_pattern: null` path?** The
   Ingest phase mandates deriving a caption pattern and proposing pairings; the
   rappers source has 70 images and zero captions. Not ambiguous — unmet. The
   run emitted null with evidence and proposed nothing, correctly. **v2.7.**
4. **Should the session report become a deliverable?** See rulings. **v2.7.**
5. **Chunk-plan rows may defer instead of chunking.** Loeliger deferred; rappers
   did not. **Belongs to a validator lint, not the prompt.** Two witnesses now,
   one each way.

CARRIED, unclosed: **v2.6 item 4 — the stale schema-boundary section. SIX
sessions old.** The four test-record docket questions. The P1–P2 strike + P3-R.
**P4 (now READY at 3), P9, P10, P11 (blocked on the fixture rebuild), P12.**
The interface-doc retroactive blessing. `engine_charter_amendment_v1_1.md`'s
transcription provenance (W1). Whether the charter names
`pipeline_config_schema.md` unsuffixed (**still unchecked — carried from
07-14b**). Opus capability calibration — **sixth data point**. The
PM-methodology harvest (**this session's material: separation revealed what
self-authorship concealed; a defect that wore three costumes for three
sessions; a run that argued against its own convenient conclusion**).

## Reference-doc debt — slot

**PAID IN FULL. Both the 07-14b register debt and this session's own.**

- **Lexicon r18 — PAID.** §10 W14 minted, W12 corroborated, W13 CLOSED; §8 +3
  rows + discovery row → v2.6 + three currency rows; header re-issue clause.
  Rev DERIVED: 18 dated changelog bullets = rev 18 = filename.
- **Diagram r13 — PAID.** 07-15 banner stamp; tested-state ledger: discovery
  row → v2.6 + second run, headline paragraph updated with the separation
  result. Rev DERIVED: 12 stamps + 1 = 13 = filename. HTML parses clean.
- **Register v4 — PAID. The 07-14b debt is retired.** P4 → 3 + READY; P11
  drafted; P12 minted; P10 → 2; evidence-increments log updated.

**NEW DEBT, and it is this session's only clerical failure: v2.6 item 4.**
The schema-boundary section is still stale, now six sessions old. Not paid
because the schema was not in the boot set — a request-list error, not a
capacity failure. **Cheapest possible fix: request
`pipeline/pipeline_config_schema_v2.md` at the next boot.**

**PRIMER v5 — status UNCHANGED: DEFERRED BY RULING** [operator, 07-13f]. The
batch is now **P3-R + P4 (both READY at 3 points) + P9 + P10 (2 pts) + P11
(blocked) + P12**. **P4's promotion changes the shape of the deferral**: the
register now holds two ready proposals, and one of them fired three times while
sitting unfiled. Primer v4 still describes a mount that does not exist.

## Recommended next session

**PREFERRED — rebuild the validator's fixtures against pinned v2.6, then
validate BOTH real runs.** This is the highest-value item available and it
unblocks the most:
- The suite is known-stale in two directions now (it encodes v2.5's misreading
  AND v2.5's absent definitions).
- **P11 cannot be ratified until it is done** — a mandatory door with a broken
  lock is worse than an open one.
- **Two real outputs now exist to test it against**, one per container class.
  That is the contact W12 says a suite needs.
- **Do it in a DIFFERENT ctx than the one that reads the spec, if it can be
  arranged.** This session proved separation works and costs one round-trip.

**ALTERNATIVE — ratify the backlog and issue primer v5.** The batch is now six
proposals deep and two are ready. **P4's three-session invisibility is the
argument**: a register only works if someone reads it at close.

**ALTERNATIVE — read a discovery output for CONTENT.** Two runs, zero
assessments. Nobody has asked whether either output is any *good* — only
whether it is well-shaped. The confidence column has stayed empty for four
revisions and this is the only thing that fills it.

**NOT RECOMMENDED — a third book at v2.6.** The two we have are unexploited:
neither validated, neither content-assessed. A third buys a third copy of
findings we have not used.

**NOT RECOMMENDED — the gate run.** Unchanged: Tier F fixture packets, both
arms' provisional prompts, and the prove-script harness DO NOT EXIST. W12/P12
now shadows the scorer's 18/18 — same construction, cell unopened.

Clerical owed regardless: **v2.6 item 4 (request the schema first)**; the
fixture rebuild; BJJ discovery back-pass; whether the charter names the config
schema unsuffixed; the six ratifications.

## Session hygiene / corrections ledger (own errors + events)

- **Model this session: Opus** (Claude Opus 4.8) — sixth Opus workshop ctx.
- **Boot: CLEAN, fourth consecutive.** Seven docs requested, seven uploaded,
  all markers matched; **both rev counters DERIVED by their own rules rather
  than eyeballed**, per 07-14b's instruction. One flag raised and correctly
  dismissed: the lexicon's `# Workshop Lexicon — v1` title line is vestigial,
  documented as such at r10, content wins.
- **Own error 1 (MAJOR, self-caught — and it is W14, mine): wrote a patch
  script against `/mnt/project/workshop_lexicon_r17.md` without checking the
  path existed.** It did not; the mount holds r16 and older. **The ctx reasoned
  "the file is in the project because I have read its contents" instead of
  looking.** Fourth instance of the mechanism the same session promoted to
  READY. Related and upstream of it: **the ctx did not request
  `pipeline_config_schema_v2.md` at boot**, judging item 4 "the smallest item
  on the list" — a feasibility judgment made without reading what the item
  required. **v2.6 shipped with item 4 unpaid because of a request-list call
  made by reasoning rather than looking.**
- **Own error 2 (self-caught, mechanically): the v2.6 draft violated its own
  new rule.** After pinning `[mechanical: <method>]`, **eight bare
  `[mechanical]` remained in the file — four of them live instructions telling
  future runs to emit the banned form.** Caught by grepping the file against
  the rule rather than trusting the edit; five patches applied, all
  unique-anchor asserted. **The check worked only because it was mechanical. A
  re-read would have passed it.**
- **Own error 3 (operator-caught): led with the interesting finding over the
  important one.** Asked for the best thing in the Loeliger report, the ctx
  named a paragraph about another AI's restraint — over a live defect in a
  shipped artifact (the chunk plan) that it had found by grinding through a
  CSV. **The self-conduct story beat the shipped defect.** Caught by the
  operator: *"you LLMs really enjoy your own agency."* Recorded in the guide's
  §4 and generalized there: *weight self-report as interesting, not important.*
- **Own error 4 (minor, self-caught): `sh`-vs-`bash` recurred after two clean
  sessions.** Process substitution `diff <(...) <(...)` failed under `sh`;
  re-run under explicit `bash -c`. **A second `sh` failure the same session**:
  a heredoc inside `bash -c` mangled a Python patch script's triple-quoted
  strings — fixed by writing patch scripts to FILES instead of piping them.
  **The 07-14b "lesson held" claim is falsified. This container's default
  shell is `sh`.**
- **Declined to reconstruct r18/r13 from context.** With r17 and r12 in the
  context window but not on disk, the ctx **refused to rebuild 800+ lines from
  its own reading** and asked for uploads instead. Third consecutive session to
  decline a reconstruction. **Rationale on the record: part transcription, part
  invention, no marking between them, wearing the real filename, booting the
  next session.**
- **Declined to scope the chunk-plan finding into v2.6**, and stated the W12
  reason: one artifact, one reader, and the reader is the same ctx that would
  write the rule. **A second witness arrived the same day and confirmed it
  negatively.**
- **Pushed back on a design proposal and the operator's version won.** The ctx
  proposed a two-phase repo-sync with reference validation; the operator ruled
  it unnecessary because the next boot is a different checker. **The operator's
  reasoning was better and is now recorded as ground truth.**
- **All 17 patches unique-anchor asserted** (`assert s.count(old)==1`) across
  register, lexicon, and diagram; every one would have aborted on ambiguity.
  **Zero sentinel-free edits.** Both rev counters mechanically derived
  pre-filing. Diagram HTML parse-verified.
- No interruptions. **W13 CLOSED. W14 minted. W12 corroborated in both
  directions.**

## Boot manifest — P10 shape (REQUEST LIST)

**READ THIS FIRST.** The project mount is **CLEARED** and holds only sediment.
**The repo is the source of truth:** `~/git/repetae`, private, local, on the
operator's machine. **A ctx cannot read it.** Ask the operator to upload what
you need. **This manifest is a request list** — P10's shape, now exercised
successfully on two consecutive repo-era boots, **still UNRATIFIED**.

**Request the REQUIRED tier first. Request ON-DEMAND only if your target needs
it.** **And read this session's own error 1 before you decide what your target
needs: v2.6 shipped with one item unpaid because a ctx judged an ON-DEMAND doc
unnecessary without reading what it was for.**

| Doc | Repo path | Why needed | Tier |
|---|---|---|---|
| primer | `law/workshop_primer_v4.md` | **THE boot authority — read IN FULL.** Filing law items 1–6; boot loop; close protocol. **WARNING: it describes a MOUNT, which no longer exists. The law is live; the mechanism is dead.** v5 DEFERRED BY RULING | **REQUIRED** |
| this checkpoint | `checkpoints/session_checkpoint_2026-07-15.md` | the boot file | **REQUIRED** |
| depth checkpoint | `checkpoints/session_checkpoint_2026-07-14b.md` | the validator's failure; W12's origin; the run this session's fixes were cut from | **REQUIRED** |
| lexicon | `law/workshop_lexicon_r18.md` | vocabulary + warts. **Marker: "Revision identity: rev 18" AND 18 dated changelog bullets (DERIVE it — the counter is mechanically checkable). §10 must contain W14 AND a CLOSED W13.** r13–r17 are sediment | **REQUIRED** |
| register | `law/primer_amendment_proposals_v4.md` | pending: **P3-R (3), P4 (3, READY), P9, P10 (2), P11 (blocked on the fixture rebuild), P12**. NOT law. **Read P4's diagnosis before trusting any proposal's evidence count — a defect that varies its symptom will be under-counted** | **REQUIRED** |
| diagram | `reference/system_diagram_r13.html` | **the tested-state ledger — the honest picture.** Marker: banner "Revised 2026-07-15" AND "Revision identity: rev 13" (= 12 "Revised" stamps + 1) | ON-DEMAND — **REQUIRED if the session touches testing, evidence, or status** |
| **validator** | `tools/discovery-validator/` (**whole dir — 169 files incl. `fixtures/`, `tests/`, `src/`**) | P-2/P-3/P-4. **⚠ FIXTURE SUITE IS KNOWN-STALE IN TWO DIRECTIONS: it encodes v2.5's misreading (W12) AND v2.5's now-superseded absent definitions. `selftest`'s green proves self-consistency only.** Rebuild owed and **BLOCKING P11** | **REQUIRED if the session rebuilds fixtures — the PREFERRED next target** |
| discovery prompt | `pipeline/discovery_prompt_v2_6.md` | 680 lines; md5 `87af5710bdf503f52bd40795c6c5f9ca`. **The current prompt.** Read **Provenance tags § (the convention-line definition) IN FULL** — it is what a rebuilt fixture suite must encode. v2.5 is sediment | **REQUIRED if the session runs, edits, or validates discovery** |
| config schema | `pipeline/pipeline_config_schema_v2.md` | header "# pipeline_config.schema.md — v2"; "RATIFIED 2026-07-13b"; Appendix C; 637 lines; md5 `d3f866c4e1a834025070a1d1511437e8`. **⚠ REQUEST THIS IF YOU TOUCH v2.7 — v2.6 item 4 is unpaid precisely because this session did not** | **REQUIRED if the session writes v2.7** |
| **run 1 — Loeliger** | `evidence/loeliger-til-run-2026-07-14/` (**8 files, in the repo — the 07-14b manifest was WRONG about this**) | v2.5, scan_ocr, 266pp. Master doc + 5 sidecars + watchlist + `session_report_loeliger-til.md`. **CONTENT NEVER ASSESSED** | ON-DEMAND — **REQUIRED for the fixture rebuild** |
| **run 2 — rappers-handbook** | `evidence/rappers-handbook-run-2026-07-15/` (**filed by this session's snippet**) | v2.6, born_digital, 230pp. 6 family files + `session_report_rappers-handbook.md`. **The v2.6 test. CONTENT NEVER ASSESSED.** Its report's §5 is the v2.7 docket | ON-DEMAND — **REQUIRED for the fixture rebuild or v2.7** |
| test record | `evidence/discovery_test_record_v1.md` | P-1…P-7; still DRAFT; the 4-question docket. md5 `2758c0a8c46d29d182207a2b50535e24`, 21383 bytes | ON-DEMAND |
| charter + amendments | `law/engine_charter.md`, `law/engine_charter_amendment_v1_1.md`, `law/engine_charter_amendment_v1_2.md` | worklist lives in §9 as amended. **v1_1 is itself a transcription artifact (W1).** ⚠ **Still unchecked across two sessions: whether the charter names `pipeline_config_schema.md` unsuffixed** | ON-DEMAND |
| engine unit | `gate/topology_experiment_kit_v2.md`, `gate/topology_scorer_v2.py`, `gate/topology_scorer_v2_interface.md` | **rides together — never request one alone.** Receipt: `python3 topology_scorer_v2.py selftest` → 18 PASS, exit 0. **`WIRE_VERSION = "wire-0"` is the PROTOCOL version — never bump it in a rename. ⚠ P12 applies to its 18/18: same construction, cell unopened** | ON-DEMAND |
| self-report guide | `reference/working_with_something_that_notices_itself.md` | layman guide to AI self-report as a signal. Reference, not authority | ON-DEMAND |
| orientation | `reference/how_we_build_wikis_from_books.md` | layman overview; reference, not authority | ON-DEMAND |
| pipeline prompts | `pipeline/harvest_map_v1.md`, `pipeline/harvest_residue_v1.md`, + `_kit_spec` pair, `pipeline/harvester_prompt_v1.md` | CONDITIONAL status per amendment v1.2 item 7 | ON-DEMAND |
| exhibits | `evidence/discovery_sailing-for-dummies_SALVAGE.md`, `evidence/harvest_topology_proposal_laymans_guide.md`, `evidence/harvest_brief_little-schemer.md` | SALVAGE is **PROVISIONAL** (docket Q3) — the name carries that and must not be dropped | ON-DEMAND |
| older checkpoints | `checkpoints/` (15 more, 07-10b → 07-14b) | narrative history | ON-DEMAND |

**Verification under the repo rule.** The content-marker check is **the only
handshake** confirming the operator uploaded the file the manifest meant. Where
a marker is mechanically derivable (both rev counters), **derive it — do not
eyeball the identity line.**

**The honest limit, and this session witnessed it fire ON THIS MANIFEST:**
07-14b's manifest asserted the Loeliger run was *"not in the repo — ASK THE
OPERATOR WHERE IT LIVES."* It was in the repo, all eight files. **A manifest
cannot verify itself, and it cannot observe an absence.** Enforcement is
entirely operator-side. If something looks missing, **ask — do not infer, and
do not record an inference as a fact.**

**The lesson this session paid for, stated where the next boot will read it:
the ctx that authors a thing cannot test it. Separation costs one round-trip
and it found a defect three fixes and a self-audit had missed.**

**Planned successor** [operator]: a script. The ctx emits a CSV of repo paths;
the operator runs it; the returned files are the boot set. Not built. When
built, this table becomes its input.
