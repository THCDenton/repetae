# Engine Charter — v1

Status: founding document. Written at the close of the architecture session (2026-07-09), while full context was still live. Every future derivation session reads this first. Amendments are versioned events: bump the version, note what changed and why.

## 1. What this is

A general-purpose pipeline engine that turns a source (book, course, transcript set, docs) into a verified knowledge product: a cited, cross-linked wiki vault and generated study cards. Extracted from a working BJJ/JJU pipeline, which remains the reference implementation and answer key.

**Why it exists (business context, two lines):** token metering per unit is the COGS number that makes the service priceable. Client zero (a new book, in a new project) validates that the engine — not the operator's memory — does the work.

## 2. Project topology

- **Workshop (this project):** derivation only. BJJ artifacts are prior art and regression answer keys. No operations run here.
- **Client zero (new project):** receives only the finished kit. If a session there needs anything not in the kit, the extraction failed. That visibility is the point.
- **Dev/ops split:** dev sessions design prompts and scorers; ops sessions (fresh chats, later the driver) execute them. Dev never executes against material it holds the answer key for — a contaminated context proves nothing.

## 3. The five-stage anatomy

Every stage has the same shape: upstream artifacts in → one prompt transforms → bounded artifacts out → linter gates → exceptions escalate.

- **Stage 0 — Source registration.** One line per source in `sources.md`: slug, type, title, location grammar making every citation mechanically resolvable (chapter-section for books, timestamps for video, anchors for forums).
- **Stage 1 — Harvest.** Extract every named thing per source: term, type, defined-vs-referenced locations, one-line sense *as this source teaches it*, in-source aliases. Records what the source calls things, never what the wiki calls things.
- **Stage 2 — Registry.** Cross-source concept symbol table; one machine-parseable line per concept; the sole naming authority. Reasoning lives in an append-only rulings file. The single-namespace property is load-bearing: exactly one process may mutate the registry, ever.
- **Stage 3 — Node build.** Reader-facing pages per the style contract. Grep-don't-load; every cited location verified in-session (or in-packet); completeness = every attributed location and edge taught, delegated with a link, or explicitly out of scope. Emits sentinel batches + `REGISTRY DELTAS`.
- **Stage 4 — Assembly/outputs.** Pure scripting: splitter renders the vault; linter regenerates the ledger and worklists; card packager emits `.apkg`.

Cross-cutting (not stages): style contract (binds every prompt, wins all conflicts), linter (gates both sides of every job), escalation format (≤10 lines, evidence both ways, a stated lean).

## 4. The map/reduce decomposition

Law of the pipeline: **every stage splits into reading (map: batchable, independent, half price) and deciding (reduce: sequential, cheap once reading is pre-paid).** Judgment is the only thing irreducibly sequential and expensive; the architecture minimizes judgment per unit of work.

| Stage | Map (one batch job) | Reduce (in order) |
|---|---|---|
| Harvest | Per-span extraction; **no identity judgments** | Script merge (exact-key joins, location unions, overlap dedupe) + model residue pass for fan-in/fan-out and sense drift only |
| Registry | Evidence dossiers per candidate pair: research, evidence both ways, a lean, **no verdict** | Verdict pass; sole registry mutator; escalates coin flips |
| Node build | Author against a frozen registry snapshot | Script: apply deltas sequentially; mint collisions → retry lane |
| Cards | One request per finished node; pure map, no shared state | Script only: validate, package `.apkg` |

Design consequences already identified:
- Harvest spans **overlap slightly**; merge dedupes. (Overlap size: open question.)
- Harvest residue pass inherits the fan-in/fan-out machinery from glossary builder v7.
- Registry dossiers cite evidence about the *world*, not about registry state — stated invariant so dossiers can't go stale mid-run.
- Node batches run against a registry **snapshot**; the collector detects canonical-mint collisions and routes losers to retry.

## 5. Runtime: unsupervised but monitored

- **Driver loop per unit:** pick batch (ledger order, unit budget) → build packet (pre-grepped source slices) → API batch job (cached prefix, tokens metered) → lint gate → pass: apply deltas, file shard, loop; fail: **retry once** with lint report prepended; fail again: **park**. A parked unit is terminal until a human looks. One stubborn node must never burn tokens in a circle.
- **Human surface:** dashboards (ledger, lint history, token log, spend) and the escalation queue. Nothing else requires a person.
- **Escalations** attach only to judgment (reduce) steps.

## 6. Runtime: mechanics and platform

