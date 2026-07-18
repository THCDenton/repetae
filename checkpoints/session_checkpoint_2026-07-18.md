# Session checkpoint — 2026-07-18 (v2.7 written AND tested; a new defect class found)

Purpose: boot file for the next session. **Files are the only memory, and the
files live in a git repo the ctx cannot read.** Written under checkpoint schema
v2.1 (five mandatory slots, boot manifest last). Reads alongside 07-15b.
**Model this session: Opus** (Claude Opus 4.8) — eighth Opus workshop ctx, per
the 07-13d handoff law (an eighth capability-probe record).

**Boot CLEAN.** Requested files arrived as file attachments (not pastes), md5s
verified against the 07-15b handshake on disk before any script ran. The
paste-is-not-a-file lesson held: every file this session ran a script against
reached `/mnt/user-data/uploads` first and was `ls`+`md5sum`-confirmed.

## What this session was

**The v2.7 session 07-15b scoped but couldn't write — written, tested against a
real book, and vindicated. Then the test found a NEW defect class.**

This is the strongest kind of result the project produces: v2.7 was drafted by
this ctx, then shipped UNTESTED to a separate discovery run on Loeliger, then
audited by a THIRD independent ctx. Neither the runner nor the auditor saw this
ctx's reasoning. They converged. That is the P12 loop working exactly as
designed — a self-authored artifact validated by separated output.

## Verified state changes

