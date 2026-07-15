# Session checkpoint — 2026-07-11 (workshop, meta-infrastructure)

Purpose: boot file for the next session. Files are the only memory; this
file plus the artifacts below is everything this session knew that matters.
Supersedes nothing — reads alongside the 2026-07-10 and 2026-07-10b
workshop checkpoints. Context note: workshop project throughout; no
context hop.

## What this session was

Meta-infrastructure only. Compiled the workshop's own vernacular
(`workshop_lexicon_v1.md`) as a drift-control reference; drew the
end-to-end system diagram covering ratified + planned + undesigned actors
and per-hop wire schemas (`system_diagram_v1.html`); built the session
primer (`workshop_primer_v1.md`) that boots every fresh workshop chat by
enforcing lexicon vocabulary on both operator and Claude. Zero work on
engine content (harvest_map, registry prompts, schema v2). Acceptable as
reference-tier infrastructure; the next session returns to charter-worklist
work.

## State changes since the 07-10b checkpoint (verified)

1. Workshop vocabulary is now pinned in a reference artifact rather than
   distributed across charter + amendment + prompts + checkpoints. Six
   drift instances catalogued in the lexicon warts ledger §10 (phantom
   filenames, tag count, mode enum shorthand, "current for jju"
   mis-labeling, etc.).
2. Diagram format ratified as HTML (`system_diagram_v1.html`); the
   intermediate `system_diagram_v1.md` is retired (W7). No .md
   counterpart may be recreated — design-state prose (wire schemas,
   actor status ledger, "what does not exist yet" inventory) lives
   embedded in the HTML below the interactive stage.
3. Primer artifact minted: `workshop_primer_v1.md`. Operator pastes it
   as the opening message of every new workshop chat.
4. New engine vocabulary minted this session (see lexicon changelog):
   ingest, text substrate, fidelity gate, generic ingest node (PROPOSED),
   packet builder, downstream contract (lean, unruled), registry_dossier
   + registry_verdict (working names), cards_map (UNDESIGNED), primer.
5. No engine artifacts modified — charter, schema, prompts, kits:
   unchanged since 07-10b.

## Artifacts shipped this session (operator: download + file into workshop project)

1. `workshop_lexicon_v1.md` — reference, not authority. Ten sections +
   append-only changelog. Governs vocabulary; the primer requires every
   fresh workshop chat to read it first.
2. `system_diagram_v1.html` — interactive mermaid diagram (pan/zoom) +
   prose sections below (status legend, wire schemas H1–H14, actor
   status ledger, undesigned inventory). Reference, not authority;
   statuses rot — newest checkpoint wins.
3. `workshop_primer_v1.md` — reference, not authority. Boot file for
   workshop chats.
4. **RETIRE:** `system_diagram_v1.md` — per W7, remove from project
   knowledge. Do not recreate.

## Rulings and leans from this session

- **Diagram is HTML-only.** [operator-decided] HTML is the format for
  operator consumption; .md counterpart retired and non-recreatable (W7).
- **Prose destination.** [operator-decided] Wire schemas / actor status
  ledger / undesigned inventory embed inside `system_diagram_v1.html`,
  below the interactive stage; no separate .md.
- **Primer artifact class.** [operator-decided] Primer is a first-class
  engine reference artifact; workshop chats begin by pasting it as the
  opening message.
- **Vocabulary policing calibration.** [operator-decided] Claude
  requests clarification when ambiguity would change an artifact or a
  decision; stylistic imprecision is not a trigger. Trigger examples
  live in the primer §"Vocabulary discipline".
- **BJJ material stays as prior art in-file.** [operator-decided,
  earlier this session] Not deleted — lexicon §2 "jju / prior art"
  entry + §8 split table pin the read-only ancestor status.
- **W1 (six-book survey filename tangle) remains unresolved by ruling.**
  [operator-decided, recorded, not resolved] Left for a future
  housekeeping session that folds amendment v1.1 into a regenerated
  charter body.
