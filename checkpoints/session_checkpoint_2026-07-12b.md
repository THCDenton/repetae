# Session checkpoint — 2026-07-12b (design chat: harvest autonomy, intake screening, DAG topology)

Purpose: boot file for the amendment session. Files are the only memory.
Reads alongside the 07-12 checkpoint; supersedes several entries in its open
register (enumerated below). Written under checkpoint schema v2.1.

## What this session was

An **un-booted design chat** (operator + ctx, claude.ai project session),
not a chartered workshop session. No boot verification loop ran — dependency
claims below are correspondingly weaker and flagged. Reference-class
throughout: no engine artifacts, no reference-doc edits (lockstep held).

Arc: opened as "give workers web license / reduce operator load," and
escalated through three consequential moves: (1) **full harvest autonomy**
ruled by the operator; (2) **intake screening** designed end-to-end;
(3) a **new harvest topology** (extract/prove/judge/assemble DAG) derived
under an explicit operator reins-grant, superseding the fold-vs-tree
question with a proposal gated on a cheap experiment.

## Artifacts shipped this session (operator: download + file into workshop project)

1. `session_checkpoint_2026-07-12b.md` — this file.
2. `harvest_topology_proposal_laymans_guide.md` — the topology proposal,
   layman-formatted, with status/evidence labels; includes the chunk-plan
   revision and an appendix answering "couldn't the bracket carry to-do
   lists?" Supersedes the abandoned `merge_script_laymans_guide.md`
   (which remains DO-NOT-FILE). This one IS for filing — it is the
   amendment session's exhibit for the topology item.

## Rulings (this session) — ratification pending at amendment unless noted

- **Harvest judgment loop eliminated** [operator-ruled]. No escalation
  lane at harvest. Judges must rule — full stop — via the tiebreak
  ladder: (1) in-source evidence, (2) discovery interview conventions +
  forecast, (3) tradition-scoped web per `web_policy`, (4) recoverable-
  direction default (split over union, reservation over forced homing),
  tagged `tiebreak: default, confidence: low`. Every ruling documents its
  reasoning + method for the diagnostic loop. In-source evidence outranks
  forecasts, always. Tuning loop = read reasoning, tune prompts, re-run
  the whole process. Scope: harvest only — registry coin-flip escalation
  and node-build parking untouched. The failure loop (lint parks) is
  retained and stays operator-facing.
- **Web license** [operator-directed, jointly refined]. Restored per JJU
  scope with three guards: question-keyed admissibility (evidence of what
  the source/tradition MEANS — never of what is true; hostile sources
  admissible when they describe usage); select-don't-introduce (web may
  select among in-source-evidenced readings, never introduce one, never
  overrule an in-source definition); per-source `web_policy`
  (`off | in-tradition | open`) set at discovery.
- **Intake screening** [operator-directed]. New Stage 0 step, before
  ingest/registration. Provenance capture FIRST (submitter identity,
  hashes, timestamps — retained permanently in a screening ledger even
  when content is destroyed). Tiers:
  1. **halt-and-report** — illegal to possess (CSAM defining case).
     Non-overridable by any stage. Runbook: fail closed; detection
     creates duty (no unactioned flags, ever); no further copies, no
     further processing, minimal human eyes; report w/ submitter
     provenance (NCMEC CyberTipline in the US); preserve per statute;
     dispose as directed.
  2. **too-hot** — legal but declined. Defined as the **pinned written
     Anthropic Usage Policy** (version + date cited in each verdict), NOT
     runtime refusal behavior and NOT taste. Operator law, verbatim
     intent: **"distaste is never a decline reason"** — contested-but-
     legal content proceeds (lexicographer treatment). Plus a
     counsel-flag lane for distribution-side questions (licensing above
     all) that model policy cannot answer.
  3. **proceed** — everything else, with framing/scope constraints where
     discovery sets them.
  External dependency: one counsel hour, three questions — (a) does the
  pinned-policy screening standard hold up, (b) does the per-tenant
  processing posture + ToS warranty/indemnity hold up, (c) halt-tier
  statutory specifics (provider status, preservation windows, retention).
  ToS must disclose that illegal material is reported with submitter
  identifying information.
