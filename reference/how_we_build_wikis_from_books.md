# How We Build Wikis from Books — orientation document

Status: reference explainer, written 2026-07-10 from the project files. This is
a *description* of the system, not an authority over it. If anything here
conflicts with `engine_charter.md` (+ amendments), `runbook.md`,
`operator_playbook_v1.md`, or the current prompt set, those win — update this
doc, don't argue from it. For live state, read the newest
`session_checkpoint_*.md` first.

## What the system is

A pipeline that turns a source (book, course, transcript set, docs) into a
verified knowledge product: a cited, cross-linked wiki vault (Obsidian-style
markdown) plus generated study cards. It was built and proven on one book —
*Jiu-Jitsu University* (slug `jju`) — producing a BJJ wiki of ~180+ nodes, and
is now being generalized into a domain-agnostic engine. The BJJ build remains
the reference implementation and regression answer key.

The business motive: token metering per unit of work is the COGS number that
makes the service priceable. "Client zero" (a new book, in a fresh project)
exists to prove the engine — not the operator's memory — does the work.

## The two governing laws

**1. Files are the only memory.** Sessions, chats, and contexts are
disposable. Every session reads its inputs from project files, ships bounded
artifacts, and dies. Anything worth keeping is flushed to a file before the
session ends. Never trust transcript memory; a fresh context grepping real
files beats a long context half-remembering them. Session checkpoints
(`session_checkpoint_<date>.md`) are the boot files that carry state between
derivation sessions.

**2. Map/reduce decomposition.** Every stage splits into *reading* (map:
batchable, independent, cheap — and map steps make NO identity judgments) and
*deciding* (reduce: sequential, the sole judgment site of its stage).
Judgment is the only irreducibly expensive thing; the architecture minimizes
judgment per unit of work. Scope violations (a map step deciding identity)
are the critical failure class.

## The pipeline in one line

**source → discovery → per-source harvest → concept registry → nodes →
assembly (vault, cards)**

### Stage 0 — Source registration
One line per source in `sources.md`: slug, type, title, and a *location
grammar* that makes every citation mechanically resolvable (`jju:37-2` for
chapter-section, `t=14m32s` for video, anchors for forums). Never cite an
unregistered slug.

### Stage 0.5 — Discovery (ratified 2026-07-10, charter amendment v1.1)
A supervised *conversational* session (the one stage where the human is the
reduce step). It reads the raw source and interviews the operator to settle
per-source conventions: entity types and page templates, scope
inclusions/exclusions, content-mode map (prose/tabular/dialogic/code),
ingest/extraction settings, visual policy, alias weather, license posture.
Output family: `discovery_<slug>.md` master doc + machine sidecars (harvest
brief, content-mode map CSV, loc-anchors, registry queue). Every convention
line carries a provenance tag; ambiguity escalates, never silently defaults.
Current prompt: `discovery_prompt_v2_4.md` (untested as of the 07-10
checkpoint).

### Stage 1 — Harvest
Extract every named thing per source: term, type, defined-vs-referenced
locations, a one-line sense *as this source teaches it*, in-source aliases.
Harvest records what the *source* calls things, never what the wiki calls
things. Map = per-span extraction over slightly overlapping spans; reduce =
script merge plus a model "residue pass" only for fan-in/fan-out and sense
drift. The BJJ glossary (`glossary_index_v31.md` + entry files, frozen) is
this stage's finished output for `jju`. Current prompt:
`harvester_prompt_v1.md`; a generalized `harvest_map` is the next derivation
target.

### Stage 2 — Registry
The cross-source concept symbol table and *sole naming authority*: one
machine-parseable line per concept (canonical snake_case name, type, parent,
status, aliases, defined_at). Exactly one process may ever mutate it — the
single-namespace property is load-bearing. All reasoning lives in an
append-only `registry_rulings.md`; if the registry starts growing prose,
that's the old index failure recurring. Merging a new source is a four-step
referee: map builds evidence dossiers per candidate pair (evidence both ways,
a lean, no verdict); the reduce/verdict pass decides and escalates coin
flips to the human. Prompt: `registry_prompt_v1.md`.

### Stage 3 — Node build
Author reader-facing pages against a frozen registry snapshot, per the style
contract. Key disciplines: grep-don't-load (pull only the cited source
slices); verify every cited location in-session; completeness means every
attributed location and edge is taught, delegated with a link, or explicitly
out of scope. Batches are sized by *verification units* (edge-weight, ~8 per
session for BJJ; a hub position counts 4–6, a technique 1–2). Sessions emit
sentinel-delimited node batches (`===== NODE: <canonical> =====` + YAML
frontmatter) plus a `REGISTRY DELTAS` block the operator applies afterward.
Prompt: `node_builder_prompt_v5.md`.

