# Discovery — sailing-for-dummies (Sailing For Dummies, 2nd Edition)
Status: conventions ratified 2026-07-09, discovery_prompt_v2.

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

**Correction to first-pass reading** (recorded because it nearly became a false convention):
prose appeared truncated mid-clause. It is not — soft-hyphen lines merged two source lines
(mean 133 chars vs. 47). **No prose text is lost**; the damage was my display clamp, not the source.

Control-char census — bimodal, **zero overlap**, so repair is mechanical, not inferential:

| Byte | Count | Context | Meaning |
|---|---|---|---|
| `\x02` | 1626 | 861 `alpha–alpha` | soft hyphen (`dagger\x02board`) |
| `\x02` | ” | 765 `newline–space` | bullet |
| `\x03` | 98 | always line-initial | "In This Chapter" bullet |
| `❑` | 36 | line-initial | checklist bullet |
| `•` | 60 | line-initial | third-level bullet |

- repair: de-hyphenate the 861; normalize three bullet classes to `-`; retain the 168 running
  heads as a sidecar page index (they are load-bearing — see Location grammar). [operator-decided]

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

- `knot` separate from `maneuver`: no `cues` slot; Ch.19 is `procedure`-pure (20 steps, 0 tables).
- `tradeoffs` added (v2-proposed); Ch.12–13 argue them explicitly:
  > giving up the ease-of-use advantages of an A-sail in the quest for a bit more speed.
- `data_table`, `code_block` dropped (tables out of scope per Q1; no listings).
- `further_reading` dropped: no bibliography, only internal cross-refs.

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

Tack state (`port tack`/`starboard tack`) becomes a `cues` dimension, not a fork: tack does
not fork a node's *content* — a jibe is one procedure whose handedness mirrors. Forking would
double the vault for a mirror symmetry with no reader benefit.

**A first-pass hypothesis was falsified and is recorded to prevent its revival:** crew roles
were expected to drive the split. Counts refute it — `trimmer` 2, `tactician` 1, `bowman` 2,
against `crew` 266. Crew roles are *mentioned*, never *taught*.
Surviving contender `windward`/`leeward` is deferred — see Escalation E1.

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
Per-section, mechanically derived (counts of `Table N-M`, numbered steps, `Figure N-M`).
**Busts the conventions cap; emitted as `content_mode_map_sailing-for-dummies.csv`** per the
bounded-artifact invariant. 23 sections mapped.

Summary: `prose` ch1–3, ch13, ch15–17, ch20, appB; `mixed` ch4–12, ch14, ch18;
`procedure-pure` ch19; `glossary` appA; `mechanism` appC.
Six sections carry tables whose structure is lost (ch8, ch10, ch12, ch14, ch16); per Q1 that
content is out of scope and the section is harvested as prose around the table.

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

### Alias & fan-out weather
Naming is **canonical and orderly**, not chaotic. [inferred-confirmed]
Dominant constructions: `X, or Y,` (136 occurrences) and `called Y` (84). Only 7
`(also called X)`; 1 `also known as`; 1 `sometimes called`.
> Asymmetrical spinnakers, or A-sails, are a great evolution of the spinnaker.

Synonyms are abundant but introduced deliberately at first use. Fan-out risk is moderate,
concentrated where parts are first named.

### Versioning / era
- **Pedagogical versioning: no.** The source does not iteratively redefine its own terms.
- **Era-bound: mildly.** 2nd edition, 2006. `ISAF` has since been renamed **World Sailing**
  (2015); the doc records `ISAF` as the source states it, with the rename noted for the
  registry rather than corrected in-source. Contact details (phone numbers, URLs at
  line 1521) are stale. Homeland Security regulations cited at line 3030 are era-bound.
- The rulebook itself versions on a four-year cycle by the source's own account
  ("Every four years, ISAF updates the rules") — relevant to `snapshot_cadence`, which
  this session does **not** settle.

### Single-artifact flag
`false`. [inferred-confirmed] The source does not build one system across its length; it
surveys a domain. No part-of/implements edge set is implied by the book's structure.