- **Tenancy (item g)** [operator-ruled]: deprioritized, risk accepted.
  Recorded for the ledger, not resolved. Design sketch preserved: all
  durable state tenant-scoped; registry single-namespace per tenant;
  customer-supplied sources; no cross-tenant reuse. Revisit if the
  business model changes.
- **Chunk plan** [operator-proposed, session-agreed]. Chunk at the
  source's natural teaching boundary (chapter → section → applicable
  convention), size-bounded fallback for oversized units. The chunk plan
  is a **discovery deliverable** (TOC + loc-anchors machinery already
  exists). Retires global `span_size`/`span_overlap` as constants —
  per-source measurements now.
- **Topology: extract / prove / judge / assemble DAG** [session-derived
  under operator reins-grant; hypothesis, experiment-gated]. See exhibit
  doc for the full design. Key laws embedded in it:
  - **Prove-script three-citations law**: a script may link two sightings
    only by (1) same ink — overlapping-span dedupe, (2) the source said
    so — stated-alias union-find, (3) discovery ruled so — brief laws.
    Scripts apply equality and stated claims, **never similarity**. No
    thresholds, no string-distance, no verdict-bearing heuristics.
    Anything unprovable ships to a judge whole. Consequence:
    `residue_heuristics` (charter §10 TBD) **dissolves** — heuristic
    signals survive only in non-verdict roles (suspicion labels on case
    files, packet-grep prioritization).
  - **Judge tiering with punt-upward**: everything to the cheap tier
    first; "escalate to stronger model" is a model's ruling (allowed),
    not a script's threshold (forbidden). Queue shrinks in waves.
  - **Case files born complete**: no judge dispatch until the last
    extract chunk lands (phase barrier). This property is the design's
    entire advantage over tree/fold; protect it.
  - **Ratification gate**: do NOT ratify fold or DAG at the amendment.
    Ratify the topology-independent items; gate topology on the cheap
    experiment — run the sealed map kit (phase 1) + residue kit fixtures
    (phase 3) + full JJU regression span, diff against
    `glossary_index_v31` as the known-good answer key.
- **Wire schema: JSON in flight, prose at rest** [session-agreed]. Worker
  → script traffic is JSON (one object per sighting/verdict); durable
  state (index, shards, rulings) stays human-readable JJU-style blocks —
  the tuning loop requires the operator-readable layer. Bounds survive as
  schema (`maxLength` on sense, closed enums for type/status/boundary
  injected per-source from the brief). Sentinel blocks retire on machine
  lanes only; supervised chat stages keep them. Lint = literal schema
  validation; failure reports name exact field + rule and prepend to the
  single retry. `custom_id = stage:unit:attempt` remains the join key.
- **RED runtime semantics** [session-agreed]. Event-driven: results join
  by `custom_id`, never position. Phase barrier as above; a parked
  extract chunk stalls the barrier BY DESIGN. Three lanes, no overlap:
  **certainty → scripts, judgment → models, broken → operator.** Operator
  surface reduced to exactly two events: lint-parks and halt-tier
  screening. API-level failures (HTTP errors, in-batch request errors)
  get mechanical retry with backoff on a separate strike counter — they
  never burn the lint-retry budget; repeated infra failure also parks.
  Batch-lane specifics for the driver: per-request status inside
  "succeeded" batches; collect results within the 29-day expiry.
- **Discovery v2.5 direction** [session-agreed]. Additions: mechanical
  ambiguity probe in the structural read (dispersion/collision script →
  ranked watchlist, `[mechanical]` provenance); arbitration axis widened
  to mode + tiebreak preferences + ambiguity forecast (watchlist-driven
  interview pass; operator leans captured per term and per ambiguity
  class); new sidecar `arbitration_seed_<slug>.md` (pre-opened
  reservations/fan-outs with TOC-derived home ranges, `[discovery-
  forecast]` provenance) consumed as judge-visible boot state, NEVER in
  the brief (consistent with native-seeds law: merge-level recall aid);
  chunk plan deliverable; exit-exam extension (each forecast names the
  in-source evidence that would confirm/kill it).
