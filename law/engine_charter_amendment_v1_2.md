# Engine Charter — Amendment v1.2

Status: ratified 2026-07-12 (amendment session, operator-ratified item by
item; wholesale confirmation on the presented docket). Apply by appending
this file alongside `engine_charter.md` v1 and amendment v1.1; a future
housekeeping session may fold all three into a regenerated body. Per
"Amendments are versioned events": this file records what changed and why.

Evidence discipline (per the 07-12 correction): every item below carries a
status label. RATIFIED = law now. UNDER EXPERIMENT = two labeled candidates
and a gate; neither is law. CONDITIONAL = pre-agreed consequence table that
the experiment's result applies mechanically. Nothing here silently promotes
a hypothesis.

## 1. Harvest topology — UNDER EXPERIMENT (§4 harvest row suspended)

The v1 charter's §4 harvest row (map = per-span extraction; reduce = script
merge + residue pass) is **suspended, not law**. It was ratified as an
aspiration with zero end-to-end test; the JJU excursion (07-12 checkpoint,
Ground truth) showed the proven prior art has a different shape. Two
candidates now stand, neither ratified:

- **(A) Recursive fold** — one integrator per iteration reads accumulated
  state (index + arbitration + touched shards) + new material, emits
  next-version state. JJU's proven pattern; proof-of-life is for the ONLINE
  setting (can't look ahead), which is not our setting.
- **(B) Extract / prove / judge / assemble DAG** — parallel extract, script
  prove pass, judge tier on born-complete case files behind a phase barrier,
  script assemble. Hypothesis, offline-optimized. Exhibit:
  `harvest_topology_proposal_laymans_guide.md` (evidence labels in footer).

**Gate:** the topology experiment — sealed map kit (phase 1) + residue kit
fixtures (phase 3) + the full JJU regression span, diffed against
`glossary_index_v31` as the known-good answer key. Design of span choice,
diff metric, and pass criteria is a new worklist item (§11 below).

**Placement (operator-confirmed):** the workshop *builds* the experiment kit
+ scorer; an **ops ctx runs it** in the project holding the answer key (JJU)
or a scratch ops project with the key sealed. Charter §2 is controlling: dev
never executes against material it holds the answer key for — a contaminated
run proves nothing and forces a re-run anyway.

The **stage-level** map/reduce law of §4 survives regardless of the
experiment's outcome: registry, node build, and cards remain map/reduce
shaped. Only the harvest row is in play.

## 2. Scripts-never-similarity law — RATIFIED (topology-independent)

A script may link two sightings only by:
1. **same ink** — overlapping-span dedupe (literally the same text);
2. **the source said so** — stated-alias union-find;
3. **discovery ruled so** — brief laws.

Scripts apply **equality and stated claims, never similarity**: no
thresholds, no string distance, no verdict-bearing heuristics of any kind,
in any topology. Anything a script cannot prove ships to a judge **whole**.
Rationale (recorded): a false split is recoverable; a false merge is not,
and heuristics produce false merges silently — violating the diagnostics
criterion in §9 below. Heuristic signals survive only in non-verdict roles:
suspicion labels on case files, packet-grep prioritization.

**Consequence:** charter §10's `residue_heuristics` open question is
**DISSOLVED** (under DAG the three-citations law replaces it; under fold no
residue judge exists). `pipeline_config_schema.md` §3.5 drops the field at
this close (patched, versioned).

## 3. Harvest autonomy + evidence policy — RATIFIED (§5 amended)

**The harvest judgment loop is eliminated.** No escalation lane exists at
harvest. Judges must rule — full stop — via the **tiebreak ladder**:

1. **In-source evidence** — outranks everything else, always.
2. Discovery interview conventions + forecast.
3. Tradition-scoped web, per the source's `web_policy`.
4. **Recoverable-direction default** — split over union, reservation over
   forced homing — tagged `tiebreak: default, confidence: low`.

Every ruling documents its reasoning + method (feeds the diagnostic loop,
§9). Tuning loop = read reasoning, tune prompts, re-run the whole process.

**Web license restored** per JJU scope, under three guards:
- **Question-keyed admissibility** — web results are evidence of what the
  source/tradition MEANS, never of what is true; hostile sources are
  admissible when they describe usage.
- **Select-don't-introduce** — web may select among in-source-evidenced
  readings; it may never introduce a reading or overrule an in-source
  definition.
- **Per-source `web_policy`** — `off | in-tradition | open`, set at
  discovery.

**Human surface = exactly two events:** lint parks and halt-tier screening
(item 6). The escalation *format* (≤10 lines, evidence both ways, stated
lean) survives, repurposed as a flagged-ruling class inside the arbitration
file. **Scope: harvest only** — registry coin-flip escalation and node-build
parking are untouched. The failure loop (retry-once-then-park) is retained
and stays operator-facing.

## 4. State model + wire schema — RATIFIED (§7 amended)

**Index/shard split** (JJU's proven pattern) is the harvest state model:
- **Index** — bounded, versioned: routing table with `@shards:[…]` tags,
  fan-out sense tables, status ledger, running context log. Small enough to
  load fully.
- **Shards** — range-named, **immutable in birth order**. New material for
  an old term appends to the CURRENT shard; the term's `@shards:[…]` tag
  extends; earlier shards are never touched.
- **Arbitration file** — versioned alongside the index; carries Q-tags,
  reservations, `[destination]` tags, and the flagged-ruling class.

**Wire schema: JSON in flight, prose at rest.** Worker → script traffic is
JSON (one object per sighting/verdict). Durable state (index, shards,
rulings) stays human-readable per-canonical multi-line blocks — the tuning
loop requires the operator-readable layer. Bounds survive as schema
(`maxLength` on sense; closed enums for type/status/boundary injected
per-source from the brief). Sentinel blocks retire on machine lanes only;
supervised chat stages keep them. **Lint = literal schema validation**;
failure reports name the exact field + rule and prepend to the single retry.
`custom_id = stage:unit:attempt` remains the universal join key.

**Runtime semantics (event-driven):** results join by `custom_id`, never
position. **Phase barrier:** case files are born complete — no judge
dispatch until the last extract chunk lands; a parked extract chunk stalls
the barrier BY DESIGN. Three lanes, no overlap: **certainty → scripts,
judgment → models, broken → operator.** API-level failures (HTTP errors,
in-batch request errors) get mechanical retry with backoff on a **separate
strike counter** — they never burn the lint-retry budget; repeated infra
failure also parks. Batch lane: per-request status inside "succeeded"
batches; collect within the 29-day expiry.

This item is the **first tenant of the config-schema-v2 amendment session**
(owed per amendment v1.1 §3), which this amendment does not replace: wire
schema v0's field set enters the live config only through that session.

## 5. Router — RATIFIED at reduced role (§5/§6)

With autonomy ratified, no judgment queue exists; the 07-12 proposal of a
first-class router-with-escalation-queue is **superseded in place**. The
router is a Node-RED switch on `verdict.status` plus delivery of the two
operator events as a driver-written file + a ping. No queue UI, no delivery
subsystem. Re-widening later is additive if diagnostics ever argue for it.

## 6. Stage 0 gains intake screening — RATIFIED (stage list amended)

A screening step runs **before ingest/registration**; `sources.md`
registration is gated on a pass verdict.

**Provenance capture FIRST:** submitter identity, content hashes,
timestamps — recorded in a **screening ledger** (new durable artifact
class) and retained permanently, even when content is destroyed.

**Tiers:**
1. **halt-and-report** — illegal to possess (CSAM the defining case).
   Non-overridable by any stage. Runbook: fail closed; detection creates
   duty (no unactioned flags, ever); no further copies, no further
   processing, minimal human eyes; report with submitter provenance (NCMEC
   CyberTipline in the US); preserve per statute; dispose as directed.
2. **too-hot** — legal but declined. Standard = the **pinned written
   Anthropic Usage Policy** (version + date cited in each verdict) — NOT
   runtime refusal behavior, NOT taste. Operator law, verbatim intent:
   **"distaste is never a decline reason"** — contested-but-legal content
   proceeds (lexicographer treatment). Counsel-flag lane for
   distribution-side questions (licensing above all) that model policy
   cannot answer.
3. **proceed** — everything else, with framing/scope constraints where
   discovery sets them.

**External gate (recorded, not resolved):** one counsel hour, three
questions — (a) pinned-policy screening standard, (b) per-tenant processing
posture + ToS warranty/indemnity, (c) halt-tier statutory specifics
(provider status, preservation windows, retention). This gates **accepting
third-party submissions**, not this design. ToS must disclose that illegal
material is reported with submitter identifying information.

## 7. Fates of merge / map / residue — CONDITIONAL (applies mechanically)

| Artifact | If DAG passes the gate | If fold passes the gate |
|---|---|---|
| merge script (worklist item 5) | RESURRECTED as **prove script + case-file builder** | stays retired; no separate merge actor |
| `harvest_map_v1` | partial rehabilitation: **extract-prompt ancestor** | ancestor to the integrator derivation |
| `harvest_residue_v1` | rehabilitated as **judge ancestor**, two flaws fixed (evidence-rich packets; autonomous per item 3) | ancestor to the integrator derivation |
| integrator-prompt worklist item | becomes **extract-prompt + judge-prompt** derivations | stands as the single integrator derivation |

Either way: **no artifact is edited or deleted** — status changes only. Kit
fixtures remain valid under both branches (shared intake grammar; the
adversarial cases exist in any topology).

## 8. Discovery v2.5 — direction RATIFIED (derivation is its own session)

- **Mechanical ambiguity probe** in the structural read: dispersion/
  collision script → ranked watchlist, `[mechanical]` provenance.
- **Arbitration axis widened**: mode + tiebreak preferences + ambiguity
  forecast; watchlist-driven interview pass; operator leans captured per
  term and per ambiguity class.
- **New sidecar `arbitration_seed_<slug>.md`**: pre-opened reservations/
  fan-outs with TOC-derived home ranges, `[discovery-forecast]` provenance;
  consumed as judge-visible boot state, **NEVER in the brief** (native-seeds
  law: merge-level recall aid).
- **Chunk plan as a discovery deliverable**: chunk at the source's natural
  teaching boundary (chapter → section → applicable convention), with a
  size-bounded fallback for oversized units. **Retires global `span_size` /
  `span_overlap` as constants** — per-source measurements now (config
  schema treatment at the schema-v2 session).
- **Exit-exam extension**: each forecast names the in-source evidence that
  would confirm or kill it.

## 9. Diagnostics — RATIFIED (§5)

The run ledger gains a **surprise rate**: case-file questions discovery
didn't forecast + forecasts that never materialized. High surprise → tune
discovery; low surprise with bad rulings → tune judges. Park rate trends on
the §5 dashboards; a jump on a new source is a discovery attention signal;
an empty-forever park tray is suspicious, not reassuring. **Success
criterion: breaks are loud and cheap, never silent.** Expected phases
(expectation-setting, not law): early runs park a lot (the plan working);
each new source TYPE spikes parks once; steady state ≈ a couple of parks per
book. Maintenance channel, not fire bell.

## 10. Tenancy — deprioritized, risk ACCEPTED (recorded)

Not resolved; recorded so no future session can claim it was overlooked.
Design sketch preserved: all durable state tenant-scoped; registry
single-namespace per tenant; customer-supplied sources; no cross-tenant
reuse. Revisit trigger: the business model changes.

## 11. Worklist (§9) — amended

- Item 5 (merge script): **conditional per item 7's table.**
- New: **topology experiment kit + scorer** (workshop builds; ops runs —
  item 1's placement rule). Includes experiment design: span choice, diff
  metric, pass criteria.
- New: **ambiguity-probe script** (discovery v2.5).
- New: **discovery v2.5 prompt derivation.**
- Gated on the experiment: **extract-prompt + judge-prompt** derivations
  (DAG branch) or **integrator-prompt** derivation (fold branch).
- Owed and reaffirmed: **config-schema-v2 amendment session** (wire schema
  v0 is its first tenant; chunk-plan fields its second).

## 12. Open questions (§10) — delta

**Dissolved:** `residue_heuristics` (item 2); global `span_size` /
`span_overlap` constants (item 8 — chunk plan).

**New:** topology experiment design (span choice, diff metric, pass
criteria, run logistics); judge tier ladder (which model tiers; punt-upward
budget — "escalate to a stronger model" is a model's ruling, allowed; never
a script's threshold, forbidden); wire schema v0 field set + versioning
discipline; seeded-forecast bias check (prune false forecasts via surprise
rate); zero-sighting sanity flag (dense chunk, empty return → park tray,
not silent pass).

**Carried unchanged:** parked-shard aging; registry snapshot cadence; cards
design; linter generalization; target models per stage; reference-layer
form (W1 standing); output shape; reference-artifact version suffix;
prompt-via-failures method (now applies to extract + judge prompts).

## Workshop procedure rider — RATIFIED (applied in primer v3 at this close)

**Un-booted design chats are permitted** but MUST close with a schema-v2.1
checkpoint whose dependency ledger is marked **weakened**; the next booted
session re-verifies from its manifest. Exemplar:
`session_checkpoint_2026-07-12b.md`. (Primer v3 also absorbs the two
07-12-owed procedure patches: intel-request-first for cross-project needs;
index/mount latency handling in the boot loop.)

## Unchanged and reaffirmed

- Files are the only memory; one engine artifact per fresh session.
- Style contract wins all conflicts.
- "Never upgrade 'the source implies' into 'the source says'" — now
  proceduralized as the tiebreak ladder's ordering (item 3).
- Dev/ops split (§2) — controlling for the experiment's placement.
- Batch-lane economics and platform posture (§6).
- Book-derived content personal-use unless licensed; the sellable assets
  are the engine, methodology, and services (§11) — extended, not changed,
  by item 6's screening ledger and counsel gate.