1. **discovery_prompt_v2.7 WRITTEN AND TESTED.** md5 `1a19649fda7e971969a414e9612f23e9`,
   723 lines (from v2.6's 680). Four ruled changes from the 07-15b scope, all
   applied by patch script with md5-gate + self-check, and all three fixes
   EXERCISED by a real challenge in the test book:
   - **Item 11 (schema boundary) — Option B applied.** The enumerated field
     lists are GONE; replaced by a rule pointing at `pipeline_config_schema_v2.md`.
     **Test result:** the schema was NOT in the run's environment. The run wrote
     fields plain, minted NO `v2-proposed`, minted NO `v3-proposed`, and flagged
     "field status unverified" in the read-back — instead of reconstructing a
     remembered list. The rule's "uncertainty is a read-back flag, not a guess"
     branch fired correctly on first contact.
   - **Item 1 (graded `[mechanical:]` tag) — applied.** Tag is now
     `[mechanical: <method>; <grade>]`, grade ∈ {exhaustive, sampled, partial}.
     **Test result:** the run graded `Class: = Function: = 172, exact` as
     `exhaustive` (the case it was built for); the auditor confirmed every tag
     carries a valid grade and NO partial-graded universal shipped — the rappers
     defect class did not recur.
   - **Item 2 folded into item 1** (one fix). A `partial`-graded universal is a
     defect requiring downgrade — this is what would have blocked the false
     rappers "always The <Name>" line.
   - **Item 5 (raster rule) — now a DETECTOR, not only a confirmer.** **Test
     result: this is the fix that earned its keep.** The run rasterized up front
     and caught the `■`→`B` block-glyph OCR corruption that is INVISIBLE in the
     text layer. Under the old confirmer-only rule, nothing would have triggered
     a look — the text extraction looked clean. The detector change caught a
     defect the confirmer would have shipped.
2. **discovery_audit_prompt v2 WRITTEN.** md5 `6a07525397fd6ba5a4b88b2e35f09abe`,
   151 lines. **Generalized, not synced** — see the ruling. The only
   version-coupled section (the hard-coded five-sidecar roster) was replaced by
   the principle that generates it. Method lines, stance, and the function claim
   ("goldfish who read 3%") are untouched. **This is the FIRST version of this
   file with a repo home** — v1 never had one.
3. **NEW DEFECT CLASS FOUND AND DOCKETED: "coverage by silence."** The Loeliger
   chunk plan claims "every in-scope range in exactly one chunk" but silently
   drops printed p174–179. **Confirmed by TWO independent methods:** the
   auditor's arithmetic (chunk rows jump p173→p180) AND this session's raster
   read of the pages against the binary. **What is actually dropped:** §6.2 "A
   Classy Cross-Reference" (the class-organized keyword index) and §6.3 "Sum
   Total" (the chapter summary). Root cause: **printed p174 does double duty**
   (dictionary end + §6.2 start), and the plan's boundary logic assumed one
   page = one owner. Drafted as `docket_chunk_coverage_reverify_v1.md`, md5
   `0d22783c4a236dc906c46d6618da4af7`.
4. **THE OPERATOR SHARPENED THE FINDING FROM "lint" TO "detector + re-verify
   loop"** [operator-decided]: the coverage arithmetic should not merely fail
   the run on a gap — it should TRIGGER a mandatory re-verification of the
   affected pages (rasterize, read, then chunk-or-evidence-exclude). **This is
   the identical confirmer→detector upgrade v2.7 made to the raster rule, one
   level up.** The rule's teeth: *a page may not be dropped by silence; it is
   dropped only by a stated, page-checked reason.*
5. **THE AUDIT PROMPT IS NOT IN SCHEMA-LOCKSTEP WITH DISCOVERY** [operator-reasoned,
   ctx-confirmed]. The instinct "keep the audit prompt in sync with discovery"
   is BACKWARDS: the audit prompt's value is that it does NOT know what the
   discovery prompt says (it reads output cold). Syncing it leaks the answer
   key. The correct coupling: **the audit prompt gets MORE GENERAL as discovery
   evolves, never synced to it.** Every version-specific detail is a staleness
   bug AND a contamination risk. This is a genuine second finding, distinct from
   schema-lockstep despite looking identical — owed to the register.
6. **AUDIT FINDINGS ARE IN THE REPO after all.** 07-15b carried
   `discovery_eval_findings_rappers-handbook.md` as "NOT IN THE REPO." The
   requisition `req` returned it OK (md5 `0e9ee488…`). Either filed since, or
   the 07-15b claim was wrong. **That loose-evidence cleanup item is already
   done.** (Same W14 shape: a manifest asserted an absence a script falsified.)

## Rulings (this session)

- **v2.7 scope held TIGHT** [operator-ruled]: core items 1, 2, 5, 11 + item 3's
  logic. Items 4/7/9 NOT folded in (the 07-15b "if cheap" options) — deliberately
  left to keep the session from the scope-creep that killed 07-15b. Item 6
  docketed, item 10 not acted on.
- **Item 11 → Option B**, as ruled 07-15b. Applied verbatim to spec.
- **Audit prompt GENERALIZED, not synced** [operator-decided]. Bumped to v2 (the
  coupling model changed, not just content). The generalization is safe
  regardless of the file's untrusted-reconstruction baseline — but it does NOT
  fix that baseline. **v2 is more general, NOT more validated.** Its real test
  is the same as v1's: run it cold on a pile and see if it bites. Not done.
- **Coverage finding → DOCKET, homes UNDECIDED** [operator-ruled: *"draft the
  rule as a docket item, decide homes later"*]. Two candidate homes (discovery
  prompt author-time check; engine lint independent check); v2.7-era logic
  argues both, the way schema-lockstep needed both ends. Deferred as its own
  session's work.
- **Loeliger p174–179 patch: NOT done this session.** Captured in the docket as
  local cleanup owed. The pages are identified (§6.2 + §6.3); a future session
  adds a chunk or an evidenced exclusion.

## Ground truth learned this session

- **The confirmer→detector upgrade is a REUSABLE MOVE, not a one-off.** v2.7 made
  it for the raster rule; the operator immediately recognized the same shape for
  coverage arithmetic. Watch for it elsewhere: any check phrased as "double-check
  a verdict you already have" is a candidate to become "go looking up front."
- **"Coverage by silence" is a distinct class from "defer instead of chunk."**
  Defer = a chunk that names itself and doesn't cut. Coverage-by-silence = a
  range no chunk names at all. Both are honest-looking, both invisible to a
  reader, both catchable only by arithmetic. The docket says so explicitly so a
  future session doesn't merge them.
- **A shared boundary page breaks the one-page-one-owner assumption.** Printed
  p174 is dictionary-tail AND §6.2-head. This is a discovery-prompt-level
  assumption worth a note (not fixed this session) — it will recur wherever
  back-matter abuts a prose section.
- **The text layer lies, confirmed a THIRD time.** The run caught `■`→`B` by
  raster; this session caught the same corruption on p173–174 by raster while
  investigating the gap. `pdftotext` on this scan reads clean and is wrong in
  exactly the content-bearing places.
- **"Most complex stage" is the wrong frame for discovery** [ctx-reasoned, on
  operator question]. Discovery is the hardest to AUTHOR (it meets the unknown,
  makes irreducible judgment calls) but the design actively pushes MECHANISM out
  of it (item 11 removed a field list; the coverage finding wants to push a
  check into a lint). The harvest's coordination-without-communication is a
  deeper runtime complexity. Discovery should be thick with judgment, thin on
  mechanism. Recorded because it's a design-orientation the project keeps
  re-deriving.

## Dependency ledger (verified-how) — schema v2.1 slot

**ALL FILES THIS SESSION RAN A SCRIPT AGAINST ARRIVED AS ATTACHMENTS ON DISK.**

| Dependency | Status | Verified how |
|---|---|---|
| `session_checkpoint_2026-07-15b.md` | ✓ FILE | supplied at boot; drove this boot |
| `discovery_prompt_v2_6.md` | ✓ **FILE, ON DISK** | md5 `87af5710…` EXACT, 680L. Patch base. |
| `pipeline_config_schema_v2.md` | ✓ **FILE, ON DISK** | md5 `d3f866c4…` EXACT, 637L. Item 11 diffed against §3.2 + App C — `span` removal (line 622) + tag retirement (634–637) confirmed by grep. |
| `discovery_eval_findings_rappers-handbook.md` | ✓ **FILE, ON DISK** | md5 `0e9ee488…`, 271L. **IS in the repo — corrects 07-15b.** |
| `discovery_audit_prompt_v1.md` | ✓ **FILE, ON DISK** | md5 `2b7c0ea4…`, 131L. Patch base for audit v2. **Still a RECONSTRUCTION — baseline untrusted.** |
| Loeliger PDF | ✓ **FILE, ON DISK** | md5 `dc645428…`, 9.79 MB, 266pp. `InvisibleOCR` font confirmed. Rasterized p173–180 (file 188–195; print = file − 15). |
| Loeliger run report + audit | ✓ PASTE ONLY | read for evidence; the run's own report and the third-ctx audit. Not on disk; no script run against them. |
| register v4 | ✓ FILE (close-sync) | md5 `936b6f16…`, 812L. Still current — v5 NOT filed. |

## Propagation / blast radius

- **v2.7's blast radius is unchanged from 07-15b and now REALIZED:** both real
  runs' config fragments still carry `span`-era shape and the retired tag. When
  v2.7's schema-boundary rule is next exercised in a config session, those
  fragments are the input that would hit lint rule 1. Nothing on fire (they are
  input, never live config), but the debt is real and named.
- **The coverage docket's radius is the validator AND discovery.** If homed as a
  lint, it's a new fixture. If homed in discovery, it's a v2.8 change. Undecided.
- **The Loeliger vault is INCOMPLETE until p174–179 is patched.** §6.2 and §6.3
  are currently un-harvestable. Any downstream build off this run inherits the
  gap.
- **v2.7, audit v2, and the docket are IN OUTPUTS, NOT IN THE REPO.** Confirmed
  ABSENT by close-sync. They do not exist to the next session until synced.

## Open design questions register — delta

NEW:
1. **Should discovery run the coverage arithmetic itself, or should a lint, or
   both?** The docket's central undecided question. Schema-lockstep logic says
   both (a rule in the writer alone rots when the writer changes).
2. **Does the audit prompt v2 actually bite?** Generalized but untested — same
   flaw as v1, in the most flattering direction. A clean test: run v2 cold on a
   pile it hasn't seen and see if it finds real defects without the roster.
3. **Should discovery handle shared boundary pages explicitly?** The
   one-page-one-owner assumption is what let the p174 gap form. A prompt-level
   fix is possible; not scoped.

CARRIED, unclosed: the four test-record docket questions. P1–P2 strike + P3-R.
**P4 (READY at 3), P9, P10 (shape now evidenced 4×, still UNRATIFIED), P11
(blocked on the fixture rebuild), P12, P13, P14** — plus the **two new proposals
this session (audit-generalization rule; audit-≠-schema-lockstep distinction).**
The interface-doc retroactive blessing. `engine_charter_amendment_v1_1.md`'s W1
provenance. Opus capability calibration — **eighth data point.** The rappers
pile's four known defects, still `ratified`. The BJJ discovery back-pass.

## Reference-doc debt — slot

**NONE re-issued this session** (no design changed in a reference doc). Lexicon
r18 and diagram r13 stand.

**OWED AT THE NEXT DESIGN SESSION:**
- **Register v5** — now owes SIX proposals: P13 + P14 (drafted 07-15b, still
  unfiled — the W10 pattern, flagged AGAIN), plus this session's two new
  (audit-generalization; audit-≠-schema-lockstep). Carried from 07-15b: the
  register batch is P3-R + P4 + P9 + P10 + P11 + P12 + P13 + P14 + the two new.
- **Lexicon** — carried from 07-15b, none done: W15 (*a paste is not a file*),
  `meta artifact`, the three-names disambiguation pair. **Plus new this session:
  `coverage by silence` (the defect class) and `confirmer→detector` (the reusable
  upgrade move).**
- **Diagram** — v2.7 is now tested; when synced, the tested-state ledger gains a
  discovery-v2.7-VALIDATED entry. Diagram r14 owed at next design session.

**NOT IN THE REPO:** the Loeliger run report and the third-ctx audit are paste-only
evidence. Worth filing at `evidence/loeliger-til-run-2026-07-14/` (the v2.7 re-run
extends the 07-14 run family) so the vindication isn't one lost transcript from gone.

## Session hygiene / corrections ledger (own errors + events)

- **Model this session: Opus** (Claude Opus 4.8) — eighth Opus workshop ctx.
- **Boot: CLEAN.** All script-target files requested and received as attachments,
  md5-verified on disk against the 07-15b handshake before any script ran.
- **The paste-is-not-a-file lesson HELD.** Zero scripts run against pasted
  content. The Loeliger run report and audit were read as evidence (paste), never
  scripted against — correctly distinguished.
- **Own event (self-caught, good): the patch self-check FAILED on first run** —
  the raster-detector edit's anchor didn't match (a line-wrap in the check
  string, not the file). The script REFUSED to write a v2.7 missing a ruled fix.
  Fixed the check, re-ran, passed. **This is the script-over-reading discipline
  catching a real miss — the same class as 07-15b's `span` catch.**
- **Scope held tight against temptation.** Two extra artifacts (audit v2, the
  docket) rode along, but each was operator-chosen at a decision point, and the
  v2.7 core scope was NOT widened. The audit v2 and docket are genuinely separate
  from the engine artifact; primer-style passenger logic.
- **Independent verification run on every artifact.** Each patch output was
  grep-checked for the original defects independently of the script's own
  self-check — reading is not checking, twice enforced.
- No interruptions. **v2.7 shipped AND tested. Audit v2 shipped. One docket
  filed. No reference doc churned. Register still unfiled (flagged loudly).**

## Boot manifest — P10 shape (REQUEST LIST)

**READ THIS FIRST.** The project mount is **CLEARED**. **The repo is the source
of truth:** `~/git/repetae`, private, local, on the operator's machine. **A ctx
cannot read it.** Ask the operator to upload what you need. **This manifest is a
request list** — P10's shape, exercised on FOUR consecutive repo-era boots, still
UNRATIFIED.

**THE PATTERN THAT WORKS (P13, unfiled, drafted in 07-15b Rulings):** emit a
shell snippet, do not list filenames in prose. It must carry a loud `MISSING:`/
`ABSENT:` branch, an md5/lines/bytes header per file, and tiering. **Operator
environment: Pop!_OS, X11, GNOME; local shell; repo at `~/git/repetae`; `xclip`
present (no `wl-copy`/`xsel`).** [confirmed this session by `echo $XDG_SESSION_TYPE`]

**⚠ A PASTE IS NOT A FILE.** If you will run a script against a document, request
it as a FILE ATTACHMENT (paperclip / drag-drop) and `ls` before you trust it. A
pasted snippet-output lands in context, NOT on `/mnt/user-data/uploads`.

**⚠ NEW POLICY THIS SESSION [operator-decided]:** snippets that emit info for the
operator to paste back should tail `| tee /dev/tty | xclip -selection clipboard`
(see on screen AND land on clipboard). **This is the TEXT channel. It does NOT
replace file attachments for anything a script must touch.** (An attempt to build
a file-onto-clipboard command via `x-special/gnome-copied-files` half-worked and
is DOCKETED as a to-do, not solved — the file-paste that ultimately worked was
plain drag-drop.)

| Doc | Repo path | Why needed | Tier |
|---|---|---|---|
| primer | `law/workshop_primer_v4.md` | **THE boot authority.** Filing law 1–6; boot loop; close protocol. **Describes a dead MOUNT and a pre-repo close protocol; the LAW is live, both mechanisms dead.** v5 DEFERRED — a RATE LIMITER, not a debt (07-15b). EXEMPT from the engine/reference split | **REQUIRED** |
| this checkpoint | `checkpoints/session_checkpoint_2026-07-18.md` | the boot file. v2.7 written+tested; the new coverage docket; the still-unfiled register | **REQUIRED** |
| prior checkpoint | `checkpoints/session_checkpoint_2026-07-15b.md` | v2.7's ruled scope + the unfiled P13/P14 drafts + the item-11 characterization | **REQUIRED** |
| lexicon | `law/workshop_lexicon_r18.md` | vocabulary + warts. Marker: "Revision identity: rev 18" AND 18 dated changelog bullets (`- 2026-07-15 —`, NOT bold-dated — DERIVE, don't eyeball). §10 has W14, W13 CLOSED. **OWES: W15, `meta artifact`, three-names pair, `coverage by silence`, `confirmer→detector`** | **REQUIRED** |
| register | `law/primer_amendment_proposals_v4.md` | md5 `936b6f16…`, 812L. pending: P3-R, P4 (READY), P9, P10, P11 (blocked), P12. **P13 + P14 DRAFTED 07-15b, STILL UNFILED. Two more owed this session. v5 owes all of them.** NOT law | **REQUIRED** |
| **discovery v2.7** | ⚠ **IN OUTPUTS, NOT YET IN REPO** — `pipeline/discovery_prompt_v2_7.md` when synced | md5 `1a19649f…`, 723L. **The tested current prompt.** REQUEST AS ATTACHMENT if patching v2.8 | **REQUIRED if the session touches discovery** |
| **coverage docket** | ⚠ **IN OUTPUTS, NOT YET IN REPO** — path TBD (`evidence/` or a dockets dir, NOT `pipeline/`) | md5 `0d22783c…`. The new "coverage by silence" finding + the detector/re-verify rule + undecided homes | **REQUIRED if the session acts on coverage** |
| **audit prompt v2** | ⚠ **IN OUTPUTS, NOT YET IN REPO** — `pipeline/discovery_audit_prompt_v2.md` when synced | md5 `6a075253…`, 151L. Generalized. **First version with a repo home. Untested — run it cold to validate** | **REQUIRED if the session audits a run** |
| config schema | `pipeline/pipeline_config_schema_v2.md` | 637L; md5 `d3f866c4…`. The authority item 11 points at. REQUEST AS ATTACHMENT for any schema/config work | **REQUIRED if the session writes config or a fragment** |
| audit findings | `evidence/discovery_eval_findings_rappers-handbook.md` | md5 `0e9ee488…`, 271L. **IS in the repo (07-15b said it wasn't).** The rappers evidence base | ON-DEMAND |
| audit prompt v1 | `pipeline/discovery_audit_prompt_v1.md` | md5 `2b7c0ea4…`, 131L. The RECONSTRUCTION — superseded by v2 but still the only in-repo version until v2 syncs | ON-DEMAND |
| Loeliger PDF | ⚠ **operator-held; not in repo** — request as attachment | md5 `dc645428…`, 266pp. The test book. print = file − 15. Rasterize; the text layer lies | ON-DEMAND — REQUIRED to patch the p174–179 gap |
| diagram | `reference/system_diagram_r13.html` | the tested-state ledger. Marker: "Revised 2026-07-15" + "rev 13". **Owes r14 once v2.7-tested is recorded** | ON-DEMAND — REQUIRED if the session touches testing/status |
| validator | `tools/discovery-validator/` (whole dir — 178 files) | P-2/P-3/P-4. Fixture suite KNOWN-STALE, will be staler once v2.7 lands. Rebuild BLOCKING P11. **The coverage docket may add a partition lint here** | REQUIRED if the session rebuilds fixtures |
| charter + amendments | `law/engine_charter.md` + v1_1 + v1_2 | worklist §9 as amended. v1_1 is a transcription artifact (W1). **P14 (schema lockstep) is charter-amendment territory → v1.3, not the primer** | ON-DEMAND |
| run families | `evidence/loeliger-til-run-2026-07-14/` (8 files) + `evidence/rappers-handbook-run-2026-07-15/` (7 files) | the two real runs. **Loeliger now has a v2.7 re-run report + audit (paste-only, owed filing here).** rappers pile: 4 known defects, still `ratified` | ON-DEMAND |
| engine unit | `gate/topology_experiment_kit_v2.md` + `_scorer_v2.py` + `_interface.md` | rides together. Receipt: `selftest` → 18 PASS. `WIRE_VERSION="wire-0"` is PROTOCOL — never bump in a rename. P12 applies to its 18/18 | ON-DEMAND |
| older checkpoints | `checkpoints/` (17 more, 07-10b → 07-15b) | narrative history | ON-DEMAND |

**Verification under the repo rule.** The content-marker check is the only
handshake confirming the operator uploaded the file the manifest meant. Where a
marker is mechanically derivable (rev counters, md5s), DERIVE it. Where you will
run a script, demand a FILE. **This session's close-sync confirmed all three new
artifacts ABSENT from the repo — they are in outputs and must be synced before
the next session can see them.**

**The lesson this session ADDS, stated where the next boot will read it: the
confirmer→detector upgrade generalizes. v2.7 applied it to the raster rule and
it caught an invisible OCR corruption; the operator applied it to coverage
arithmetic the same hour. Any check that only double-checks a verdict you
already hold is a candidate to become one that goes hunting first.**
