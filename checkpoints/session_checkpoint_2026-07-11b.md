# Session checkpoint — 2026-07-11b (workshop, harvest_map derivation)

Purpose: boot file for the next session. Files are the only memory; this file
plus the artifacts below is everything this session knew that matters. Reads
alongside the 2026-07-11, 2026-07-10b, and 2026-07-10 workshop checkpoints;
supersedes none of them. **First checkpoint written in the proposed schema v2**
(new slots: dependency ledger with verified-how, propagation log, open-design
register, reference-doc debt). The schema is dogfooded here and proposed for
ratification in the last section.

Context note: workshop project throughout. The mid-session engine-spine
absence was caused by the operator hopping this ctx across projects to let
Claude sample them — not data loss. Ruling below: don't do that; the mount
reflects only the chat's own project.

## What this session was

The `harvest_map_v1` derivation the 07-11 checkpoint queued. Shipped the engine
artifact and its sealed kit spec. The session also ran a file-recovery
firefight (the spine was off the mount for several turns), deepened the residue
design against CS prior art, and produced four ratified changes to how the
workshop itself operates.

Under the OLD single-artifact rule that spread is a violation. Under this
session's **engine/reference split** (ratified below) it is not: the one engine
artifact is `harvest_map_v1` (+ its kit); everything else is the session's
*record*, which every session owes by definition.

## State changes since the 07-11 checkpoint (verified)

1. **`harvest_map_v1` SHIPPED** — the 07-11 NEXT target is built. Real
   subtraction from `harvester_prompt_v1` (verified against the authoritative
   mount copy, not the in-context copy). Contains: the transcribe-vs-infer
   identity law with two-sided examples (incl. the four-fins case); boundary
   doctrine (size-agnostic worker, `whole|head-cut|tail-cut` flag); output wire
   grammar; five mode blocks (`prose|tabular|dialogic|code_listing|mixed`);
   the downstream contract (interval join key, `defined` > `ref`, `whole` >
   partial, overlap-floor precondition). harvest_residue is **not** built here
   by design.
2. **Kit spec SHIPPED — 4 of 8 spans concrete.** Sailing 4 fully specified with
   line-ranges (alias chain / Beaufort table / procedure-pure knots / two-regime
   exhibit). Schemer 3 + jju regression 1 are `[PENDING]` — failure modes named,
   line-ranges blocked on absent sources (see ledger). Answer keys + packets +
   scorer script are an ops build per the dev/ops split; not authored here.
3. **Two carried leans RATIFIED** (lose lean status): span-sizing =
   parameterize; residue scope = separate later session + downstream-contract
   note only. Both [operator-decided].
4. **Four workshop-governance rulings** (next section).
5. **Platform ground-truth**: navigate ≠ remount; refile = remount (details in
   Ground truth).

## Artifacts shipped this session (operator: download + file into workshop project)

1. `harvest_map_v1.md` — **engine artifact.** Stage 1 map-phase worker prompt.
2. `harvest_map_v1_kit_spec.md` — companion kit spec (4/8 concrete).
3. `session_checkpoint_2026-07-11b.md` — this file (reference artifact).

## Rulings (this session) — all [operator-decided]

- **Span-sizing lean → RATIFIED as stated.** `span_size`/`span_overlap` stay
  config dials (RESERVED, charter §10); the worker carries boundary doctrine;
  kit sizes are fixture-not-policy; the kit later measures real sizes.
- **Residue scope lean → RATIFIED as stated.** `harvest_residue` is its own
  later session with its own kit; `harvest_map_v1` only ends with the
  downstream-contract note.
- **Single-artifact rule → REPEALED; REPLACED by the engine/reference split.**
  One *engine* artifact per session (a worker prompt, schema, script — the thing
  the session is *for*). *Reference* artifacts (the annotated graph/diagram, the
  lexicon, the checkpoint) are the session's record and ride along with every
  session by definition — they are not "second artifacts." Rationale: the graph
  must be living in the strictest sense, moving in lockstep with every change to
  Repetae (workers or Node-RED) or it inverts from asset to liability; lockstep
  is also what carries a ctx's hard-won realizations across the jump to the next.
- **Lexicon update cadence.** Optional-to-*add* per ctx, at discretion, based on
  how the model has matured — no obligation most sessions. MANDATORY the moment a
  term is coined or redefined in an artifact (an un-minted used term is a W-class
  defect). Pairs with vocabulary discipline: flag terms at point of use; the
  flagged set is the session-close lexicon delta.