- **Unchanged from 07-10b (still leans, still re-present at next
  session start):**
  - Span-sizing: parameterize — unruled.
  - Residue scope: harvest_residue is its own later session;
    harvest_map_v1 ends with a downstream contract note — unruled.

## Ground truth learned this session

- **Vocabulary-first ordering worked.** Sequence lexicon → diagram →
  primer meant each downstream artifact used only vocabulary the upstream
  artifact had already minted. When the diagram needed a word the lexicon
  didn't have (ingest, packet builder, cards_map, etc.), the discipline
  was to patch the lexicon first, then use the term. Recommend future
  infrastructure sessions follow this ordering.
- **Drift search method.** Cataloguing warts before drafting: searched
  conversation history, cross-read all project files, compared claims
  against each other. Yielded six drift instances that became §10 seed
  content. Reusable for future housekeeping sessions.
- **HTML viewer pattern.** Self-contained HTML + embedded mermaid source
  + CDN loader = double-clickable local viewer with no install. Parse
  validation locally via jsdom + `mermaid.parse()`; Chrome-based full
  rendering requires a browser (sandbox lacks one — parse-only is
  sufficient for CI-style validation before shipping).
- **Nothing new about the platform** beyond 07-10b's findings.

## Dependency status for the next session (harvest_map_v1 derivation, all green)

engine_charter ✓ · amendment v1.1 ✓ · pipeline_config_schema ✓ ·
discovery_prompt_v2.4 ✓ · harvester_prompt_v1 + glossary machinery ✓ ·
Schemer discovery + sidecars ✓ · sailing discovery ✓ (salvage,
provisional, sufficient) · **NEW dependencies to file first:**
`workshop_lexicon_v1.md`, `system_diagram_v1.html`,
`workshop_primer_v1.md`; retire `system_diagram_v1.md`. The primer
requires the lexicon and diagram to be present — file all three before
booting the next session.

## Recommended next session

**harvest_map_v1 derivation.** Same target 07-10b recommended — this
session did not touch it. Workshop project, single-artifact. Boot
sequence: paste `workshop_primer_v1.md` content as opening message →
Claude reads lexicon + diagram → provide this checkpoint (+ 07-10b for
depth). Open with the two unsettled leans (span-sizing dial;
residue-separate + downstream contract) as button decisions, then an
outline for review before drafting. Deliverables: `harvest_map_v1.md`
(generic doctrine incl. transcribe-vs-infer law with two-sided examples
+ boundary doctrine + output grammar + downstream contract; five mode
blocks) and the sealed kit spec (8 spans: sailing 4 + Schemer 3 + jju
regression; scorer definition; provisional span sizes stamped
fixture-not-policy).

## Session hygiene notes

- **Single-artifact rule was broken.** This session produced four
  reference artifacts (lexicon, diagram .md, diagram HTML, primer, each
  with mid-session updates). Tightly coupled infrastructure,
  operator-directed. Two readings: (a) the rule needs a carve-out for
  reference-tier / infrastructure sessions where artifacts co-depend, or
  (b) the primer should have been its own session. Not ruled; flag for
  consideration at a future housekeeping session. A future ruling could
  mint an "infrastructure session" type in lexicon §3.
- **Vocabulary-first pattern (above)** worth codifying as workshop
  discipline if another infrastructure session runs.
- **Corrections ledger (own errors):**
  - Draft lexicon initially carried "current for jju" phrasing that
    misread prior art as the engine's current set; operator flagged,
    corrected in-session (pre-filing revision, logged in lexicon
    changelog).
  - Initially named the diagram viewer `system_diagram_v1_viewer.html`
    because I framed HTML as a "generated preview" — a stance the
    operator's later ruling correctly overrode. Renaming to
    `system_diagram_v1.html` was mechanical once HTML was ruled the
    artifact of record.
  - Near-miss: almost shipped the diagram-format ruling only as a §8
    table swap without also filing W7. Warts ledger entry added on
    second pass.
