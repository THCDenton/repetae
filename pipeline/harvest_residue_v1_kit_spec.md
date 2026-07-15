# Harvest Residue v1 — sealed kit spec

Purpose: the adversarial test kit for `harvest_residue_v1.md`, per charter
§8. Same anatomy as the harvest_map kit — prompt file (shipped), paste-ready
packet per item, sealed script-derived answer key, scorer — with one
structural difference: **fixtures are residue items (merge-output clusters),
not raw spans.** A residue fixture is a hand- or script-assembled
`===== RESIDUE ITEM =====` block whose sightings are drawn from real map
output where available, and synthesized to the wire grammar where the map
kit has not yet produced fixtures. Synthesized sightings are stamped
**fixture-not-policy** like every provisional kit value.

Hard items only; easy items passing proves nothing. The set below is chosen
so that every verdict in the enum (`union | split | distinct | escalate`)
has at least one item whose *correct* answer is that verdict — a residue
pass that unions everything, or escalates everything, must fail the kit.

## Items (7): sailing 4 · Schemer 2 · jju regression 1

### Sailing (4) — specifiable now · source `discovery_sailing-for-dummies_SALVAGE.md`

1. **`res:sail:dinghy` — source-numbered fan-out with stray refs.** The
   source itself numbers two senses ("dinghy: (1) a sailboat with a
   centerboard…; (2) a small rowboat" — salvage, defined-entries exhibit).
   Fixture: the numbered-sense `defined` sighting plus ref-only sightings
   of `dinghy` from other locations whose context matches sense (1) only.
   **Correct verdict: `split`**, source numbering kept, refs attached to
   the right sense. **Tests:** split mechanics + not flattening a stated
   sense table. Key from the salvage exhibit text.

2. **`res:sail:rudder_debris` — figure-label debris polluting a real
   entry.** The salvage records ~793 short capitalized lines where real
   headings and figure-label debris (`Rudder`, `Keel Bulb Rudder`) are
   lexically indistinguishable; map workers will emit some as near-empty
   sightings. Fixture: one honest `defined` sighting of `rudder` + two
   debris sightings (empty-sense refs, one of them `head-cut`).
   **Correct verdict: `union`** — debris discounted as evidence, kept as
   ref locations, sense taken wholly from the defined sighting.
   **Tests:** the discount-but-never-drop rule; no sense contamination.

3. **`res:sail:two_regime` — the E1/E2 exhibit, an engine question in a
   residue costume.** The source states two coexisting rule regimes
   (p.281, salvage line 10121): rules of the road for all boats, Racing
   Rules for racers, overlapping rather than partitioning. Fixture: right-
   of-way sightings whose senses genuinely clash across the regimes.
   **Correct verdict: `escalate`** — the split-vs-union answer depends on
   per-region configuration (E1/E2), which is a charter-class open
   question no session may silently decide. **Tests:** the un-escalated
   coin-flip failure class — the single most important item in the kit; a
   confident `split` here fails critically.

4. **`res:sail:windward_leeward` — false-positive fan-out.** E1's
   evidence: `windward`/`leeward` appear 7× in Ch.13 vs 80× elsewhere;
   the racing region differs by rules, not geometry. Fixture: sightings
   from racing and non-racing chapters, senses phrased differently but
   describing the same geometry. **Correct verdict: `union`** (per the
   recorded E1 lean: no role split). **Tests:** resisting a
   region-flavored split when the sense evidence says one entity.

### Schemer (2) — `[PENDING]` sightings · brief present, master doc absent

The failure modes are fixed by the brief's naming weather; the fixture
sightings need real map output or the master discovery doc's nominated
passages, neither on the workshop mount.

5. **`res:schemer:rember_star` — significant-suffix false fan-in.**
   Merge's alias/similarity heuristic flags `rember` vs `rember*` as a
   fan-in candidate. The brief rules the trailing `*` significant:
   different entities. **Correct verdict: `distinct`, citing the brief.**
   **Tests:** distinct-by-law suffixes; the flag-is-not-evidence rule.

6. **`res:schemer:drift` — layered redefinition.** A function is revised
   across chapters ("capture each definition, let merge consolidate" —
   brief); merge flags `sense_drift`. Fixture: three `defined` sightings
   of one function at increasing sophistication. **Correct verdict:
   `union`** with the most complete teaching as the sense and earlier
   definitions retained as refs. **Tests:** drift consolidation without
   inventing a composite sense the source never states.

### jju regression (1) — `[PENDING]` · BJJ prior art, not on this mount

7. **`res:jju:fanout_regression` — regression against v7's resolved
   fan-outs.** Glossary builder v7 resolved real fan-outs into the frozen
   `glossary_index_v31.md`; charter §4 says this pass inherits that
   machinery. Fixture: reconstruct one hard v7 fan-out as a residue item
   (sightings back-derived from the frozen entry's locations); answer key
   = the frozen entry itself. **Tests:** the generalized pass reproduces
   the ancestor's known-good resolution. Assembled in the BJJ project,
   per the dev/ops split.

## Scorer

Parses the three sentinel blocks and compares to the sealed key. Scored
classes:

- **verdict errors** — wrong verdict for an item (union where the key says
  split, etc.). A `distinct` where the key says `union` scores as an
  ordinary verdict error (recoverable over-split); a `union` where the key
  says `distinct` or `split` additionally counts as a **false merge**,
  reported separately — it is the unrecoverable direction.
- **scope violations (CRITICAL — any nonzero count fails the run):** a
  ruled verdict where the key says `escalate` (the silent coin flip);
  world-knowledge or cross-source justification powering a verdict; a
  sense line containing content absent from every sighting and slice; a
  coined type; any reference outside the packet.
- **sense fidelity** — merged sense lines must be assembled from sighting/
  slice text; scored by containment, not paraphrase-similarity.
- **lint** — verdict-line grammar; merged-line / split-form grammar; no
  `boundary:` surviving into glossary lines; ruling ≤6 lines; escalation
  ≤10 lines with evidence both ways AND a stated lean; sentinel match;
  queue order preserved.

Answer keys are script-derived and sealed — never pasted into an ops chat.
Every ops run's raw output is kept as a fixture; residue fixtures double as
future merge-script test inputs (the intake grammar is shared).

## Kit status

- **Prompt** `harvest_residue_v1.md` — shipped this session.
- **Items** — 4 of 7 specifiable from material on the workshop mount
  (sailing salvage); 2 blocked on Schemer map output or the master
  discovery doc; 1 blocked on BJJ prior art (assemble in that project).
- **Answer keys + paste-ready packets + scorer script** — **ops build**,
  per the dev/ops split. The workshop specifies items, correct verdicts,
  failure modes, and scorer definition; ops assembles sealed keys against
  material the workshop does not hold. Not authored here.
- **Dependency note:** fixtures ideally use real `harvest_map_v1` output;
  the map kit has not run yet, so sailing items may be synthesized to the
  wire grammar (stamped fixture-not-policy) and later replaced by real
  fixtures once the map kit produces them.
