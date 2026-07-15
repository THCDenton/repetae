# Session checkpoint — 2026-07-14 (the repo migration + the discovery validator)

Purpose: boot file for the next session. **Files are the only memory — and as
of this session, the files live in a git repo, not a project mount.** Written
under checkpoint schema v2.1 (five mandatory slots, boot manifest last), with
the manifest slot rewritten per P10. Reads alongside 07-13g.
**Model this session: Opus** (Claude Opus 4.8) — fourth Opus workshop ctx.
Per the 07-13d handoff law, this is a fourth capability-probe record.

**THIS CHECKPOINT IS A HYBRID AND SAYS SO.** It is the last checkpoint written
from a project mount and the first written for a repo-era boot. Its boot
manifest is a REQUEST LIST (P10 shape), not a mount-currency table — but P9
and P10 are **UNRATIFIED PROPOSALS**, not law. If the next boot finds a
populated mount, the 07-13g manifest's rules still apply and this manifest is
a request list the ctx does not need. If the next boot finds an empty mount,
this manifest is the only path forward. **It is written to work either way,
and that dual-purpose is a compromise, not a design.**

## What this session was

A **migration session**, and the second in two days — but one level up. 07-13g
migrated three files to suffixed names to retire W11 for those files. This
session **retired the mount itself.** The operator ruled the project cleared
and the git repo (`~/git/repetae`, local, private) the single source of truth.
The migration was performed live: 36 project files placed into a directory
structure, verified, committed.

The session also **built one tool** — the discovery output validator (P-2 +
P-3 + P-4 from the test record) — and **paid the project's oldest clerical
debt** (W9, five sessions).

It also produced the session's sharpest self-inflicted lesson: **the ctx spent
three turns searching transcripts for files that were sitting on the mount it
had already inventoried twice.** See Session hygiene.

## Verified state changes

1. **THE REPO MIGRATION PERFORMED — the mount is retired as source of truth.**
   Structure built and populated at `~/git/repetae`:
   - `law/` (6) — primer v4, lexicon r16, charter + amendments v1_1/v1_2,
     register v3
   - `pipeline/` (7) — discovery v2.5, harvester v1, harvest map/residue +
     kit specs, **`pipeline_config_schema_v2.md`**
   - `gate/` (3) — kit v2, scorer v2, scorer interface v2 (the engine unit)
   - `evidence/` (4) — test record, SALVAGE exhibit, topology guide, Schemer
     brief
   - `reference/` (2) — orientation doc, diagram r11
   - `checkpoints/` (14) — full history, 07-10b → 07-13g
   - `tools/discovery-validator/` — this session's build
   **Operator-verified via `tree`; duplicates removed; structure confirmed
   clean.**
2. **W9 IS DEAD — `pipeline_config_schema_v2.md` filed after FIVE sessions of
   lag.** The operator located the 07-13b download. Verified on arrival: header
   `# pipeline_config.schema.md — v2`; `RATIFIED 2026-07-13b` present;
   Appendix C present; 637 lines (v1 was 343); md5
   `d3f866c4e1a834025070a1d1511437e8`. **Filed into the repo under the SUFFIXED
   name** (`_v2`) per filing law item 4 — the mount had carried it unsuffixed,
   which was the W11 trap. **This was the project's oldest unretired clerical
   debt and the largest remaining stem-stable hazard. Both now gone.**
3. **THE DISCOVERY VALIDATOR BUILT AND SHIPPED —
   `tools/discovery-validator/`.** Implements P-2 (forecast quarantine), P-3
   (provenance-tag lint), P-4 (output-family conformance) from
   `discovery_test_record_v1.md`. ~400 lines Python, zero dependencies.
   **Receipt, run by the OPERATOR on his own machine post-migration:
   `python3 tests/selftest.py` → 19/19 PASS, SELF-TEST GREEN.** Not a ctx
   claim — operator-executed, output pasted back.
4. **The validator's fixture suite: 1 valid run + 18 negative runs, each
   breaking EXACTLY ONE rule.** The self-test asserts **specificity**: each
   negative must raise its own code and no other. A validator whose codes lie
   sends an operator chasing the wrong defect.
5. **Register re-filed as `primer_amendment_proposals_v3.md`. P9 + P10 added.**
   P9 files the repo rule; P10 files the boot-manifest schema change P9
   requires. **Both UNRATIFIED, 1 evidence point each** — drafted from a ruling,
   not from accumulated failures. P3-R remains the ready batch at 3 points.
   v2 is sediment.