- **Batch API is the default lane.** 50% off input and output, no minimum batch size, up to 100k requests/batch; results unordered, retrievable 29 days; poll, no webhooks; typical completion minutes-to-hours, 24h ceiling. Latency is the currency we have plenty of.
- **Prompt caching stacks with batch** (best-effort in batch; identical shared prefixes across a batch maximize hits). Request shape: cached prefix = stage prompt + style contract + registry snapshot; variable suffix = unit packet.
- **Sync lane exists** for interactive one-offs (e.g., rebuilding a single node after resolving an escalation). Same subflow, one config flag.
- **Model tiering per stage:** judgment steps get the strong model; conversion/extraction get mid-tier; card generation gets the cheap tier. "You are Claude Opus" in legacy prompts was an assumption, not a requirement. Chat-prototyped prompts are an upper bound: spot-check on the target model with a micro-batch before trusting the economics.
- **Orchestration: Node-RED**, chosen for the free dashboard and visual debuggability — but explicitly replaceable by cron + one Python driver; nothing real may live in the flow. Prompts stay in versioned files on disk; nodes are thin executors. Flow JSON lives in git next to the prompts. No state in flow/global context. API key in env, never in flow JSON.
- **Scheduled per-batch execution** is the default (cron submits; a collector flow harvests finished jobs), matching the disposable-sessions philosophy and failing cheap. A continuous daemon is a later option once park logic is proven airtight.

## 7. File store (the actual system; everything else is stateless machinery)

```
engagement/
  pipeline_config.yaml        # domain, models per stage, span size, outputs
  prompts/                    # versioned stage prompts (the cached prefix)
  sources/<slug>/             # raw text + span_manifest.csv
  glossary/<slug>.md          # merged harvest (+ rulings)
  registry/registry_vN.md     # symbol table (+ rulings)
  nodes/batch_NN.txt          # shards; splitter renders vault/
  vault/  cards/              # outputs
  state/
    jobs.jsonl                # append-only: job_id, stage, batch_id, status
    node_ledger.csv           # linter-generated, never hand-edited
    token_log.csv             # tokens + $ per unit — the COGS log
    escalations/  parked/     # one file per open question / dead shard
```

**Invariants:**
1. Files are the only memory. Sessions, flows, and contexts are disposable.
2. `custom_id = stage:unit:attempt` is the universal join key: names the request, the result, the token-log row, the parked file. Results are unordered; reassembly keys on this, never on position.
3. Write-ahead: every state transition appends to `jobs.jsonl` **before** the action.
4. Idempotent scripts: re-applying a shard is a no-op; the applier checks before writing.
5. Single writer per artifact: verdict pass → registry; applier → vault; linter → ledger.
6. Exit-code contract for workers: 0 clean, 1 dirty, 2 escalate. Flows route on exit code, never by parsing output.
7. Batch results are written to disk immediately on collection (29-day retrieval window).
8. Restart-safety: on boot, recovery reads `jobs.jsonl`, polls anything `submitted`, downloads what finished, resumes. Killing the orchestrator at any moment must cost nothing.

## 8. Prototyping and test protocol (sealed kits)

Chat prototyping is valid because a batch request is stateless and self-contained — one fresh chat message is structurally the same object. Protocol per prompt:

- **Kit contents:** the prompt file; a paste-ready packet; a sealed answer key (derived by script from BJJ artifacts, never pasted into the ops chat); a scorer script (parses sentinel output, reports recall misses, precision inventions, scope violations, lint pass/fail).
- **Ops runs:** fresh chat → paste prefix + packet → save raw output → run scorer locally → return the *report*, not the transcript.
- **Scope violations are the critical failure class** (e.g., identity language appearing in map output). The decomposition rests on maps refusing to judge.
- Every ops output is saved as a **fixture**; the driver's collector/parser/validator are tested end-to-end against fixtures with the API mocked before any paid token moves.
- Test spans are chosen *hard* (alias-dense, fan-out-heavy per the answer key). Easy spans passing proves nothing.

## 9. Derivation worklist (dependency order)

1. ~~`engine_charter.md`~~ — this document.
2. `pipeline_config.schema.md` — everything a domain config must specify. Everything downstream reads this.
3. Generalized style contract — voice rules kept; node-type templates become config-driven slots.
4. Stage prompts, each with sealed test kit: `harvest_map`, `harvest_residue`, `registry_dossier`, `registry_verdict`, `node_builder_general`, `cards_map`.
5. Scripts: packet builder, harvest merge, delta applier, card packager, scorers — all testable dry against kit fixtures.
6. Driver: Node-RED flows + fixture-mocked plumbing tests.

One artifact per fresh session; each session reads this charter and its target's dependencies, ships files, dies.

## 10. Open questions (unsettled; do not silently decide)

- Span overlap size, and span sizing generally per source medium (prose vs. transcript vs. forum thread stress spans differently).
- Residue-detection heuristics: what the merge script flags for the model pass vs. resolves mechanically.
- Parked-shard aging: alarm or periodic digest so `parked/` can't rot silently.
- Registry snapshot cadence for node batches (per batch? per N batches?) and collision-rate tolerance before the cadence tightens.
- Cards design: card types per node type, dedupe across nodes, deck structure — the stage prompt has no BJJ predecessor to inherit from.
- Linter generalization: which `wiki_lint.py` checks are universal vs. BJJ-schema-specific.
- Target models per stage (pending micro-batch spot checks against the metered budget).

## 11. Standing constraints carried forward

- Book-derived content is personal-use unless licensed; the sellable assets are the engine, the methodology, and services applied to content the client owns.
- Prompt and contract edits are versioned events. The style contract wins all conflicts.
- Never upgrade "the source implies" into "the source says."
