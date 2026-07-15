# Session checkpoint — 2026-07-12 (workshop, merge-script derivation ABANDONED; JJU excursion; direction flip)

Purpose: boot file for the next workshop session. Files are the only memory.
Reads alongside the 07-11c and 07-11b checkpoints; supersedes none. Written
under checkpoint schema v2.1 (five mandatory slots including boot manifest).

This is a **long** checkpoint because a lot happened, most of it upstream of
what the session was chartered to do. The paranoid-detail JJU catalog under
"Ground truth learned" is the reason: **the cardinal-rule break that
produced it must never happen again**, and that requires the findings to
survive as durable file state a future ctx can consume without any cross-
project access.

## What this session was

Chartered as the `harvest merge` script derivation (charter worklist item 5)
per the 07-11c recommendation. Did not ship the engine artifact. Instead,
mid-session, the operator's brittleness intuition about the map/reduce split
prompted a cross-project excursion into the JJU project (**cardinal rule
break**, operator-initiated), where I read the actual JJU harvest artifacts.
What I found reversed my architectural recommendation. The session closed
without shipping the merge script — that worklist item is now provisionally
deprecated pending charter amendment — and instead produced the intel needed
for a charter-amendment session to happen next.

Session character: began engine-class, became reference-class the moment the
target was invalidated. Legal under the engine/reference split (07-11b) but
should have been announced explicitly at the moment the pivot happened
rather than post-hoc; noted in hygiene ledger.

## State changes since the 07-11c checkpoint (verified)

1. **`harvest merge` NOT SHIPPED.** Worklist item 5 remains open but now
   provisionally deprecated pending charter amendment (see Rulings).
2. **Direction flip: from map/reduce split to recursive fold**
   [operator-proposed, session-agreed, ratification pending]. Detailed
   below and in Rulings.
3. **Two structural design pieces named** [operator-proposed, session-
   agreed]: the **router** (a Node-RED first-class actor that triages
   integrator output into downstream vs operator-escalation lanes) and
   the **index/shard split** (JJU's proven state model — small routing
   index + immutable range-named shards).
4. **JJU pipeline shape catalogued in paranoid detail** — see Ground
   truth. This is durable file state now; no future ctx needs cross-
   project access to know how JJU actually worked.
5. **Filing miss discovered and repaired mid-session.** Three of four boot
   docs (lexicon, diagram, checkpoint) on the mount at boot were stale
   copies from earlier points in the 07-11c session; final-copies were
   refiled after the manifest verification loop flagged them. Confirmed
   the primer's boot-manifest slot (schema v2.1) does its job on the
   first live run.
