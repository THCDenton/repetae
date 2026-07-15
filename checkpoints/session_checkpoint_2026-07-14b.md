# Session checkpoint — 2026-07-14b (the first real discovery run + the grader that lied)

Purpose: boot file for the next session. **Files are the only memory, and the
files live in a git repo the ctx cannot read.** Written under checkpoint schema
v2.1 (five mandatory slots, boot manifest last). Reads alongside 07-14.
**Model this session: Opus** (Claude Opus 4.8) — fifth Opus workshop ctx. Per
the 07-13d handoff law, this is a fifth capability-probe record.

**THIS IS THE FIRST TRUE REPO-ERA BOOT.** Every file this session read arrived
as an operator upload. The mount was populated and was NOT read — the ctx
stated the path it used and stayed on it. The 07-14 hybrid manifest worked as
a request list on its first contact with reality: the ctx named four REQUIRED
docs, the operator sent seven, all seven verified against their pinned markers.
**P10's shape is now evidenced once, not merely drafted.** P9 and P10 remain
UNRATIFIED.

## What this session was

**The day the machine got used.** Discovery ran end-to-end against a real book
for the first time in the project's history, closing the standing missing proof
point open since 07-11. Then the validator built yesterday ate the output and
**failed** — 49 violations, at least 33 of them its own bugs. Two were found
and fixed live; the rest were handed back as questions, not answers.

The session also **paid the reference-doc debt** (lexicon r17 + diagram r12),
which 07-14 left unpaid and which had become the project's oldest clerical item
the moment W9 died.

The headline, and it should not be softened: **a book went through the machine
and the thing that broke was the grader.**

## Verified state changes

1. **DISCOVERY RAN END-TO-END AGAINST A REAL BOOK — the standing missing proof
   point, open since 2026-07-11, is CLOSED.** Source: R.G. Loeliger, *Threaded
   Interpretive Languages: Their Design and Implementation* (BYTE Books, 1981),
   266pp, Internet-Archive scan, OCR text layer, slug `loeliger-til`. Run at
   **v2.5** [operator-ruled]. Executed by the OPERATOR in a fresh ctx **outside
   the project**, per discovery's isolation rule. **All six output-family files
   produced.** This ctx never ran discovery — it read the output.
2. **THE VALIDATOR FAILED ON FIRST CONTACT — and the failure was mostly its
   own.** `python3 -m src.validate check --run run --slug loeliger-til` →
   **ENVELOPE RED, 49 violations, exit 1.** Two defects found in the validator,
   both fixed in-session, **49 → 25 → 16**. Receipt: the shipped code reproduces
   16 (exit 1). Shipped md5s: `rules.py` `36af7fa2b878696084b71bdc6ec27c52`;
   `validate.py` `642afe0ac96af5bb2faafba1f27238a9`.
   - **Defect (a) — the tag-qualifier trap.** The prompt requires `[mechanical]`
     to carry "method in one clause" and **never says where the clause lives**.
     The run legally wrote BOTH `[mechanical]` (method in the line's prose,
     17×) and `[mechanical: 21 matches]` (method in the bracket, 8×). The
     validator's exact-string match rejected the qualified form as
     `TAG_ILLEGAL` **and** the bare form as `TAG_MECHANICAL_NO_METHOD` —
     **two mutually exclusive codes; no run could satisfy both.** ~24 hits.
   - **Defect (b) — sub-bullet miscounting.** Every indented continuation
     bullet was counted as a convention line needing its own tag. 75 → 62
     convention lines; 13 false `TAG_BARE`. ~9 hits.
3. **REFERENCE-DOC DEBT PAID — `workshop_lexicon_r17.md` + `system_diagram_r12.html`.**
   Both rev counters mechanically verified against their own derivation rules
   pre-filing (lexicon: 17 dated changelog bullets = rev 17; diagram: 11
   "Revised" stamps + 1 = rev 12). Filename rev == internal counter in both
   (filing law item 4). Diagram HTML parse-checked: zero unclosed tags, zero
   mismatches.
