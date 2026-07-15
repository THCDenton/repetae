# pipeline_config.schema.md — v2

Status: **schema v2 — RATIFIED 2026-07-13b** (config-schema-v2 amendment
session; deviations docket 1–13 ratified wholesale by the operator after an
arguments pass; owed per amendment v1.1 §3, reaffirmed v1.2 item 11).
First tenant: wire schema v0 (§6, per v1.2 item 4). Second tenant: the
chunk-plan / arbitration / `web_policy` per-source blocks (§3.2.1, per v1.2
items 3+8 and discovery v2.5). Full triage of the v2-proposed pile ruled
in-scope by the operator [operator-decided]. Appendix C is the v1→v2
amendment record. Originally: derivation worklist item 2 (charter §9).
Amended 2026-07-12 (charter
amendment v1.2, item 2): `residue_heuristics` removed (dissolved by the
scripts-never-similarity law); `span_size`/`span_overlap` marked
RETIRED-as-constants pending the schema-v2 session (executed 2026-07-13:
this document; disposition in §3.2.1/§3.5). [W10 note: that patch was
specified 07-12c, found unfiled at the 07-13 boot, and re-applied
verbatim-to-spec
2026-07-13 as change 0 of this re-issue.] Defines everything a domain
config must specify. Everything downstream — the generalized style contract,
every stage prompt, the packet builder, the linter, the driver — reads this
schema and MUST NOT invent configuration surface outside it. Amendments are
versioned events.

Grounding: every field below traces to a hardcoded domain assumption found in
the BJJ reference implementation (`style_contract_v1.md`, the four stage
prompts, `wiki_lint.py`) or to a runtime decision recorded in the charter.
Appendix B is the audit trail. Appendix A is the client-zero reference config:
**the BJJ build expressed in this schema.** If the engine fed Appendix A
cannot reproduce the BJJ vault, either the extraction or this schema is wrong.

---

## 1. What is NOT configuration (engine constants)

These are properties of the engine. They appear in no config file, and a
config that tries to restate them is invalid. Listed so the schema can stay
small and so nobody parameterizes a load-bearing invariant by accident.

- **File layout** (charter §7): `engagement/` tree, `state/` contents,
  `jobs.jsonl` write-ahead, single-writer map, idempotent appliers.
- **`custom_id` grammar**: `stage:unit:attempt`. Universal join key.
- **Sentinel format**: `===== NODE: <canonical> =====` + YAML frontmatter;
  frontmatter canonical is authoritative for the filename (splitter contract).
- **Registry line grammar** and the single-namespace property (one mutator).
- **Core frontmatter fields**: `canonical, title, type, status, sources,
  defined_at, requires, aliases` — always required. (`cards` is conditional;
  see §3.7.)
- **Exit-code contract**: 0 clean / 1 dirty / 2 escalate.
- **Retry policy**: retry once with lint report prepended, then park. Parked
  is terminal until a human looks. Not a knob — it is the circuit breaker.
- **Escalation format**: ≤10 lines, evidence both ways, a stated lean.
- **Map/reduce scope law**: map steps make no identity judgments; the reduce
  step of each stage is its sole judgment site. Scope violations are lint
  errors, not style preferences.
- **Universal lint checks**: sentinel/frontmatter match; required frontmatter;
  duplicate canonicals; link resolution (built / registry-known / declared
  forward, else UNRESOLVABLE); declined-link flags; `requires` acyclicity;
  parent coverage; ledger + worklist generation. Domain config *parameterizes*
  some of these (root set, exempt link suffixes) but cannot disable them.
- **Faithfulness rule**: never upgrade "the source implies" into "the source
  says." Charter §11; not negotiable per client.

---

## 2. Config file identity

One file per engagement: `engagement/pipeline_config.yaml`. Top-level keys are
exactly the sections in §3. Unknown keys are a config-lint error (fail loud,
not silently ignored).

| field | type | req | meaning |
|---|---|---|---|
| `config_version` | int | ✓ | bumped on any edit; versioned event |
| `engine_version` | string | ✓ | engine release this config was validated against |
| `engagement_id` | slug | ✓ | names the engagement dir; appears in token log |

---

## 3. Sections

### 3.1 `engagement` — domain identity

Replaces "You are authoring nodes for a BJJ wiki" and every other prompt-baked
domain framing. The `domain_brief` is injected verbatim into every stage
prompt's cached prefix.