### External refs
**Effectively none.** No bibliography. One outbound book recommendation (Dave Perry,
*Understanding the Racing Rules of Sailing*, line 10110) and two URLs. Does **not** feed a
`further_reading` slot. Cross-references are dense but *internal* (`see Chapter 2`,
`see Appendix C`, `see Figure 13-9`) and should be resolved as intra-source edges.

### License posture
`personal` [operator-decided]. Copyright © 2006 Wiley Publishing, Inc. Not client-owned,
not licensed for redistribution.

### Span-sizing observations
*Evidence only — span size/overlap are reserved engine open questions, NOT settled here.*

- Ch.19 stresses span size **downward**: each knot is a self-contained ~15-line unit
  (prose + numbered steps). Small spans suffice; large spans would merge unrelated knots.
- Ch.4–Ch.7 stress span size **upward**: procedures run 30+ numbered steps with interleaved
  prose rationale, and cutting mid-procedure severs `cues` from `procedure`.
- The **running-head injection is a hard span-boundary hazard**: `154 Part II: Casting Off
  and Sailing Away` appears *inside* Table 8-1 and inside continuous prose elsewhere. Any
  span heuristic must strip heads before measuring, or spans will silently include a page
  footer as content.
- ~793 short capitalized lines are lexically ambiguous between real `###` headings
  (`Cleat Knot`) and figure-label residue (`Rudder`, `Keel Bulb Rudder`). A residue
  heuristic keying on capitalization alone **will misfire**. Recorded for `residue_heuristics`.

## Escalations

### E1 — The racing subgraph wants a different `role_split` than the rest of the vault
- **For `null` (ratified globally):** tack is a mirror symmetry; forking every maneuver doubles
  the vault for no reader benefit. Operator-endorsed.
- **For `[windward, leeward]` in racing:** right-of-way is *defined* by the windward/leeward
  relation, which holds between two boats, not as a property of one.
- **Counter-evidence found this session:** `windward`/`leeward` are **not** concentrated in
  Ch.13 (7 vs. 80 elsewhere) — their density is in trim/points-of-sail. What *is* concentrated
  is `right-of-way` (6 vs. 3). The racing region's difference is **the rules, not the geometry**.
- **Lean:** hold `role_split: null` globally; model the racing difference via arbitration (E2).
  Revisit only if right-of-way nodes prove unrepresentable without a perspective slot.
- E1 and E2 rhyme: the racing chapters want to be a differently *configured region*. Whether
  the engine supports per-region config is an engine question, not a source question.

### E2 — `arbitration_mode` is scalar in schema v1; this source needs it plural
- **The source is explicit** (p.281, line 10121) that two regimes coexist: `rules of the road`
  for all boats, `Racing Rules` for racing boats only.
- The regimes **overlap, not partition**: three right-of-way rules hold under both;
  mark-rounding and exoneration are racing-only. A boolean `is_racing` flag cannot capture this.
- A **third tier** sits below RRS: per-regatta `Sailing Instructions` govern exoneration.
- Schema v1 offers scalar `community_arbitration`. Neither `community` nor `codified` is true
  of this source as a whole.
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

    ingest:                       # schema:v2-proposed
      input_format: text          # file is plain UTF-8 misnamed .pdf; pdfinfo fails
      extraction_method: none     # inherited extraction; cannot re-extract
      fidelity_gate: pass_prose_fail_tabular
      repairs:
        - dehyphenate: 861        # \x02 between alpha-alpha
        - normalize_bullets: [\x02, \x03, ❑, •]   # 765 + 98 + 36 + 60
        - strip_running_heads: 168    # retain as sidecar page index — load-bearing
    native_seed:                  # schema:v2-proposed
      kind: glossary
      location: "appendix A, lines 13114-13636 (page:383-390)"
      entries: 179
      caveat: "first 3 lines are Figure A-1 label residue; filter on definition-colon"
    scope:                        # schema:v2-proposed
      included: all_chapters_and_appendixes    # operator ruled include on ch13, ch18, ch2/16/17/20
      excluded: [front_matter, icons_section, index, running_heads, figure_label_residue]
    visual_dependency: high       # schema:v2-proposed
    single_artifact: false        # schema:v2-proposed
    content_mode: see_table       # schema:v2-proposed — 23 sections mapped in Conventions

