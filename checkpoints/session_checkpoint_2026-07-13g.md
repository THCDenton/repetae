# Session checkpoint — 2026-07-13g (the migration: W11 retired at the root)

Purpose: boot file for the next session. Files are the only memory. Written
under checkpoint schema v2.1 (five mandatory slots, boot manifest last).
Reads alongside 07-13f. **Model this session: Opus** (Claude Opus 4.8) —
third Opus workshop ctx. Per the 07-13d handoff law this is a third
capability-probe record: **the boot stumbled exactly where predicted, the
protections caught it for the second consecutive session, and then the
session removed the need for the protections entirely.**

## What this session was

A **filing session**, and the shortest of the 07-13 run. The operator ruled
the migration that had been PREFERRED-next for three sessions and owed for
four. No design changed. No pipeline actor moved. Three engine files got new
names, and the project's most reliable failure mode stopped being possible.

The session also produced the first clean example of **the clean fix beating
the workaround before the workaround became law**: P1–P3 were two evidence
points from ratification into primer v5; the migration killed their subject
first. P8 — the sunset clause filed at 07-13f precisely to anticipate this —
fired on schedule.

## Verified state changes

1. **W11 RECURRED A THIRD TIME — caught again by hand-applied P1–P3.** Both
   unmigrated artifacts served stale, third consecutive boot:
   - `topology_experiment_kit_v1.md` — ended §7→§8, **no §7-M**; discriminator
     `grep -c "7-M\|Manual chat lane"` = **0**. **The false-positive-marker
     trap fired exactly as the register predicted:** the stale copy DID carry
     `res:sail:rrs_reservation`, so that marker proved nothing.
   - `topology_scorer_v1.py` — self-test printed GREEN, exit 0, but **17
     PASS**; `grep -c "manual-chat\|manual lane\|deferred"` = **0**.
   Per P3: **no flags raised against the manifest, no receipt reported**,
   refile requested. Operator refiled. Post-refile verification: kit §7-M
   present at line 315 (5 subsections 7-M.1→7-M.5); scorer live run →
   **SELF-TEST GREEN, exit 0, 18 PASS** incl. the manual-lane assertion;
   discriminator = 10. **Three boots, three hits, zero exceptions. The hazard
   was 100% reproducible — which is what made the cheap greps trustworthy.**
2. **THE MIGRATION PERFORMED — three files, W11 retired at the root.**
   - `topology_experiment_kit_v1.md` → **`topology_experiment_kit_v2.md`**
   - `topology_scorer_v1.py` → **`topology_scorer_v2.py`**
   - `topology_scorer_v1_interface.md` → **`topology_scorer_v2_interface.md`**
   All three carry a prominent **"v2 is a FILING MIGRATION, not a design
   change"** note. Cross-pointers updated so the unit is internally
   consistent (kit→scorer, scorer→kit, interface→scorer).
3. **The scorer's bump was PROVEN inert, not asserted inert.** `diff` of
   everything below the docstring: **byte-identical**. Line count 722 → 734 =
   the 12-line note exactly. Post-bump live run: **18/18 GREEN, exit 0**. This
   is the receipt.
4. **`WIRE_VERSION` deliberately NOT touched.** `wire-0` is the **protocol**
   version, not the file's version; bumping it would have changed scorer
   behavior and blast-radiused every fixture. Recorded in the scorer's
   docstring so no future session "fixes" the apparent inconsistency.
5. **P8 FIRED; P1–P3 struck rather than ratified; P3-R carved out.** Register
   re-filed as `primer_amendment_proposals_v2.md`. P1/P2 are scaffolding for
   unmigrated boot docs and now have no subject. **P3 was split**: its
   manifest-vs-fresh-reading tiebreak dies with P1; its
   **never-report-an-unperformed-receipt** half is subject-independent and
   survives as **P3-R at 3 evidence points — the batch is now P3-R alone.**