4. **THREE LEXICON BOOT ERRORS FOUND AND FIXED** — all found at boot, all
   pre-existing, all the same species (*the lexicon had fallen behind itself*):
   - **W2 asserted FIVE provenance tags while §6 listed SIX** — for four
     consecutive revs (r13–r16). The sixth (`[discovery-forecast]`) was minted
     07-13; §6 was updated, W2 was not. **A wart entry was asserting a
     falsehood.** Corrected; six wins.
   - **The header self-referenced `workshop_lexicon_r15.md` twice** while its
     identity line said rev 16. Content won per filing law item 4; prose fixed.
   - **§8 registry named the lexicon current at r12, the diagram at r8, the
     register at v1** — drifted four revs behind the file containing it. And it
     named `pipeline_config_schema.md` **unsuffixed**, the exact
     blast-radius risk 07-14 flagged for r17. All corrected.
5. **W12 + W13 MINTED (lexicon §10).** W12: self-authored fixtures cannot
   detect a misread spec. W13: a spec that forbids what it does not define.
   Both are today's, both carry their full evidence.
6. **W11 annotated RETIRED-AT-THE-ROOT pending P9 ratification**; §9 gains
   **pair 14 (`mount vs repo`)**; §8 gains **two rows** (the repo; the
   validator).
7. **The 07-14 migration was verified by the operator, not asserted by the
   ctx.** `tree -I '.git'` returned 33 directories, 161 files; `checkpoints/`
   holds 15 files **including `session_checkpoint_2026-07-14.md`** — the boot
   file whose loss would have been the only real casualty of clearing the
   mount. `law/` 6, `pipeline/` 7 (incl. `pipeline_config_schema_v2.md`),
   `gate/` 3, `evidence/` 4, `reference/` 2. **Every count matches 07-14's
   record.**
8. **Worklist (charter §9 as amended): unchanged.** **Clerical RETIRED:
   lexicon r17 + diagram r12 (the 07-13g debt).** Clerical carried: BJJ
   discovery back-pass. **Promoted OUT of clerical: discovery v2.6 — now the
   next session's engine artifact (see rulings).** Carried: the
   `discovery_test_record_v1` docket (4 open questions).

## Rulings (this session)

- **Run discovery at v2.5; accept the re-run is owed** [operator-ruled,
  verbatim: *"2.5 we have stuff to deliver"*]. The ctx's lean, argued with its
  counter stated (a contaminating stale section would cost the run AND still
  owe v2.6). **The ruling paid off in a way neither party predicted: the run
  told us exactly what v2.6 must fix. The re-run is no longer a cost — it is
  the point.**