engagement:
  domain: sailing
  domain_brief: >-
    Recreational sailing from first principles through racing: the parts of a sailboat,
    the maneuvers that move it, the conditions that constrain it, and the rule systems
    governing boats that meet. Beginner audience, expert authors.
  content_license: personal
  background_knowledge: none_assumed

entity_model:
  role_split: null                # see Escalation E1
  root_categories: [part, maneuver, knot, concept, boat_class, condition]
  types:
    - name: part
      description: "Physical boat components — rudder, keel, cunningham, sprit"
      template: [breadcrumb, definition, connections, children_list, variations_by_source]
      unit_weight: 1              # GUESS
      connection_labels: [part_of, attaches_to, controls]
    - name: maneuver
      description: "Executed actions — tacking, jibing, spinnaker takedown, anchoring"
      template: [breadcrumb, definition, procedure, goals, cues, dangers, variations_by_source]
      unit_weight: 3              # GUESS
      connection_labels: [precedes, requires_part, inverse_of]
    - name: knot
      description: "The ten knots of Ch.19; procedure-pure, no cues"
      template: [breadcrumb, definition, procedure, goals, dangers]
      unit_weight: 2              # GUESS
      connection_labels: [used_for, variant_of]
    - name: concept
      description: "Abstractions — lift, apparent wind, points of sail, dead reckoning"
      template: [breadcrumb, definition, mechanism, connections]
      unit_weight: 2              # GUESS
      connection_labels: [explains, depends_on]
    - name: boat_class
      description: "ketch, sloop, catboat, dinghy, keelboat, sailboard"
      template: [breadcrumb, definition, tradeoffs, connections]   # tradeoffs = schema:v2-proposed
      unit_weight: 1              # GUESS
      connection_labels: [subclass_of, contrasts_with]
    - name: condition
      description: "Weather/water states — Beaufort force, dew point, current, death roll"
      template: [breadcrumb, definition, cues, dangers]
      unit_weight: 2              # GUESS
      connection_labels: [causes, indicated_by]

  mention_classes:                # schema:v2-proposed
    - boat_brands
    - sailing_schools
    - organizations   # US Sailing, ASA, ISAF — ALSO authority_anchors; dual status, annotated
    - events          # America's Cup, Olympics
    - people          # J.J. Isler, Peter Isler, Dave Perry
    - places

registry:
  authority_anchors:
    - US Sailing      # also mention_class:organizations
    - ASA             # also mention_class:organizations
    - ISAF            # also mention_class:organizations; renamed World Sailing (2015)
    - Racing Rules of Sailing (RRS)
    - COLREGS / rules of the road
    - "sailing-for-dummies: Appendix A"
  community_arbitration: ~        # UNSETTLED — see Escalation E2; scalar cannot express this source
  arbitration_mode:               # schema:v2-proposed — plural; do NOT flatten
    default: community            # general seamanship
    regimes:
      - name: codified
        applies_to: [ch9, ch13]   # navigation + racing
        authority: [RRS, COLREGS]
        sub_authority: "per-regatta Sailing Instructions (governs exoneration)"
    note: >-
      Regimes OVERLAP, they do not partition. Three right-of-way rules hold under both;
      mark-rounding and exoneration are racing-only. Source states this itself at p.281.
  snapshot_cadence: ~             # reserved — but note source says RRS updates every 4 years

harvest:
  span_size: ~                    # reserved — engine open question
  span_overlap: ~                 # reserved — engine open question
  residue_heuristics:
    - strip_running_heads_before_spanning   # heads inject mid-table and mid-prose
    - WARNING: >-
        ~793 short capitalized lines are lexically ambiguous between real headings
        ("Cleat Knot") and figure-label residue ("Rudder", "Keel Bulb Rudder").
        Capitalization alone WILL misfire.
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