6. **Worklist (charter §9 as amended): unchanged.** No worklist item built.
   **Clerical RETIRED: kit + scorer migration (this session).** Clerical
   carried: discovery v2.6 re-version; BJJ discovery back-pass; **config-schema
   v2 re-file (W9 lag #4 — now a FIFTH session)**. Carried: ratify or reject
   the `discovery_test_record_v1` docket (4 open questions).

## Rulings (this session)

- **The migration is a filing bump; internal versions bump to match**
  [operator-ruled, button: *"lets do the rename"*; ctx-proposed `_v2` +
  internal bump with the counter argued]. Filing law item 4 requires filename
  rev == internal rev. The alternative (`_v1_1`, honest about unchanged
  content) was rejected as inventing a convention the law lacks. Cost accepted:
  a migration note in each file so no session hunts a nonexistent design delta.
- **The interface doc migrates in lockstep, beyond the literal ruling**
  [session-ruled, flagged in-chat, not silent]. The operator said "the
  rename," and P8 names only kit + scorer. But the interface doc is an
  unmigrated boot-manifest doc: leaving it would keep one live subject in the
  mount-currency column and **prevent P8 from firing cleanly**. The
  engine-unit rule (it rides with the scorer) settles it. Recorded as a
  judgment call, not an assumption.
- **P1–P2 are struck, not ratified; P3-R survives the strike** [session-ruled,
  lean stated with strongest counter, operator ratification OWED]. Ratifying
  law that describes an impossible condition is the outcome P8 existed to
  prevent. The counter — *migration is lazy, so new unmigrated docs can appear*
  — is answered by W11 living in the lexicon's warts ledger (the right home for
  a per-doc recurring hazard) rather than as permanent primer law.
- **Reconstruction from transcripts REFUSED** [session-ruled; operator
  instruction declined with reasons; operator then supplied the real files].
  The operator asked the ctx to re-mint the kit and scorer from conversation
  history. Declined: 32KB of Python with 18 assertions cannot be faithfully
  transcribed, and the result would have carried a **v2 name outranking the
  real thing** — sediment promoted to current. Precedent cited: the sailing
  SALVAGE doc, still PROVISIONAL, exists because *the workshop transcribes; it
  does not author ops history*. The files were never lost, only stale.

## Ground truth learned this session

- **The clean fix beat the workaround, and that is the headline.** P1–P3 were
  three well-evidenced rules, drafted, stable, two points from becoming boot
  law. A 20-minute rename made them unnecessary. **The lesson generalizes: when
  a protection and a structural fix are both on the table, the structural fix
  retires the protection — so prefer spending the session on the fix.** The
  register's P8 was what made this legible instead of embarrassing.
- **A 100%-reproducible hazard is a cheap hazard.** W11 fired on three of
  three boots. That perfect reproducibility is exactly what let two one-line
  greps replace an index round-trip. **A hazard that fires intermittently would
  have been far more expensive to defend against** — and would have justified
  P1–P3 as permanent law.
- **The false-positive-marker trap was confirmed live, not theoretically.**
  The stale kit carried `res:sail:rrs_reservation` — a marker the 07-13c-era
  copy legitimately has. Any manifest marker that BOTH versions carry proves
  nothing. **A currency marker must be content the prior version demonstrably
  LACKS.** The register predicted this at 07-13f; 07-13g observed it.
- **Protocol versions are not file versions.** `WIRE_VERSION = "wire-0"` sat
  in the middle of a file being version-bumped. Renaming it would have been a
  silent behavior change disguised as clerical work. **Any future migration
  must distinguish a file's identity from the protocols it implements.**
- **The operator's "just re-mint it from the transcripts" was the session's
  sharpest test.** It was a reasonable-sounding instruction that would have
  quietly poisoned the engine unit — a fabricated scorer carrying a v2 name,
  self-testing against fixtures it invented, indistinguishable from the real
  thing until it graded a real run wrong. **Declining an operator instruction
  with reasons, and being right, is a data point for the PM-methodology
  harvest.** The correct move was not "obey" or "refuse" but "here is what
  that costs; check your downloads first" — and the files were there.