6. **Index/mount latency confirmed as a durable finding.** During the
   refile mid-session, mount lag showed the diagram absent even after
   the operator refiled — because `project_knowledge_search` had indexed
   the upload while `ls` on `/mnt/project/` hadn't caught up. This is
   filed as a new ground-truth item (naming pending; propose `W9` or
   similar in lexicon's warts register).
7. **Cross-project ctx move performed by the operator.** Ctx read JJU
   project knowledge directly; captured findings; returned to workshop.
   The extraction protocol worked but the move itself should be the
   rare exception, not the pattern — see hygiene and Rulings.

## Artifacts shipped this session (operator: download + file into workshop project)

1. `session_checkpoint_2026-07-12.md` — this file. First checkpoint dated
   07-12; ends with the schema-v2.1 boot manifest.
2. `merge_script_laymans_guide.md` — a scratch layman explainer of the
   merge script design I was advocating for. **DO NOT FILE.** It
   describes a design the session subsequently reversed on. Kept only as
   a link in this checkpoint's hygiene section for audit trail.
3. `jju_intel_request.md` — the prompt I wrote for a JJU-project ctx
   before the operator opted for the direct cross-project move instead.
   Preserved because the pattern (intel-request prompt to a separate
   ctx) is now the ratified default for future cross-project needs.
   File as reference material under `salvage/` or the equivalent.

No engine artifact. No reference-artifact patches at close, because the
reference layer is downstream of the pending charter amendment; patching it
now against a shape that hasn't been ratified would generate churn. Debt is
declared explicitly below.

## Rulings (this session)

- **`harvest merge` engine artifact NOT SHIPPED, target invalidated
  mid-session** [session-decided on evidence, operator-endorsed]. Provisional
  deprecation of worklist item 5 pending charter amendment; if the amendment
  ratifies the recursive fold, merge as a separate actor ceases to exist.
- **Direction flip proposed: recursive fold over map/reduce split**
  [operator-proposed, session-lean, ratification pending]. Detailed model:
  a single integrator worker per iteration reads accumulated state (index +
  arbitration file + touched shards) plus new span material and produces
  next-version state plus any escalations. Iteration IS the pipeline.
  Parallelism is *opt-in later*, at most an outer layer, never a
  reshape of the primitive. This matches JJU's proven pattern; the
  map/reduce split (charter §4 harvest row) does not.
- **Router as first-class actor** [operator-proposed, session-agreed,
  ratification pending]. A Node-RED node between the integrator's output
  and downstream: clean output → applier → state advances; escalations →
  operator queue → operator answers asynchronously → answers become
  durable state readable by the next iteration. This preserves charter §5
  "parked is terminal until a human looks" without collapsing into
  synchronous human-in-the-loop.
- **Index/shard split ratified as state model direction** [operator-
  proposed, session-agreed, ratification pending]. JJU's proven pattern:
  bounded index (routing table + status ledger) + range-named immutable
  shards containing per-canonical multi-line blocks. `@shards:[…]` tag on
  each index term line routes assembly. New rulings/deltas append to the
  current writable shard; earlier shards never touched.
- **`harvest_map_v1` and `harvest_residue_v1` provisionally downgraded to
  derivation ancestors** [session-lean, ratification pending]. Their
  intellectual content survives (identity law, evidence law, escalation
  format, arbitration discipline) and transfers to the integrator's
  design; their status as shipped current-set components does not, if
  the amendment ratifies. Neither artifact is edited or retired at this
  close — that's an amendment-session move.
- **Cardinal rule (no cross-project navigation) reaffirmed with narrower
  carve-out** [session-lean, ratification pending]: cross-project ctx
  moves remain forbidden as routine; the FIRST-CHOICE pattern for
  cross-project intel is **an intel-request prompt to a separate ctx in
  the target project, response relayed back**. The `jju_intel_request.md`
  produced earlier this session is the exemplar. Cross-project moves
  are last-resort only, formally accounted (session hygiene ledger
  entry each time), and produce a paranoid-detail intel dump like this
  checkpoint's Ground truth section. **Never let cross-project findings
  live only in transcript memory.**
- **Reference-doc debt DEFERRED to the amendment session** [session-
  lean]. Lexicon, diagram, primer amendments are all downstream of what
  the amendment ratifies; patching now against unratified proposals
  would inject churn. The debt is enumerated below and paid at
  amendment close.

## Ground truth learned this session

This section is the paranoid-detail catalog of what I learned about JJU's
actual harvest pipeline during the cross-project excursion. Read it as
reference material — everything here is evidence-grounded from artifacts
in the JJU project (`glossary_index_v31.md`, `glossary_arbitration_v31.md`,
`glossary_entries_<range>.md`, `harvester_prompt_v1.md`, `runbook.md`, and
the JJU source PDF itself). Nothing here is speculation; where I'm
uncertain, I say so.

### JJU pipeline shape (the fundamentals)

- **JJU harvest was sequential-stateful, not parallel-stateless.** Thirty-
  one sequential contexts, named ctx1 through ctx31. Version number of the
  aggregate index (`v31`) equals the context count. The final ctx (ctx31)
  produced version 31 of the index and arbitration files.
- **Each ctx harvested one "chapter-group"** (~5-10 sub-sections in the
  N-M section grammar). Example: ctx14 harvested chapter-group 22.0 SIT-UP
  GUARD, entries 22-0..22-4. Ctx boundaries were at chapter-group
  boundaries. Spans **did not overlap** in the "workshop workers overlap"
  sense; each ctx's span was the next non-overlapping chapter-group.
- **The book contains 41 chapter-groups.** Numbered 1-41. Ends at entry
  41-1. Chapter 41 is GUARD TOP / SUBMISSIONS. Chapter-groups themselves
  have essay preludes with prefix grammars: `intro:`, `surv-intro:`,
  `esc-intro:`, etc.
- **Every ctx read the accumulated prior state and appended.** The state
  it consumed: the current `glossary_index_v<N>.md`, the current
  `glossary_arbitration_v<N>.md`, and — critically — **only the shards
  its span cited**, paged in via the `@shards:[…]` routing tags. Not the
  full glossary. Bounded working state per iteration is what made 31
  sequential ctxs feasible without collapsing under context weight.

### The state model (index + shards + arbitration)

- **Index (`glossary_index_v<N>.md`):** the routing table + status ledger.
  Contains: (a) per-term index lines with `@shards:[…]` routing tags,
  (b) fan-out sense tables tracking multi-sensed canonicals, (c) a
  running context log (`ctx1: …`, `ctx2: …`, `ctxN: …`) recording each
  ctx's span, new canonicals, rulings, and reservation state. The index
  itself is bumped in version each ctx and is small enough to load
  fully.
- **Shards (`glossary_entries_<start>_to_<end>.md`):** the data. Range-
  named per the ctx's harvest span (e.g. `glossary_entries_22-0_to_22-4.md`).
  **Immutable in birth order** — content once written is never modified.
  New material for an old term goes in the CURRENT ctx's shard, and the
  term's `@shards:[…]` tag in the index is extended to include the new
  shard. This is JJU's answer to append-only integrity.
- **Arbitration file (`glossary_arbitration_v<N>.md`):** separate live
  document tracking open Q-tags across contexts. Bumped in version each
  ctx alongside the index. Each Q has a name (Q-mount, Q-brabo,
  Q-turtle, Q-guard-family, etc.), an evidence-both-ways trail, a
  status (OPEN / RESOLVED / TERMINAL), and per-ctx notes on whether it
  moved this iteration. Example: Q-mount opened in ctx1 (bottom sense
  homed at 3-0, top sense forward), stayed open for 27 iterations, and
  RESOLVED in ctx28 when chapter 37 (the mount top-attack chapter) came
  home.
- **Per-node ruling files** (`node_rulings_ctx-node-N.md`): separate
  artifacts from the NODE-BUILD stage, not harvest. Illustrative for the
  pattern but not part of harvest state. Filed for completeness.

### Per-canonical output format (the real shape)

Real JJU entries are **per-canonical multi-line blocks**, not per-sighting
single lines. Example verbatim from `glossary_entries_1-0_to_6-4.md`:

```
term       : the Scoop
canonical  : scoop
type       : position
aliases    : [Scoop, Scoop position]
sense      : low-weight back-defense posture; sink weight down to kill the
             opponent's attacking angle without moving the protective arm —
             Saulo's preferred escape platform from back control
locations  :
  - 1-2  [defined]
  - 2-4  [referenced]   # transitioned into from Back Survival after the
                        # all-fours roll
status     : confirmed
notes      : presented as Saulo's own development beyond traditional
             bridging back-defense.
```

Fields: `term` (surface form as source names it), `canonical` (snake_case
key), `type`, `aliases` (array of surface variants), `sense` (multi-line
prose), `locations` (list of `<N-M> [defined]|[referenced]|[destination]`
with optional trailing `#` notes per line), `status`
(`confirmed|reserved|tentative`), `notes` (multi-paragraph free-form,
cross-references to other entries and rulings).

**Fan-out sense tables in the index** track multi-sensed canonicals.
Example verbatim:

```
term   : the Mount / mount
type   : position, fan-out
status : RESOLVED — both senses [defined]
senses :
  - canonical: mount_bottom_survival   cue: "you're underneath the mount,
                                             surviving/escaping"           defined: 3-0   [CONFIRMED ctx1]
  - canonical: mount_top               cue: "you're on top, holding/attacking
                                             from mount"                   defined: 37-0  [CONFIRMED ctx28]
notes  : ctx1 only saw the bottom sense; mount_top came HOME at 37-0
         (ctx28) …
```

The workshop's designed wire grammar collapses each sighting to a single
line. JJU's real format collapses each canonical to a multi-line block
with ALL sightings inline. **These are different data models, not different
formats of the same data model.** The workshop's design has been implicitly
carrying an assumption about the shape of the output that doesn't match
JJU's shape.

### Cross-chunk resolution mechanisms

Three tagging protocols carry information across ctxs:

- **Q-tags** — named open arbitration questions. Opened when a ctx sees
  evidence that a term may be a fan-out / need an override ruling / etc.
  but doesn't have enough evidence to rule. Named memorably: Q-mount,
  Q-brabo, Q-turtle, Q-guard-family, Q-sc-escape-shape, Q-collar,
  Q-over-under, Q-base, Q-side-control, Q-knee-on-belly. Carried in the
  arbitration file across ctxs. Each ctx examines the queue and closes
  what it can with new evidence. Resolution is logged (evidence trail,
  ruling, method: "in-book" or "in-book + web" or "escalated"). At
  ctx31 four Qs remained OPEN but marked TERMINAL (no more chapters to
  provide evidence — the terminal Qs are handed to the downstream node-
  authoring context or the human, not to a future harvest ctx).
- **RESERVED status** — for terms whose home is expected later in the
  book. When ctx1 sees "the mount" in context 3-0 (bottom-survival
  sense) it can reasonably expect the offensive/top sense to be defined
  in the SUBMISSIONS chapters far downstream; that top sense is
  RESERVED. When the later chapter arrives and provides the [defined]
  home, the reservation is CONFIRMED. Not a Q — a coincidence-of-shape
  expectation, not an ambiguity.
- **[destination] tags** — for early-reference locations where a
  technique's endpoint refers to a not-yet-homed position. Example: a
  sweep at 15-2 that ends in the mount refers to `mount_top` while
  `mount_top` still has no [defined] home. Tagged `[destination]` on
  the sweep's line, not as a Q, just as a coincidence to eventually
  reassemble against the real home when it arrives.

**All three carry through immutable shards without editing them.** New
reservation-fulfillment lines get written in the current ctx's shard;
the index term line's `@shards:[…]` tag extends. Immutability preserved.

### What handled the "continuation without word repetition" case

The worry I raised earlier this session — a term defined on page 47 with
its definition continuing to page 48 without the word being repeated —
was framed against a **parallel-workers-with-narrow-spans** model. It
doesn't apply to JJU's actual pattern because JJU's ctxs are at
chapter-group boundaries, not page boundaries; the intra-chapter-group
continuation is entirely within one ctx's read. And cross-chapter-group
anaphora (a section referring to "the technique" where the name lives in
a different chapter-group) is handled by the reservation/destination
mechanism plus each ctx reading prior state fully.

**Under the recursive-fold design this transfers directly**: each
iteration reads accumulated prior state, so anaphora resolves through
state lookup, not through parallel workers reasoning about shared
context. The problem was an artifact of the wrong architecture, not a
gap in the right one.

### Cost / scale

- **Book size:** 41 chapter-groups, N-M sub-section grammar with essay
  prefixes preserved. Text-only ingest (photos stripped, personal-use
  license). Order of hundreds of pages, tens of thousands of tokens for
  the text.
- **Contexts:** 31 sequential harvest ctxs. Each ctx's working context
  = current index (small) + current arbitration file (small) + touched
  shards (few, per span citations) + span source text (a chapter-group
  worth, small). No full-glossary loads ever. Estimated per-ctx cost:
  ~100-200k input tokens + ~10-30k output. Not measured directly; rough
  extrapolation.
- **Total harvest cost estimate:** order 5M tokens ≈ $50-150 depending
  on model tier. Not measured; reference figure only.
- **Downstream stages** (registry, node-build, assembly) run additional
  ctxs; not catalogued here.

### What survives from the workshop's derivations, and what doesn't

- **Survives (intellectual content):** the identity law from harvest_map
  (transcribe-vs-infer, boundary discipline); the evidence law from
  harvest_residue (verdicts traceable to packet, no world-knowledge);
  the escalation format (≤10 lines, evidence both ways, stated lean);
  the arbitration discipline (name the question, in-book evidence
  first, web only for disambiguation-of-what-source-means, coin flips
  escalate). All of these transfer directly to the integrator worker's
  prompt.
- **Does not survive if amendment ratifies:** the specific split into
  map (per-span workers) + reduce (script merge + residue judge). The
  `harvester_prompt_v1.md`'s "each session appends" language matches
  the recursive fold; its actual structure is closer to what we should
  build than either `harvest_map_v1` or `harvest_residue_v1` is.
  Verbatim from `harvester_prompt_v1`: "Each session appends to
  `glossary_<slug>.md` and maintains a ≤15-line header: harvest cursor
  (where you stopped), open in-source questions, span log (one line
  per session)." That is a recursive-fold description.
- **Kit fixtures:** the residue kit's adversarial cases (fan-out,
  sense-drift, no_defined etc.) remain useful — the integrator has to
  handle those same cases, whichever architecture wraps around it. The
  map kit's fixtures similarly apply to any integrator that has to
  extract from a span.

