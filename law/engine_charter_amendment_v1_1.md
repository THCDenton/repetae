# Engine Charter — Amendment v1.1

Status: ratified 2026-07-09 (operator-directed, this session). Apply by
appending this file to the project alongside `engine_charter.md` v1; a future
housekeeping session may fold it into a regenerated v1.1 charter body. Per §
"Amendments are versioned events": this note records what changed and why.

Recovery note (2026-07-10): the original file was lost before filing; this
copy was transcribed verbatim from the 2026-07-09 derivation session
transcript by the workshop. Content unchanged from the ratified original.

## What changed

**1. New stage: Domain discovery (Stage 0.5, pre-harvest).**

Inserted between source registration and harvest. Reads the raw source's
front/back matter, TOC, and a stratified sample of spans; interviews the
operator; emits `discovery_<slug>.md` — a per-source conventions document
(prose conventions + a config fragment) that every downstream stage prompt
consumes via the packet builder.

**Deliberate exception to the batch anatomy:** discovery runs as a
*supervised interactive session*, not a batch job. Rationale: discovery is
almost pure judgment — the map/reduce law says judgment is the expensive
sequential part, and here the human IS the reduce step. A conversation is the
cheapest possible escalation queue: every open question is escalated, answered
in seconds, and recorded with provenance. The original checkpoint proposal
(batch job proposes, human ratifies after) is superseded by this form, which
folds ratification into the process itself.

The stage still honors the universal shape: upstream artifact in (raw source),
one prompt transforms (`discovery_prompt_v1.md` drives the session), bounded
artifact out (the conventions doc), gate (operator sign-off inline; config-lint
on the emitted fragment), exceptions escalate (unanswerable questions become
`escalations/` files, not silent defaults).

**2. Worklist reorder (charter §9).**

The six-book survey changed the dependency graph: the generalized style
contract's template slots (`data_table`, `code_block`, `tradeoffs`,
`further_reading`) and the harvest prompts' mode handling depend on what
discovery declares per source. Amended worklist order:

1. ~~`engine_charter.md`~~
2. ~~`pipeline_config.schema.md`~~
2.5. **`discovery_prompt_v1.md`** — this session's artifact.
3. Generalized style contract — now additionally reads
   `source_survey_6books.md` and the discovery conventions-doc format.
4. Stage prompts + sealed kits (unchanged list; harvest prompts now consume
   discovery output instead of guessing seeds/scope/modes).
5. Scripts. 6. Driver. (Unchanged.)

**3. Schema posture (explicitly NOT ratified here).**

Discovery necessarily proposes config fields that are still survey findings,
not schema (`native_seed`, `scope`, `content_mode`, `ingest`,
`visual_dependency`, `arbitration_mode`, `mention_classes`, `single_artifact`,
era handling — survey §2/A2, findings 1–14). The conventions doc marks every
such field `# schema:v2-proposed`. Config-lint's unknown-key rule stands: a
v2-proposed field entering a real `pipeline_config.yaml` requires the schema
v2 amendment session first. Discovery output is the *evidence pile* for that
session, not a backdoor around it.

## Unchanged and reaffirmed

- One artifact per fresh session; files are the only memory.
- Open questions (charter §10) remain open; discovery *observes* span-sizing
  behavior per source but does not settle the span_size/overlap TBDs.
- Dev/ops split: discovery is an ops session type (it runs against client
  sources in the engagement project). The workshop derives its prompt.