- **Three sessions of Opus capability data now agree.** Opus reasons well on
  artifacts and self-corrects when it checks the artifact first; its failure
  mode is confident conclusions BEFORE reading. **This session had zero such
  stumbles — because the checkpoint told it exactly what to distrust.** The fix
  remains procedural, not model-tier: a good manifest is worth more than a
  better model.

## Dependency ledger (verified-how) — schema v2.1 slot

| Dependency | Status | Verified how |
|---|---|---|
| `workshop_primer_v4.md` | ✓ | read IN FULL (boot authority); header exact "v4, issued 2026-07-13d"; filing law items 1–6, boot loop, engine/reference split, close protocol confirmed; `ls` confirms highest `_v` on stem (no v5 — correct, deferred by ruling) |
| `workshop_lexicon_r15.md` (rev 15) | ✓ | grep: "Revision identity: rev 15"; 15 dated changelog entries = rev (mechanical check); final entry "- 2026-07-13f (post-close addendum) —"; §8 rows for both new artifacts present; §10 W11 "RECURRED 2026-07-13f" present. Re-issued this close as **r16** |
| `system_diagram_r10.html` (rev 10) | ✓ | grep: "Revision identity: rev 10"; banner "Revised 2026-07-13f (tested state):"; tested-state ledger present; `.status-x` class present. Re-issued this close as **r11** |
| `session_checkpoint_2026-07-13f.md` | ✓ | newest date-suffix confirmed by `ls` (no 13g+ at boot); read in full; its manifest drove this boot and its P1–P3 instruction WORKED for the second consecutive session |
| `primer_amendment_proposals_v1.md` | ✓ | header "# Primer amendment proposals — addendum v1"; "OPEN REGISTER. Nothing here is law."; P1–P8 summary table read; P8 sunset text read in full at line 180. Re-filed this close as **v2** (P8 fired) |
| `topology_experiment_kit_v1.md` | ⚠→✓ **STALE MOUNT COPY at boot (W11, 3rd consecutive)** | boot copy: no §7-M (grep = 0), ended §7→§8, but HAD `res:sail:rrs_reservation` (false-positive-marker trap confirmed). After operator refile: §7-M at line 315, 5 subsections, header + §7-M read. **MIGRATED this close → `topology_experiment_kit_v2.md`; W11 RETIRED for this file** |
| `topology_scorer_v1.py` | ⚠→✓ **STALE MOUNT COPY at boot (W11, 3rd consecutive)** | boot copy: GREEN but **17 PASS**, discriminator grep = **0**. After refile: live run **SELF-TEST GREEN, exit 0, 18 PASS** incl. manual-lane assertion; discriminator = 10. **MIGRATED → `topology_scorer_v2.py`; body proven byte-identical by diff; re-verified 18/18 post-bump. W11 RETIRED for this file** |
| `topology_scorer_v1_interface.md` | ✓ | header "# Topology Scorer v1 — behavior (layman) + interface reference"; 4 scorer refs located. **MIGRATED → `topology_scorer_v2_interface.md`; W11 RETIRED for this file** |
| `pipeline_config_schema.md` | ⚠ **W9 lag #4 STILL — FIFTH session** | `ls` confirms `pipeline_config_schema_v2.md` ABSENT from mount; mount holds v1. Re-file OWED from the operator's 07-13b download. **This is now the project's oldest unretired clerical debt and the largest remaining W11 subject** |
| `workshop_lexicon_r14.md` | ⚠ **SEDIMENT PRESENT ON MOUNT — flagged** | 07-13f declared r14 "superseded before filing; must NOT be filed." It IS on the mount. Verified genuine sediment (grep: 0 register rows, rev-identity "rev 14"); ranks below r15 by `ls`, so currency is unharmed. **Deletable at leisure; correctness does not depend on it** (filing law item 5) |
| `discovery_test_record_v1.md` | ✓ (presence) | on mount; DRAFT, unratified; 4-question docket carried. NOT read in full — not required by this session's target |
| `discovery_prompt_v2_5.md` | ✓ (presence) | on mount; `ls` confirms highest `_v` on stem. **v2.6 re-version still OWED**. NOT re-read this session |
| Charter / amendments / harvest_map / harvest_residue / kit specs / exhibits / SALVAGE | 07-13f pins carried | NOT touched this session; next boot re-verifies per the loop |
| Known-absent carried: `sources.md`, Schemer master doc, JJU source, `glossary_index_v31.md` (JJU-side BY DESIGN) | ✗ | unchanged; unblocking |