## Dependency ledger (verified-how) — schema v2 slot

Workshop mount at boot 2026-07-12 (probe: `ls /mnt/project/`):

| Dependency | Role | Status | Verified how / when |
|---|---|---|---|
| `engine_charter.md` | law | ✓ present | `view`, 07-12 boot |
| `harvest_map_v1.md` | pending-ancestor (per this session's lean) | ✓ present | grep, 07-12 |
| `harvest_residue_v1.md` | pending-ancestor (per this session's lean) | ✓ present | grep, 07-12 |
| Both kit specs | pending-ancestor material | ✓ present | grep, 07-12 |
| `pipeline_config_schema.md` | law | ✓ present | grep, 07-12 |
| `harvester_prompt_v1.md` | recursive-fold reference | ✓ present | grep + read, 07-12 |
| `workshop_primer_v2.md` | boot procedure | ✓ present | `view`, 07-12 |
| `workshop_lexicon_v1.md` (07-11c final) | reference | ✓ present after mid-session refile | `view` early boot showed stale (07-11b); refile mid-session; verified via `project_knowledge_search` (index) |
| `session_checkpoint_2026-07-11c.md` (final) | boot chain | ✓ present after mid-session refile | same pattern as lexicon |
| `system_diagram_v1.html` (07-11c revision) | reference | ⚠️ **UNVERIFIED** on mount; project index has the 07-11c revision | `project_knowledge_search` confirmed the 07-11c banner exists in the index; last `ls` probe showed a diagram file missing (mount lag around refile); assume index truth, verify on next boot |
| `session_checkpoint_2026-07-10b.md` | boot chain depth | ✓ present | 07-12 |
| `session_checkpoint_2026-07-11.md` | boot chain depth | ✓ present | 07-12 |
| `session_checkpoint_2026-07-11b.md` | boot chain depth | ✓ present | 07-12 |
| `how_we_build_wikis_from_books.md` | orientation | ✓ present | 07-12 |
| **JJU project artifacts** | intel source (cross-project excursion) | consumed | `project_knowledge_search` on JJU project during cross-project ctx move, 07-12; catalog in Ground truth above; NEVER accessed from workshop mount |

Known-absent (unchanged, unblocking):
- Schemer master doc — carried through
- JJU source + `glossary_index_v31.md` etc. on WORKSHOP mount — deliberately absent (JJU is a separate project); intel now catalogued in this checkpoint
- `sources.md`, plain `session_checkpoint_2026-07-10.md` — carried through

## Propagation / blast-radius log — schema v2 slot

- **Recursive-fold direction (if ratified)** → touches:
  - **Charter §4** (harvest row): the map/reduce table entry gets
    replaced. "Recursive integrator" replaces "map = per-span
    extraction + reduce = merge script + residue pass." §4's overall
    map/reduce law survives at the STAGE level (registry, node-build,
    cards are still map/reduce shaped); harvest gets carved out as a
    per-stage exception.
  - **Charter §5** (runtime): router becomes a first-class named actor.
    Escalations get a named delivery mechanism (queue), not just a
    ≤10-line format.
  - **Charter §7** (file store): index/shard split gets added as the
    ratified state model for harvest, with the append-only rules made
    explicit.
  - **Charter §9** (worklist): item 5 (`harvest merge` script)
    retired. `harvest_map` and `harvest_residue` re-labeled as
    ancestors, not shipped current-set. New worklist item: the
    integrator prompt derivation.
  - **`pipeline_config_schema.md` §3.5**: `residue_heuristics`
    obsolete (no residue judge). `harvest.span_size` and
    `span_overlap` reinterpreted as chapter-group sizing hints, not
    parallel-worker parameters.
  - **`system_diagram_v1.html`**: H8 (harvest_map worker cluster), H9
    (merge), H10 (residue) collapse into a single integrator actor +
    a router node. Actor ledger rewritten.
  - **Workshop lexicon `v1`**: add `router`, `recursive fold`,
    `integrator (candidate term)`, `index/shard split`, `Q-tag`,
    `reservation`, `destination`, `index/mount latency` (as W9 or
    equivalent). Retire `merge script` if that ratifies. Retire
    `residue` and its cognates if the residue judge doesn't exist.
- **Router as first-class actor (if ratified)** → touches: Node-RED
  driver design (new node in the flow); escalation format (now
  operator's queue payload, not just an inline output shape); the
  runbook's human-loop description.
- **Index/shard split (if ratified)** → touches: pipeline config
  schema (new state-model section); driver file store (index +
  shards + arbitration file per-source paths).
- **No engine artifact shipped** → touches: this checkpoint (records
  the miss cleanly); the reference layer (no patch owed, because
  there's no engine change to record).

## Open design questions (register) — schema v2 slot

Carried forward from 07-11c:
- **Reference-layer FORM** — unchanged, unresolved. Prose vs
  mechanically-consistent graph. W1 still the standing exhibit; W9
  (index/mount latency, this session) is a related exhibit for
  hand-synced state failures.
- **Output shape** (vault + Anki inherited, not chosen) — unchanged.
- **Prompt-via-failures method** — unchanged. May be reshaped under
  recursive fold.
- **`residue_heuristics` membership** — obsolete if amendment
  ratifies; otherwise still config TBD.
- **Reference-artifact version suffix** — unchanged, unresolved.

New this session:
- **Recursive fold vs map/reduce split for harvest** — the top item.
  Ratify in the amendment session or overturn with reasoning.
- **Router escalation queue format and asynchronous UX** — what does
  the operator's queue look like? Web UI? Email? Slack? File watchers?
  The escalation FORMAT (≤10 lines) is settled; the DELIVERY is not.
- **Integrator prompt design** — one prompt or a mode-parameterized
  family? How much of `harvester_prompt_v1`'s language transfers
  literally vs needs generalization? How does content_mode (§3.5)
  interact?
- **Parallelism topology within recursive fold** — sequential-only
  first (proven mode) or intra-iteration parallelism (multiple
  workers on sub-spans within a chapter-group, folded into state
  before next iteration)? Charter §5 says "batch API is the default
  lane"; that pressures for at least some intra-iteration parallelism.
- **Fate of already-shipped `harvest_map_v1` and `harvest_residue_v1`**
  — retain as formally-ratified ancestors (a lexicon "prior art / not
  current" entry), retire, or fold their content into the integrator
  derivation session? Amendment session's call.
- **Terminal Q handling** — in JJU some Qs remained OPEN at the end
  because the book didn't provide the evidence. Handed off to the
  downstream node-authoring or human. What's the automated pipeline's
  equivalent? The router's escalation lane, presumably, with a
  status of "terminal at harvest close."

## Reference-doc debt — schema v2 slot

- **Deliberately NOT applied at this close.** The lexicon, diagram,
  and primer amendments all depend on which direction the amendment
  session ratifies. Patching now against unratified proposals would
  inject churn on a scale that violates the lockstep discipline. If
  the amendment session next ratifies, all patches happen at that
  close; if it overturns, no patches needed here anyway.
- **Enumeration of what's owed (for the amendment session's use):**
  lexicon adds — `router`, `recursive fold`, `integrator (candidate)`,
  `index/shard split`, `Q-tag / reservation / destination`,
  `index/mount latency (W9)`, `intel-request prompt (protocol)`;
  lexicon retirements — `merge script`, `residue judge / residue pass`,
  `merge kit` (all conditional on ratification). Diagram — H8/H9/H10
  collapse into one integrator actor + new router node; actor ledger
  rewritten. Primer — cross-project excursion clause tightened
  (intel-request-first, cross-project-move as last resort with
  paranoid-detail checkpoint mandatory); index/mount latency added
  to boot procedure (prefer `project_knowledge_search` for version
  verification during and shortly after refile). Charter — §4/§5/§7/§9
  amendments as enumerated in the blast-radius log.

## Recommended next session

**Charter amendment session.** The one artifact of the session is a
charter amendment file (`engine_charter_amendment_v1_2.md` or similar
numbering) that ratifies (or overturns) the direction lean of this
session. Deliverables:

- Amendment text formally proposing (a) recursive fold for harvest,
  (b) router as first-class actor, (c) index/shard split as state
  model, and (d) fates of merge script + harvest_map + harvest_residue.
- Ratification decision on each item (operator).
- The full reference-doc debt above, applied at close (lockstep).
- Next-session-recommendation update (probably: integrator prompt
  derivation).

Boot: paste `workshop_primer_v2.md` → run verification loop against
the boot manifest below → workshop_lexicon_v1 (07-11c) → system_diagram_v1
(07-11c; note the mid-session refile — verify via changelog/banner,
prefer `project_knowledge_search` if `view` shows stale) → this
checkpoint → 07-11c checkpoint (depth) → engine_charter + v1.1 amendment.
Also read: `harvester_prompt_v1.md` (the recursive-fold ancestor),
`harvest_map_v1.md` + `harvest_residue_v1.md` (pending-ancestor
material), `how_we_build_wikis_from_books.md` (orientation).

The amendment session should specifically NOT try to derive the
integrator prompt itself. That's the session after. This one settles
what the pipeline IS; the next one builds against the settled shape.

## Session hygiene / corrections ledger (own errors)

Several this session, several load-bearing. Naming them:

- **BIG ONE: architectural advocacy on unproven foundation.** I
  advocated for the merge script design with confidence I did not have
  evidence for. My evidence base was the workshop's aspirational
  documents (charter §4, the map/reduce diagram); I treated them as
  ratified engineering practice when they were ratified aspirations
  with zero end-to-end test. When the operator raised brittleness
  intuition, I steelmanned it structurally but kept advocating for
  the design because "the charter said so." The charter said so
  based on ratifying an aspiration. This is the correction: **for any
  load-bearing design call, name explicitly what evidence supports it
  and where the evidence gaps are, before advocating.** In practice:
  a design that's never been run end-to-end is a hypothesis; label it
  as such in the design's own text.
- **Pattern-matching error on operator's proposal.** When the operator
  said "recursive," I heard "pairwise tree reduction" (a CS pattern I
  knew) and steelmanned that. The operator meant "recursive fold" (a
  different pattern), which is what JJU actually does. I should treat
  operator's intuition as **data**, not translate it into the nearest
  CS pattern I know and then defend or attack the translation. The
  correction: when the operator's proposal doesn't fit a known
  pattern, ASK what shape they mean rather than assuming.
- **Cardinal rule break: cross-project ctx move.** Operator-initiated,
  legal only as a rare exception. I did write an intel-request prompt
  earlier in the session (the correct pattern), then agreed to the
  ctx-move when the operator escalated. I should have said more
  forcefully: "let's stay with the intel-request-to-separate-ctx
  pattern; that's what it's for." The Ruling now codifies this: intel
  request is the default; cross-project ctx move is the last resort,
  formally accounted, and produces a paranoid-detail intel catalog in
  the resulting checkpoint (which this document is).
- **Session character shift not announced.** Session was chartered as
  engine-class (merge script). When the target was invalidated
  mid-session, it should have been announced as pivoting to reference-
  class ("this session is now producing a checkpoint + intel catalog,
  not an engine artifact"). Instead I kept working the design surface.
  Correction: the moment a chartered target is invalidated, the ctx
  should announce the character change explicitly and reframe
  deliverables. This is now written down.
- **Filing miss (three docs stale on mount at boot).** Not my error —
  the operator's filing gesture at the previous close missed the final
  copies. But: the manifest verification loop caught it on first live
  run, which is the intended behavior. Recorded as evidence that
  schema v2.1 (boot manifest slot) is doing its job.
- **Index/mount latency confirmed.** Second observation this session
  (first was the sibling-ctx boot failure catalogued in 07-11c). Now
  a durable finding: `project_knowledge_search` and the `/mnt/project/`
  mount have different freshness windows during and shortly after
  refile. The `ls` probe is not a reliable version check in that
  window. Adopting `project_knowledge_search` for content-marker
  verification during that window is the mitigation.
- **This checkpoint is 4x the length of a typical one.** Deliberate —
  the JJU findings needed paranoid detail to survive as file-durable
  state. The alternative is another cardinal-rule break next time.
  Length is honest cost of the rule-break we just did; better to pay
  it once here than every time a future ctx needs the same intel.

## Boot manifest — schema v2.1 slot (pins the next boot)

Verify each doc by opening it and matching the content-level marker.
Filenames alone are never version evidence.

| Doc | File | Content-level revision marker |
|---|---|---|
| primer | `workshop_primer_v2.md` | header: "Workshop Session Primer — v2, issued 2026-07-11c" |
| lexicon | `workshop_lexicon_v1.md` | last changelog line dated "2026-07-11c (post-close addendum, operator-directed)" |
| diagram | `system_diagram_v1.html` | banner ends: "Revised 2026-07-11c: `harvest_residue` PLANNED → RATIFIED…"; HRES actor ledger row = RATIFIED |
| checkpoint (this session) | `session_checkpoint_2026-07-12.md` | this file; newest date-suffix on the mount at time of writing; ends with this boot manifest |
| checkpoint (prior for depth) | `session_checkpoint_2026-07-11c.md` | ends with the schema-v2.1 boot manifest table |

Mismatch → primer v2's rules: older than manifest = flag before work
(the manifest is authoritative for the pinned copy); newer = find the
later checkpoint and re-anchor; stale primer = hard stop.

**Extra verification note for next boot** (from this session's index/
mount latency finding): if `view` on any boot doc shows a stale copy
but `project_knowledge_search` on a distinctive phrase from the marker
returns a hit, trust the index — the mount is lagging, not the truth.
Proceed after logging the lag observation.
