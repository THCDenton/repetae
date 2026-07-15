# Session checkpoint — 2026-07-10b (workshop, salvage/resync)

Purpose: boot file for the next session. Files are the only memory; this
file plus the artifacts below is everything this session knew that matters.
Supersedes nothing — reads alongside the 2026-07-10 workshop checkpoint.
Context note: this session was hopped across THREE projects mid-flight
(pipeline workshop → sailing engagement, briefly elsewhere). Next session:
start in the workshop (Repetae) project.

## What this session was

Booted from the 07-10 checkpoint to start harvest_map derivation; became a
salvage-and-resync session instead when two dependency files proved lost.
Mixed roles (state verification, two file recoveries, harvest_map design
discussion, operator re-sync at layman level). Acceptable as a recovery
emergency; next session is single-artifact.

## State changes since the 07-10 checkpoint (verified, not assumed)

1. **the-little-schemer: discovery RATIFIED** under discovery_prompt_v2.4
   (2026-07-10, Opus ops run). The ingest fix + clean re-run happened.
   v2.4 loses its UNTESTED flag; full output family produced (master doc,
   harvest_brief, content_mode_map.csv, loc_anchors.csv); loc grammar
   printed=phys−16 proven; enum discipline held; 3 kit nominations with
   named failure modes; zero blocking escalations; two designed handoffs
   (role_split → span-sizing; cross-source arbitration → registry queue).
   **The end-to-end proof point is banked.**
2. Operator actions possibly still pending from that run: paste the
   registration line into sources.md; file the four Schemer artifacts
   into project knowledge.
3. **Two files confirmed never filed** (project searches, absence proven):
   `engine_charter_amendment_v1.1.md`, `discovery_sailing-for-dummies.md`
   (+ its CSV sidecar). Operator ruled them gone.

## Artifacts shipped this session (operator: download + file into workshop project)

1. `engine_charter_amendment_v1.1.md` — RE-ISSUE. Verbatim transcription
   of the ratified 07-09 text recovered from the dead "phase 1 draft"
   transcript, plus a dated recovery note. Known wart, left as-written:
   §2 references `source_survey_6books.md`, a filename that never existed
   (real artifact: `pdf_shape_survey.md`) — one-line fix when a
   housekeeping session folds the amendment into a charter v1.1 body.
2. `discovery_sailing-for-dummies_SALVAGE.md` — ~85% verbatim
   reconstruction from the "Sailing book analysis" ops transcript (lives
   in the sailing engagement project; transcripts are only searchable
   from inside their own project). PROVISIONAL per in-file salvage
   notice; gaps marked [NOT RECOVERED] (five short axis sections, E1
   body, middle of YAML fragment). **All four kit nominations recovered
   verbatim.** CSV sidecar not recovered (was already sentenced to v2.4
   regeneration for enum discipline).
   **Operator ruling: shelve as-is; ops inspection later.** [operator-decided]

## Rulings and leans from this session

- Sailing salvage: shelve as-is, inspect later. [operator-decided]
- Checkpoint before starting harvest_map derivation. [operator-decided]
- Span-sizing: NOT settled (charter §10 fence stands). Workshop lean,
  explained to and engaged by operator but not clicked: **parameterize** —
  span_size/overlap stay config dials; the worker prompt carries
  boundary-robustness doctrine (report what's visible, mark defined-vs-ref
  honestly, merge dedupes overlap); kit packets use provisional sizes
  stamped fixture-not-policy; the kit later becomes the instrument that
  settles the real numbers. Re-present at next session start.
- Residue scope: NOT settled. Workshop lean: harvest_residue is its own
  later session per charter worklist; harvest_map_v1 ends its output
  grammar with a short **downstream contract** note (stable keys, what a
  boundary-cut entity looks like on the wire). Re-present at start.

## Salvaged design facts for harvest_map derivation (from transcripts — re-verify against files at derivation time)

- harvest_map = the generic per-span worker prompt (map phase). Packet =
  generic prompt (cached prefix) + per-source brief verbatim + mode block
  (selected via mode map) + span text. custom_id = stage:unit:attempt.
- Charter worklist lists harvest_map and harvest_residue as SEPARATE
  artifacts, each with its own sealed kit.
- Derivation shape: subtraction/relocation from harvester_prompt_v1
  (ancestor: glossary builder v7). Registration → config; arbitration →
  residue/escalation queue; cursor/header machinery dies (driver owns
  position). Survives: extract every named thing, defined-vs-ref,
  source-faithful sense lines, aliases-as-stated.
- Wire-format ancestor (harvester_prompt_v1 glossary line):
  `- <term-key> — <type>. defined <loc> (ref <loc>,…). <one-line sense>.`
- No-identity-judgments law (draft recovered): workers may TRANSCRIBE
  identity claims the span itself states ("also known as" parentheticals,
  the source's own sense numbering) but never INFER identity — no
  "probably the same as," nothing outside the packet. State with examples
  on both sides. Scope violations = the kit's critical failure class.
- Kit protocol (charter §8): prompt file + paste-ready packet + sealed
  script-derived answer key (never pasted into ops chats) + scorer
  (recall misses / precision inventions / scope violations / lint).
  Hard spans only. Kit inputs: sailing's 4 nominations (recovered
  verbatim in the salvage file) + Schemer's 3 (in its ratified doc) +
  jju regression (glossary machinery in workshop project).
- Mode-block set pinned by the v2.4 enum: prose | tabular | dialogic |
  code_listing | mixed.

## Ground truth about the platform (hard-won today)

- A hopped conversation's `/mnt/project` disk mount can be EMPTY while
  `project_knowledge_search` still works. Search; don't trust the mount.
- Past-chat search is scoped per project: ops transcripts are salvageable
  only from inside their engagement project. This is how the sailing doc
  was recovered — and the recovery playbook if it happens again:
  transcript create_file calls preserve full artifact text.
- Chat-uploaded files do NOT follow the operator across sessions; this
  session's two output files exist only as downloads until filed.

## Dependency status for harvest_map derivation (all green)

engine_charter ✓ (workshop project knowledge) · amendment ✓ (re-issued,
file it) · pipeline_config_schema ✓ (project) · discovery_prompt_v2.4 ✓
(project) · harvester_prompt_v1 + glossary machinery ✓ (project) ·
Schemer discovery + sidecars ✓ (file if not yet) · sailing discovery ✓
(salvage, provisional — sufficient: kit nominations verbatim).

## Recommended next session

**harvest_map_v1 derivation.** Workshop project, single-artifact. Boot:
this checkpoint (+ 07-10 checkpoint for deeper history). Open with the two
unsettled leans (span-sizing dial; residue-separate + downstream contract)
as button decisions, then an outline for review before drafting.
Deliverables: `harvest_map_v1.md` (generic doctrine incl. transcribe-vs-
infer law with two-sided examples + boundary doctrine + output grammar +
downstream contract; five mode blocks) and the sealed kit spec (8 spans:
sailing 4 + Schemer 3 + jju regression; scorer definition; provisional
span sizes stamped fixture-not-policy).

## Session hygiene notes

- Operator re-sync pattern that worked: plain-language glossary of the
  whole system ("goldfish sessions, paperwork is the memory"), factory/
  warehouse metaphors, data samples at every pipeline hop. Consider a
  two-paragraph layman recap at every session start.
- Corrections ledger (own errors): said "Node-RED holds zero state" —
  operator correctly objected; precise form: the SYSTEM is stateful, every
  ACTOR is stateless (state concentrated in the file store). Also
  initially framed sailing discovery as unrecoverable before checking the
  engagement project's transcripts — search before declaring loss.