## Propagation / blast-radius log

- **ZERO design blast radius. This is the point of the session.** No pipeline
  actor, wire schema, enum, fixture, threshold, prompt, or gate rule changed.
  The scorer's code body is byte-identical by `diff`; the kit's design text is
  unchanged from the 07-13c ship.
- **Filename blast radius, fully chased:** every live pointer to the old names
  updated — kit body (3 refs → v2), scorer docstring + usage strings, interface
  doc (4 refs), lexicon §8 (3 registry rows re-keyed), diagram tested-state
  ledger (3 rows re-keyed). **Historical banner stamps in the diagram retain
  the v1 names deliberately** — they are a record of what happened at 07-13c,
  not pointers. Same for each file's own migration note.
- **`WIRE_VERSION` untouched** — protocol, not file identity. Zero fixture
  blast radius. The 07-13c enum-propagation discipline is intact.
- **Register semantics changed without the primer changing.** P1–P3 went from
  "ready — awaiting ratification" to struck-recommended. **No boot law moved;
  primer v4 is still the authority and still contains none of P1–P3.** The only
  live protection remains this checkpoint's manifest — and after this
  migration, it has far less to protect.

## Open design questions register — delta

NEW:
1. **Ratify the strike?** P1–P2 struck-recommended, P3-R proposed as the batch.
   Needs an operator ruling. Lean stated in the register with the strongest
   counter (lazy migration ⇒ new unmigrated docs could appear) and its answer
   (that is what the W11 wart entry is for).
2. **Does the interface-doc migration need retroactive blessing?** Taken as a
   session ruling beyond the literal "rename" instruction, flagged not silent.
   Lean: it was necessary for P8 to fire cleanly; ratify it.

CARRIED (all four from the 07-13f test-record docket, none closed): fixture
sequencing (v2.5 vs owed v2.6); fixture sources (synthetic vs Schemer
ClearScan); whether the SALVAGE doc's PROVISIONAL status must retire before
Run B counts as first-party evidence; whether P-1 is workshop or ops.

CLOSED THIS SESSION: the suffix convention (**resolved: `_v2` + internal bump
to match, per filing law item 4** — was carried as an open question since
07-13e).

Also carried: boot-set weight; **Opus capability calibration — third data
point: a well-specified manifest eliminated the failure mode entirely this
session**; the PM-methodology harvest (**this session's prime material: the
declined transcript-reconstruction instruction, and the clean-fix-beats-the-
workaround pattern**).

## Reference-doc debt — slot

**PAID at this close, in lockstep:**
- **Lexicon r16** (`workshop_lexicon_r16.md`) — §8 three rows re-keyed to the
  migrated filenames with W11-retired annotations; §2 filing-law note
  corrected (it named the kit and scorer as W11's live subjects — no longer
  true; now names `pipeline_config_schema.md` and the unmigrated exhibits);
  §10 W11 annotated **RECURRED-3x-then-RETIRED** for these three files, **LIVE**
  for remaining stem-stable docs; +1 dated changelog entry. Rev derivation
  verified mechanically pre-filing: **16 dated changelog entries = rev 16** =
  filename.
- **Diagram r11** (`system_diagram_r11.html`) — banner stamp "Revised
  2026-07-13g (the migration)" appended; rev identity → rev 11; tested-state
  ledger three rows re-keyed. Rev derivation verified mechanically pre-filing:
  **10 "Revised" stamps + 1 = rev 11** = filename. HTML integrity checked
  (`<tr>`/`</tr>` 35/35, `<p>`/`</p>` 26/26, mermaid block intact).