- **Boot / cross-project procedure.** The mount reflects only the chat's own
  project and does not follow UI navigation; do not source-sample other projects
  by hopping ctx mid-session — file the material in or attach it. Retain a cheap
  per-dependency existence probe at boot, **weakened from halt to flag** (the
  reference-file check is insufficient; it passed while the whole spine was
  absent).
- **Reference-layer investment — principle RATIFIED, form OPEN.** RATIFIED: the
  reference layer is worth funding as the system scales to commercial size;
  content growth (terms, edges, actors) is linear-and-worth-it. OPEN (see
  register): its *form*. Hand-synced prose has pairwise, super-linear
  maintenance cost — W1 is the first contradiction already surfaced at four docs.
  The investment is only safe in a form where consistency is mechanical, not
  remembered.

## Ground truth learned this session

**Platform.**
- **navigate ≠ remount; refile = remount.** Moving the UI to another project
  left the mount byte-identical; re-filing into this chat's own project
  refreshed it within the ctx. The mount tracks the chat's own project only.
- **A green `✓` was false on disk.** The 07-11 "all dependencies green" line
  asserted belief, not verification — the entire engine spine was off the mount.
  A checkmark must mean "resolved on disk this session," hence the verified-how
  ledger below.
- **The catch is a per-file probe**, not "is the mount empty." The reference-file
  check passed; testing each *declared dependency path* is what surfaced the gap.

**Design grounding** `[model-knowledge, unverified]` — CS prior art that shaped
the residue design; informs the build, asserts nothing about any source:
- **Halo / ghost-region (domain decomposition).** Overlap ≥ the largest single-
  entity footprint makes every entity seen whole by ≥1 worker; boundary cuts then
  collapse into ordinary dedupe. Overlap is a **correctness floor**, not just an
  efficiency dial — this is now the contract's precondition.
- **Shotgun assembly / OLC-consensus.** Merge = an idempotent sweep-line interval
  join (sort by loc, cluster by term-key over overlapping intervals, union
  evidence, `defined` > `ref`, `whole` > partial). The analogy breaks exactly
  where text has no single truth-per-position: fan-out / sense-drift are
  *semantic* leftovers overlap can't kill — that irreducible set is residue's
  entire input, which is why it can't be swept into the dumb script.

## Dependency ledger (verified-how) — schema v2 slot

| Dependency | Role | Status | Verified how / when |
|---|---|---|---|
| `harvester_prompt_v1.md` | derivation ancestor | ✓ present | `view` on mount, 07-11 (3971 B, matches in-ctx) |
| `engine_charter.md` (+ amendment) | law | ✓ present | mount `ls`, 07-11 17:13 |
| `pipeline_config_schema.md` | schema surface | ✓ present | mount `ls`, 07-11 17:19 |
| `discovery_prompt_v2_4.md` | mode enum, axes | ✓ present | mount `ls`, 07-11 17:14 |
| `discovery_sailing-..._SALVAGE.md` | sailing kit spans | ✓ present | in-ctx + mount; 4 spans specified |
| `harvest_brief_little-schemer.md` | Schemer failure modes | ✓ present | mount `ls`, 07-11 17:11 |
| **Schemer master discovery doc** | **3 kit nominations** | **✗ ABSENT** | not on mount; only the brief is |
| **JJU source + `glossary_index_v31.md`** | **jju regression span + key** | **✗ ABSENT** | BJJ project; not on workshop mount |

Bare `✓` is retired; every line states its verification.

## Propagation / blast-radius log — schema v2 slot

Design calls ratified this session and what each touches (the edges the next
session inherits, not just the decision):

- **Span-sizing = dial + boundary doctrine** → touches: the prompt (boundary
  section + `boundary:` field); schema §3.5 (confirms `span_size`/`span_overlap`
  stay TBD); the future merge script (must read `boundary:`); the future residue
  node (its trigger); the driver (owns slice position, reads size from config);
  the kit (becomes the size-measuring instrument); diagram hops H6/H8.
- **Residue = separate + contract note** → touches: the prompt's closing
  contract; the future merge/residue split derives against a stated interface;
  schema §3.5 `residue_heuristics` (fan_in/fan_out/sense_drift fall out of the
  merge-can-prove line); diagram hop H9.
- **Single-artifact repeal → engine/reference split** → touches: the primer
  (rule text), lexicon §3 (session vocabulary), and the checkpoint format itself
  (this file rides along legally under it).
- **Lexicon cadence** → touches: primer (vocabulary discipline = flag-at-use →
  session-close delta), lexicon changelog protocol.

## Open design questions (register) — schema v2 slot