- **The defect burden is shared between discovery and the validator; pinning
  discovery's output shape shrinks the validator's mechanism** [operator-ruled,
  the session's sharpest call]. The ctx partially pushed back — discovery
  *already has* the schema inline, and the schema governs the config fragment,
  which is the one part nothing complained about; the failures are all in the
  **unpinned prose**. **Restated and accepted: the problem is not a missing
  schema, it is that the un-schema'd parts are the parts that break.**
  Consequence: **v2.6 is PROMOTED from clerical re-version to the next
  session's engine artifact, with today's run as its evidence.**
- **The 16 surviving violations are NOT ruled — they are docketed**
  [session-ruled; the ctx declined to guess]. 14 are W13's gap: the prompt
  forbids a bare convention line and never defines a convention line. **Any
  rule the validator adopted would be invented law, enforcing something no
  document says.** Recorded rather than resolved.
- **W12-candidate from 07-14 ("adopting the operator's framing over the ctx's
  own verified state") NOT filed** [operator-ruled: *"dont worry about the file
  hunting. you're not gonna have files to worry about soon enough"*]. **The
  operator's reasoning is better than the ctx's proposal was: it was a
  MOUNT-ERA failure mode, and there is no mount.** The W12 slot was
  consequently taken by this session's finding. Recorded so no future session
  re-litigates it as an oversight.
- **Both reference docs this session, not one** [operator-ruled, after the ctx
  hedged and proposed doing the lexicon alone]. **The ctx's hedge was wrong and
  the operator was right to press it** — the edits were surgical against files
  already read. Recorded as a corrections-ledger item, not just a ruling.
- **Clear the mount** [operator-ruled, after the ctx supplied a three-check
  list and declined to certify safety it could not observe]. The ctx's position
  on the record: **it cannot see the repo, so any "it's safe" would have been
  paperwork read back as observation.** The operator ran `tree`; both flagged
  gaps closed.

## Ground truth learned this session

- **A self-authored fixture suite tests self-consistency, never conformance.**
  The validator's 19/19 was structurally incapable of catching its own bugs:
  **the same ctx authored the spec-reading, the code, and the 18 fixtures**, so
  the fixtures inherited the misreading. Green meant *the code matches my
  reading of the spec*. It never meant *the code matches the spec*. **This
  generalizes to every self-hosted green in the project — the scorer's 18/18 is
  the identical construction and carries the identical cell, unopened only
  because it has never met real output.** Proposed standing rule: *a suite
  authored by the same ctx as the code it tests is provisional until a real run
  contradicts it or fails to.*
- **Writing a hazard down does not retire it. Running the thing does.** The
  07-14 checkpoint predicted this failure **verbatim** — "green means the code
  implements the spec. It does not mean the spec matches reality" — and the
  ctx that wrote that sentence built the fixtures anyway, and the failure
  happened anyway. **The paperwork was correct and useless. One real book found
  three bugs in ten minutes.** This is the strongest single argument the
  project has produced for the "only door" question and for spending sessions
  on contact rather than on protection.
- **The expensive failure is not a deliverable that breaks loudly — it is a
  grader that is confidently green.** A broken deliverable announces itself. A
  lying grader certifies everything downstream of it. **The tested-state
  ledger's founding headline died today and was recorded as FALSIFIED rather
  than quietly rewritten** — that is the ledger working.
- **The 45→62 overrun and the 14 bare lines may not be findings at all.** Both
  depend on definitions the prompt never supplies. **A validator that reports
  a number derived from its own guess about what to count is reporting its
  guess, not the run.** Left open deliberately.
- **A repo path is not a receipt.** The ctx caught itself saying "it's in your
  repo at `pipeline/discovery_prompt_v2_5.md`" — which it did not know. It knew
  the file was uploaded and that a manifest *claims* that path. **Under P9 a
  ctx cannot observe the repo at all; every repo statement it makes is
  paperwork recitation.** Belongs in the P9/P10 ratification discussion.
- **The operator's questions did work the paperwork cannot.** Four times the
  operator's plain question caught something the apparatus missed: an invented
  nickname used as if it were lexicon ("interview form?"), a source-of-truth
  ambiguity ("did you read that from mount?"), a nonexistent file treated as an
  option ("wait where even is 2.6?"), and a ctx hedging about its own capacity
  ("you don't think you could do both?"). **None of these were catchable by a
  boot check.**
- **The run was good, and the prompt was the weak link.** The Loeliger output
  is careful work — it distinguished `END` from `END,`, identified `■` as the
  book's printed space symbol rather than OCR noise and preserved it, caught
  that quoted mnemonics are ASCII codes not opcodes, excluded running heads as
  probe artifacts. **It adhered. There was simply not one thing to adhere to.**
  You cannot instruct your way out of an underspecified spec.

## Dependency ledger (verified-how) — schema v2.1 slot

**ALL SEVEN DOCS ARRIVED AS OPERATOR UPLOADS. The mount was populated and NOT
read.** Path stated at boot and held throughout.

| Dependency | Status | Verified how |
|---|---|---|
| `workshop_primer_v4.md` | ✓ | **read IN FULL** (both halves; lines 143–185 explicitly re-read after truncation). Header exact "v4, issued 2026-07-13d"; filing law items 1–6 confirmed. **v5 still DEFERRED BY RULING** |
| `workshop_lexicon_r16.md` | ✓ → superseded | grep: "Revision identity: rev 16" = 1, mechanically derived (16 dated changelog bullets = 16). W11 "RECURRED A THIRD TIME" + "RETIRED for the kit" both = 1. **Three defects found (see state changes 4). Re-issued as r17. r16 is sediment** |
| `primer_amendment_proposals_v3.md` | ✓ | header "re-filed as v3 on 2026-07-14"; summary table shows P3-R + P9 + P10. **Read in full. NOT amended this session** — see reference-doc debt |
| `session_checkpoint_2026-07-13g.md` | ✓ | read; the migration record; P8 sunset + the W11 case history |
| `session_checkpoint_2026-07-14.md` | ✓ | supplied in-context at boot; drove this boot; **all markers matched, including its own md5 record of the test record** |
| `system_diagram_r11.html` | ✓ → superseded | grep "Revised 2026-07-13g" = 1; "Revision identity: rev 11" = 1; rev mechanically derived (10 stamps + 1 = 11). **Re-issued as r12. r11 is sediment** |
| `discovery_prompt_v2_5.md` | ✓ | header exact; **547 lines**; "Terminal states" = 1. **Operator setup + Isolation + Preflight + Provenance tags read IN FULL this session** (the ctx had previously read only the output-family spec — see own error 1) |
| `discovery_test_record_v1.md` | ✓ | **md5 `2758c0a8c46d29d182207a2b50535e24`, 21383 bytes — EXACT match to the 07-14 checkpoint's recorded values.** Still DRAFT; 4-question docket carried |
| Loeliger source PDF | ✓ (probed, not read) | `pdfinfo` + pypdf: 266 pages, 485,730 chars extracted, mean 1,826/page, **257/266 pages > 300 chars**, 7 near-empty. Creator=Internet Archive. **Text layer sound.** The ctx probed it to assess feedability; **it did NOT run discovery on it** |
| Loeliger output family (6 files) | ✓ | all six present, correct slug. Fed to the validator. **CONTENT NOT ASSESSED — only shape** |
| `rules.py` + `validate.py` | ✓ (partial) | uploaded as TWO FILES, not the directory. **The 19/19 self-test could NOT be re-run — no fixtures, no `tests/`. The receipt that the shipped code equals yesterday's code DOES NOT EXIST for this session.** See own error 3 |
| `session_report_loeliger-til.md`, `watchlist.csv` | ✗ **NOT READ** | both arrived; **deliberately excluded** from the validator's run dir (not family members) and **never read** — the session ended before the report was opened. **Carried: the session report is unread evidence** |
| Known-absent: `sources.md`, Schemer master doc, JJU source, `glossary_index_v31.md` | ✗ | unchanged; unblocking |

## Propagation / blast-radius log

- **ZERO design blast radius.** No pipeline actor, wire schema, enum, fixture,
  threshold, prompt, or gate rule changed. **`discovery_prompt_v2_5.md` was NOT
  edited** — every finding against it is docketed for v2.6, not applied.
- **The validator changed and nothing depends on it.** Two files patched;
  `VALIDATOR_VERSION` deliberately **not** bumped (it reads `envelope-0`) —
  the ctx flagged this rather than sweeping it, per 07-13g's `WIRE_VERSION`
  lesson. **Open question: should a behavior fix bump it? Not ruled.**
- **The fixture suite is now KNOWN-STALE and was NOT rebuilt.** It encodes the
  same misreading the code did. **This is the largest unretired hazard the
  session created**: a future ctx running `selftest` will get a green that
  proves less than it appears to. Recorded in the lexicon, the diagram, and the
  validator's own docstring. **Rebuild owed with v2.6.**
- **Two reference docs re-issued; five stale §8 rows corrected.** The lexicon's
  registry had drifted four revs behind itself — **that class of drift is
  invisible to the boot loop** (the file's own identity line was correct; only
  its table was wrong).
- **The 07-14 blast-radius flag is now CLOSED**: lexicon §8 did name the config
  schema unsuffixed. Found, fixed. **The charter was NOT checked for the same
  reference — carried.**

## Open design questions register — delta

NEW:
1. **What is a convention line?** (W13.) The prompt mandates a tag on every
   convention line and never defines one. **Blocks P-3 enforcement entirely.**
   14 of 16 surviving violations. **v2.6.**
2. **Is 62 > ~45 a real overrun?** "~45" is soft, and it is unclear whether the
   bound counts what the validator counts. **v2.6.**
3. **Should the validator's registration-line check accept a backticked line?**
   1 violation; probably cosmetic; unruled.
4. **Should `VALIDATOR_VERSION` bump on a behavior fix?** It reads `envelope-0`
   and the behavior changed materially. Not ruled; flagged not swept.
5. **Does the scorer's 18/18 need re-earning?** W12 generalizes to it exactly:
   same construction, same ctx-authored fixtures, same cell. **The gate is
   where it opens.** Nobody has proposed re-testing it.

CARRIED, unclosed: **P11 ("is the validator the only door?") — STILL UNDRAFTED
across two sessions.** Today is its strongest evidence: the validator ran only
because the operator brought output to a ctx that happened to remember it
existed. **Ratify P9 + P10 together.** The four test-record docket questions.
The P1–P2 strike + P3-R. The interface-doc retroactive blessing.
`engine_charter_amendment_v1_1.md`'s transcription provenance (W1).
Opus capability calibration — **fifth data point**. The PM-methodology harvest
(**this session's material: a grader that passed its own exam and failed the
real one; four operator questions that beat the apparatus**).

## Reference-doc debt — slot

**PAID IN FULL. The 07-13g debt is retired.**

- **Lexicon r17 — PAID.** §8 +2 rows (repo, validator) + 5 corrected rows; §9
  pair 14 (mount vs repo); §10 W2 corrected, W11 root-retired, **W12 + W13
  minted**; header re-issue clause + rev identity → 17. Rev verified: 17
  changelog bullets = rev 17 = filename.
- **Diagram r12 — PAID.** 07-14 banner stamp; tested-state ledger: discovery
  row → **first real run**, **new validator row**, headline recorded as
  **FALSIFIED**, empty-confidence paragraph rewritten (*a run is not a
  measurement*); config-schema row re-keyed + W9 closed. Rev verified: 11
  stamps + 1 = 12 = filename. HTML parses clean.
- **Register v4 — NOT WRITTEN. NEW DEBT, and it is this session's only
  clerical failure.** Today produced at least one clear proposal (**P11**, the
  only-door question, now twice-evidenced) and arguably a second (**the
  self-authored-suite rule from W12**). Neither is filed. **The register's own
  rule 2 says a session that surfaces a new recurring failure adds a proposal
  with 1 evidence point.** Not done — the session spent its capacity on the run,
  three debugging rounds, and both reference docs. **This is now the oldest
  unretired clerical debt, inheriting the title r17/r12 vacated today.**

**PRIMER v5 — status UNCHANGED: DEFERRED BY RULING** [operator, 07-13f]. **The
argument for it strengthened materially today.** P9/P10 are no longer
speculative: **this session was the first true repo-era boot and the request-list
manifest worked.** P10's shape has an evidence point now. Meanwhile primer v4 —
still THE boot authority — describes a mount that no longer exists, and the
lexicon it points to now contains a disambiguation pair explaining that the
primer is describing a dead world. **A boot authority that requires a footnote
to be read correctly is on borrowed time.**

## Recommended next session

**PREFERRED — discovery v2.6, with today's run as its evidence.** Promoted from
clerical to engine artifact by ruling. The docket is written and specific:
**pin the tag syntax** (one form, killing W12's defect (a) at the source);
**define a convention line** (W13 — closes 14 of 16 violations and is the only
thing that makes P-3 enforceable); **rule the ~45 bound** (what it counts);
**fix the stale schema-boundary section** (the original v2.6 debt, now five
sessions old and the smallest item on the list). **Then rebuild the validator's
fixtures against the pinned spec — by a DIFFERENT ctx than the one that reads
it, if that can be arranged.** W12 says a suite authored by the code's author
proves nothing; the cheapest fix available is separation.

**Do this before another book.** Running a second book at v2.5 buys a second
copy of today's findings.

**ALTERNATIVE — ratify the backlog** (P1–P2 strike, P3-R, interface-doc
blessing, P9, P10) and issue primer v5. Five rulings, all boot law. **Now
stronger than yesterday: P10 has been exercised once.** Draft P11 in the same
session — it is twice-evidenced and undrafted.

**ALTERNATIVE — read the Loeliger output for CONTENT.** Nobody has. The
validator checked shape; the master doc, the six sidecars, and the unread
`session_report_loeliger-til.md` are all sitting there. **The run's quality is
entirely unassessed** and it is the only real evidence the project has ever
produced.

**NOT RECOMMENDED — the gate run.** Unchanged from 07-14: **the Tier F fixture
packets, both arms' provisional prompts, and the prove-script harness DO NOT
EXIST.** And W12 now casts a shadow over the scorer's 18/18 — same
construction, same cell. **The ctx that mints the fixtures cannot be the ctx
that scores the run** is now an evidenced rule, not a precaution.

Clerical owed regardless: **register v4 (P11 + the self-authored-suite rule) —
now the oldest debt**; the validator's fixture rebuild; BJJ discovery
back-pass; the five ratifications above.

## Session hygiene / corrections ledger (own errors + events)

- **Model this session: Opus** (Claude Opus 4.8) — fifth Opus workshop ctx.
- **Boot: CLEAN, third consecutive. First boot ever run entirely from uploads.**
  All seven docs verified against the 07-14 manifest's markers, including an
  md5 match on the test record. **Three defects found IN the lexicon at boot** —
  the boot loop worked.
- **Own error 1 (MAJOR, operator-caught): reasoned about how to feed a book for
  FOUR MESSAGES without reading discovery's ingest section.** The ctx proposed
  extraction strategies, offered the operator a choice between invented options,
  and used the word "packet" for a thing that has a different meaning in the
  lexicon. The operator asked *"packet? what are you planning on making right
  now?"* — and the answer was: nothing, because the prompt already said. Its
  **Operator setup** section states the preferred method (attach directly in
  chat) and names the exact hazard the operator had already avoided. **This is
  register P4 — "read the runbook before reasoning about feasibility" — firing
  live. P4 sits at 1 evidence point and has never been ratified. It now has a
  second point and nobody filed it.**
- **Own error 2 (MAJOR, self-caught, the session's real finding): shipped a
  grader whose exam it wrote itself.** See W12. Fixed, recorded, generalized.
- **Own error 3 (minor, flagged): accepted a partial upload of the validator
  and proceeded.** Two files, no fixtures, no `tests/`. **The ctx flagged that
  it could not re-run 19/19 to prove the code arrived intact — and then ran it
  against real output anyway.** Defensible (the bug hunt did not need the
  fixtures) but recorded: **the shipped validator has no receipt tying it to
  yesterday's operator-run green.**
- **Own error 4 (minor, self-caught): invented a nickname and used it as
  vocabulary.** "Interview form" for `discovery_prompt_v2_5.md`, unflagged,
  across three messages — until the operator asked *"interview form? do I have
  that in my repo?"* **Primer law: police your own output at point of use. The
  ctx was holding the lexicon while drifting the vernacular.** Corrected with a
  translation table.
- **Own error 5 (minor, self-caught): trusted a docstring over the code.** The
  validator's own usage line documented a CLI that does not exist
  (`--run` without the `check` subcommand). Cost one turn. **The interface doc's
  own law — where doc and code disagree, the code is the behavior — applied to
  the validator's docstring. Fixed in the shipped file.**
- **Own error 6 (minor, self-caught): mis-anchored the changelog entry.**
  Inserted 07-14b's entry BEFORE 07-13g's, breaking chronology in an
  append-only log. Caught by re-reading the tail; moved. **Also: the first rev
  verification used a regex that under-counted (15 vs 17) — the FILE was right
  and the CHECK was wrong. Re-derived by the counter's own stated rule before
  concluding.** Recorded because the reflex to trust the check over the file is
  the same reflex W12 is about.
- **Own error 7 (minor, operator-caught): hedged about capacity instead of
  scoping honestly.** Proposed doing one reference doc "or both badly." The
  operator pushed: *"you don't think you could do both without issue?"* **Both
  were done, comfortably.** The hedge was defensive, not analytical.
- **Declined to certify what it could not observe — correctly.** Asked whether
  it was safe to clear the mount, the ctx said **no, it could not tell** — it
  cannot see the repo, and any answer would have been paperwork read back as
  observation. It supplied a three-check list instead. **The operator ran
  `tree`; both flagged gaps closed; the mount was cleared on evidence rather
  than assurance.**
- **Pushed back on an operator diagnosis and the diagnosis survived, refined.**
  The operator said discovery needs the schema; the ctx noted discovery *has*
  the schema inline and that the schema governs the one section nothing
  complained about. **The operator's underlying point — pin the shape, shrink
  the validator — was right and is now the basis of v2.6.** Recorded as the
  operator's, refined by the ctx.
- **All 13 patches unique-anchor asserted** (`assert s.count(old)==1`) across
  both reference docs; every one would have aborted on ambiguity. **Zero
  sentinel-free edits.** Both rev counters mechanically derived pre-filing per
  their own rules. Diagram HTML parse-verified.
- **No `sh`-vs-`bash` errors this session** — every multi-command and
  `${PIPESTATUS}` construct was run under explicit `bash -c` from the start.
  **The 07-13g/07-14 two-session pattern did not recur; the lesson held.**
- **The mount was present all session and was never read.** Path stated at
  boot, held throughout, re-confirmed when the operator asked.
- No interruptions. **W9 stays dead. W11 root-retired. W12 + W13 minted.**

## Boot manifest — P10 shape (REQUEST LIST)

**READ THIS FIRST.** The project mount is **CLEARED** [operator-confirmed
07-14b]. **The repo is the source of truth:** `~/git/repetae`, private, local,
on the operator's machine. **A ctx cannot read it.** Ask the operator to upload
what you need. **This manifest is a request list, not a currency table** — P10's
shape, exercised successfully on its first repo-era boot (this one), **still
UNRATIFIED**.

**Request the REQUIRED tier first. Request ON-DEMAND only if your target needs
it.** Do not pad out of caution — that friction is what tempts a future ctx to
re-mount.

| Doc | Repo path | Why needed | Tier |
|---|---|---|---|
| primer | `law/workshop_primer_v4.md` | **THE boot authority — read IN FULL.** Filing law items 1–6; boot loop; close protocol. **WARNING: it describes a MOUNT, which no longer exists. Read it knowing the mechanism is dead and the law is not.** v5 DEFERRED BY RULING; do not bump unprompted | **REQUIRED** |
| this checkpoint | `checkpoints/session_checkpoint_2026-07-14b.md` | the boot file | **REQUIRED** |
| depth checkpoint | `checkpoints/session_checkpoint_2026-07-14.md` | the repo migration; the validator's build session; the manifest this boot inherited | **REQUIRED** |
| lexicon | `law/workshop_lexicon_r17.md` | vocabulary + warts. **Marker: "Revision identity: rev 17" AND 17 dated changelog bullets (derive it — the counter is mechanically checkable). §10 must contain W12 AND W13. §9 must contain pair 14 (mount vs repo).** r13–r16 are sediment | **REQUIRED** |
| register | `law/primer_amendment_proposals_v3.md` | pending: **P3-R (3 pts), P9, P10 (1 pt each)**. NOT law. **v4 is OWED — P11 and the self-authored-suite rule are unfiled. If you file them, this becomes v4** | **REQUIRED** |
| diagram | `reference/system_diagram_r12.html` | **the tested-state ledger — the honest picture.** Marker: banner "Revised 2026-07-14 (the repo migration + first real discovery run)" AND "Revision identity: rev 12" (= 11 "Revised" stamps + 1) | ON-DEMAND — **REQUIRED if the session touches testing, evidence, or status** |
| discovery prompt | `pipeline/discovery_prompt_v2_5.md` | 547 lines. **v2.6 is the recommended next engine artifact; this is its input.** Read **Operator setup + Isolation + Preflight IN FULL** — not just the output family (see own error 1) | **REQUIRED if the session runs, edits, or re-versions discovery** |
| validator | `tools/discovery-validator/` (**whole dir — do NOT accept two files, see own error 3**) | P-2/P-3/P-4. **Marker: `rules.py` md5 `36af7fa2b878696084b71bdc6ec27c52`; `validate.py` md5 `642afe0ac96af5bb2faafba1f27238a9`.** Receipt: `python3 -m src.validate check --run <dir> --slug <slug>`. **⚠ THE FIXTURE SUITE IS KNOWN-STALE — `selftest`'s green proves self-consistency, not conformance (W12). Rebuild owed with v2.6** | ON-DEMAND |
| **Loeliger run output** | not in the repo — **operator-held, 8 files** | `discovery_loeliger-til.md` + 5 sidecars + `watchlist.csv` + **`session_report_loeliger-til.md` (NEVER READ — unassessed evidence)**. **The only real output this project has ever produced. Its CONTENT has never been assessed by anyone.** ⚠ **Not filed in the repo as of this close — ASK THE OPERATOR WHERE IT LIVES** | ON-DEMAND — **REQUIRED if the session writes v2.6** |
| test record | `evidence/discovery_test_record_v1.md` | P-1…P-7; still DRAFT; the 4-question docket. md5 `2758c0a8c46d29d182207a2b50535e24`, 21383 bytes | ON-DEMAND |
| charter + amendments | `law/engine_charter.md`, `law/engine_charter_amendment_v1_1.md`, `law/engine_charter_amendment_v1_2.md` | worklist lives in §9 as amended. **v1_1 is itself a transcription artifact (W1) — law with an asterisk.** ⚠ **Unchecked: whether the charter names `pipeline_config_schema.md` unsuffixed (the lexicon did — fixed in r17)** | ON-DEMAND |
| engine unit | `gate/topology_experiment_kit_v2.md`, `gate/topology_scorer_v2.py`, `gate/topology_scorer_v2_interface.md` | **rides together — never request one alone.** Receipt: `python3 topology_scorer_v2.py selftest` → 18 PASS, exit 0. **`WIRE_VERSION = "wire-0"` is the PROTOCOL version — never bump it in a rename. ⚠ W12 applies to its 18/18: same construction, ctx-authored fixtures, cell unopened** | ON-DEMAND |
| config schema | `pipeline/pipeline_config_schema_v2.md` | header "# pipeline_config.schema.md — v2"; "RATIFIED 2026-07-13b"; Appendix C; 637 lines; md5 `d3f866c4e1a834025070a1d1511437e8`. **W9 CLOSED 07-14** | ON-DEMAND |
| pipeline prompts | `pipeline/harvest_map_v1.md`, `pipeline/harvest_residue_v1.md`, + `_kit_spec` pair, `pipeline/harvester_prompt_v1.md` | CONDITIONAL status per amendment v1.2 item 7 | ON-DEMAND |
| exhibits | `evidence/discovery_sailing-for-dummies_SALVAGE.md`, `evidence/harvest_topology_proposal_laymans_guide.md`, `evidence/harvest_brief_little-schemer.md` | SALVAGE is **PROVISIONAL** (docket Q3) — the name carries that and must not be dropped | ON-DEMAND |
| orientation | `reference/how_we_build_wikis_from_books.md` | layman overview; reference, not authority | ON-DEMAND |
| older checkpoints | `checkpoints/` (13 more, 07-10b → 07-13g) | narrative history | ON-DEMAND |

**Verification under the repo rule.** The content-marker check is **the only
handshake** confirming the operator uploaded the file the manifest meant. There
is no mount copy to compare against. **For every REQUIRED doc, confirm the
marker before working.** Where a marker is mechanically derivable (both rev
counters), **derive it — do not eyeball the identity line.** This session found
three defects in a file whose identity line was perfectly correct.

**The honest limit, unchanged from 07-14 and now witnessed:** this manifest
cannot verify itself. A ctx cannot detect a repo file that was never handed
over, nor distinguish "absent because unneeded" from "absent because
forgotten." **Enforcement is entirely operator-side.** If something looks
missing, ask — do not infer, and do not proceed on a guess.

**And the lesson this session paid for, stated where the next boot will read
it: a green self-test is not evidence. Ask what authored the fixtures.**

**Planned successor** [operator]: a script. The ctx emits a CSV of repo paths;
the operator runs it; the returned files are the boot set. Not built. When
built, this table becomes its input.