- **Register v2** (`primer_amendment_proposals_v2.md`) — P8 discharged; P1–P2
  struck-recommended; P3 split and **P3-R** minted at 3 evidence points; all
  three P1–P3 evidence counts incremented to 3 per the register's own rule; a
  new **evidence increments log** section added (the mechanism the 07-13f
  ruling specified); the interface-doc judgment call recorded under P8.
  **v1 is sediment.**

**PRIMER v5 — status UNCHANGED: DEFERRED BY RULING** [operator, 07-13f]. This
session did **not** bump the primer and did not attempt to. **What changed is
the size of the deferral's cost: it just shrank dramatically.** The reason the
deferral was risky was P1–P3 sitting unratified while W11 fired every boot.
W11 is now retired for the artifacts that were firing. **The register's
remaining batch (P3-R) protects against a rarer failure, so deferring further
is cheaper than it was yesterday.**

**What the deferral still costs:** P3-R is not law. A ctx that fabricates a
receipt is still only caught by an operator noticing. That happened once
(07-13e) and was expensive.

## Recommended next session

**PREFERRED — the gate run, manual chat lane (kit §7-M).** The blocker is
gone. The migration was the last thing standing between this project and its
first contact with real material, and the standing missing proof point (*no
book has completed discovery end-to-end against a clean substrate*, open since
07-11) is not getting younger. The operator drives per §7-M.1: mints
`custom_id`s, assembles packets, runs each worker in a fresh ctx OUTSIDE the
project, pastes fenced output back; the workshop ctx collects into `wire.jsonl`
and runs `python3 topology_scorer_v2.py score --run DIR` (**Layer A only; no
`--key`**) after each batch. Layer B / compare / the gate verdict need the
sealed key and stay ops-side. Before the first packet: fix the **parity
constraint** (§7-M.5 — same model for both arms' equivalent actors, recorded in
`meta.json`; a tier difference measures the tier, not the topology), and pick
the arm + Tier F fixture. Run Layer A incrementally per §7-M.3 — a
transcription defect found late contaminates everything filed after it.

**ALTERNATIVE — the config-schema re-file (5 minutes, oldest debt, W11's last
big subject).** `pipeline_config_schema_v2.md` has been owed since 07-13b and
absent across five boots. It is the largest remaining stem-stable hazard. **If
the operator has the 07-13b download to hand, this is nearly free and should
be folded into any session rather than given its own.**

**ALTERNATIVE — ratify the test record + build P-2/P-3/P-4** (the cheap lint
half). Honest caveat unchanged from 07-13f: it lands with the same cell the
scorer has — green on fixtures we authored, never having seen real output —
and it CANNOT detect fabricated provenance.

Clerical owed regardless: **config-schema v2 re-file (FIFTH session)**;
discovery v2.6 re-version; BJJ discovery back-pass; ratify-or-reject the strike
(P1–P2) and P3-R.

## Session hygiene / corrections ledger (own errors + events)

- **Model this session: Opus** (Claude Opus 4.8) — third Opus workshop ctx;
  third capability-probe record per the 07-13d handoff law.
- **Boot: CLEAN. Zero stumbles, zero false flags, zero invalid receipts.** W11
  fired on both unmigrated artifacts exactly as the 07-13f manifest predicted;
  P1–P3 applied by hand; refile requested and honored. **The manifest did the
  work — this is the strongest evidence yet that the fix is procedural, not
  model-tier.**
- **Own error 1 (minor, self-caught): a `str_replace` anchor failed** on the
  lexicon W11 patch — a leading-newline mismatch against the file's actual
  wrapping. Caught immediately by the tool's own failure, re-read the exact
  bytes with `view`, re-anchored, succeeded. No damage. Lesson reinforced:
  re-read anchors immediately before editing; do not reconstruct them from
  earlier output.
- **Own error 2 (minor, self-caught): two bash heredoc/`$()` constructs failed**
  under `sh` (`Bad substitution`, `Syntax error: "(" unexpected`). Re-run under
  explicit `bash -c`. No damage; the affected checks were re-run and passed.