- **Reference-layer FORM** — prose docs (super-linear maintenance, drift-prone;
  W1) vs. a single mechanically-consistent graph the lexicon/checkpoint read
  *from*, lint-checkable for drift. **Highest-value open item from this ctx.**
  Principle (fund it) is ratified; form is unresolved.
- **Output shape** — vault + Anki is inherited from the BJJ build, not chosen.
  Worth a deliberate look before more machinery hardens around it. Not this
  session's business; flagged as strategy.
- **Prompt-via-failures method** — write a crude prompt, run it on hard kit
  spans, let failures write the real prompt. Unratified methodology change; an
  ops activity (dev holds no answer keys). Re-present if kit work is next.
- **Single-artifact carve-out / "infrastructure session" type** — largely
  resolved by the engine/reference split above; any residue folds into the W1
  housekeeping session.

## Reference-doc debt (owed to honor the lockstep ruling) — schema v2 slot

Not yet applied at time of writing (offered at session close):
- **`workshop_lexicon_v1.md`**: mint `boundary doctrine`, `downstream contract`
  (interval-key form), `engine artifact` vs `reference artifact`, `blast-radius
  trace`; consider `halo/overlap-floor`, `OLC merge`. Record the four rulings.
  §8: `harvest_map` NEXT → shipped engine artifact; add kit-spec row. Changelog
  line.
- **`system_diagram_v1.html`**: recolor `harvest_map` NEXT → RATIFIED; annotate
  the merge→residue hop with the downstream contract; ledger + undesigned-
  inventory refresh (residue still PLANNED).
- **`workshop_primer_v1.md`** (a versioned event — deserves a clean pass):
  replace the single-artifact rule with the engine/reference split; add the
  cross-project/boot-probe procedure; state vocabulary flag-at-point-of-use.
- **This checkpoint schema** — ratify v2 (below) or keep proposed.

## Recommended next session

**`harvest_residue` derivation** — the natural engine continuation: the
downstream contract was just built to enable it, and keeping momentum on engine
artifacts is the check against the meta-layer outgrowing the machine. Strong
alternative: the **reference-layer-form design session** (the highest-value open
question). Either way, **land the lexicon + diagram lockstep patches first** (the
two living docs the ratified rule most directly governs) — offered at this close
so they don't wait.

Boot: paste `workshop_primer_v1.md` → read lexicon + diagram → this checkpoint
(+ 07-11 / 07-10b for depth). If `harvest_residue`: dependencies are the
downstream contract in `harvest_map_v1.md` (present) + the charter's map/reduce
law; no absent sources block it.

## Session hygiene / corrections ledger (own errors)

- **Boot dependency miss.** Proceeded through boot and outline design working
  from in-context file copies without verifying the declared engine-spine
  resolved on disk; the gap (whole spine absent) surfaced only when the ancestor
  was needed. Cause was partly operator ctx-hopping, but the probe that would
  have caught it did not run → retained as boot procedure.
- **Vocabulary.** Used `boundary doctrine` and the interval-key contract
  specifics before minting them; flagged only near session end, not at point of
  use → lexicon delta owed.
- **Near-miss.** Initially framed "collapse the meta-docs" in a way that read as
  cutting the reference layer's *function*; operator pushback corrected it to
  collapse-*form*-not-function. Recorded so the distinction isn't re-collapsed.
- **Ambiguity.** Resolved "sound advice lets apply it" by sorting the four
  suggestions rather than asking; defensible (the two leans were separately and
  explicitly confirmed), but it is a primer clarify-trigger phrase.

## Proposed checkpoint-schema v2 (dogfooded above)

The old format had no home for several things every session actually owes, so
they evaporated between sessions — which is how the "all green ✓" line was
possible. v2 adds four slots, all exercised above:

1. **Dependency ledger with verified-how** — replaces bare `✓`; each dependency
   states how and when it was verified on disk.
2. **Propagation / blast-radius log** — each ratified design call plus the edges
   it touches, so the next session inherits the impact map, not just the verdict.
3. **Open design questions register** — distinct from leans; the live forks with
   status, so the big unresolved questions can't quietly vanish.
4. **Reference-doc debt** — what this session owes the lexicon/diagram/primer, so
   lockstep (the new engine/reference ruling) is auditable rather than hoped-for.

Retained from v1: what-this-was, state changes, artifacts, rulings (provenance-
tagged), ground truth, recommended next, hygiene/corrections ledger.

Status: **proposed.** This checkpoint is the first instance. Ratify at the next
session start, or amend the slots first.
