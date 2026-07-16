# Discovery — rappers-handbook (The Rapper's Handbook, Second Edition)
Status: conventions ratified 2026-07-15, discovery_prompt_v2.6.

## Conventions

### Identity
- Slug `rappers-handbook`; type `book`. [operator-decided]
- *The Rapper's Handbook, Second Edition*, by Escher (Blake Harrison) with Alexander Rappaport, Flocabulary LLC, 2009; ISBN 978-1-934773-26-0. [mechanical: front matter + copyright page, verbatim]
- Domain-brief contribution [inferred-confirmed]: the first comprehensive how-to manual for rapping as a craft. It teaches rhyme construction (slant, in-rhyme, multis), performance (flow, hand gestures, crowd control), competitive battling, and song composition. Its pedagogy is exhibit-driven: it marks rhyming syllables inside real lyric excerpts and reasons about them. It is a 2009 snapshot of a living oral tradition, written by practitioners for beginners.
- Preflight attestation: environment contains only this prompt and the source; no other content. [operator-decided]
- Source-of-record is the uploaded raw binary `rapper.pdf` (filename is incidental — it matches co-author Rappaport's surname, not the title). [mechanical: %PDF-1.6 magic bytes verified, format matches claim]

### Ingest
- Container `born_digital`; produced by Adobe InDesign CS2 → PDF Library 7.0, 230 pages, 324×504pt. No OCR layer. [mechanical: pdfinfo + pdffonts — embedded Type1C/TrueType subsets only, no invisible OCR font]
- **The text layer silently destroys the book's core teaching.** Rhyming syllables are marked in BOLD inside lyric excerpts; `pdftotext -layout` and `-raw` drop the distinction and emit undifferentiated plain text. Confirmed against rasterized pp. 40–41. [mechanical: raster comparison, 2 pages]
- Ruled extraction strategy: pdfplumber word extraction with `fontname` retained; bold = any font whose name contains `Bold`. Recovers the scansion exactly. [mechanical: 3 strategies compared — -layout FAIL, -raw FAIL, pdfplumber PASS]
- `row_clustering: {method: top-gap, gap_threshold_pt: 3.0}`. [mechanical: measured on p41 — intra-line jitter ≤0.9pt (bold sits fractionally off-baseline), true line breaks ≥12.7pt; no overlap between the two populations]
- `columns: 1` for the entire body. **Exception: Appendix I (p215–p217) is a two-column list with a single-column intro paragraph above it — a mixed zone.** Repair = x-midpoint bisection scoped to the list zone only; page-scoped bisection shreds the intro. [mechanical: raster-adjudicated, x-midpoint 162pt]
- `hyphenation: {style: dejustified, marker: "-"}`; 28 line-end hyphens book-wide. [mechanical: grep over full extraction]
- `repair_vocab` (closed, 2 items): `and- forth` → `and-forth`; `for- paddle` → `for-paddle`. [mechanical: 4 stray mid-word splits found, 2 are genuine artifacts]
- `preserve_patterns`: `three- or`, `near- endless` — suspended hyphens, correct English, not damage. [mechanical: same census, hand-adjudicated]
- Per-class verdicts: prose PASS; lyric scansion PASS (on strategy 3 only); `droppin' knowledge` sidebar PASS; gesture procedures PASS as text but the teaching is absent from text; Appendix I FAIL until zone-scoped repair; Appendix II/III PASS. [mechanical: 3+ adversarial locations per class, MARGINAL/FAIL raster-confirmed]
- `figure_manifest`: 70 image placements across 68 pages. Two classes — `part_opener` (6 full-bleed, 507×763 @150ppi, pdf pp. 11/31/107/149/195) and inline sidebar/banner art (~64). [mechanical: pdfimages -list + size profile]
- `caption_pattern: null`. **The source has no captions.** Zero numbered figure labels; the 11 hits for "Figure" are the ordinary verb ("figure out"). Proximity-based caption pairing has nothing to attach to and was not performed. [mechanical: 0 matches for `Figure [0-9]`, `Fig.`, `Diagram`, `Table [0-9]`]
- `fidelity_canaries`: (1) p41 `The **fact** is I kick **phat** **raps**, so know **that**` — bold spans must survive; (2) p215 left column must read `An ax to grind` → `Cold war` without interleaving `Cup of Joe`; (3) p126 must extract a heading and no body text. [mechanical: each verified against raster]

### Location grammar
- Grammar: `p<N>` where N is the **printed** page number. [operator-decided]
- **`printed_page = pdf_page − 10`, universally.** [mechanical: 203 of 230 pages carry a head number; all 203 give offset exactly 10; zero exceptions. The 27 without heads are part-openers and blanks, suppressed by design.]
- Running heads: recto = `CHAPTER NAME <page>`; verso = `<page> THE RAPPER'S HANDBOOK`. [mechanical: pattern verified across sampled recto/verso pairs]
- Front matter is roman (vii–xii); body is arabic from p2. [mechanical: TOC + head inspection]
- Figure references use `fig:` + printed page (e.g. `fig:p126`), NOT `fig:N-M` — the source numbers no figures. [inferred-confirmed]
- Interpolation rule for gaps: a location between two anchors belongs to the earlier anchor's chapter. [inferred-confirmed]

### Entity types
- Four types: `technique`, `gesture`, `drill`, `artist`. [operator-decided]
- `technique` [operator-decided] — a named rhyme/word craft device the book defines and teaches. Slots: `breadcrumb, definition, mechanism, procedure, goals, cues, options, variations_by_source, connections, children_list`. Unit-weight guess: ~35 book-wide (GUESS).
- `gesture` [operator-decided] — a named hand movement for performance. Slots: `breadcrumb, definition, procedure, cues, dangers, connections, children_list`. Unit-weight guess: ~10 (GUESS). `children_list` carries `Variation:` sub-gestures.
- `drill` [operator-decided] — a ruled practice activity or game. Slots: `breadcrumb, definition, procedure, goals, staged_list, options, dangers, connections`. Unit-weight guess: ~12 (GUESS).
- `artist` [operator-decided] — a named rapper/group cited or taught from. Slots: `breadcrumb, definition, role_doors, connections, further_reading`. Unit-weight guess: ~20 (GUESS).
- `role_doors` earns its place on `artist` only: the book addresses the same artist as exemplar-to-study and as battle-opponent-to-beat. [inferred-confirmed]

### Mention classes
- **Null.** The operator promoted `artist` from mention class to full entity type; no reference-only class remains. [operator-decided]
- Dual-status note: artists are simultaneously entity content AND registry authority anchors (they are the `droppin' knowledge` speakers). Routed to the registry queue. [inferred-confirmed]

### Ontology openness & arbitration
- Openness `open`; arbitration mode `community`. [operator-decided]
- Authority anchors: the book's own definitions first; the named practitioners it quotes second. [inferred-confirmed]
- `web_policy: in-tradition`. Judges may consult hip-hop-tradition sources to resolve a term; the source's own 2009 usage governs where they conflict. Evidence: the tradition is living and heavily web-documented, but this source is a 2009 snapshot and the vocabulary has drifted since. [operator-decided]
- Tiebreak preference, craft-term-polysemy class: **split freely — pre-open fan-outs**. [operator-decided]

### Role split
- Null for `technique`, `gesture`, `drill`. Present for `artist` (exemplar vs. opponent) — carried in `role_doors`, not a type split. [inferred-confirmed]

### Native seeds
- Appendix I: ~90-idiom closed list, raw material for the Wordplay technique. **Native seed only — not harvested as entities.** [operator-decided]
- Appendix II (rhymes for famous names) and Appendix III (rhymes for "rhymeless" words) are closed lists with a bold-headword pattern; same seed status. [mechanical: bold-headword structure confirmed, `**George Bush** — ...`]
- No glossary, no index. [mechanical: TOC + back-matter inspection]
- Residue contaminating the seed: Appendix I's two-column zone interleaves without repair, which would corrupt ~90 idioms into nonsense pairs. Repair is mandatory before seed use. [mechanical: raster-adjudicated]

### Scope & exclusions
- **Full book in scope, p2–p220.** Part Five (Setting up a Studio, p168–p179) included despite era-bound 2009 gear advice. [operator-decided]
- Front matter (pp. i–xii) and back matter (p209–p214) are in scope as registry-anchor sources, not entity content. [inferred-confirmed]

### Content-mode map
- Pinned enum used: `prose` (8 chapters), `mixed` (22), `tabular` (5). `dialogic` and `code_listing` are unused — no chapter is predominantly either. [mechanical: per-chapter classification, 35 rows]

### Chunk plan
- Boundary `chapter`; fallback bound **4,500 est. tokens**. [operator-decided]
- `Guide to Battling` (p142–p158) measures **4,903 tok and exceeds the bound** — the only chapter that does. Split into two `fallback_split` rows at the book's own heading "How to Use Personal Punches" (p147), never mid-teaching-unit. [mechanical: per-chapter token census over the real extraction]
- `Repeating Words` and `Visual Wordplay` both begin on printed p93 (the latter mid-page). Page-level loc-grammar cannot split a shared page, so they merge into one `convention`-boundary chunk at the book's own "Other Techniques" sub-group. [mechanical: running head on p93 reads OTHER TECHNIQUES]
- Coverage: 36 rows, 219/219 in-scope pages, every page in exactly one chunk, zero gaps. [mechanical: coverage script over the shipped CSV]
- Book totals 51,150 est. tokens; mean 237 tok/printed page. [mechanical: word count × 1.35 over full extraction]

### Visual policy
- **`describe`**, per source. License-gated: `content_license: licensed` forbids embedding. [operator-decided]
- The `Hand Gestures` chapter (p122–p134) is genuinely visual-dependent: printed p126 is a heading (`The Poppin-Off-of-the-Top-of-the-Dome Finger Flick`) plus a full-page illustration and **zero body text**. `ignore` would delete a teaching chapter. [mechanical: raster of pdf p136 confirms heading + art only]
- Part-opener art (6 pages, pdf pp. 11/31/107/149/195) is decorative: `ignore`. [mechanical: 507×763 @150ppi, no teaching text]

### Alias & fan-out weather
- Techniques carry a formal name plus a house shorthand ("multi-syllable rhyme" = "multi" = "multis"). [mechanical: 52 occurrences of multi/multis]
- Gestures use a fixed `The <Name>` frame; `Variation: The <Name>` introduces a child, not a sibling. [mechanical: heading census in p122–p134]
- House vocabulary (`flow` 110, `verse` 86, `spit` 86, `battle` 66) saturates the book. [mechanical: in-session probe census]

### Versioning/era
- Era-bound: a 2009 snapshot. Part Five's studio gear (mic preamps, software) is dated; the craft chapters are not. [inferred-confirmed]
- The sole `Part 1 [BASIC]` / `Part 2 [ADVANCED]` tier split occurs **only** in the Multis chapter. It is not a book-wide scheme. [mechanical: exactly 1 occurrence of each marker book-wide]

### Single-artifact flag
- False. The book cites companion Flocabulary titles and an external discography. [mechanical: "Also by Flocabulary" page + Discography]

### External refs
- Light bibliography load: the `Sources` section (p213–p214) lists ~10 items (an interview, dictionaries, web references). [mechanical: section inspection]
- The Discography (p209–p212) is a rights-clearance block, not a reading list. [mechanical: EMI/Morley per-song copyright entries]

### License posture
- `content_license: licensed`. [operator-decided]
- Evidence: front matter reserves all rights and forbids reproduction absent written permission; the Discography carries per-song clearances from EMI April Music, EMI Blackwood Music, and Morley Music, each marked All Rights Reserved / International Copyright Secured. The ~21 lyric excerpts are third-party copyrights licensed to Flocabulary for this book. We hold no license. [mechanical: copyright page + Discography, verbatim]

## Effort forecast
~10 lines, heuristic, flagged as such.
- Expected entities ~75–80: technique ~35, gesture ~10, drill ~12, artist ~20. Derivation: 36 chapters × observed 2–3 named teachables per teaching chapter, discounted for the 6 intro/part-opener chapters that name none.
- Openness class `open` → the arbitration layer, not the workers, is the expensive sequential part.
- The book is small (51k tok) and cheap to harvest. The judgment budget is dominated by the artist type: ~20 artists × dual status (entity + registry anchor) ≈ 40 verdicts before any technique is adjudicated.
- Falsifiable claim (exit exam): if `technique` yields fewer than 20 entities, the type is over-specified and `drill` has absorbed it — check whether Freestyle Rap Games entries were typed as technique.
- Falsifiable claim (exit exam): if `gesture` yields more than 15, the `Variation:` frame is being read as a sibling rather than a child — check `children_list` population on The Ninja Star.

## Ambiguity forecast

Watchlist (in-session probe; census = heading nouns + craft-term list; dispersion = distinct TOC units containing the term; collision = definition-pattern + mode-distinct distant ranges). Top rows:

| term | count | dispersion | collision | home ranges | status |
|---|---|---|---|---|---|
| verse | 86 | 21 | none | book-wide | DOWNGRADED [mechanical: close-read, single stable sense] |
| spit | 86 | 20 | none | book-wide | DOWNGRADED [mechanical: close-read, house verb for "to rap"] |
| flow | 110 | 17 | YES | p98–121, p180–185 | SEEDED [mechanical: distinct senses in distant ranges] |
| emcee | 32 | 16 | none | book-wide | not seeded |
| beat | 40 | 14 | weak | book-wide | not seeded |
| battle | 66 | 12 | weak | p142–167 | not seeded [mechanical: has its own Part; low collision] |
| wordplay | 61 | 12 | none | p54–62 | not seeded |
| multis | 52 | 8 | none | p39–53 | not seeded [mechanical: book defines it explicitly] |
| bar | 17 | 6 | YES | p199–208, p39–53 | SEEDED [mechanical: unit-of-structure vs single-line] |

- `flow` — operator lean: **no opinion**. Exit exam: CONFIRMED if a p180–p185 span yields a `flow` mention unresolvable to the craft sense of p98–p109; KILLED if all resolve to craft sense (signal was a stemming artifact). [discovery-forecast]
- `bar` — operator lean: **no opinion**. Exit exam: CONFIRMED if p199–p208 uses `bar` as a countable song unit while p39–p53 uses it for one written line; KILLED if one sense holds throughout the book's own teaching voice. [discovery-forecast]
- Per-class tiebreak preference (craft-term polysemy): split freely, pre-open fan-outs. [operator-decided]
- **Probe finding:** the two highest-dispersion terms were both false positives. On a house-vocabulary source, dispersion measures ubiquity, not ambiguity; collision was the signal that predicted trouble. Exit exam: if this repeats on a second source, rank on collision and demote dispersion to a tiebreak. [discovery-forecast]

## Escalations

**1. `licensed` posture vs. verbatim-sidebar harvest — unresolved tension.**
The operator ruled `content_license: licensed` (Group 1) and, on re-ask with the license context in view, ruled that `droppin' knowledge` sidebars are harvested **verbatim** into entity content (Group 11). Both are recorded as ruled.

Evidence for the tension: the same `licensed` posture hard-gated Visual policy to describe-never-embed, on the reasoning that reproducing van Hée's artwork is verbatim reproduction rather than transformative use. The 25 sidebars are verbatim third-party quotation — practitioner interview text and, in at least one case (The Coup, "Pimps", p122), quoted song dialogue covered by the EMI/Morley clearances Flocabulary obtained for this book only. Reproducing them applies a rule to text that the visual gate rejects for images, on the same underlying rights.

Evidence the other way: the sidebars are quotes *about craft*, and their pedagogical value is the claim, not the wording. An entity carrying Bun B's point about multisyllabic bar-endings as attributed paraphrase would be transformative and would lose little. The operator may also hold license facts this session cannot see.

Lean: harvest the claim, attribute the speaker, do not reproduce the words. **Not ruled here — the operator ruled otherwise, twice, and the ruling stands.** Flagged for whoever runs harvest; the honest place to resolve it is with the license facts in hand.

## Registry queue

- `[model-knowledge, unverified]` — Every artist named in this book (Rakim, Jay-Z, Bun B, Ludacris, Wordsworth, Big Daddy Kane, The Coup, Ugly Duckling, Melle Mel, Mos Def, Nas, OutKast, Papoose, Kanye West, Eminem, Akir, Median, Punchline) is a real recording artist with a career extending beyond this 2009 source. The book is not a biographical authority on any of them. Dossier work belongs to the registry, not here.
- `[model-knowledge, unverified]` — Hip-hop craft vocabulary has drifted since 2009; "bars" in particular is used more loosely in later usage. Bears on the `in-tradition` web_policy: judges consulting the tradition may encounter post-2009 senses. Unverified; not asserted as fact about this source.
- Proposed authority anchors: the book's own definitions (primary); the quoted practitioners (secondary).
- Dual-status members: all ~20 artists are simultaneously entity content and authority anchors — the registry needs both records.
- Sources section (p213–p214) lists an interview and reference works that may seed dossiers.

## Config fragment

```yaml
# INPUT to schema/config sessions — not live config.
sources:
  - slug: rappers-handbook                              # v1 plain
    type: book
    title: "The Rapper's Handbook, Second Edition"
    loc_grammar: "p<N>, N = printed page; printed = pdf - 10"
    text_path: null                                     # extraction is a deliverable; see ingest
    media_notes: "70 images / 68 pages; no captions; 6 part-opener plates"
# schema:v2-proposed
    ingest:
      container: born_digital
      ocr_engine: null
      columns: 1
      zone_model: "single-column body; Appendix I p215-p217 = two-column list zone + single-column intro para"
      row_clustering: {method: top-gap, gap_threshold_pt: 3.0}
      hyphenation: {style: dejustified, marker: "-"}
      repair_vocab: ["and- forth", "for- paddle"]
      preserve_patterns: ["three- or", "near- endless"]
      code_detection: null
      table_mode: "appendix lists only"
      icon_mechanism: null
      danger_classes: ["bold-loss-on-naive-extraction", "appendix-I-column-interleave"]
      fidelity_canaries:
        - "p41: The **fact** is I kick **phat** **raps**, so know **that**"
        - "p215 left column: An ax to grind ... Cold war (no interleave)"
        - "p126: heading only, zero body text"
      figure_manifest: {placements: 70, pages: 68, part_openers: 6}
      caption_pattern: null
      source_of_record: "rapper.pdf (raw binary, %PDF-1.6 verified)"
      extraction_strategy: "pdfplumber words + fontname; bold = fontname contains 'Bold'"
    chunk_boundary: chapter
    chunk_fallback_max: {unit: est_tokens, value: 4500}
    chunk_overrides:
      - {loc: "p142-p158", reason: "4903 tok > bound; split at p147 (book's own heading)"}
      - {loc: "p93-p94", reason: "two chapters share printed p93; merged at Other Techniques sub-group"}
    native_seed: ["Appendix I (~90 idioms)", "Appendix II", "Appendix III"]
    scope: {included: "p2-p220 (full book)", excluded: none}
    visual_policy: describe
    content_mode: "see content_mode_map_rappers-handbook.csv"
    mention_classes: null
    arbitration_mode: community
    single_artifact: false
    web_policy: in-tradition
    era: {bound: 2009, dated_ranges: ["p168-p179 studio gear"]}
    arbitration:
      tiebreak_preferences: {craft_term_polysemy: "split freely - pre-open fan-outs"}
      seed_path: arbitration_seed_rappers-handbook.md
engagement:
  domain: "rap craft / hip-hop lyricism"                # v1 plain
  content_license: licensed
entity_model:                                            # v1 plain
  types: [technique, gesture, drill, artist]
  root_categories: [freestyling, rhyme-craft, performing, battling, recording, writing]
  role_split: {artist: [exemplar, opponent]}
registry:                                                # v1 plain
  authority_anchors: ["book's own definitions", "quoted practitioners"]
  community_arbitration: true
  snapshot_cadence: null                                 # reserved question - not settled here
```

## Kit nominations

- **p41 (In-Rhyme/Multis scansion)** — tests the bold-loss failure mode: a worker on a naive text layer sees two ordinary lines and silently under-teaches. The canary for the whole source.
- **p126 (Poppin-Off-of-the-Top-of-the-Dome Finger Flick)** — tests figure-borne teaching: heading with zero body text. A worker must flag, not invent.
- **p215 (Appendix I)** — tests zone-scoped column repair: page-scoped bisection shreds the intro paragraph, no repair shreds the idiom list.
- **p93 (Repeating Words + Visual Wordplay)** — tests shared-page boundary handling: two teaching units, one page, page-level grammar.
- **p180–p185 (On the Mic)** — tests the `flow` fan-out: three candidate senses within six pages.

## Sidecar manifest

- `harvest_brief_rappers-handbook.md` (24 lines / ~309 tok — within the 25-line, 350-token budget)
- `content_mode_map_rappers-handbook.csv` (35 rows)
- `loc_anchors_rappers-handbook.csv` (36 rows)
- `arbitration_seed_rappers-handbook.md` (2 seeded, 2 downgraded)
- `chunk_plan_rappers-handbook.csv` (36 rows, coverage verified)

## Deviations

- **No caption pattern derived, and no caption pairings proposed.** The prompt's Ingest phase requires deriving a caption pattern (e.g. `Figure N-M:`) and proposing proximity pairings flagged `[mechanical: ...]`. This source has zero captions — mechanically verified, not assumed. A pairing count here would have been fabricated. The figure manifest ships without it; `fig:` references use printed page instead of `fig:N-M`.
- **`text_path: null` in the config fragment.** Extraction was measured and the strategy ruled, but no companion ingest session exists and this session emits conventions, not a clean-text artifact. The strategy is pinned precisely enough (`extraction_strategy` + `gap_threshold_pt` + canaries) for an ingest session to reproduce it.
- **`snapshot_cadence: null`** — a reserved open question; observed and handed off, not settled.
- **Effort forecast unit-weights are guesses**, flagged inline as such per the axis's own instruction.
- **The Group 11 ruling ships with an escalation attached** rather than as a clean convention line. Recording a ruled decision while flagging its tension with another ruled decision is not a departure from the prompt's letter, but it is unusual enough to name here.
- **COLLISION DOCTRINE INVOKED — convention-line bound exceeded: 61 against the ≤50 born_digital bound.** Master doc 241/300 lines: PASS.
  Line discipline was checked FIRST, per v2.6's instruction not to reach for the doctrine before auditing conditions 2–4. That audit found real defects and 11 lines were cut: pointers (`Sidecar: ...`, `see § Ambiguity forecast`) failing condition 2; engine-law restatements (the native-seeds law, the tiebreak ladder's status) failing condition 3; commentary no consumer acts on (edition history, cross-refs-are-edges) failing condition 4. The Effort forecast was also mis-nested as a `###` inside `## Conventions`, which inflated the count by 5 — it is a `##` section and is not counted. All tag defects cleared: 0 untagged.
  The residual 61 is concentrated in Ingest (12 lines). Every one is a measured `ingest:` field the axis mandates — per-class verdicts, gap threshold, repair vocab, preserve patterns, canaries, figure manifest, caption-pattern null result. Cutting to 50 means deleting the measurements that make the bold-loss finding traceable rather than asserted. Stopping the cut here; operator rules.
  **Counter-evidence against re-ruling the bound, recorded honestly:** v2.6 re-ruled ≤45→≤50/≤75 on the strength of one scan_ocr run, and warned that a doctrine firing on every run of a source class is a mis-set constant. This is ONE born_digital run. One data point is not a class. This overage is evidence toward a v2.7 re-measurement, not grounds for one — and this source is atypical for born_digital: its `ingest:` axis costs 12 lines rather than the ~3 the ≤50 bound assumes, because a font-level teaching signal had to be measured and proven. A born_digital source without that property would likely land near 45.

## Changelog
(empty — no post-ratification amendments)

- rappers-handbook | book | The Rapper's Handbook, Second Edition / Escher (Blake Harrison) with Alexander Rappaport / 2009 | loc-grammar: p<N>, N = printed page (printed = pdf − 10)