| field | type | req | notes |
|---|---|---|---|
| `domain` | string | ✓ | short name, e.g. "Brazilian Jiu-Jitsu" |
| `domain_brief` | string (2–4 sentences) | ✓ | what the wiki is, who reads it, what "teaching" means here |
| `content_license` | enum `personal \| licensed \| client_owned` | ✓ | gates hosting-sensitive outputs (photos, public deploy). `personal` forbids public hosting (charter §11) |
| `background_knowledge` | enum `allowed \| forbidden` | ✓ | whether nodes may include uncontroversial shared domain knowledge phrased neutrally (BJJ: allowed). For domains the operator can't smell-check, `forbidden` forces every claim to a citation |

### 3.2 `sources` — list of registered sources

Config mirrors `sources.md`; `sources.md` remains the append-log of record and
the two are lint-checked for agreement.

Per source:

| field | type | req | notes |
|---|---|---|---|
| `slug` | slug | ✓ | short, lowercase, permanent |
| `type` | enum `book \| video \| article \| forum \| docs \| course` | ✓ | selects harvest defaults and location-grammar family |
| `title` | string | ✓ | full title / author / year |
| `loc_grammar` | string | ✓ | must make every citation mechanically resolvable (e.g. `chapter-section N-M`, `t=XmYs`, `post-anchor`) |
| `text_path` | path | ✓ | extracted text under `sources/<slug>/` |
| `media_notes` | string | – | e.g. "images stripped; visual layer unavailable" |
| `web_policy` | enum `off \| in-tradition \| open` | ✓ | harvest-stage web license, ruled at discovery (v1.2 item 3; button ruling per discovery v2.5). Default when unset: `off` — the recoverable direction |
| `arbitration` | object | – | per-source arbitration block; see §3.2.1 |
| `chunk` | object | ✓ | the chunk-plan block; see §3.2.1. Replaces the retired `span` override |
| `ingest` | object | ✓ | measured extraction parameters; see §3.2.1. Discovery v2.5 step 1 MEASURES exactly these fields |
| `scope` | object | – | in/out-of-scope ruling from discovery; see §3.2.1 |
| `content_mode` | object | – | mode-map pointer + default; see §3.2.1 |
| `mention_classes` | list | – | reference-only entity classes; see §3.2.1 |
| `native_seed` | object | – | native seed capture; see §3.2.1 |
| `era_handling` | object | – | edition/era posture; see §3.2.1 |
| `visual_policy` | object | – | figure/visual treatment; see §3.2.1 |
| `single_artifact` | — | – | **RESERVED** — evidence lost with the salvage gap; field name held, shape TBD (see §5) |

### 3.2.1 Per-source v2 blocks

New in v2. Every field here is measured or ruled at discovery (Stage 0.5)
and arrives via the config fragment; none may be invented at config-writing
time. Evidence provenance per block is recorded in Appendix C.

**`arbitration`** (v1.2 items 3+8; sailing escalation E2):