### Stage 4 — Assembly / outputs
Pure scripting, no model: `split_nodes.sh` renders the vault from batch
shards; `wiki_lint.py` regenerates the ledger (`node_ledger.csv`) and
worklists; a card packager emits `.apkg`. Generated state is never
hand-edited.

## Cross-cutting machinery (not stages)

- **Style contract** (`style_contract_v1.md`): binds every prompt and wins
  all conflicts for anything a reader sees. Core rules: neutral instructional
  voice; no source/instructor names in body prose (names live only in
  *Variations / by source* and citations); no builder metacommentary ever;
  every borrowed fact carries a compact citation (`(jju:37-2)`); quotes are
  rare, <15 words. Fixed frontmatter schema (canonical, title, type, status,
  sources, requires, aliases, defined_at, cards) and fixed section order per
  node type.
- **Linter** (`wiki_lint.py`): gates both sides of every job. Universal
  checks: sentinel/frontmatter match, required frontmatter, duplicate
  canonicals, link resolution (built / registry-known / declared-forward,
  else UNRESOLVABLE), `requires` acyclicity, parent coverage, ledger +
  worklist generation. `forward_declined.txt` is the whitelist for
  deliberate deferrals.
- **Escalation format**: ≤10 lines, evidence both ways, a stated lean. The
  human smell-checks reasoning; "your lean is fine, proceed" is a complete
  answer.
- **Faithfulness rule**: never upgrade "the source implies" into "the source
  says." Non-negotiable per client.
- **Retry policy** (runtime): fail lint → retry once with the lint report
  prepended → fail again → park. Parked is terminal until a human looks; one
  stubborn node must never burn tokens in a circle.

## The human loop (operator supervision)

Before each session: run `wiki_lint.py`; open a *fresh* conversation; give
the phase one-liner plus the lint report. After: save emitted files, run
`split_nodes.sh`, apply the `REGISTRY DELTAS` block, re-run the linter.
Clean → file artifacts into the project. Dirty → don't debug it yourself;
the dirty report becomes the next session's first task. The lint report and
ledger ARE the system state — the operator should never need to read a
ruling doc to know where things stand. Full detail:
`operator_playbook_v1.md`.

## Project topology and roles

- **Workshop (this project)**: derivation only — designing prompts, schema,
  scorers. BJJ artifacts are prior art and answer keys; no operations run
  here.
- **Client zero (a separate project)**: receives only the finished kit. If a
  session there needs anything not in the kit, the extraction failed — that
  visibility is the point.
- **Dev/ops split**: dev sessions design; ops sessions (fresh chats, later an
  automated driver) execute. Dev never executes against material it holds
  the answer key for. Division of labor as of 07-10: Fable (workshop) builds
  prompts only; Opus (ops) does all bookwork; dev emits patch instructions
  rather than editing ops artifacts.
- **Sealed test kits**: each stage prompt ships with a paste-ready packet, a
  sealed answer key (script-derived, never pasted into ops chats), and a
  scorer. Test spans are chosen adversarially hard; every ops output is kept
  as a fixture.

## Generalization state (as of 2026-07-10)

- `engine_charter.md` (+ v1.1 amendment): the founding document; every
  derivation session reads it first.
- `pipeline_config_schema.md` v1: everything a domain config must specify;
  §1 fences engine constants that config may NOT touch; Appendix A expresses
  the BJJ build in the schema as the regression target. A schema-v2
  amendment queue (F1–F15 + ingest block + visual policy) exists but is NOT
  ratified — proposed fields carry `# schema:v2-proposed`.
- Six-book source survey done (`source_survey_4books.md` + addendum): the
  five-stage architecture survived all six teaching modes; every break
  landed in config/ingest/prompt design, not the architecture.
- PDF shape survey (n=5): one generic ingest node parameterized by an
  `ingest:` config fragment suffices.
- Discovery stage derived and dry-run (Sailing for Dummies discovery doc
  exists); `discovery_prompt_v2_4.md` is current but untested.
- Recommended next derivation: `harvest_map` prompt (or a v2.4 end-to-end
  dry run first — both orders sound).

## Standing cautions

- Book-derived content is personal-use unless licensed; photos especially.
  Never host publicly without permission review.
- Uploading a PDF to project knowledge silently replaces it with lossy text;
  raw binaries go as direct chat attachments (zip if transformed).
- If an older document contradicts the current prompt set, the current set
  wins — retire old docs, don't patch them.
- Do not treat unratified proposals (schema v2, figure-worker stage, generic
  ingest prompt) as decided.