6. **Boot: CLEAN, second consecutive.** All 07-13g manifest markers matched.
   Scorer live run at boot → 18/18 GREEN, exit 0. **W11 did not fire on the
   migrated artifacts, exactly as 07-13g predicted.** The 07-13g migration is
   now VINDICATED by a clean boot, not merely asserted.
7. **Worklist (charter §9 as amended): unchanged. No worklist item built.**
   The validator is a *tool*, not a worklist item — it is P-2/P-3/P-4 from an
   unratified test record. **Clerical RETIRED: config-schema v2 re-file (W9,
   five sessions).** Clerical carried: discovery v2.6 re-version; BJJ discovery
   back-pass. Carried: the `discovery_test_record_v1` docket (4 open questions).

## Rulings (this session)

- **The repo is the single source of truth; the mount is cleared**
  [operator-ruled, verbatim: *"everything lives on the git repo... no more
  expired files, no more junk. single source of truth is the repo"*]. Filed as
  P9. **Not yet law** — needs ratification into primer v5.
- **Sediment stays local, out of the repo AND out of the project**
  [operator-ruled]. 15 superseded files live on the operator's machine,
  unversioned, retrievable on request. **Note the wording shift this forces:
  the repo is the single source of truth for CURRENT state, not for
  everything.** Recorded in P9.
- **Commit the config schema as-is rather than chase perfection**
  [operator-ruled: *"a single source of truth that's out-of-date is better than
  multiple sources in different states of currency"*]. **Superseded within the
  same session** — the ctx pushed back (an unsuffixed file whose header says v2
  is not merely stale, it is *indistinguishable from current by its own
  markers* — the 07-13g false-positive-marker trap), and the operator then
  located the real v2. **The pushback was correct and the debt died.**
- **Version suffixes survive the migration** [operator-ruled]. Git could carry
  rev identity via tags; it will not. Filing law items 1–6 stay intact; only
  the *mechanism* changes (operator runs `ls` against the repo, not a ctx
  against a mount). Rationale: changing two conventions at once is how
  migrations go wrong.
- **Hard fail, no tiers, for the validator** [operator-ruled: *"right now
  simple pass/fail"*]. Any violation fails the run. A watchlist at 21 rows
  blocks everything. Tiering deferred until failure classes are understood in
  practice. **The ctx leaned tiered and was overruled; the ruling is cleaner
  and is recorded as the operator's.**
- **Logic in scripts, Node-RED as wiring** [operator-ruled: *"we'll write
  scripts, consumed by red, but they live in the repo and will have their own
  unit test suite"*]. Node-RED calls tools via exec; the brain never lives in
  flow JSON.
- **Python, not JavaScript, despite Node-RED being a JS tool** [operator-ruled
  after the ctx flagged the inconsistency]. Rationale: the scorer is already
  Python and Node-RED shells out identically to either. **Two runtimes is worse
  than one arguably-wrong one.**
- **Reconstruction from transcripts REFUSED — second consecutive session**
  [session-ruled; operator instruction declined with reasons; the files were
  then found on the mount]. The operator asked the ctx to rebuild
  `session_checkpoint_2026-07-13g.md` from conversation search. Declined:
  search returned only *fragments*, and a reconstruction would have been part
  transcription and part invention **with no marking distinguishing the two**,
  wearing the real filename, booting the next session. **A fabricated scorer
  eventually fails a self-test. A fabricated checkpoint fails silently and
  every session after inherits the fiction.** Precedent: 07-13g's identical
  refusal; the SALVAGE doc.

## Ground truth learned this session

- **The structural fix beat the workaround AGAIN, one level up.** 07-13g's
  lesson was *prefer the fix that retires the protection*. This session applied
  it to the hazard class itself: the migration retired three files from W11;
  the repo retires **the mount**, and with it W11 and W9 entirely. **The
  pattern is now two-for-two and should be considered a project law in
  everything but ratification.**
- **The ctx wasted three turns searching for files it already had.** The
  operator said *"I might need help finding these files"* and the ctx adopted
  the framing without checking it — running `conversation_search` twice, then
  declining to reconstruct, when **every missing file was on the mount it had
  already inventoried twice in the same session.** The fix was one `cp` loop.
  **Diagnosis: the ctx pattern-matched on the operator's framing instead of
  on its own verified state.** This is a NEW failure mode, distinct from the
  07-13d "concludes before reading" pattern — here the ctx *had* read, and
  then ignored what it read because the operator's words pointed elsewhere.
  **Recorded as W12 candidate; see below.**
- **A receipt executed by the operator on his own machine is the strongest
  receipt available.** The validator's 19/19 was not a ctx claim about a ctx
  run — the operator ran it post-migration in the real repo and pasted the
  output. **That is the only class of receipt that survives the ctx being
  wrong about itself** (the P3-R failure class). Worth generalizing: after any
  migration, the receipt should be re-run by the operator, not the ctx.
- **The validator has the scorer's cell, and its own README says so.** Green
  against 18 fixtures the ctx authored from a spec the ctx read. **Green means
  the code implements the spec. It does not mean the spec matches reality.**
  Only one ratified discovery run exists (sailing, 07-09) and it predates
  several checked rules. **First real discovery run is the first honest test.**
- **The contract binds shape, never truth.** Recorded three times in the
  validator's own files at the operator's framing: *"it's a contract for us
  goldfish — once it's set in stone, we can back out."* True — and the limit is
  that a fabricated `[operator-decided]` tag on a ruling no operator made is
  perfectly well-formed and passes clean. **P-5 (provenance integrity) is not
  buildable as a lint. Do not let a green envelope be read as a green run.**
- **A contract is only a contract if it is the only door.** Agreed in-session,
  **and then not filed.** The validator is currently a script someone may
  remember to run. Making it the mandatory next stage after discovery is a
  filing-law question, not a code question. **UNFILED DEBT — see open
  questions.**
- **The mount was also a floor, and the repo removes it.** P9's strongest
  counter, recorded because it is real: on 07-13e and 07-13f a stale-but-
  present mount let those boots *degrade* rather than *die*. Under P9 an
  incomplete handover produces a ctx that can do nothing at all. **That is the
  right trade — loudly broken beats confidently wrong — but it is a trade.**

## Dependency ledger (verified-how) — schema v2.1 slot

| Dependency | Status | Verified how |
|---|---|---|
| `workshop_primer_v4.md` | ✓ | read at boot; header exact "v4, issued 2026-07-13d"; filing law items 1–6 confirmed. **Now at `law/` in repo.** v5 still DEFERRED BY RULING |
| `workshop_lexicon_r16.md` | ✓ | grep: "Revision identity: rev 16" = 1; "RECURRED A THIRD TIME 2026-07-13g" = 1; "RETIRED for the kit" = 1. **Now at `law/`.** **NOT re-issued this session — see reference-doc debt (r17 OWED)** |
| `system_diagram_r11.html` | ✓ | grep: "Revised 2026-07-13g" = 1; "Revision identity: rev 11" = 1. **Now at `reference/`.** **NOT re-issued — r12 OWED** |
| `session_checkpoint_2026-07-13g.md` | ✓ | read IN FULL (supplied in-context by the operator at boot); drove this boot; all markers matched. **Now at `checkpoints/`** |
| `topology_scorer_v2.py` | ✓ | **live run at boot: SELF-TEST GREEN, exit 0, 18 PASS** (under `bash -c`; `sh` mangles `$PIPESTATUS`). Re-verified post-copy into repo structure: GREEN. **Now at `gate/`** |
| `topology_experiment_kit_v2.md` | ✓ | header "# Topology Experiment Kit v2"; "FILING MIGRATION" note = 1; §7-M present (7 hits). Read §7-M in full. **Now at `gate/`** |
| `topology_scorer_v2_interface.md` | ✓ | header "# Topology Scorer v2 — behavior (layman) + interface reference". **Now at `gate/`** |
| `pipeline_config_schema_v2.md` | ✓ **W9 RETIRED — FIVE-SESSION DEBT PAID** | operator supplied the 07-13b download. header "# pipeline_config.schema.md — v2"; "RATIFIED 2026-07-13b" = 1; Appendix C at lines 9/125/169; 637 lines; md5 `d3f866c4e1a834025070a1d1511437e8`. **Filed SUFFIXED at `pipeline/pipeline_config_schema_v2.md`** |
| `discovery_prompt_v2_5.md` | ✓ | read output-family spec (§1–6) and provenance-tag defs IN FULL — these are the validator's source of truth. Every constant in `src/rules.py` traces to a line here. **v2.6 still OWED.** Now at `pipeline/` |
| `discovery_test_record_v1.md` | ✓ | uploaded by operator; **md5-matched against the mount copy** (`2758c0a8c46d29d182207a2b50535e24`, 21383 bytes, identical). P-1…P-7 structure read; P-2/P-3/P-4 read in full. Still **DRAFT, unratified**; 4-question docket carried. Now at `evidence/` |
| `primer_amendment_proposals_v2.md` | ✓ → superseded | read structure + summary table + tail. **Re-filed as v3 this session. v2 is sediment.** |
| `discovery_sailing-for-dummies_SALVAGE.md` | ✓ (presence + partial) | fed to the validator as a smoke test → RED, 29 legible violations. **NOT a verdict on the sailing run** — it is a v2-era artifact predating v2.5 rules, fed as a single file with no sidecars. Proves only that the validator survives real text. Still PROVISIONAL, docket Q3. Now at `evidence/` |
| `engine_charter_amendment_v1_1.md` | ⚠ ✓ present, **but note its nature** | on mount, filed to `law/`. **This file is ITSELF a transcription artifact** — the original was lost before filing and a 07-10 session rebuilt it from the 07-09 transcript; it carries a recovery note saying so. Lexicon W1 records a citation error inside it that drifted twice. **Law with an asterisk.** Not acted on |
| `engine_charter.md`, `_v1_2`, harvest map/residue + kit specs, harvester_prompt_v1, orientation doc, Schemer brief, topology guide | ✓ (presence) | copied to repo; `tree`-verified by operator. NOT read this session |
| Known-absent carried: `sources.md`, Schemer master doc, JJU source, `glossary_index_v31.md` (JJU-side BY DESIGN) | ✗ | unchanged; unblocking |

## Propagation / blast-radius log

- **ZERO design blast radius.** No pipeline actor, wire schema, enum, fixture,
  threshold, prompt, or gate rule changed. The migration moved bytes and
  renamed one file.
- **Storage blast radius: TOTAL, and that is the point.** Every project file
  now has a repo path. The mount is redundant and slated for clearing. **Every
  future boot's mechanism changes** — see P9/P10.
- **One rename, chased:** `pipeline_config_schema.md` → `..._v2.md`. No
  in-repo pointer updates were performed. **RISK, unretired: lexicon §8 and
  possibly the charter reference the config schema by its unsuffixed name.**
  Not checked this session. Flagged for r17.
- **`WIRE_VERSION` untouched** (07-13g's lesson held; nothing tempted a sweep).
- **The validator introduces no coupling.** It reads discovery output and
  exits 0 or 1. Nothing depends on it yet — which is exactly the problem the
  "only door" question names.

## Open design questions register — delta

NEW:
1. **Ratify P9 + P10?** The repo rule and the manifest-schema change it
   requires. Recommend ratifying **together** — P9 without P10 is a cleared
   mount plus a mount-shaped manifest, i.e. a boot with no defined path. P10's
   specific columns should be treated PROVISIONAL until the first repo-era boot
   reports back.
2. **Is the validator the ONLY door?** Agreed in principle, filed nowhere. If a
   future session can hand discovery output downstream without passing the
   validator, the shape is a suggestion, not a contract. **This is a
   filing-law/primer question. Proposed as P11 — NOT drafted this session.**
3. **W12 candidate: "adopting the operator's framing over the ctx's own
   verified state."** New failure mode, one instance (this session, the file
   search). Distinct from W11 (stale artifacts) and from the 07-13d pattern
   (concluding before reading). **Needs a lexicon warts entry, or a decision
   that one instance is not a pattern.**
4. **Does `engine_charter_amendment_v1_1.md`'s transcription provenance need
   addressing?** It is law-with-an-asterisk with a known internal citation
   error (W1). Surfaced by the migration; not acted on.

CARRIED (all four from the 07-13f test-record docket, none closed): fixture
sequencing (v2.5 vs owed v2.6); fixture sources (synthetic vs Schemer
ClearScan); whether SALVAGE's PROVISIONAL status must retire before Run B
counts as first-party evidence; whether P-1 is workshop or ops.

CARRIED from 07-13g, still unratified: **the P1–P2 strike + P3-R**; **the
interface-doc migration's retroactive blessing**.

Also carried: boot-set weight; **Opus capability calibration — fourth data
point (see W12 candidate; the failure was not capability but framing
adoption)**; the PM-methodology harvest (**this session's material: the
second consecutive declined reconstruction; the config-schema pushback that
paid a five-session debt; the ctx's own three-turn search failure**).

## Reference-doc debt — slot

**UNPAID AT THIS CLOSE. This is a KNOWN VIOLATION of the primer's lockstep
rule and is recorded rather than hidden.**

- **Lexicon r17 — OWED.** Needs: §8 registry rows for the repo structure and
  the validator; W9 annotated RETIRED (five sessions, closed 07-14); W11
  annotated **RETIRED-AT-THE-ROOT-pending-P9-ratification**; the W12 candidate
  entry; a check of whether §8 names `pipeline_config_schema.md` unsuffixed
  (blast-radius risk above); a disambiguation entry for *mount* vs *repo*.
- **Diagram r12 — OWED.** Needs: banner stamp for 07-14; the validator as a
  node between discovery and downstream; the tested-state ledger updated with
  the validator's 19/19.
- **Register v3 — PAID** (`primer_amendment_proposals_v3.md`, P9 + P10 filed
  with strongest counters and confidence levels per the register's own rules).

**Why unpaid:** context budget. The session spent its capacity on the
migration, the validator build, and three wasted search turns. **The ctx
flagged its own context health to the operator before the migration and the
operator correctly scoped the session to exclude the repo work from the ctx's
plate.** The debt is real and should be the first item of the next session —
**it is now the project's oldest unretired clerical debt, inheriting the title
W9 vacated today.**

**PRIMER v5 — status UNCHANGED: DEFERRED BY RULING** [operator, 07-13f]. The
deferral's cost changed shape again: the register now holds **P3-R (ready, 3
points), P9, and P10 (1 point each, both structural)**. P9/P10 are not
protections against a hazard — they describe the world the project now lives
in. **A primer that describes a mount is now describing a world that no longer
exists.** That is a stronger argument for v5 than any protection was.

## Recommended next session

**PREFERRED — pay the reference-doc debt, then run discovery on a book.**
The debt is now the oldest clerical item and the lexicon is a boot authority
describing a retired mechanism. It is also cheap. **Then the discovery run:**
the standing missing proof point (*no book has completed discovery end-to-end
against a clean substrate*, open since 07-11) is now the oldest open question
in the project, and **the validator built today has nothing to eat.** Its
fixtures are all self-authored — the cell only opens on real output. The
operator drives: fresh ctx OUTSIDE the project, feed the book, get the output
family back, run the validator against it.

**The ruling owed first:** discovery is at v2.5 and **v2.6 is owed**. The test
record says the end-to-end run *"should wait for v2.6, or accept that a re-run
is owed."* **Ctx lean: run v2.5 now, accept the re-run.** A re-run costs a
session; not running costs the proof point staying open a fifth day while
everything downstream rests on a prompt no one has fully executed.

**ALTERNATIVE — ratify the backlog** (P1–P2 strike, P3-R, interface-doc
blessing, P9, P10) and bump primer v5. Five rulings and a version bump. **This
is a bigger pile than it looks and it is all boot law.**

**ALTERNATIVE — Node-RED, first flow.** Now legitimate: there is a real script
to call. But one exec node is a thin first flow and teaches little about the
packet lane where Node-RED will actually earn its keep.

**NOT RECOMMENDED — the gate run.** Still blocked, and the blocker is not W11.
**The Tier F fixture packets, both arms' provisional prompts, and the
prove-script harness DO NOT EXIST.** The kit specifies them; nobody has built
them. 07-13g's "the blocker is gone" was true of W11 and **overstated about the
run**. Building them is a session (or three), and it carries a placement
constraint: **the ctx that mints the fixtures and keys cannot also be the ctx
that scores the run.**

Clerical owed regardless: **lexicon r17 + diagram r12 (now the oldest debt)**;
discovery v2.6 re-version; BJJ discovery back-pass; the five ratifications
above.

## Session hygiene / corrections ledger (own errors + events)

- **Model this session: Opus** (Claude Opus 4.8) — fourth Opus workshop ctx.
- **Boot: CLEAN, second consecutive.** Every 07-13g marker matched. Scorer live
  run 18/18 at boot. **W11 did not fire — the 07-13g migration works.**
- **Own error 1 (MAJOR, operator-caught): three turns wasted searching
  transcripts for files that were on the mount.** The operator asked for help
  finding 8 missing files; the ctx ran `conversation_search` twice, surfaced
  only fragments, declined a reconstruction — **and never ran the `cp` loop it
  had had available since it inventoried the mount twice earlier in the same
  session.** The operator's frustration was earned and the ctx said so.
  **Root cause: adopted the operator's framing ("I need help finding these")
  over its own verified state ("I have already listed all 51 files").**
  Proposed as W12. **The cost was operator patience and ctx context, and the
  fix was one command.**
- **Own error 2 (minor, self-caught): `mkdir -p {a,b,c}` brace expansion failed
  under `sh`**, silently creating a literal directory named `{src,tests,fixtures`
  and scattering six fixture files to `/`. Caught on the next `ls`; both cleaned
  up; all subsequent multi-dir work run under explicit `bash -c`. **Same class
  as 07-13g's own error 2 — this is now a two-session pattern and belongs in
  the lexicon: THIS CONTAINER'S DEFAULT SHELL IS `sh`, NOT `bash`.**
- **Own error 3 (minor, self-caught): `${PIPESTATUS[0]}` failed under `sh`**
  during the boot scorer run. Re-run under `bash -c`; receipt valid. Same root
  cause as error 2.
- **Declined an operator instruction, with reasons, for the second consecutive
  session — and was right again.** Asked to rebuild the 07-13g checkpoint from
  transcripts. Declined: search returned fragments only; the result would have
  been part-transcription/part-invention, unmarked, wearing the real filename,
  booting the next session. **The file was on the mount.** Logged as
  PM-methodology harvest material.
- **Pushed back on an operator ruling and the operator reversed — correctly.**
  The operator ruled "commit the stale config, a stale single source beats
  competing sources." The ctx argued the v1 file's own header says v1 with no
  signal a v2 exists, making it *indistinguishable from current by its own
  markers* — the 07-13g false-positive-marker trap. The operator then found
  the real v2. **A five-session debt died because a ruling got argued with.**
- **The validator's receipt was executed by the OPERATOR, not the ctx** —
  19/19 GREEN in the real repo after the move. **This is the receipt class
  P3-R exists to protect; an operator-run receipt cannot be fabricated by a
  ctx that is wrong about itself.**
- **The SALVAGE smoke test was reported with its caveat attached, not as a
  finding.** RED with 29 violations — but the doc is v2-era, fed without
  sidecars, and predates the rules. Reported as "the validator survives real
  text," **not** as "the sailing run is defective."
- **No sentinel-free editing violations.** The register's 4 patches each used a
  unique anchor; `build_invalid.py` asserts anchor uniqueness (`ANCHOR
  AMBIGUOUS` guard) on all 18 fixture edits and would have aborted on
  ambiguity.
- **Two operator renames caught before they landed:**
  `discovery_sailing-for-dummies.md` (dropped SALVAGE — would have made a
  provisional transcription look like a real run) and
  `ingest_brief_the-little-schemer.md` (harvest→ingest is a *lexicon* change,
  not a rename). Both reverted to mount names by the operator.
- **Context health flagged proactively to the operator** before the migration
  planning, leading to a correct scoping decision (ctx writes the checkpoint;
  operator executes the repo work). **Recorded as a good pattern.**
- No interruptions. No new W-class events **except the W12 candidate above**.
  W9 RETIRED. W11 retired at the root pending P9 ratification.

## Boot manifest — P10 shape (REQUEST LIST, not a mount-currency table)

**READ THIS FIRST.** The project mount is being cleared. **The repo is the
source of truth:** `~/git/repetae` on the operator's machine, private, local.
A ctx cannot read it. **Ask the operator to upload what you need.**

**If the mount is still populated:** the 07-13g manifest's verification rules
still work and P9/P10 are unratified proposals — use whichever path is
available and say which you used.

**If the mount is empty:** this table is the only path. Request the REQUIRED
tier first; request ON-DEMAND items only if the session's target needs them.
Do not pad the request out of caution — that is the friction P9 warns will
tempt a future ctx into re-mounting.

| Doc | Repo path | Why needed | Tier |
|---|---|---|---|
| primer | `law/workshop_primer_v4.md` | **THE boot authority — read IN FULL.** Filing law items 1–6; boot loop; close protocol. v5 DEFERRED BY RULING; do not bump unprompted | **REQUIRED** |
| this checkpoint | `checkpoints/session_checkpoint_2026-07-14.md` | the boot file | **REQUIRED** |
| depth checkpoint | `checkpoints/session_checkpoint_2026-07-13g.md` | the migration session; the W11 record and the P8 sunset that this session's P9 generalizes | **REQUIRED** |
| lexicon | `law/workshop_lexicon_r16.md` | vocabulary + warts ledger. **r17 is OWED and this session did not write it — r16 describes a MOUNT the project no longer uses.** Read it knowing that | **REQUIRED** |
| register | `law/primer_amendment_proposals_v3.md` | pending proposals: **P3-R (ready, 3 pts), P9, P10 (1 pt each)**. NOT law. If you hand-apply a protection, increment its evidence count at close | **REQUIRED** |
| charter + amendments | `law/engine_charter.md`, `law/engine_charter_amendment_v1_1.md`, `law/engine_charter_amendment_v1_2.md` | the worklist lives in §9 as amended. **v1_1 is itself a transcription artifact — see the ledger** | ON-DEMAND |
| diagram | `reference/system_diagram_r11.html` | tested-state ledger. **r12 OWED** | ON-DEMAND |
| discovery prompt | `pipeline/discovery_prompt_v2_5.md` | 547 lines; the validator's source of truth; **v2.6 OWED** | ON-DEMAND — **REQUIRED if the session runs or edits discovery** |
| test record | `evidence/discovery_test_record_v1.md` | P-1…P-7; still DRAFT; the 4-question docket | ON-DEMAND |
| validator | `tools/discovery-validator/` (whole dir) | P-2/P-3/P-4 built 07-14. **Receipt: `python3 tests/selftest.py` → 19/19 PASS, SELF-TEST GREEN** (operator-run). Fixtures SYNTHETIC | ON-DEMAND |
| engine unit | `gate/topology_experiment_kit_v2.md`, `gate/topology_scorer_v2.py`, `gate/topology_scorer_v2_interface.md` | **rides together — never request one alone.** Receipt: `python3 topology_scorer_v2.py selftest` → 18 PASS, exit 0. **`WIRE_VERSION = "wire-0"` is the PROTOCOL version — never bump it in a rename** | ON-DEMAND |
| config schema | `pipeline/pipeline_config_schema_v2.md` | header "# pipeline_config.schema.md — v2"; "RATIFIED 2026-07-13b"; Appendix C; 637 lines. **W9 CLOSED 07-14** | ON-DEMAND |
| pipeline prompts | `pipeline/harvest_map_v1.md`, `pipeline/harvest_residue_v1.md`, + `_kit_spec` pair, `pipeline/harvester_prompt_v1.md` | CONDITIONAL status per amendment v1.2 item 7 | ON-DEMAND |
| exhibits | `evidence/discovery_sailing-for-dummies_SALVAGE.md`, `evidence/harvest_topology_proposal_laymans_guide.md`, `evidence/harvest_brief_little-schemer.md` | SALVAGE is **PROVISIONAL** (docket Q3) — the name carries that and must not be dropped | ON-DEMAND |
| orientation | `reference/how_we_build_wikis_from_books.md` | layman overview; reference, not authority | ON-DEMAND |
| older checkpoints | `checkpoints/` (12 more, 07-10b → 07-13f) | narrative history | ON-DEMAND |

**Verification under the repo rule.** The content-marker check SURVIVES and
matters MORE: with no mount to compare against, **the marker is the only
handshake confirming the operator uploaded the file the manifest meant.** For
every REQUIRED doc above, confirm the marker before working. This session
md5-matched an uploaded file against its mount copy and confirmed identity —
**that check is not available post-clearing.**

**The honest limit, stated in P9 and repeated here: this manifest cannot
verify itself.** A ctx cannot detect a file that exists in the repo and was
not handed over. It cannot distinguish "absent because unneeded" from "absent
because forgotten." **Enforcement is entirely operator-side.** If something
looks missing, ask — do not infer, and do not proceed on a guess.

**Planned successor** [operator]: a script. The ctx emits a CSV of repo paths;
the operator runs it; the returned files are the boot set. Not built. When
built, this table becomes its input.