- **Own error 3 (near-miss, caught by reading): almost bumped `WIRE_VERSION`.**
  A blanket version-string sweep over the scorer would have caught `wire-0` and
  silently changed protocol behavior inside a "clerical" rename. Caught by
  grepping version strings and reading each hit before editing rather than
  running a global `sed`. **Recorded as the sharpest hazard of the session** —
  the most dangerous edit was the one that looked most routine.
- **Declined an operator instruction, with reasons, and was right.** The
  operator instructed the ctx to re-mint the kit and scorer from conversation
  transcripts. The ctx declined, cited the SALVAGE precedent, named the
  specific harm (a fabricated v2 outranking the real artifact), and suggested
  checking downloads first. **The operator had the files.** Logged as
  PM-methodology harvest material and as evidence for the loud-rulings posture.
- **All patches unique-anchor asserted** — 5 lexicon patches, 4 diagram
  patches, 5 register patches, each with an explicit `assert count == 1`
  guard that would have aborted on ambiguity. Sentinel-free editing throughout.
- **Live scorer receipts (both valid, both performed):** pre-migration
  post-refile → GREEN, exit 0, 18/18; post-migration `topology_scorer_v2.py
  selftest` → GREEN, exit 0, 18/18. **Plus a `diff` proving the code body
  byte-identical** — the migration's central claim was demonstrated, not
  asserted.
- **Rev derivations mechanically verified pre-filing:** lexicon = 16 dated
  changelog entries → rev 16; diagram = 10 "Revised" stamps + 1 → rev 11. Each
  checked against that counter's own stated rule.
- **`refile = remount` used successfully** (operator refiled kit + scorer
  mid-boot, via upload). Not a ctx move; no cross-project hop; nothing to
  catalog.
- **Sediment flagged, not acted on:** `workshop_lexicon_r14.md` is on the mount
  despite 07-13f declaring it never-to-be-filed. Verified inert. Per filing law
  item 5, correctness never depends on deletion — reported as courtesy only.
- No interruptions. No new W-class events. W11 retired for three files, LIVE
  for the rest. W9 lag #4 persists into a fifth session.

## Boot manifest — schema v2.1 slot (pins the next boot)

Verify each doc by confirming its exact filename is the highest suffix on its
stem, opening it, and matching the content marker.

**MAJOR CHANGE FROM 07-13f: the mount-currency column is nearly empty.** The
kit, scorer, and interface doc are MIGRATED — `ls` now ranks them and a stale
copy cannot impersonate the current one. **Do NOT expect W11 on them; if a
`_v1`-named copy appears, it is sediment by its own filename.** The remaining
stem-stable docs are listed with their exposure intact.

