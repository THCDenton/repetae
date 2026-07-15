# Topology Experiment Kit v2 — the gate (kit spec + experiment design)

**v2 is a FILING MIGRATION, not a design change.** Content is byte-identical
to `topology_experiment_kit_v1.md` as shipped 2026-07-13c, except this note
and the two self-referential filename strings below. The bump exists to
satisfy the primer's filing law (filename rev must equal internal rev) and to
retire this file's W11/W9 exposure — same-name copies could impersonate the
current one, and did so on three consecutive boots (07-13e, 07-13f, 07-13g).
**Do not hunt for a design delta between v1 and v2. There is none.**
Migration performed 2026-07-13g [operator-ruled, button].

Status: SHIPPED 2026-07-13c (design unchanged), migrated to suffixed filing
2026-07-13g; ratification pending operator docket.
Includes the manual chat-lane protocol (§7-M) — the first run executes
manually in chat by operator ruling; §7's batch runbook holds for later
API runs. Worklist
item per charter §9 as amended (v1.2 item 11: "topology experiment kit +
scorer — workshop builds; ops runs — includes experiment design: span
choice, diff metric, pass criteria"). Engine unit: this spec + the scorer
`topology_scorer_v2.py` ride together (kit-spec-rides-along precedent).

**What this decides.** The v1 charter's §4 harvest row is SUSPENDED
(amendment v1.2 item 1). Two candidates stand: **(A) recursive fold**
(JJU's proven pattern — proof-of-life in the ONLINE setting, which is not
our setting) and **(B) extract/prove/judge/assemble DAG** (hypothesis,
offline-optimized; exhibit `harvest_topology_proposal_laymans_guide.md`).
This kit is the gate between them. Neither is law until the gate rules.

**Placement (charter §2, controlling).** The workshop builds this kit and
the scorer; **an ops ctx runs the experiment** in the project holding the
JJU answer key (or a scratch ops project with the key sealed). Dev never
executes against material it holds the answer key for. The scorer's
self-test here uses synthetic fixtures only.

---

## 1. The two arms

**arm** *(vocabulary flag — candidate lexicon entry)*: one topology
candidate instantiated as a runnable configuration of prompts + scripts
for the experiment. Both arms consume identical inputs (same chunk plan,
same brief, same spans) and emit the two common surfaces of §2.

### Arm A — recursive fold
One **provisional integrator** per iteration reads accumulated state
(index + arbitration file + touched shards, per the ratified §7 state
model) plus one new chunk, and emits next-version state. Sequential by
construction: chunk *k+1* waits on *k*.

### Arm B — extract / prove / judge / assemble DAG
1. **Extract** — parallel stateless workers, one per chunk, sightings only
   (identity law: transcribe, never infer).
2. **Prove** — a script links only what it can prove under the
   three-citations law (§4 contract) and builds **born-complete case
   files** behind the phase barrier.
3. **Judge** — parallel judges, one per independent case file; autonomous
   rulings via the tiebreak ladder (no escalation lane).
4. **Assemble** — a script prints the export surface. Pure mechanics.

### The provisional-arm law *(vocabulary flag)*
The extract/judge and integrator derivations are BLOCKED on this
experiment by design (v1.2 item 7) — so the experiment necessarily runs on
**provisional prompts stamped fixture-not-policy**, built from the
conditional-fates table's ancestors:

| Arm actor | Ancestor | Permitted adaptations (exhaustive) |
|---|---|---|
| B extract | `harvest_map_v1.md`, verbatim | (i) emit wire-0 `sighting` JSON instead of the prose wire line — field-for-field identical content (§6.2 IS that line) |
| B judge | `harvest_residue_v1.md` | (i) wire-0 `ruling` JSON output; (ii) the two conditional-fates fixes: evidence-rich born-complete case files as input; autonomy — `escalate` removed, tiebreak ladder installed, flagged-ruling as a field; (iii) web rung per packet `web_policy`, select-don't-introduce |
| A integrator | `harvester_prompt_v1.md` / JJU prior art (BJJ project, ops-side) | (i) wire-0 `sighting` + `ruling` emission per packet alongside its state output; (ii) autonomy — same ladder, no operator questions mid-run; (iii) index/shard state form per §7 |

Permitted adaptations are ONLY: speaking wire-0, and complying with law
already ratified (autonomy, three-citations, state model). **Nothing
else** — no prompt-quality tuning on either side beyond parity fixes,
so the experiment measures topology, not prompt polish. **Fairness
clause:** comparable adaptation effort per arm; every adaptation is
logged in the run report. If a run fails for a reason a one-line prompt
fix would cure, fix BOTH arms' equivalents (or neither) and re-run.

Provisional prompts are experiment fixtures. Whichever arm wins, the real
derivations happen in their own sessions per the conditional-fates table;
nothing in this kit ratifies a prompt.

---

## 2. Common surfaces (what makes the arms comparable)

**Surface 1 — the wire.** Both arms emit wire-0 objects
(`pipeline_config_schema.md` v2 §6): `sighting`, `ruling`, `park`, in the
envelope, closed-world. Topology-neutral by construction — only the
producers differ (extract workers vs the integrator's per-packet
emissions). Every model-actor output in either arm lands in the run's
`wire.jsonl` before any script consumes it.

**Surface 2 — the export.** *(vocabulary flag: export surface)* Each
arm's assemble step emits the per-source glossary in the ratified
**merged-line grammar** (residue v1 output grammar; lexicon §4):

```
- `<term-key>` — <type>. defined <loc> (ref <loc>,…). <sense>. [aliases-in-source: <as stated>]
```
Split form (numbered senses, source numbering kept where stated):
```
- `<term-key>` — <type>. senses: (1) <sense> — defined <loc> (ref <loc>,…); (2) <sense> — defined <loc> (ref <loc>,…). [aliases-in-source: <as stated>]
```

For arm A, "assemble" = a script that flattens the final index + shards
into this grammar; for arm B it is Phase 4. **The scorer diffs exports
and audits wires; it never reads either arm's internal state.** Internal
state (fold's index/shards, DAG's case files) is kept as run fixtures for
diagnosis, not scored.

**Surface 3 — link provenance.** Any script-made link (prove script in B;
any state-merging script in A) is logged one JSON object per link:
`{"a": <term_key@loc>, "b": <term_key@loc>, "citation":
"same_ink|stated_alias|brief_law", "evidence": <loc or brief line>}` in
`links.jsonl`. A link without a valid citation is the scorer's
similarity-linking critical class. (Model-made identity decisions ride
the wire as `ruling` objects and are audited there instead.)

---

## 3. Fixture set — Tier F and Tier R *(vocabulary flags)*

### Tier F — fixture tier (adversarial, per-fixture keys)
The existing sealed kits, translated to wire-0 + autonomy. Failure-mode
regression: catches an arm that wins the diff by luck while committing
the classes the decomposition exists to prevent.

**F-map (4): sailing map-kit spans 1–4, unchanged** (conditional alias
chain; Beaufort table; figure-dependent knots; two-regime exhibit).
Expected output translates mechanically: same content, `sighting` JSON.
Per-span keys per `harvest_map_v1_kit_spec.md`, re-serialized to wire-0
by ops. Arm A runs the same spans as sequential chunks; its per-packet
sightings are scored by the same keys.

**F-res (6): residue items translated under autonomy.** The old enum
(`union|split|distinct|escalate`) predates ratified autonomy; wire-0 has
NO escalate. Translation:

| Item | Was | Now (wire-0 expected ruling) |
|---|---|---|
| `res:sail:dinghy` | split | `split`, `method: in_source` (source's own numbering), `confidence: high` |
| `res:sail:rudder_debris` | union | `union`, `method: in_source`, debris discounted-not-dropped |
| `res:sail:two_regime` → **3a** | escalate | packet INCLUDES the discovery arbitration regime-map (schema v2 `arbitration.mode`, the E2 surface): expected `split` per the config regimes, `method: discovery` |
| `res:sail:two_regime` → **3b** | escalate | same material, packet WITHOUT the arbitration block: expected recoverable-direction ruling — `split`, `method: default`, `confidence: low`, `flagged: true` (evidence both ways + lean in `reasoning`). A confident `union` here is a false merge, critical. |
| `res:sail:windward_leeward` | union | `union` per the recorded E1 lean, `method: discovery` (the lean is a discovery convention) |
| `res:sail:rrs_reservation` **(NEW)** | — | ref-only sightings of `racing_rules_of_sailing` around p.281 + a synthesized arbitration-seed line forecasting the defined home in the racing chapter beyond the fixture's coverage: expected `reservation`, `method: discovery`. Restores the coverage guarantee — every wire-0 ruling value has an item whose correct answer is that value. Sightings synthesized to wire-0, stamped fixture-not-policy (residue-kit precedent). |

The 3a/3b pair additionally tests **config sensitivity of the ladder**:
the same evidence must rule differently when rung 2 is present vs absent.
Schemer items 5–6 and the jju residue item remain `[PENDING]` per the
residue kit spec and are NOT required for the gate (Tier R covers JJU).

Under arm A there are no case files; Tier F residue material is delivered
as chunks whose content forces the same questions, and the integrator's
`ruling` objects are scored against the same expected rulings (matched by
`subjects`, not by case-file id).

### Tier R — regression tier (the keyed diff, the gate metric)
The full JJU regression span, both arms end-to-end, exports diffed
against the frozen `glossary_index_v31.md`.

**Span choice (workshop sets criteria; ops picks the concrete range —
they hold the material):**
- Contiguous chapter run already covered by the sealed JJU test kit.
- Restricted key must contain **≥40 entries**, including **≥3 resolved
  fan-outs** (v7's known hard cases) and **≥2 stated alias chains** — so
  the identity classes have statistical teeth, not anecdotes.
- Large enough that arm B needs ≥6 parallel extract chunks (otherwise
  the operational comparison is degenerate).

**Restricted key derivation (ops, scripted, sealed):** the subset of
`glossary_index_v31.md` entries whose defined home OR any ref location
falls inside the chosen span, re-serialized to the merged-line grammar.
Entries whose defining evidence lies OUTSIDE the span are moved OUT of the
key into an `expect-reservation` annex (a plain list, one term name per
line — the scorer's expected format): the correct behavior for them is a
reservation, not an entry — an arm is not penalized for honestly not
knowing what the span cannot teach. The key and annex are script-derived
and SEALED: never pasted into an ops chat; read by the scorer from disk.

---

## 4. Prove-script contract (arm B, phase 2 — ops-assembled harness)

The prove script does not exist (merge script retired; conditionally
resurrected per v1.2 item 7). The experiment needs one; building the
ratified version here would be a second engine artifact. Ruling for this
kit (docketed): **the workshop specifies the contract; ops assembles a
harness implementation stamped fixture-not-policy**; if arm B wins, the
real prove script gets its own derivation session.

Contract (exhaustive — anything beyond this is a violation the scorer
catches via `links.jsonl`):
- Input: the run's `sighting` objects. Output: (a) clean merges applied
  to the draft export, (b) case files, born complete, one per unresolved
  cluster, (c) `links.jsonl` per §2 surface 3.
- May link two sightings ONLY by: **same ink** (overlapping-span dedupe),
  **stated alias** (union-find over `aliases_in_source`), **brief law**
  (discovery-ruled equivalences). Equality and stated claims, never
  similarity: no thresholds, no string distance, no verdict-bearing
  heuristics.
- Everything unprovable ships to a judge WHOLE: the case file carries
  every sighting of the cluster plus pre-grepped slices around each loc.
- Heuristic signals survive only as suspicion labels on case files
  (non-verdict) — the intake `flag:` slot, per the residue precedent.
- Phase barrier: no case file is released until the last extract chunk
  lands or parks; a parked chunk stalls the barrier BY DESIGN and is
  recorded in the run report.

---

## 5. Diff metric (what the scorer measures)

### Layer A — wire + ruling audit (both arms, Tier F and Tier R)
1. **Wire conformance:** every object validates against wire-0 under the
   closed-world rule (unknown field fails). Failures name field + rule.
2. **Ruling discipline:** enum only; `method: default` ⇒
   `confidence: low`; `flagged: true` ⇒ reasoning carries evidence both
   ways + a lean within ≤10 lines; `evidence` non-empty; every ruling's
   evidence locs inside the packet manifest (cross-packet reach =
   critical).
3. **Tier F expected-ruling comparison:** per fixture, ruling vs key.
   `union` where the key says `split`/`distinct` is a **false merge** —
   reported separately (the unrecoverable direction). Other mismatches
   are ordinary verdict errors.
4. **Link audit:** every `links.jsonl` entry carries one of the three
   citations with evidence. Anything else = similarity-linking, critical.
5. **Park accounting:** parks by reason; separate lint/infra counters
   (wire-0 §6.4). Parks are not errors — the diagnostics law expects
   loud-and-cheap breaks — but they are counted and reported.

### Layer B — export diff vs the sealed key (Tier R; the gate numbers)
Matching is alias-aware using the key's own stated aliases only (no
similarity). Classes:
- **false_merge** — ≥2 key entries collapsed into 1 export entry.
  Unrecoverable direction; reported separately; weighted first.
- **false_split** — 1 key entry spread over ≥2 export entries.
  Recoverable; ordinary error.
- **recall_miss** — key entry with no export counterpart. (Entries in the
  `expect-reservation` annex are scored instead as: reservation present =
  correct; confident entry or silence = miss.)
- **precision_invention** — export entry with no key counterpart.
- **split_fidelity** — key entries with numbered senses must be split in
  the export with the source's numbering; a flattened sense table scores
  as a false merge of senses.
- **sense_containment** — content-word containment of the key sense in
  the matched export sense (containment, never paraphrase-similarity —
  residue-kit precedent). Reported as a ratio; informs the noise band.
- **ref_coverage** — fraction of the key entry's locations present.

### Operational metrics (recorded per arm, from run metadata)
Sequential wave count (the DAG claim: 2–3 vs ~N chunks); model-call
count; total tokens (batch metadata); wall-clock; park count. Recorded,
not capped — cost symmetry: both arms run the batch half-price lane.

---

## 6. Pass criteria — the gate rule *(vocabulary flag: gate verdict)*

**Critical-fail classes (arm-level; any nonzero fails the arm's run):**
identity-law violations in sightings (inferred identity on the wire);
similarity-linking (link audit); cross-packet reach powering a ruling;
world-knowledge-powered union (Tier F keys mark where this is the trap);
coined types; `method: default` without `confidence: low`; a confident
ruling where the Tier F key requires the flagged low-confidence default
(the silent coin flip, autonomy-shaped — the old un-escalated-coin-flip
class, translated).

**noise band** *(vocabulary flag)*: max(1 entry, 2% of restricted-key
entries) for count classes; 0.05 for mean sense_containment. Differences
inside the band are ties.

**Gate verdicts:**
- **DAG RATIFIED** iff arm B has no critical fail AND, on Tier R, arm B
  is not worse than arm A beyond the noise band on ANY of: false_merge
  (compared absolutely, band = 0 — the unrecoverable class admits no
  band), false_split, recall_miss, precision_invention, split_fidelity,
  mean sense_containment; AND arm B posts the claimed operational wins
  (strictly fewer sequential waves AND total tokens ≤ arm A's). The
  proposal's promise is "matches or beats on every axis at once" — so
  matching quality without the operational win is NOT a pass.
- **FOLD RETAINED** iff arm B critical-fails while arm A does not, OR
  arm B loses any Layer B class beyond the band ("loses something the
  careful reader wouldn't have — the careful reader takes the crown back
  with evidence"), OR arm B fails the operational condition.
- **NO RATIFICATION** iff both arms critical-fail or the run is
  operationally invalid (barrier deadlock, expired batch, contaminated
  key). Then the tuning loop: read the reasoning fields, tune the
  provisional prompts (fairness clause — both arms), re-run. The gate
  question stays open; nothing silently promotes.

The gate verdict applies the conditional-fates table (v1.2 item 7)
mechanically at the next workshop session; the ops run itself ratifies
nothing.

---

## 7. Ops runbook (what the workshop hands over)

1. **Ships from the workshop:** this spec; `topology_scorer_v2.py`
   (self-tested against synthetic fixtures — key-free by construction).
2. **Ops assembles (BJJ/JJU side, sealed):** Tier R span choice per §3
   criteria; restricted key + expect-reservation annex (scripted,
   sealed); Tier F packet assembly (map spans verbatim from the map kit;
   residue case files per §3 translation, fixture-not-policy stamps);
   the provisional integrator prompt from JJU prior art (§1 adaptations
   only, logged); the prove-script harness (§4 contract); wire-0
   re-serialization of the existing sealed keys.
3. **Run order:** Tier F both arms → scorer Layer A; if either arm
   critical-fails on fixtures, apply the tuning loop BEFORE spending
   Tier R tokens. Then Tier R both arms → full scorer → compare mode →
   gate verdict.
4. **Contamination rules:** keys are script-derived and sealed, read by
   the scorer from disk, never pasted into any ops chat; no arm's actor
   ever sees a key; every run's raw output (wire.jsonl, links.jsonl,
   export, internal state, batch metadata) returns to the workshop as
   fixtures; the scorer report + gate verdict return in the ops
   checkpoint.
5. **Batch discipline:** both arms on the batch lane; per-request status
   inside "succeeded" batches; collect within the 29-day expiry; infra
   retries on the separate strike counter.

## 7-M. Manual chat lane — API mimicry protocol

The first experiment run executes MANUALLY in chat (operator ruling,
2026-07-13c: iterative API testing is not yet affordable). This section
is the rigorous process for mimicking API usage in chat. It amends §7's
batch assumptions; everything not amended here holds unchanged. The
architecture was chat-ready by construction — packets are paste-ready by
definition, workers are stateless single-packet actors, outputs are
bounded sentinel/fenced blocks, `custom_id` travels inside the packet —
so this protocol formalizes discipline rather than redesigning anything.

### 7-M.1 The operator is the driver
Every driver duty transfers to the operator by hand:
- **Mint `custom_id`s** before dispatch: `stage:unit:attempt`
  (`extract:c03:1`, `judge:cf_dinghy:1`, `integrate:c03:1`). Keep a
  dispatch log (a plain text list is fine): custom_id, ctx identifier,
  dispatched/collected/parked.
- **Assemble packets** in the exact concatenation order the prompts
  declare: generic prompt ⊕ harvest brief (verbatim) ⊕ mode block ⊕
  span/case-file/state. One paste, one message, nothing else in it.
- **Collect** each output by whole-fence copy into the run dir's
  `wire.jsonl` (and `export.md` at assemble time).
- **Run the retry loop manually:** after each collection batch, run
  `topology_scorer_v2.py score --run DIR` (Layer A only — no `--key`).
  A wire fault on an object = ONE retry: fresh ctx, same packet, the
  lint failure report (exact field + rule) prepended. A second failure
  = park: append a `park` object to `wire.jsonl` yourself with the
  verbatim report; separate strike counters per §6.4 (a chat-platform
  failure — dead ctx, refusal, truncation — is an `infra` strike, never
  a lint strike).

### 7-M.2 Ctx hygiene (the contamination rule, sharpened)
- **One worker = one fresh ctx.** No exceptions. A ctx that has seen any
  other packet, any key, or any project file is burned for worker duty.
- A judge ctx sees exactly ONE case file. A DAG extract ctx sees exactly
  ONE span packet.
- The fold integrator needs the INVERSE discipline: each iteration's ctx
  receives exactly the current index + arbitration file + touched shards
  + the new chunk — deliberate, complete, and nothing else (no prior
  transcripts, no memory of earlier iterations beyond the state files).
- **Keys touch no chat, ever.** The scorer reads them from disk.
- Workers run in ctxs OUTSIDE this project (a project ctx can search
  project knowledge — that is cross-packet reach by ambient tooling).
  navigate ≠ remount cuts both ways: a clean ctx stays clean only if
  nothing is filed into its reach.
- **Web rung policing:** chat ctxs can search the web; the batch lane
  cannot. Extract workers and any actor whose packet's `web_policy` is
  `off` must be instructed NOT to search (already in the ancestor
  prompts: "no web"); judges use the web rung only per the packet's
  stated policy. A ruling whose reasoning cites web content under
  `web_policy: off` is a critical finding — record it in the run report
  even though the scorer cannot detect it mechanically.

### 7-M.3 Transcription integrity (copy-paste is now a pipeline stage)
- Provisional prompts for the manual lane instruct workers to emit
  wire-0 objects ONLY inside a single fenced code block; the operator
  copies whole fences, never fragments.
- Wire-lint's closed-world validation doubles as the corruption
  detector: truncation or mangling almost always breaks the schema
  loudly. A lint failure that looks like transport damage (half an
  object, fence residue) is an `infra` strike, not a worker lint strike
  — re-collect before re-dispatching.
- Run `score` incrementally after every collection batch, not only at
  the end; a transcription defect found late contaminates everything
  filed after it.

### 7-M.4 Operational metrics under the manual lane
**Ruling [session-ruled 2026-07-13c, lean stated, operator ratification
at the docket — see docket item 12]:** the manual run measures **waves
exactly** (they are structural facts: fold = one wave per chunk, DAG =
extract + judge + scripts) and **defers token certification** to the
first API run. No character-count proxy: inventing a measurement
violates the honest-TBD posture (schema v2 precedent — honest
placeholders over invented values). `meta.json` for a manual run:

```
{ "lane": "manual-chat", "waves": <int>, "tokens": null,
  "model_per_actor": { "extract": "<model>", "judge": "<model>",
                       "integrator": "<model>" } }
```

The scorer's compare mode, when BOTH reports declare
`lane: manual-chat`, enforces the wave condition, DEFERS the token
condition (reported, listed under `"deferred"`), and can therefore emit
**DAG RATIFIED with token certification recorded as debt**: the first
API run re-measures; a token blowout there is a re-open trigger for the
gate, and any prompts derived meanwhile remain valid ancestors under
either outcome (the conditional-fates table is status-only in both
directions — recoverable by design).

### 7-M.5 Parity constraints chat introduces
- Same model for both arms' equivalent actors (extract/judge vs
  integrator), recorded in `meta.json` — a model-tier difference would
  measure the tier, not the topology.
- Comparable ctx settings per actor class (no long custom instructions
  on one arm's ctxs and not the other's).
- The fairness clause (§1) applies to manual-lane adaptations too: any
  chat-specific instruction added to one arm's provisional prompt gets
  its equivalent on the other, and every adaptation is logged.

## 8. Kit status

- **Spec** — this file, SHIPPED 2026-07-13c (ratification pending docket).
- **Scorer** — `topology_scorer_v2.py`, SHIPPED, self-test green on
  synthetic fixtures (run receipt in the session checkpoint).
- **Tier F** — sailing material fully specified (6 residue items incl.
  the new reservation item and the 3a/3b pair; 4 map spans by reference);
  Schemer/jju fixture slots remain `[PENDING]`, NOT gate-blocking.
- **Tier R** — criteria fixed here; concrete span + sealed key = ops
  build.
- **Provisional prompts** — adaptation law fixed here; assembly = ops
  build (fold arm) / mechanical wire-0 adaptation (DAG arm actors).
- **Prove-script harness** — contract fixed here (§4); assembly = ops
  build, fixture-not-policy.
