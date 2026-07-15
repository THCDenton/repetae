# Discovery — sailing-for-dummies (Sailing For Dummies, 2nd Edition)
Status: conventions ratified 2026-07-09, discovery_prompt_v2.

SALVAGE NOTICE (2026-07-10, workshop): the ratified file was lost before filing.
This copy was transcribed from the ops session transcript ("Sailing book
analysis"). Sections marked [NOT RECOVERED] did not surface verbatim; their
substance is summarized from the session's interview and read-back where
possible. This copy is PROVISIONAL until an ops session verifies it against
the source, per the division-of-labor rule (the workshop transcribes; only
ops sessions author or amend ops artifacts). All operator rulings (Q1–Q6)
and both escalations were recovered and are faithful.

## Conventions

### Identity
- slug: `sailing-for-dummies` [operator-decided]
- type: `book` [inferred-confirmed]
- title/author/year: *Sailing For Dummies*, 2nd Edition / J.J. Isler and Peter Isler / 2006, Wiley Publishing [inferred-confirmed]
- domain_brief: Recreational sailing from first principles through racing — the parts of a
  sailboat, the maneuvers that move it, the conditions that constrain it, and the rule
  systems governing boats that meet. Beginner audience; authors are an Olympic medalist and
  an America's Cup tactician, so the racing material carries real authority. Contributes
  breadth of canonical vocabulary plus a 179-entry native glossary. [inferred-confirmed]

### Ingest
- input format: **plain UTF-8 text, misnamed `.pdf`** [inferred-confirmed]
  `pdfinfo` fails: `Syntax Error: Couldn't find trailer dictionary`. The file is a
  pre-existing extraction; we inherit it and **cannot re-extract at higher fidelity**.
- extraction method: none available — file consumed as-is [operator-decided]
- size: 16,074 lines / ~142k words / 391 book pages
- fidelity-gate result: **PASS for prose, FAIL for tabular and figure content** [operator-decided]
  Operator accepted the source as-is under this split verdict (Q1 = accept).
- [NOT RECOVERED — the final Ingest section may additionally record the retraction
  proven mid-session: apparent mid-clause truncation was a display artifact; soft-hyphen
  lines merged two source lines; **no prose text is lost**. Read-back confirms this stands.]

### Location grammar
- grammar: `page:N`, parent `chapter-N` [inferred-confirmed]
- mechanism: page-anchor table built from 168 surviving running heads, in two forms —
  recto `Chapter 1: Ready, Set, Go... 11`, verso `154 Part II: Casting Off...`
- coverage: **359 of 391 pages anchored.** The 32 gaps are chapter-opening and part-divider
  pages, which carry no running head by design; they interpolate unambiguously.
- **caveat:** a page's body runs *backward* from its head — heads linearize into footer
  position. Resolution is `page:N → lines(prev_head+1, head_N)`.

**PROVEN** — three citations resolved against the extracted text:
- `Table 8-1` (TOC p.153) → resolves into Ch.8 Beaufort text ✓
- `Appendix A` glossary (TOC p.383) → resolves onto `block / cam cleat / catboat` ✓
- `Ch.19` (running head p.367) → resolves onto figure-eight knot prose ✓

### Entity types
[operator-decided — type set ratified Q5; `knot` kept separate on the template argument]

| Type | What counts | Template slots | unit_weight |
|---|---|---|---|
| `part` | Physical boat components — rudder, keel, cunningham, sprit | breadcrumb, definition, connections, children_list, variations_by_source | 1 *(guess)* |
| `maneuver` | Executed actions — tacking, jibing, spinnaker takedown, anchoring | breadcrumb, definition, procedure, goals, cues, dangers, variations_by_source | 3 *(guess)* |
| `knot` | The ten knots of Ch.19 | breadcrumb, definition, procedure, goals, dangers | 2 *(guess)* |
| `concept` | Abstractions — lift, apparent wind, points of sail, dead reckoning | breadcrumb, definition, mechanism, connections | 2 *(guess)* |
| `boat_class` | ketch, sloop, catboat, dinghy, keelboat, sailboard | breadcrumb, definition, tradeoffs, connections | 1 *(guess)* |
| `condition` | Weather/water states — Beaufort force, dew point, current, death roll | breadcrumb, definition, cues, dangers | 2 *(guess)* |

All unit_weights are **guesses**, flagged as such per prompt.

- `knot` justified separate from `maneuver`: knots have no `cues` slot and Ch.19 is
  `procedure`-pure (20 numbered steps, 0 tables).
- slot `tradeoffs` added (v2-proposed): Ch.12–13 argue tradeoffs explicitly. Exhibit:
  > these boats are giving up the ease-of-use advantages of an A-sail in the quest
  > for a bit more speed.
- slots `data_table` and `code_block` **dropped**: tables ruled out of scope (Q1);
  no code listings exist in this source.
- slot `further_reading` **dropped**: the book has no bibliography, only internal
  cross-references. One outbound recommendation exists (Dave Perry, *Understanding the
  Racing Rules of Sailing*) — insufficient to earn a slot.

### Mention classes
Tracked as references, never built as nodes [operator-decided]:
`boat brands/logos (Ch.20)`, `sailing schools`, `US Sailing`, `ASA`, `ISAF`,
`America's Cup`, `Olympics`, `J.J. Isler`, `Peter Isler`, `Dave Perry`, place names.

**Dual-status note (operator-confirmed):** `US Sailing`, `ASA`, and `ISAF` are simultaneously
**mention_class members** (they appear as named organizations in prose) and
**authority_anchors** (they are naming authorities for the domain). This is not a
contradiction but must be explicit: the harvester treats them as mentions; the registry
treats them as anchors. A thing may be both, annotated.

### Ontology openness & arbitration
- openness: **near-closed** [inferred-confirmed] — sailing vocabulary is settled by long
  usage; the source ships its own 179-entry glossary.
- arbitration mode: **split** [operator-decided]
  - `community` for general seamanship (the bulk of the source)
  - `codified` for the racing and navigation subgraph (Ch.9, Ch.13)
- authority_anchors: `US Sailing`, `ASA`, `ISAF`, `Racing Rules of Sailing (RRS)`,
  `COLREGS / rules of the road`, this source's Appendix A.

The split is **not currently config-expressible** (`community_arbitration` is a scalar in
schema v1). It is recorded here as a convention line and carried into the fragment as a
v2-proposed comment. See Escalation E2.

**Exhibit — the source distinguishes the two regimes in its own voice** (p.281, line 10121):
> Starboard tack has the right-of-way over port tack. This rule and the following two rules
> are in force under the rules of the road (for nonracing sailboats) and the Racing Rules
> (for racing sailboats only).

Critically, the regimes **overlap rather than partition**: three rules hold in both, while
mark-rounding and exoneration are racing-only. Exoneration further defers to per-regatta
`Sailing Instructions` — a third authority tier beneath RRS.

### Role split
- `role_split: null` [operator-decided]

Tack state (`port tack` / `starboard tack`) is recorded as a `cues` dimension, not a fork.
Unlike a genuine perspective split (e.g. top/bottom in BJJ), tack does not fork a node's
*content* — a jibe is one procedure whose handedness mirrors. Forking would double the
vault for a mirror symmetry with no reader benefit.

**A first-pass hypothesis was falsified here and is recorded to prevent its revival:** crew
roles were expected to drive the split. Counts refute it — `trimmer` 2, `tactician` 1,
`bowman` 2, against `crew` 266. Crew roles are *mentioned*, never *taught*.

The surviving contender, `windward`/`leeward`, is deferred — see Escalation E1.

### Native seeds
- **Yes — Appendix A glossary, lines 13114–13636** (`page:383`–`page:390`). [inferred-confirmed]
- **179 defined entries** in `term: definition` form; 16 carry numbered senses.
  > dinghy: (1) A sailboat with a centerboard (or daggerboard or leeboard); (2) a small rowboat.
- Also present: a full back-of-book index (line 14096–end), and per-chapter
  "In This Chapter" bullet boxes (98 `\x03` bullets).
- **Trust caveat:** the glossary's first three lines (`block`, `cam cleat`, `catboat`) are
  bare terms with no definitions — Figure A-1 label residue, not entries. The seed requires
  a definition-colon filter. Seeds are recall aids for harvest, not term lists to trust blindly.

### Scope & exclusions
[operator-decided — Q3 = "include it"]

**In scope: all 20 chapters and all three appendixes**, including Ch.13 (racing) and
Ch.18 (sailboards), which were flagged as arguably a different domain. Operator ruled include.
Ch.2, Ch.16, Ch.17, and Ch.20 — flagged as directory/lifestyle/buying content — likewise included.

**Excluded** (structural, not content): front matter, "Icons Used in This Book", back-of-book
index, running heads, figure-label residue.

No exclusion in this document was made on the session's own authority.

### Content-mode map
Spilled to `content_mode_map_sailing-for-dummies.csv` per the cap invariant's named remedy.
Per-section, mechanically derived (counts of `Table N-M`, numbered steps, `Figure N-M`).
Six sections carry tables whose structure is lost (ch8, ch10, ch12, ch14, ch16); per Q1 that
content is out of scope and the section is harvested as prose around the table.

[NOT RECOVERED — the sidecar CSV itself. Note from the 07-10 checkpoint: if ever
regenerated, it needs v2.4 enum discipline (mode column from the pinned enum only).]

### Visual dependency
**HIGH.** [inferred-confirmed] 148 figures across the book; all image content is absent.

1. **Table structure lost.** Exhibit — Table 8-1 (line 5647); note the running head injected
   *inside* the table body:
   > Force Wind Speed Description Water-Surface Dummies
   > 0 0 Calm Smooth, like Good time for a nap.
   > a mirror.
   > 154 Part II: Casting Off and Sailing Away
2. **Figure captions shatter** into one-word column lines, interleave with unmarked diagram
   labels, and emit in layout order (Fig 1-3 precedes 1-2):
   > Figure 1-3:
   > Two
   > dinghies:
   > Rudder Rudder Bulb Rudder
3. **Procedures living in figures are unrecoverable.** Ch.19: "Check out Figure 19-6 to tie a
   round turn and two half hitches." The steps *are* the figure.
4. **All six margin icons stripped** (Warning, Safety, Tip, Remember, two story icons).
   Operator accepted the loss (Q2) and declined lexical reconstruction of `dangers` —
   reconstructing a safety slot by guessing is the wrong place to guess. Consequence: in body
   text, a Tip and a Warning are indistinguishable.

### Alias & fan-out
[NOT RECOVERED verbatim — substance from session evidence:] Naming runs through
`X, or Y,` (136×) and `called Y` (84×), only 7 `(also called X)` — e.g.
`Asymmetrical spinnakers, or A-sails`. Synonyms abundant but *orderly*: a
canonical-naming source, not a chaotic one. Residue hazard: ~793 short
capitalized lines where real headings (`Cleat Knot`) and figure-label debris
(`Rudder`, `Keel Bulb Rudder`) are lexically indistinguishable.

### Versioning / era
[NOT RECOVERED verbatim — substance:] `era_bound: mild` — ISAF→World Sailing
rename (2015, model-knowledge), stale URLs/phone numbers, 2006-era regulations.
No pedagogical versioning. `snapshot_cadence` deliberately left `~` despite the
source stating "Every four years, ISAF updates the rules" — reserved engine
question; evidence recorded, not settled.

### Single-artifact
[NOT RECOVERED — wording unknown. No contrary evidence appears anywhere in the
recovered transcript.]

### External refs
[NOT RECOVERED verbatim — substance:] internal cross-references only; single
outbound recommendation (Dave Perry, *Understanding the Racing Rules of
Sailing*), insufficient for a `further_reading` slot.

### License posture
[NOT RECOVERED — wording unknown.]

### Span-sizing observations
[NOT RECOVERED verbatim — substance from read-back:] `span_size`/`span_overlap`
left `~` (reserved). Observations recorded only: Ch.19 pulls toward small spans;
Ch.4–7 pull toward large spans.

## Escalations

### E1 — `role_split`: windward/leeward for the racing subgraph
[PARTIALLY RECOVERED — lean and evidence from read-back; exact body wording lost:]
Evidence cuts *against* the motivating intuition — `windward`/`leeward` appear
7× in Ch.13 vs 80× elsewhere; the racing region differs by **rules, not
geometry**. Lean: hold `role_split: null`; model the racing difference via E2.
Recovered verbatim tail: "Revisit if right-of-way nodes prove unrepresentable
without a perspective slot."
- **Note:** E1 and E2 rhyme — the racing chapters repeatedly want to be a differently
  configured *region* of the source. Whether the engine supports per-region configuration
  at all is an engine question, not a source question.

### E2 — `arbitration_mode` is scalar in schema v1; this source needs it plural
≤10 lines. Evidence both ways; **not resolved.**

- **The source is explicit** (line 10121) that two rule regimes coexist: `rules of the road`
  for all boats, `Racing Rules` for racing boats only.
- The regimes **overlap rather than partition** — three right-of-way rules hold under both;
  mark-rounding and exoneration are racing-only. A boolean `is_racing` flag on nodes would
  not capture this.
- A **third tier** exists below RRS: per-regatta `Sailing Instructions` govern exoneration.
- Schema v1 offers `community_arbitration` as a single value. Neither `community` nor
  `codified` is true of this source as a whole.
- **Lean:** carry `arbitration_mode: split` as v2-proposed with a `regimes` sub-map. Do not
  flatten to whichever mode covers more pages — that discards the source's key property.

## Config fragment

*INPUT to the schema-v2 and config sessions. Not a live config.*

```yaml
sources:
  - slug: sailing-for-dummies
    type: book
    title: "Sailing For Dummies, 2nd Edition — J.J. Isler & Peter Isler (2006)"
    loc_grammar: "page:N (parent chapter-N); anchored by 168 running heads, 359/391 pages"
    text_path: ./sailing-for-dummies.txt
    span: ~                       # reserved — engine open question, not settled here
    media_notes: >-
      HIGH visual dependency. 148 figures, all absent. Table structure lost; figure
      captions shattered and out of reading order; all six For Dummies margin icons
      stripped (Warning/Safety/Tip/Remember/two story icons) — Tip and Warning are
      indistinguishable in body text.
```
[NOT RECOVERED — middle of the fragment: native_seed, scope, entity type /
mention_classes fields (recovered comment fragment: "Capitalization alone WILL
misfire."), arbitration comment. Recovered tail:]
```yaml
  era_handling:                   # schema:v2-proposed
    pedagogical_versioning: false
    era_bound: mild               # ISAF→World Sailing (2015); stale URLs/phones; 2006 regs
```

## Kit nominations

Hard spans nominated for the `harvest_map` sealed kit:

1. **`lines 1000–1100` (Ch.1, `page:13–15`) — alias hotspot.** Highest alias density in the
   book (6 constructions / 100 lines). Every underwater fin gets named, renamed, and
   conditionally renamed in one breath: `keel` / `centerboard` / `daggerboard` (if it
   retracts vertically) / `leeboard` (if side-mounted). Tests whether the harvester can
   hold a conditional alias chain without collapsing four parts into one node.

2. **`lines 5647–5720` (Ch.8, `page:153–155`) — Table 8-1, Beaufort Scale.** The flagship
   structural failure: flattened columns, cells wrapping across lines, and a running head
   injected *inside* the table body. Tests residue stripping and confirms the harvester
   does not hallucinate table structure that the ingest destroyed.

3. **`lines 12761–12800` (Ch.19, `page:367–368`) — knots, procedure-pure.** Alias-dense
   (`two half hitches` = `double half hitch`; `round turn and two half hitches` as a
   distinct entity), figure-dependent ("Check out Figure 19-6 to tie…"), and the steps for
   at least one knot exist only in the absent figure. Tests graceful degradation: does the
   harvester emit a `knot` node with an honestly empty `procedure`, or invent steps?

4. **`lines 10106–10135` (Ch.13, `page:281`) — the two-regime exhibit.** The source names
   both rule systems in one sentence and marks which rules belong to which. Tests whether
   arbitration-mode splitting survives harvest. Directly exercises Escalations E1 and E2.

---
- sailing-for-dummies | book | Sailing For Dummies, 2nd Edition / J.J. Isler & Peter Isler / 2006 | loc-grammar: page:N (parent chapter-N)