- **Diagnostics** [session-agreed]. Run ledger gains a **surprise rate**:
  case-file questions discovery didn't forecast + forecasts that never
  materialized. High surprise → tune discovery; low surprise with bad
  rulings → tune judges. Park rate trends on the §5 dashboards; a jump on
  a new source = discovery attention signal. Empty-forever park tray is
  suspicious, not reassuring. Success criterion is not "no breaks" —
  it is **"breaks are loud and cheap, never silent."**
- **Expected failure phases** [session-agreed, expectation-setting]:
  early runs park a lot (the plan working); each new source TYPE spikes
  parks once; steady state ≈ a couple of parks per book. Maintenance
  channel, not fire bell.

## Dependency ledger — schema v2 slot (weakened; un-booted session)

Consulted this session via `project_knowledge_search` / `view` on the
project mount, WITHOUT the boot verification loop: `engine_charter.md` +
v1.1 amendment, `discovery_prompt_v2_4.md`, `harvest_map_v1.md`,
`harvest_residue_v1.md` + both kit specs, `harvester_prompt_v1.md`,
`pipeline_config_schema.md`, `workshop_lexicon_v1.md`,
`session_checkpoint_2026-07-12.md`, `how_we_build_wikis_from_books.md`.
Boot-manifest pins from 07-12 are carried forward **unverified**; the
amendment session must run the full verification loop at boot.

## Propagation / blast-radius log — schema v2 slot

- **Autonomy ruling** → charter §5 (human surface = parks + halt only;
  escalation format repurposed as a flagged-ruling class inside the
  arbitration file); judge prompt derivation; router triage simplification.
- **Screening** → stage list (Stage 0 screener before ingest);
  `sources.md` registration gated on pass verdict; config schema
  (screening block, verdict enum); ToS (external); screening ledger as a
  new durable artifact class.
- **Topology (if experiment passes)** → charter §4 (harvest row =
  extract/prove/judge/assemble; stage-level map/reduce law survives);
  §9 worklist (item 5 merge script RESURRECTED as prove script +
  case-file builder; integrator-prompt item becomes extract-prompt +
  judge-prompt derivations); diagram (H8/H9/H10 → four actors + RED
  barrier; harvest_map partially rehabilitated as the extract ancestor;
  residue judge rehabilitated with its two flaws fixed — evidence-rich,
  autonomous).