| field | type | req | notes |
|---|---|---|---|
| `mode` | enum `community \| codified \| academic \| ground_truth` OR map of regime → mode | ✓ if block present | scalar for single-regime sources; the map form exists because one source can carry plural regimes (sailing: community seamanship + codified racing rules). Regime keys are source-local |
| `anchors` | list per mode/regime | – | naming/usage authorities for tradition-scoped web (guarded per v1.2 item 3: select-don't-introduce; question-keyed admissibility) |
| `tiebreak_preferences` | map ambiguity-class → preference | – | per-class operator leans from the discovery watchlist pass; leans, never sense rulings |
| `seed_path` | path | – | the `arbitration_seed_<slug>.md` sidecar. Judge-visible boot state, tiebreak rung 2. NEVER injected into briefs or worker packets (config-lint 12) |

**`chunk`** (v1.2 item 8; discovery v2.5 — retires the span constants):

| field | type | req | notes |
|---|---|---|---|
| `boundary` | enum `chapter \| section \| convention` | ✓ | the ruled natural teaching boundary; `convention` = a source-specific applicable convention named in the master doc |
| `fallback_max` | object `{unit, value}` | ✓ | size bound for oversized units; a **per-source measured button ruling**, never a global default |
| `overrides` | list | – | per-range exceptions to the boundary rule, each citing its loc range |
| `plan_path` | path | ✓ | the `chunk_plan_<slug>.csv` sidecar — the actual unit list. Consumers: packet builder + driver. Any overlap policy is topology-owned downstream and consumes these units (07-13 ruling) |

**`ingest`** (discovery v2.5 step 1 measures these; sailing salvage is the
motivating exhibit — table shatter, icon stripping, caption disorder):

| field | type | req | notes |
|---|---|---|---|
| `container` | enum `born_digital \| scan_ocr` | ✓ | |
| `ocr_engine` | string | ✓ if `scan_ocr` | |
| `columns` | int | ✓ | |
| `zone_model` | string | – | layout zoning method |
| `row_clustering` | object `{method, gap_threshold_pt}` | – | |
| `hyphenation` | object `{style, marker}` | – | |
| `repair_vocab` | list | – | closed substitution lists only — never open-ended fuzzy repair (scripts-never-similarity) |
| `preserve_patterns` | list | – | noise-looking content that is content |
| `code_detection` | string | – | |
| `table_mode` | string | – | |
| `icon_mechanism` | string | – | e.g. margin-icon recovery (sailing: six icons stripped, Tip/Warning indistinguishable) |
| `danger_classes` | list | – | |
| `fidelity_canaries` | list | ✓ | exact strings that must reconstruct; re-run at any re-ingest |
| `figure_manifest` | path | – | the up-front figure census (id, page, bbox); no rasterization at manifest time |
| `caption_pattern` | string | – | e.g. `Figure N-M:` |
| `source_of_record` | enum `pdf \| text` | ✓ | which artifact downstream disputes resolve against |

Note: the source-level `text_path` (§3.2) remains the single canonical
pointer to the extracted substrate; `ingest` does not carry a duplicate
(collision resolved this session — see Appendix C and docket).

**`scope`** (sailing Q3 exemplar):

| field | type | req | notes |
|---|---|---|---|
| `include` | `all` or list of loc ranges | ✓ if block present | |
| `exclusions` | list of `{range, reason}` | – | each exclusion cites its discovery ruling |

**`content_mode`**:

| field | type | req | notes |
|---|---|---|---|
| `map_path` | path | ✓ if block present | the content-mode-map CSV sidecar; mode column values only from the pinned enum `prose \| tabular \| dialogic \| code_listing \| mixed` (config-lint 13) |
| `default` | enum (same) | ✓ if block present | mode assumed where the map is silent |

**`mention_classes`** (sailing dual-status exemplar: US Sailing / ASA /
ISAF are simultaneously governing bodies and certification brands):

| field | type | req | notes |
|---|---|---|---|
| (list items) | object `{class, treatment, notes}` | – | `treatment` enum: `reference_only \| dual_status \| build`. Tracked-as-references entities never become nodes unless re-ruled |

**`native_seed`** (native-seeds law: merge-level recall aid; NEVER in the
brief or worker packets):

| field | type | req | notes |
|---|---|---|---|
| `path` | path | – | seed list sidecar (source-stated term inventory) |
| `origin` | string | ✓ if block present | where in the source the seed comes from (index, glossary, TOC) — provenance, one clause |

**`era_handling`** (sailing exemplar recovered verbatim):

| field | type | req | notes |
|---|---|---|---|
| `pedagogical_versioning` | bool | ✓ if block present | does the source teach version-dependent content |
| `era_bound` | enum `none \| mild \| strong` | ✓ if block present | |
| `notes` | string | – | e.g. "ISAF→World Sailing (2015); stale URLs; 2006 regs" |

**`visual_policy`** (sailing Q2 exemplar — operator accepted figure loss,
declined lexical reconstruction):

| field | type | req | notes |
|---|---|---|---|
| `figures` | enum `build \| degrade \| skip` | ✓ if block present | `degrade` = honest empty slots, never invented content |
| `notes` | string | – | sub-structure deliberately minimal; richer shape is an open question (§5) |

### 3.3 `entity_model` — the domain's type schema

Replaces the BJJ-baked `position | technique | control | action | concept`
set and the per-type page templates in the style contract. The generalized
style contract (worklist item 3) keeps voice rules and reads templates from
here.

Engine-reserved structural types always exist and are not declared:
`category`, `landing`, `path`, `discard`.

| field | type | req | notes |
|---|---|---|---|
| `types` | list | ✓ | domain content types; each per the sub-table below |
| `root_categories` | list of canonicals | ✓ | the only entries allowed `parent: root`; linter enforces |
| `role_split` | object or `null` | – | if the domain has perspective-split entities (BJJ: top/bottom). Fields: `roles` (list of suffix slugs), `landing_required: bool`. `null` disables landing-page lint expectations |

Per type:

| field | type | req | notes |
|---|---|---|---|
| `name` | slug | ✓ | frontmatter `type` value |
| `description` | string | ✓ | one line; goes to harvester + registry prompts so extraction knows what counts as a named thing |
| `template` | ordered list of section slots | ✓ | from the engine's slot vocabulary: `breadcrumb, definition, procedure, goals, options, cues, dangers, mechanism, variations_by_source, connections, children_list, role_doors, staged_list, data_table, code_block, tradeoffs, further_reading` (last four added v2 — survey findings; sailing ratified `tradeoffs` in use and dropped the other three for that source, which is exactly per-source template selection doing its job) |
| `unit_weight` | number or range | ✓ | verification-load estimate for batch budgeting (BJJ: technique 1–2, position hub 4–6) |
| `connection_labels` | list | – | reader-facing edge groupings (BJJ: *Set up from · Combines with · Countered by · Leads to*). Defaults to a generic set |

### 3.4 `registry`

| field | type | req | notes |
|---|---|---|---|
| `authority_anchors` | list of strings | ✓ | naming/provenance authorities for the dossier + verdict passes (BJJ: BJJ Heroes, Wikipedia). Dossiers cite evidence about the world, never registry state |
| `community_arbitration` | bool | ✓ | whether web research settles identity at the REGISTRY stage (BJJ: true). Domains with no public community (internal docs) set false → verdicts rest on in-source evidence only, more escalations expected. v2 note: harvest-stage web use is governed separately by per-source `web_policy` + `arbitration.mode` (§3.2.1); this bool is registry-stage only and unchanged |
| `snapshot_cadence` | enum `per_batch \| per_n_batches(N)` | ✓ | **TBD — charter §10.** Schema reserves the field; default `per_batch` until collision-rate data exists |

### 3.5 `harvest`

Harvest topology is UNDER EXPERIMENT (v1.2 item 1); this section holds only
topology-neutral surface until the gate rules. Per-source harvest inputs
(chunking, arbitration, web policy) live in §3.2.1 — they exist in any
topology.

| field | type | req | notes |
|---|---|---|---|
| `span_size` | — | — | **RETIRED as a constant** (v1.2 item 8) — disposition executed this session: the §3.2.1 `chunk` block replaces it. Key is now UNKNOWN to config-lint |
| `span_overlap` | — | — | **RETIRED as a constant** (v1.2 item 8) — same disposition. Key now UNKNOWN to config-lint |
| `overlap_policy` | — | — | **RESERVED, topology-owned** — the winning topology's overlap policy consumes chunk-plan units; field shape arrives via a post-gate versioned event, not this session (07-13 ruling) |

### 3.6 `node_build`

| field | type | req | notes |
|---|---|---|---|
| `unit_budget` | number | ✓ | verification units per batch job (BJJ: ≈8) |
| `structure_fill` | bool | ✓ | landing/category pages ride along in authoring batches (BJJ: true) |

### 3.7 `outputs`

| field | type | req | notes |
|---|---|---|---|
| `vault.enabled` | bool | ✓ | |
| `vault.photos` | object or `null` | – | `path_grammar` (BJJ: `photos/<slug>/<loc>/`) + `hosting: personal_only`. Config-lint: photos + `content_license: personal` + public deploy = error |
| `cards.enabled` | bool | ✓ | when true, `cards` becomes a required frontmatter field and `*<cards.link_suffix>` links are lint-exempt |
| `cards.link_suffix` | string | – | default `_anki_cards` |
| `cards.card_types` | map node-type → card types | ✓ if enabled | **TBD — charter §10.** No BJJ predecessor; the cards_map kit will populate the vocabulary |
| `cards.deck_structure` | object | ✓ if enabled | **TBD — charter §10** |

### 3.8 `models` — tiering per stage

Map of stage step → model string. Steps: `harvest_map, harvest_residue,
registry_dossier, registry_verdict, node_build, cards_map`.
v2 note: the two harvest step names describe the SUSPENDED v1 shape; under
v1.2 item 7's conditional fates they become `extract, judge` (DAG) or
`integrator` (fold) via a post-gate versioned event. Keys are placeholders,
not law.
Guidance (charter §6): judgment steps strong, extraction mid, cards cheap —
but every assignment is **TBD pending micro-batch spot checks** against the
metered budget. Config-lint warns if a judgment step is assigned below the
mid tier.

### 3.9 `runtime`

| field | type | req | notes |
|---|---|---|---|
| `lane_default` | enum `batch \| sync` | ✓ | batch is the engine default; sync exists for one-offs |
| `poll_interval` | duration | – | collector polling; default 10m |
| `budget.max_spend_per_run_usd` | number | ✓ | hard stop; driver refuses to submit past it |
| `budget.max_tokens_per_unit` | number | – | tripwire → park, not retry (a unit burning tokens is the failure the park rule exists for) |
| `parked_aging` | object | – | **TBD — charter §10** (alarm vs. periodic digest). Field reserved: `mode`, `threshold` |

### 3.10 `prompts` — version pinning

Map of stage step → prompt filename under `engagement/prompts/`
(e.g. `node_build: node_builder_general_v1.md`). Prompt edits are versioned
events; the config names exactly which version each stage runs, so a run is
reproducible from config + prompts dir alone.

### 3.11 `wire` — wire schema pin (NEW in v2)

| field | type | req | notes |
|---|---|---|---|
| `schema_version` | string | ✓ | pins which wire schema (§6) this engagement's workers and scripts speak — same reproducibility logic as `prompts` pinning. v2 ships `wire-0` |

---

## 4. Config-lint (validation rules)

Run at driver boot and on any config change; exit-code contract applies.

1. Unknown top-level or per-section keys → error.
2. Every `sources[].slug` unique; `sources.md` and config agree.
3. Every `entity_model.types[].template` slot is in the engine vocabulary.
4. `root_categories` non-empty; each will be linted as `type: category`,
   `parent: root`.
5. `role_split` null ⟺ no landing-page expectations in wiki-lint.
6. `cards.enabled: true` requires `card_types` and `deck_structure` present
   (TBD values may be stubs, but the keys must exist and be acknowledged).
7. `content_license: personal` + any public-hosting output flag → error.
8. Every step in `models` and `prompts` covered; prompt files exist on disk.
9. Any field marked TBD in this schema that is still at its placeholder when
   `lane_default: batch` submits a paid job → warning in the run header, so
   an unsettled default can't burn tokens silently.
10. (v2) `chunk` block: `boundary` from its enum; `fallback_max` carries both
    `unit` and `value`; `plan_path` exists on disk; every `overrides[]` entry
    cites a loc range valid under the source's `loc_grammar`.
11. (v2) `web_policy` present for every source (explicitly, even when `off` —
    an absent ruling and a ruled `off` must be distinguishable in the file).
12. (v2) `arbitration.seed_path`, `native_seed.path`, `content_mode.map_path`,
    `ingest.figure_manifest`: files exist on disk. Packet-builder lint: seed
    and native-seed content in a brief or worker packet is an ERROR (the
    quarantine is mechanical, not honor-system).
13. (v2) content-mode map: mode column values only from the pinned enum;
    an improvised mode value is an error, not a new mode.
14. (v2) `wire.schema_version` present and known to the engine; every worker
    result object validates against §6 under the closed-world rule before any
    script consumes it. Wire-lint failure reports name the exact field + rule
    and prepend to the single retry (v1.2 item 4).
15. (v2) `ingest.fidelity_canaries` non-empty; driver re-runs canaries at any
    re-ingest and treats a canary failure as a park, not a warning.

---

## 5. Open questions surfaced as fields (do not silently decide)

This schema deliberately reserves fields for every charter §10 open question
that is configuration-shaped, with placeholders rather than invented defaults:
`registry.snapshot_cadence`, `cards.card_types`, `cards.deck_structure`,
`runtime.parked_aging`, all `models` assignments. New in v2:
`harvest.overlap_policy` (topology-owned, post-gate); `single_artifact`
(name reserved, shape lost with the salvage gap — re-derive at the next
discovery run that needs it); `visual_policy` sub-structure beyond the
minimal enum; wire schema evolution beyond `wire-0` (bump discipline is law
in §6, future field sets are not). Settling each is a config
edit (versioned) informed by kit runs — not a schema change. Charter §10
items that are *not* config-shaped (linter check classification) are handled
in §1/§4 here: universal checks are constants; domain checks derive from
`entity_model` and `outputs`.

---

## 6. Wire schema v0 (`wire-0`) — NEW in v2, first tenant

Ratified direction: v1.2 item 4 ("JSON in flight, prose at rest"); this
section is the field set that item 4 said "enters the live config only
through that session." Topology-neutral by construction: sighting and
ruling objects exist under both experiment branches; only their producers
differ (extract workers vs. an integrator's per-packet emissions).

**Contract.** Worker → script traffic is JSON, one object per sighting or
ruling, wrapped in the envelope. Durable state (index, shards, rulings)
stays human-readable prose — the wire is for flight only. Lint = literal
schema validation under a **closed-world rule**: an unknown field fails,
mirroring config-lint rule 1. Failure reports name the exact field + rule
and prepend to the single retry. Enums and bounds marked *injected* below
arrive in the worker's packet from config + discovery output — a worker
never guesses a vocabulary.

### 6.1 Envelope (every object)

| field | type | notes |
|---|---|---|
| `custom_id` | string | `stage:unit:attempt` — the universal join key; results join by it, never by position |
| `wire_schema_version` | string | `wire-0` |
| `kind` | enum `sighting \| ruling \| park` | payload discriminator |
| `payload` | object | one of §6.2–6.4 |

### 6.2 `sighting` — extract/map lane

The JSON form of the ratified harvest_map v1 wire line (RATIFIED 07-11b);
field-for-field, nothing added, nothing dropped:

| field | type | notes |
|---|---|---|
| `term_key` | string | snake_case, source-local; collides freely across sources |
| `type` | enum, *injected* | from `entity_model.types[].name` + discovery |
| `status` | enum `defined \| ref` | |
| `loc` | string | per-source `loc_grammar`; pattern-validated where the grammar is regular |
| `sense` | string, `maxLength` *injected* | one-line, source-faithful |
| `aliases_in_source` | list of strings | as stated ONLY — no identity judgments on the wire (map-scope law) |
| `boundary` | enum `whole \| head-cut \| tail-cut` | |

### 6.3 `ruling` — judge lane (autonomy-shaped)

No escalation lane exists at harvest (v1.2 item 3); the wire therefore has
no `escalate` value. Flagged rulings are a field, not an exit.

| field | type | notes |
|---|---|---|
| `ruling` | enum `union \| split \| distinct \| reservation` | `reservation` is the recoverable-direction parking of a sense question inside the arbitration file — a ruling, not an escape |
| `subjects` | list of term_key + loc-interval refs | what the ruling binds |
| `method` | enum `in_source \| discovery \| web \| default` | the tiebreak rung that decided it (ladder order is law) |
| `confidence` | enum `high \| medium \| low` | `method: default` forces `low` |
| `flagged` | bool | the flagged-ruling class (the repurposed escalation format lives in `reasoning` when true: evidence both ways + stated lean, ≤10 lines) |
| `reasoning` | string, `maxLength` *injected* | every ruling documents reasoning — feeds the surprise-rate diagnostics |
| `evidence` | list of loc citations | every verdict traceable to the packet |

### 6.4 `park` — broken lane

| field | type | notes |
|---|---|---|
| `park_reason` | enum `lint_fail \| token_tripwire \| infra \| canary` | |
| `attempt` | int | which strike; lint retries and infra retries burn SEPARATE counters (v1.2 item 4) |
| `report` | string | the lint/wire failure report verbatim |

### 6.5 Versioning discipline

`wire_schema_version` is mandatory in every object. Bump rules: adding an
OPTIONAL field = minor revision within `wire-0` (validators accept, workers
may omit); any removal, rename, type change, enum change, or new required
field = a new version (`wire-1`), which is a schema amendment — a versioned
event through a session, never an in-run edit. Config pins the version
(§3.11); a worker speaking a version the config doesn't pin is a wire-lint
failure, not a warning. Runtime semantics riding the wire (ratified, v1.2
item 4, restated not amended): phase barrier — where a judge lane exists,
case files are born complete and no judge dispatch happens until the last
extract chunk lands; a parked chunk stalls the barrier BY DESIGN. Three
lanes, no overlap: certainty → scripts, judgment → models, broken →
operator.

---

## Appendix A — client-zero reference config (`bjj`)

The BJJ build, expressed in this schema. Regression target: engine + this
config must reproduce the existing vault (modulo settled TBDs).

v2 note: BJJ predates discovery — the v2 per-source blocks were never
measured for it. Backfill posture below is honest placeholders (`TBD`,
flagged), never invented measurements; a BJJ regression run under v2 first
owes a discovery back-pass to fill them. `[model-knowledge]` leans are
marked where a plausible value is known but unratified.

```yaml
config_version: 2
engine_version: pre-release
engagement_id: bjj

wire:
  schema_version: wire-0

engagement:
  domain: Brazilian Jiu-Jitsu
  domain_brief: >
    A cited, cross-linked reference wiki for BJJ positions, techniques, and
    concepts, built from instructional sources. Pages teach in a neutral
    instructional voice; readers are practitioners looking up what a thing
    is and how to do it.
  content_license: personal
  background_knowledge: allowed

sources:
  - slug: jju
    type: book
    title: Jiu-Jitsu University — Saulo Ribeiro & Kevin Howell, Victory Belt 2008
    loc_grammar: 'chapter-section N-M; essay prefixes intro:/surv-intro:/esc-intro: preserved'
    text_path: sources/jju/jju_text.txt
    media_notes: images stripped; photo layer handled separately (personal use)
    web_policy: TBD                # lean in-tradition per JJU scope [model-knowledge]; needs a ruling
    chunk:
      boundary: TBD                # never measured; discovery back-pass owed
      fallback_max: {unit: TBD, value: TBD}
      plan_path: TBD
    ingest:
      container: born_digital      # [model-knowledge]
      columns: TBD
      fidelity_canaries: []        # TBD — lint 15 will park until filled
      source_of_record: text

entity_model:
  types:
    - name: position
      description: a configuration of two bodies with role-relative goals
      template: [breadcrumb, definition, goals, options, dangers, variations_by_source, connections]
      unit_weight: 4-6        # hubs; simple positions lower
    - name: technique
      description: a named procedure executed from a position
      template: [breadcrumb, definition, procedure, cues, dangers, variations_by_source, connections]
      unit_weight: 1-2
    - name: control
      description: a named grip/pressure configuration used inside positions and techniques
      template: [breadcrumb, definition, mechanism, variations_by_source, connections]
      unit_weight: 1
    - name: action
      description: a named movement primitive
      template: [breadcrumb, definition, mechanism, variations_by_source, connections]
      unit_weight: 1
    - name: concept
      description: a named principle, methodology, or pedagogy element
      template: [breadcrumb, definition, mechanism, variations_by_source, connections]
      unit_weight: 1
  root_categories: [position, sweep, choke, guard_pass, escape, takedown, concept]
  role_split:
    roles: [top, bottom]
    landing_required: true

registry:
  authority_anchors: [BJJ Heroes, Wikipedia]
  community_arbitration: true
  snapshot_cadence: per_batch        # TBD placeholder

harvest: {}                          # span constants RETIRED (v1.2 item 8); residue_heuristics DISSOLVED (v1.2 item 2); overlap_policy RESERVED (topology-owned)

node_build:
  unit_budget: 8
  structure_fill: true

outputs:
  vault:
    enabled: true
    photos:
      path_grammar: photos/<slug>/<loc>/
      hosting: personal_only
  cards:
    enabled: true
    link_suffix: _anki_cards
    card_types: TBD                  # charter §10 — no BJJ predecessor
    deck_structure: TBD              # charter §10

models:                              # ALL TBD pending micro-batch spot checks
  harvest_map: TBD-mid
  harvest_residue: TBD-strong
  registry_dossier: TBD-mid
  registry_verdict: TBD-strong
  node_build: TBD-strong
  cards_map: TBD-cheap

runtime:
  lane_default: batch
  poll_interval: 10m
  budget:
    max_spend_per_run_usd: 10
    max_tokens_per_unit: 400000
  parked_aging: TBD                  # charter §10

prompts:                             # generalized prompts pending (worklist 4)
  harvest_map: harvest_map_v1.md
  harvest_residue: harvest_residue_v1.md
  registry_dossier: registry_dossier_v1.md
  registry_verdict: registry_verdict_v1.md
  node_build: node_builder_general_v1.md
  cards_map: cards_map_v1.md
```

---

## Appendix B — extraction audit trail (BJJ hardcoding → config field)

| Where it was baked in | What it said | Now lives at |
|---|---|---|
| all four prompts | "You are Claude Opus … BJJ wiki" | `engagement.domain/domain_brief`; model in `models.*` |
| node_builder v5 | "uncontroversial shared BJJ knowledge" allowance | `engagement.background_knowledge` |
| style contract, frontmatter | type enum position…path | `entity_model.types` + engine-reserved structural types |
| style contract, templates | per-type section order | `entity_model.types[].template` |
| style contract, Connections | *Set up from · Combines with…* | `entity_model.types[].connection_labels` |
| registry prompt | "~6 top categories … parent: root" | `entity_model.root_categories` |
| style contract, landing | mount → mount_top / mount_bottom | `entity_model.role_split` |
| node_builder v5 §2 | unit weights, ≈8-unit budget | `entity_model.types[].unit_weight`, `node_build.unit_budget` |
| registry prompt, referee | "BJJ Heroes and Wikipedia are the anchors" | `registry.authority_anchors`, `registry.community_arbitration` |
| wiki_lint.py | `_anki_cards` link exemption; `cards` required field | `outputs.cards.link_suffix` / `.enabled` |
| style contract, photos | `photos/<slug>/<loc>/`, personal-use only | `outputs.vault.photos`, `engagement.content_license` |
| harvester prompt | span sizing "read closely, not skimmed" | retired as constant (v1.2 item 8); per-source chunk plan |
| charter §4/§6 | snapshot cadence, tiering, batch default | `registry.snapshot_cadence`, `models`, `runtime.lane_default` |
| operator playbook | prompt edits are versioned events | `prompts` pinning + `config_version` |
| amendment v1.2 item 4 (wire) | JSON in flight; maxLength on sense; closed enums injected; custom_id join key | §6 wire-0 + `wire.schema_version` |
| harvest_map v1 wire line (RATIFIED 07-11b) | term-key/type/status/loc/sense/aliases/boundary grammar | §6.2 `sighting` field-for-field |
| v1.2 item 3 (autonomy + ladder) | judges must rule; tiebreak ladder; flagged-ruling class; web guards | §6.3 `ruling` enums; `sources[].web_policy`; `arbitration.*` |
| v1.2 item 8 + discovery v2.5 | chunk at natural teaching boundary; per-source measured fallback; CSV sidecar | §3.2.1 `chunk` block |
| discovery v2.5 step 1 | ingest measurement targets | §3.2.1 `ingest` block, field-for-field |
| sailing salvage, entity model | slot `tradeoffs` in live use; slots selected/dropped per source | §3.3 slot vocabulary +4 |
| sailing salvage E2 | arbitration_mode scalar insufficient; plural regimes exist | `arbitration.mode` scalar-or-map |
| sailing salvage, dual-status | US Sailing / ASA / ISAF reference-only + dual-status | `mention_classes` treatment enum |
| sailing salvage, era block (verbatim) | pedagogical_versioning + era_bound | `era_handling` |
| sailing salvage Q2/Q3 | figure-loss acceptance; scope include/exclude rulings | `visual_policy`, `scope` |
| native-seeds law (lexicon §9) | merge-level recall aid, never in brief | `native_seed` + quarantine lint 12 |

---

## Appendix C — amendment record, v1 → v2 (2026-07-13 session)

Versioned-event audit trail; the durable patch spec (W10 lesson: record
specs, not just facts). Base: v1 as filed, with the 07-12c item-2 patch
re-applied verbatim-to-spec first (W10 closure — that patch was specified
07-12c, never landed, and is folded here; see header note).

| # | Change | Provenance |
|---|---|---|
| 0 | W10 re-application: `residue_heuristics` removed (§3.5/§5/App A); span constants RETIRED | v1.2 item 2 spec via 07-12c checkpoint [ratified] |
| 1 | §6 wire schema v0: envelope, sighting, ruling, park objects; closed-world validation; versioning discipline; §3.11 `wire.schema_version` pin | v1.2 item 4 [ratified direction]; sighting = harvest_map v1 line, field-for-field [ratified 07-11b]; ruling enums per autonomy [v1.2 item 3] |
| 2 | §3.2.1 `chunk` block ratified; §3.2 `span` per-source override REMOVED; `harvest.overlap_policy` RESERVED topology-owned | v1.2 item 8; discovery v2.5; 07-13 overlap ruling |
| 3 | `web_policy` per-source, required, default-off | v1.2 item 3; v2.5 button ruling |
| 4 | `arbitration` block: mode scalar-or-map (regimes), anchors, tiebreak_preferences, seed_path + packet quarantine lint | v1.2 items 3+8; sailing E2 (plural regimes); native-seeds/seed quarantine law |
| 5 | `ingest` block ratified, field-for-field from the v2.5 measurement list; `text_path` stays source-level only (collision resolved: no duplicate inside `ingest`) | discovery v2.5 step 1; sailing salvage exhibits |
| 6 | `scope`, `content_mode`, `mention_classes`, `native_seed`, `era_handling`, `visual_policy` ratified with minimal shapes | sailing salvage (Q2, Q3, dual-status note, era block verbatim); native-seeds law |
| 7 | `single_artifact` name RESERVED, shape NOT ratified | salvage gap — exemplar lost; do-not-silently-decide |
| 8 | §3.3 slot vocabulary +4: `data_table, code_block, tradeoffs, further_reading` | amendment v1.1 §3 list; sailing ratified `tradeoffs` in use |
| 9 | `registry.community_arbitration` UNCHANGED, scoped registry-stage-only by note | minimal-churn; harvest-stage web governed by §3.2.1 |
| 10 | Config-lint rules 10–15 added | consequences of 1–6 |
| 11 | §3.8 harvest step names marked CONDITIONAL placeholders | v1.2 items 1+7 |
| 12 | Appendix A bumped to config_version 2, honest-TBD backfill posture | this session's ruling |

Fields still v2-proposed after this session: NONE — the pile is fully
triaged (ratified, reserved-by-name, or dissolved). The `# schema:v2-proposed`
tag retires for existing fields; discovery may mint NEW proposals against a
future v3, tagged `# schema:v3-proposed`.