| Doc | File | Content marker | Mount-currency |
|---|---|---|---|
| primer | `workshop_primer_v4.md` | header "v4, issued 2026-07-13d"; section "Filing & versioning law". **THE boot authority — read IN FULL. v5 remains DEFERRED BY RULING (07-13f); its proposals live in the register. Do NOT bump the primer unprompted.** If `workshop_primer_v5.md` exists, it is newer; re-anchor on its checkpoint | migrated (`_v`) — `ls` ranks |
| lexicon | `workshop_lexicon_r16.md` | "Revision identity: rev 16"; final changelog "- 2026-07-13g — **the migration session**"; §10 W11 contains "RECURRED A THIRD TIME 2026-07-13g" AND "STATUS: RETIRED for the kit, scorer, and scorer-interface doc". **r14 AND r15 are sediment** | migrated (`_r`) — `ls` ranks |
| diagram | `system_diagram_r11.html` | banner "Revised 2026-07-13g (the migration):" AND "Revision identity: rev 11" | migrated (`_r`) — `ls` ranks |
| **kit spec** | **`topology_experiment_kit_v2.md`** | header "# Topology Experiment Kit v2"; **"v2 is a FILING MIGRATION, not a design change"** note in the first paragraph; §7-M present (5 subsections, "Manual chat lane — API mimicry protocol") at ~line 322; §3 Tier F table incl. `res:sail:rrs_reservation` | ✅ **MIGRATED 07-13g — W11 RETIRED. `topology_experiment_kit_v1.md` is sediment** |
| **scorer** | **`topology_scorer_v2.py`** | docstring line 2 "topology_scorer_v2.py"; "v2 IS A FILING MIGRATION" note. Receipt: `python3 topology_scorer_v2.py selftest` → **SELF-TEST GREEN, exit 0, 18 PASS** incl. "manual lane: tokens deferred, waves enforced → DAG RATIFIED with deferred list" | ✅ **MIGRATED 07-13g — W11 RETIRED. `topology_scorer_v1.py` is sediment.** Note: `WIRE_VERSION = "wire-0"` is the PROTOCOL version — **never bump it as part of a file rename** |
| **scorer doc** | **`topology_scorer_v2_interface.md`** | header "# Topology Scorer v2 — behavior (layman) + interface reference"; §2.5 documents `deferred` | ✅ **MIGRATED 07-13g — W11 RETIRED. v1 is sediment** |
| **register** | **`primer_amendment_proposals_v2.md`** | header "# Primer amendment proposals — addendum v2"; "**re-filed as v2 on 2026-07-13g when P8's sunset clause TRIGGERED**"; summary table shows P1–P2 STRUCK-RECOMMENDED and **P3-R** present | unmigrated but suffixed at mint. **NOT a boot authority — read for pending proposals. v1 is sediment.** If you hand-apply a protection, increment its evidence count at close |
| test record | `discovery_test_record_v1.md` | header "# Discovery — test record & test proposals, v1"; "Status: DRAFT for operator ratification"; Part 1 / Part 2 split; P-1…P-7 present | unmigrated but NEW (no ancestor ⇒ cannot be impersonated yet) |
| discovery prompt | `discovery_prompt_v2_5.md` | header "# Discovery Prompt v2.5"; 547 lines; §"Terminal states" lists ratified / blocked-with-handoff / failed. **v2.6 OWED** (→ `discovery_prompt_v2_6.md`) | migrated (`_v`) — `ls` ranks |
| config schema | `pipeline_config_schema_v2.md` | header "# pipeline_config.schema.md — v2" AND "RATIFIED 2026-07-13b"; Appendix C. **OWED from the operator's 07-13b download — absent across FIVE boots** | ⚠ **W11 LIVE — the largest remaining stem-stable hazard. Mount holds `pipeline_config_schema.md` v1. If you read the v1 file, you are reading sediment** |
| salvage exhibit | `discovery_sailing-for-dummies_SALVAGE.md` | header "Status: conventions ratified 2026-07-09, discovery_prompt_v2"; SALVAGE NOTICE; **PROVISIONAL — docket Q3** | ⚠ unmigrated — W11-eligible; index-check if it looks off |
| charter amendment | `engine_charter_amendment_v1_2.md` | header "# Engine Charter — Amendment v1.2" + "ratified 2026-07-12" | ⚠ unmigrated but stable; index-check if off |
| checkpoint (this) | `session_checkpoint_2026-07-13g.md` | newest date-suffix on the mount; ends with this manifest | date-suffix (`ls` ranks) |
| checkpoint (depth) | `session_checkpoint_2026-07-13f.md` | header "tested state + the discovery test record"; holds the tested-state findings and the 4-question docket | date-suffix |
| topology exhibit | `harvest_topology_proposal_laymans_guide.md` | footer evidence label; bracket appendix; Phase 1 chunk-plan bullet | ⚠ unmigrated; index-check if off |

Mismatch → primer v4's rules apply: older suffix = flag before work; newer
suffix = find the later checkpoint and re-anchor; **stale stem-stable copy
(marker missing/old but no newer suffix) = request a refile, do NOT proceed on
the mount copy (W11 — now only applies to the docs marked ⚠ above)**; stale
primer = the boot's one hard stop.