- **Wire schema** → first tenant of the config-schema-v2 amendment
  session (per amendment v1.1's own requirement); lint gate; kit scorers
  (JSON fixtures); Node-RED router (switch on verdict.status).
- **Discovery v2.5** → discovery prompt derivation session; new
  ambiguity-probe script worklist item.
- **`residue_heuristics`** → dissolved; remove from config §3.5 at
  amendment close.

## Open design questions register — updates

Resolved or dissolved this session:
- Router delivery UX — dissolved (no judgment queue exists; parks + halt
  need only a driver-written file + a ping).
- Terminal-Q handling — ruled by ladder + default tags.
- JJU escalation-volume intel request — dropped, moot under autonomy.
- Parallelism topology within recursive fold — superseded by the DAG
  proposal + experiment gate.
- `residue_heuristics` membership — dissolved by the three-citations law.

New this session:
- Topology experiment design: span choice, diff metric, pass criteria,
  who runs it (pre-amendment or gated session).
- Judge tier ladder: which model tiers, punt-upward budget.
- Wire schema v0 field set + versioning discipline.
- Seeded-forecast bias check: prune false forecasts via surprise rate.
- Zero-sighting sanity flag: threshold for "dense chunk, empty return →
  park tray, not silent pass."

Carried unchanged: reference-layer form (W1 standing); output shape
(vault + Anki inherited); reference-artifact version suffix;
prompt-via-failures method (now applies to extract + judge prompts).

## Reference-doc debt — schema v2 slot

All deferred to amendment close (lockstep held; nothing patched from an
un-booted chat). Adds on top of the 07-12 enumeration:
- **Lexicon adds:** case file, prove script, three-citations law, judge /
  judge tiering / punt-upward, tiebreak ladder, `web_policy`,
  select-don't-introduce, screening tiers + halt-tier runbook, screening
  ledger, wire schema, JSON-in-flight/prose-at-rest, phase barrier,
  surprise rate, chunk plan, "loud and cheap, never silent."
- **Lexicon status changes (conditional on experiment):** recursive fold
  → candidate-superseded; merge script → un-retired as prove script;
  residue judge → rehabilitated-with-fixes.
- **Charter:** §4/§5/§7/§9/§10 per blast radius; §0/stage-list gains the
  screener.
- **Diagram:** harvest cluster redrawn as E/P/J/A + RED barrier + park
  tray + halt alarm.
- **Primer (candidate law, amendment to rule):** un-booted design chats
  are permitted but MUST close with a schema-v2.1 checkpoint (this doc as
  exemplar), and their dependency ledgers are marked weakened.

## Recommended next session

**Amendment session**, unchanged as next — agenda restated:
(a) topology: ratify the topology-independent set now (state model,
autonomy, screening, discovery v2.5 direction, wire-schema direction),
gate fold-vs-DAG on the experiment; (b) router (revised, reduced role);
(c) index/shard state model; (d) fates of merge/map/residue (revised per
blast radius — resurrection and rehabilitation, not just retirement);
(e) evidence policy + autonomy as ruled above; (f) intake screening +
halt-tier runbook; (g) tenancy — record deprioritization. Then the
topology experiment, then extract/judge prompt derivations.

Boot: per the 07-12 boot manifest (verify properly this time) + this
checkpoint + the topology proposal exhibit.

## Session hygiene / corrections ledger

- **Un-booted session.** No verification loop; acceptable for a design
  chat, but flagged, and this checkpoint's dependency claims are
  weakened accordingly.
- **Ctx reversed its own 48-hour-old advocacy** (fold) on analysis. Per
  the 07-12 "big one" correction, the reversal is evidence-labeled: the
  fold's proof-of-life proves the ONLINE setting; ours is offline. The
  DAG is labeled hypothesis-with-gate, not law. The correction was
  applied this time rather than violated.
- **Operator delegated topology under an explicit reins-grant.**
  Delegation ≠ ratification; the ruling returns to the operator at the
  amendment, gated on evidence.
- **Layman-format artifacts worked** (proposal doc + in-chat newsroom
  walkthroughs); the prior layman guide remains DO-NOT-FILE and is
  superseded by the exhibit's footer.
- **Operator's bracket proposal** was evaluated on merits and found
  viable-but-convergent — the corrected version of the 07-12
  pattern-matching failure (treat operator intuition as data; this time
  the data redirected the design twice: autonomy and topology).

## Boot manifest — schema v2.1 slot (pins the next boot)

Rows 1–4 carried forward from the 07-12 manifest **UNVERIFIED this
session** (un-booted); amendment boot must verify all six.

| Doc | File | Content-level revision marker |
|---|---|---|
| primer | `workshop_primer_v2.md` | header: "Workshop Session Primer — v2, issued 2026-07-11c" |
| lexicon | `workshop_lexicon_v1.md` | last changelog line dated "2026-07-11c (post-close addendum, operator-directed)" |
| diagram | `system_diagram_v1.html` | banner ends: "Revised 2026-07-11c: `harvest_residue` PLANNED → RATIFIED…" |
| checkpoint (prior) | `session_checkpoint_2026-07-12.md` | ends with its schema-v2.1 boot manifest |
| checkpoint (this session) | `session_checkpoint_2026-07-12b.md` | header contains "design chat"; ends with this manifest |
| topology exhibit | `harvest_topology_proposal_laymans_guide.md` | footer evidence label present; appendix "Couldn't the bracket carry to-do lists?" present; Phase 1 contains the chunk-plan bullet |

Mismatch → primer v2's rules. Index/mount latency note from 07-12
applies: prefer `project_knowledge_search` content-marker checks during
and shortly after refile.
