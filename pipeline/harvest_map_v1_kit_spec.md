# Harvest Map v1 — sealed kit spec

Purpose: the adversarial test kit for `harvest_map_v1.md`, per charter §8. A
kit is the prompt file (shipped), a paste-ready packet per span, a **sealed**
script-derived answer key (never pasted into an ops chat), and a scorer. Hard
spans only — easy spans passing proves nothing.

**Span-size note.** Every span below carries a provisional line-range **stamped
fixture-not-policy**: a test fixture chosen to exercise a failure mode, not the
source's official `span_size` (RESERVED, charter §10). The kit is the
instrument that later *measures* real sizes.

## Spans (8): sailing 4 · Schemer 3 · jju regression 1

### Sailing (4) — fully specified · source `discovery_sailing-for-dummies_SALVAGE.md`

1. **`sail:1000–1100` (Ch.1, page:13–15) — conditional alias chain.** The
   book's highest alias density. `keel` / `centerboard` (retracts vertically) /
   `daggerboard` / `leeboard` (side-mounted) are named, renamed, and
   conditionally renamed in one breath. **Tests the identity law:** does the
   worker hold the chain as **four distinct entities with stated conditions**,
   or falsely collapse four underwater fins into one node? Mode: prose.

2. **`sail:5647–5720` (Ch.8, page:153–155) — Table 8-1, Beaufort scale.** The
   flagship structural failure: flattened columns, cells wrapping across lines,
   and a running head (`154 Part II: Casting Off…`) injected *inside* the table
   body. **Tests tabular mode:** does the worker strip the residue and harvest
   legible terms **without hallucinating** the destroyed table structure?
   Mode: tabular.

3. **`sail:12761–12800` (Ch.19, page:367–368) — procedure-pure knots,
   figure-dependent.** Alias-dense (`round turn and two half hitches` as a
   distinct entity; `two half hitches` = `double half hitch`), and the tying
   steps for at least one knot exist **only in the absent figure** ("Check out
   Figure 19-6 to tie…"). **Tests graceful degradation:** a `knot` node with an
   honestly empty procedure, or invented steps? Mode: mixed (prose + procedure
   with absent-figure gaps).

4. **`sail:10106–10135` (Ch.13, page:281) — two-regime exhibit.** One sentence
   names both rule systems and marks which rules belong to which ("in force
   under the rules of the road… and the Racing Rules…"). **Tests
   transcribe-vs-infer on a stated distinction:** record the two regimes **as
   the source states them**, without inferring a merge or a resolution. Directly
   exercises escalations E1/E2. Mode: prose.

### Schemer (3) — PENDING exact spans · source: Little Schemer master discovery doc (not on mount)

The Schemer master discovery doc, which holds the ratified kit nominations, is
not currently on the mount; only the harvest brief is. The three failure modes
below are reconstructed from the brief's naming-weather and are the **intended**
targets — exact line-ranges must be filled from the master doc (or re-nominated
in a Schemer ops session) **before the kit is sealed**.

5. **`schemer:[PENDING]` — trailing-`*` significance.** `rember` vs `rember*`
   are different entities (list-of-lists variant). **Tests:** suffix-distinct
   names kept distinct, never merged on visual similarity. Mode: dialogic +
   code_listing.

6. **`schemer:[PENDING]` — `-f` / `-g` higher-order variants.** `insertL-f`,
   `insert-g` are distinct entities. **Tests:** distinct-variant discipline
   across a family of near-identical names. Mode: dialogic + code_listing.

7. **`schemer:[PENDING]` — OCR repair + definition built across Q&A.** Code OCR
   lies (`( cdr` → `(cdr`; `atom ?` → `atom?`), and a function's definition is
   assembled across a dialogic exchange. **Tests:** repair the closed
   substitutions without dropping terms, and attribute the sense to what the
   exchange teaches. Mode: code_listing + dialogic.

### jju regression (1) — PENDING span + answer key · source: BJJ prior art (not on mount)

8. **`jju:[PENDING]` — regression against the frozen glossary.** One hard span
   from the JJU source, answer key derived from the frozen
   `glossary_index_v31.md`. **Tests regression:** the generalized `harvest_map`
   must not lose recall or precision versus the BJJ-era ancestor's known-good
   output on established content. The JJU source and frozen glossary are
   read-only prior art in the BJJ project, not on the workshop mount; this span
   and its script-derived key must be assembled there.

## Scorer

Parses each `===== HARVEST … =====` block and compares wire lines to the sealed
answer key. Four scored classes:

- **recall misses** — named things in the key the worker did not emit.
- **precision inventions** — things the worker emitted that are not in the
  source (hallucinations, invented table structure, fabricated procedure steps).
- **scope violations (CRITICAL)** — any inferred identity: a false merge of
  distinct entities; "same as" / "probably" / cross-span recall language; a
  coined type; any claim not legible in the span. **Any nonzero count fails the
  span outright**, regardless of recall / precision — this is the failure the
  decomposition exists to prevent.
- **lint** — wire-format conformance: line grammar, a `type` from the source's
  declared set, a legible in-span `loc`, a valid `boundary` value, sentinel
  match.

Answer keys are **script-derived and sealed** — never pasted into an ops chat,
so a worker cannot read its own key. Every ops run's raw output is kept as a
fixture.

## Kit status

- **Prompt** `harvest_map_v1.md` — shipped this session.
- **Spans** — 4 of 8 fully specified (sailing); 4 of 8 blocked on absent
  sources (Schemer master doc; JJU prior art). Failure modes named; line-ranges
  `[PENDING]`.
- **Answer keys + paste-ready packets + scorer script** — **ops build**, per
  the dev/ops split: the workshop specifies spans, failure modes, and scorer
  definition; ops assembles the sealed key against material the workshop does
  not hold. Not authored here.
