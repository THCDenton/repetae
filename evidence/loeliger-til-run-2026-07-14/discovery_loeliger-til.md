# Discovery — loeliger-til (Threaded Interpretive Languages: Their Design and Implementation)
Status: conventions ratified 2026-07-14, discovery_prompt_v2.5.

## Conventions

### Identity
- slug: `loeliger-til` [inferred-confirmed]
- type: `book` [mechanical: 251 printed pages, ISBN-era Byte Books monograph]
- title/author/year: Threaded Interpretive Languages: Their Design and Implementation / R. G. Loeliger / Byte Books, 1981 [mechanical: PDF title metadata + title page]
- domain-brief contribution: A from-scratch engineering treatment of threaded interpretive language design, built on Z80 with 6800 parallels. Teaches the inner/outer interpreter split, dictionary structure, and threading mechanics, then supplies a 172-keyword reference dictionary with per-keyword machine code. Forth-adjacent by vocabulary and lineage but deliberately not Forth. [inferred-confirmed]
- Preflight attestation: environment contains only prompt + source; no other content [operator-decided, 2026-07-14]

### Ingest
- container: `scan_ocr` [mechanical: Creator=Internet Archive, Producer=LuraDocument MRC; InvisibleOCR CID font over JPX/JBIG2 page images]
- ocr_engine: unnamed; text layer supplied by the Internet Archive scan pipeline [mechanical: font table shows `InvisibleOCR` only]
- methods compared: `pdftotext -layout` vs `pdftotext -raw` on p:89 [mechanical]
- strategy: `-layout` [inferred-confirmed]. `-raw` REJECTED: on p:89 it reads the label/opcode column top-to-bottom then dumps all 40 comments as a trailing block, severing every instruction from its comment. Fatal for a book whose payload is annotated listings.
- columns / zone_model: single text column; code listings are a 4-zone row (label / opcode / operand / `;`comment) preserved only under `-layout` [mechanical]
- hyphenation: end-of-line hyphens present, 62 sites, standard justified-typesetting style [mechanical]
- repair_vocab: `{REG}` → `(REG)` over a closed register/variable token list; 176 of 210 sites repaired [operator-decided]. Raster-confirmed against p:89: text layer renders Z80 parens as braces. Semantically load-bearing — `(HL)` is a memory reference, `HL` is a register pair.
  - secondary: em-dash → hyphen inside index expressions `(IX—2)` → `(IX-2)`, 13 sites [mechanical]
  - residual 34 unrepaired braces are dominantly CORRECT rejections (prose braces: `{MODE = 0}`, `{0,...,9}`, `{A DIGIT}`). Known tail: `{H L}` (OCR-split register), `{LBEND}`, `{COUNT}`, `{MULTIPLIER}` (variable names outside the token list). Bounded, not systematic. [mechanical]
- preserve_patterns: `■` U+25A0, 613 occurrences — the book's printed symbol for one ASCII space, NOT OCR noise [mechanical + in-source proof, see Falsified priors]
- code_detection: opcode-mnemonic density + `;`-prefixed comment column [mechanical]
- table_mode: Ch.6 dictionary entries are label/value rows (`Class:` / `Function:` / …), not ruled tables [mechanical]
- fidelity_canaries (must reconstruct exactly): `LD (LBP),HL` · `RES 5,(HL)` · `JP (IY)` · `CP "LD"` · `The only token separator is an ASCII space (■)`
- caption_pattern: `Figure N.M:` — dot separator, colon terminator [mechanical: 21 matches]. The colon discriminates a CAPTION from an in-prose REFERENCE ("Figure 5.1 is the example we will pursue").
- figure_manifest: caption-derived — 21 figures, 7 tables, 13 listings [operator-decided]. See Deviations: `pdfimages` carries zero signal in this container.
- source_of_record: the raw PDF; clean text derived in-session [inferred-confirmed]
- **Per-class verdicts** (not global):
  - prose: **PASS** [mechanical: ~2,233 chars/page mean across 267 pages; 8 near-empty]
  - code_listing: **MARGINAL → PASS after ruled repair** [raster-confirmed p:89]
  - figure-adjacent: **PASS** (text layer; caption pattern derived)
  - tabular (Ch.6 template): **PASS** [mechanical: `Class:` = `Function:` = 172, exact]
  - figure manifest: **FAIL — mechanically impossible in this container** (deviation ruled)

### Location grammar
- grammar: `p:<printed page>` where `pdf_page = printed_page + 15` [mechanical]
- PROVEN: offset constant 15 across 247 of 250 numbered pages, zero drift p:1→p:251 [mechanical]
- 3+ random citations resolved: `p:1` → pdf 16 (`OVERVIEW 1`); `p:89` → pdf 104 (`ROUTINES, ROUTINES, ROUTINES 89`, independently raster-verified); `p:179` → pdf 194; `p:234` → pdf 249 [mechanical]
- Running heads encode recto/verso: odd pages carry the chapter title, even pages carry the book title — a free chapter-boundary signal [mechanical]
- Front matter uses roman numerals (i–xii); body uses arabic. Grammar covers the arabic body only; front matter is out of scope.
- figures: `fig:N.M` [inferred-confirmed, matching the source's own dot form]
- Anchor table is a deliverable: `loc_anchors_loeliger-til.csv` (251 rows, full coverage, no interpolation needed — offset is constant)

### Entity types
- Two types [operator-decided]: `keyword`, `concept`
- `keyword` — a named TIL word. Ch.6 defines 172 formally; Chs.1–5,7 teach others in prose.
  - template slots, derived from the source's own template [mechanical]: `breadcrumb, definition (←Function:), mechanism (←Z80 Code / 6800 Code), options (←Usage:), cues (←Input/Output:), dangers (←Notes:), connections, code_block, data_table`
  - source-native categorization is free: `Class:` [mechanical, 172/172] — I/O 21, Arithmetic 21, System 20, Compiler Directive (Immediate) 15, Program Control Directive (Headerless) 13, Stack 11, Memory Reference 10, Interstack 10, Subroutine 9, Defining Word 8, System Variable 8, Relational 5, Logical 4, Utility 4, Literal Handler (Headerless) 3, Vocabulary 3. Strays: `Arithmetic.` (trailing-dot OCR, fold into Arithmetic), `System (Incomplete)` (possibly the author's own annotation — registry queue).
  - `BYTES:` is OPTIONAL, not universal — 3 of 172 [mechanical]. Do not model as a required slot.
  - unit_weight: guess ~1 [flagged guess]
- `concept` — a named TIL mechanism taught in prose (threading, inner interpreter, outer interpreter, dictionary header, vocabulary, compile vs execution mode).
  - template slots: `breadcrumb, definition, mechanism, goals, procedure, connections, variations_by_source, dangers`
  - unit_weight: guess ~2 [flagged guess]

### Mention classes
- Reference-only named things: CPU architectures (Z80, 6800), other languages named for contrast (BASIC, FORTRAN, Forth), cited authors/works. [inferred-confirmed]
- Dual-status: **Z80** and **6800** are mentions AND authority anchors — the book's semantics for a keyword are defined by its machine code on these CPUs. Registry queue.

### Ontology openness & arbitration
- openness: `near-closed` [inferred-confirmed] — Ch.6 is an enumerated 172-entry dictionary; the concept set is bounded by 98 numbered sections.
- arbitration_mode: `codified` + `community` [inferred-confirmed] — the book codifies its own dictionary (primary); the Forth-family tradition is a live secondary community.
- authority_anchors: the Ch.6 dictionary entry for any keyword it defines; the Z80/6800 code body for mechanism. [inferred-confirmed]
- **web_policy: `in-tradition`** [operator-decided] — Forth-family sources may be consulted; the source's own dictionary outranks them. Evidence weighed: Forth is a living tradition documenting NEXT/DUP/CREATE across 45 years, but Loeliger's TIL deliberately differs from Forth while borrowing its vocabulary — external usage risks importing the tradition's sense over the book's.
- **tiebreak preference** (class: "TIL keyword drawn from ordinary English"): **reservation-tolerant — let harvest decide** [operator-decided]. A lean inside the ratified ladder; no ladder reorder.
- Straddling: recorded, not flattened — this source straddles `codified` (own dictionary) and `community` (Forth tradition).

### Role split
- `null` — no perspective-split entities. Single authorial voice throughout. [inferred-confirmed]

### Native seeds
- Subject Index, p:249–251, 45 entries [mechanical]
- Ch.6 dictionary, 172 entries — a second and far stronger seed [mechanical]
- Seeds are MERGE-level recall aids only; never per-span worker input (native-seeds law).
- Seed residue: index entries carry page pointers that must not be read as content.

### Scope & exclusions
- IN: `p:1–244` (Chs.1–8) [operator-decided]
- OUT: Subject Index `p:249–251` — reference apparatus [operator-decided]
- OUT: Bibliography and Notes `p:245–248` — reference apparatus; bibliography load recorded under External refs instead [operator-decided]
- OUT: front matter (roman i–xii), not addressable under the ruled grammar [inferred-confirmed]

### Content-mode map
Deliverable: `content_mode_map_loeliger-til.csv`. Ch.5 `code_listing`; Ch.6 `tabular`; Chs.2,3,4,7 `mixed`; Chs.1,8 `prose`. [mechanical + inferred-confirmed]

### Chunk plan
- boundary ladder [operator-decided]: **Ch.6 → applicable convention (one dictionary entry = one chunk)**; **Chs.1–5,7,8 → section (numbered §N.M)**
- fallback_max: **1200 tokens** [operator-decided], MEASURED against this source: Ch.6 entries median 83 / p90 144 / max 446 tok; non-Ch.6 sections mean 632 tok; page median 309 tok. The bound sits above both p90s, so only true outliers split.
- Fallback splits never cut mid-teaching-unit; each carries a `notes` reason.
- Deliverable: `chunk_plan_loeliger-til.csv` — 179 rows (172 Ch.6 entries + 7 chapter-section groups), full in-scope coverage.

### Visual policy
- **`describe`**, all figure classes [operator-decided]. License-gated: `content_license: licensed` forecloses `embed`.
- Evidence: the 21 figures are memory-layout and control-flow diagrams carrying teaching content the prose references but does not restate — e.g. `Figure 2.3: Typical memory configuration`, `Figure 2.4: Inner interpreter routines`. `ignore` would lose material.

### Alias & fan-out weather
- Suffix-bearing forms are DISTINCT words, not aliases: `END` vs `END,`; `:` `;` `;CODE`. [mechanical]
- `$` prefix marks a routine: `$CRLF`, `$KEY`, `$ECHO`, `$DISPLAY`. [mechanical]
- Dual-CPU: one keyword, two code bodies (Z80 + 6800). NOT two keywords. [inferred-confirmed]
- Hardest spans nominated for the harvest kit — see Kit nominations.

### Versioning/era
- Era-bound: 1981. Z80/6800 8-bit assembly; hexadecimal without `0x`; "microcomputer" idiom. Pre-dates ANS Forth (1994) and Forth-83 — terminology is FIG-Forth-era or the author's own. [model-knowledge, unverified → registry queue]
- No pedagogical versioning within the book. [inferred-confirmed]

### Single-artifact flag
- `false` — the book is self-contained but describes a system implemented across many routines; not a single-artifact source. [inferred-confirmed]

### External refs
- Bibliography and Notes, p:245–248 (out of scope for harvest, recorded here). Internal cross-refs ("see Figure 5.1", "as in Chapter 3") are edges, not external refs. [inferred-confirmed]

### License posture
- `content_license: licensed` [operator-decided] — 1981 Byte Books, commercially published, in copyright. Gates visual policy to describe-never-embed.

## Ambiguity forecast

Reviewed watchlist (ranked, `[mechanical]`, ≤20 rows). Full CSV: `watchlist.csv`.

| term | freq | disp | collision | home ranges | operator lean |
|---|---|---|---|---|---|
| END | 78 | 8 | 8.55 | ch6:26 ch4:25 | **expected fan-out** [operator-decided] |
| NEXT | 116 | 7 | 7.44 | ch3:31 ch5:27 ch2:23 ch6:20 | **none recorded** (no opinion) |
| ASCII | 92 | 8 | 7.81 | ch6:28 ch4:25 ch5:21 | (class default) |
| CONSTANT | 45 | 6 | 7.38 | ch2:20 ch6:9 | (class default) |
| Z80 | 204 | 7 | 7.36 | ch6:126 ch7:43 | (class default) |
| IF | 138 | 8 | 7.29 | ch6:54 ch5:35 | (class default) |
| EXECUTE | 47 | 6 | 7.14 | ch2:14 ch3:12 | (class default) |
| OK | 42 | 7 | 7.05 | ch6:13 ch4:9 | (class default) |
| FORGET | 15 | 7 | 6.72 | ch2:4 ch6:4 | (class default) |
| SEMI | 40 | 6 | 6.52 | ch3:17 ch2:12 | (class default) |
| CURRENT | 70 | 7 | 6.27 | ch6:41 ch4:12 | (class default) |
| ELSE | 92 | 7 | 6.27 | ch6:35 ch7:23 | (class default) |
| SEARCH | 28 | 5 | 6.18 | ch5:17 ch6:8 | (class default) |
| DUP | 85 | 6 | 6.07 | ch3:35 ch6:22 | (class default) |
| CODE | 75 | 6 | 6.04 | ch6:33 ch2:13 | (class default) |
| BASIC | 20 | 8 | 7.87 | ch4:4 ch7:4 bib:4 | (class default) |

**Class default** = reservation-tolerant, let harvest decide [operator-decided].

**Probe artifacts — ranked high, excluded as non-terms** [mechanical]: THREADED / INTERPRETIVE / LANGUAGES (freq 124–125, disp 10) score at the top **solely because they are the verso running head on every even page**. TIL (freq 227, disp 10) is the book's subject; ubiquity carries no ambiguity signal. Recorded as evidence that dispersion rewards page furniture — signals rank, never rule.

**Dominant ambiguity class:** this book's keyword vocabulary is drawn from ordinary English. Ch.6 defines the words formally; Chs.1–5 use them both as keywords and as English, often in one sentence. Case discriminates imperfectly (listings are all-caps).

**Exit-exam evidence lines** — every forecast names what would confirm or kill it:
- **END** → CONFIRMED if Ch.6 holds separate `Class:`-bearing entries for `END` and `END,`. KILLED if one entry covers both, or if `END,` proves an OCR artifact.
- **NEXT** → CONFIRMED as fan-out if Ch.6's `NEXT` entry describes the compiled jump while Ch.3/Ch.5 prose names the routine as a separate thing. KILLED if both describe one indivisible thing seen from two angles.
- **Dominant-class forecast** → CONFIRMED if ≥3 of {CONSTANT, DUP, EXECUTE, FORGET, CURRENT, CODE} raise a reservation during harvest. KILLED if harvest resolves all of them from Ch.6 with no reservation.
- **Effort forecast (172 keywords)** → CONFIRMED if the harvest yields 165–180 keyword entities. KILLED if it yields <150 or >200.
- **Chunk-plan forecast (fallback rare)** → CONFIRMED if <10 of 179 chunks hit the 1200-token fallback. KILLED if >25 do.

## Escalations

None open. Two candidate escalations were resolved by evidence before they needed you:
- The `■` glyph (613 sites) looked like OCR noise; the source states its meaning outright, so no ruling was needed.
- The brace/paren damage looked possibly-systematic-possibly-random; the census proved it a closed list, making it a cheap button rather than an open question.

## Registry queue

- `[model-knowledge, unverified]` Forth lineage: FIG-Forth / Forth-79 / Forth-83 / ANS Forth (1994) post-date or surround this 1981 book; its terminology is pre-standard. Needs registry verification before any cross-source alignment.
- `[model-knowledge, unverified]` `(HL)` = memory-reference semantics in Z80 assembly; `JP (IY)` is an indirect jump. Used to justify the repair ruling — verify.
- `[model-knowledge, unverified]` In Forth-family languages a trailing `,` conventionally means "compile into the dictionary", supporting `END,` ≠ `END`. Verify; the in-source evidence (separate `Class:` entries) is what actually decides it.
- Dual-status: **Z80**, **6800** — mention AND authority anchor.
- Proposed anchors: Ch.6 dictionary entry (per keyword); Z80/6800 code body (per mechanism).
- `System (Incomplete)` as a `Class:` value — author's annotation or OCR damage? Unresolved; low stakes.

## Effort forecast

~10 lines, heuristic [flagged as such].
- `keyword` entities: **172**, near-certain — the count is mechanical and exact (`Class:` = `Function:` = 172), not a density extrapolation. Rare luxury.
- `concept` entities: **~40–70**, from 98 numbered sections outside Ch.6, discounted because many sections are procedural rather than concept-bearing.
- Total: **~215–245 entities** across 244 in-scope pages.
- Openness class `near-closed` → the registry's verdict volume should be modest: the dictionary is enumerated, so most keyword verdicts are lookups, not judgments.
- The expensive sequential part is **not** the keyword mass — it's the dominant ambiguity class. Each English-derived keyword may raise a reservation, and reservations are judgment-budget, not extraction-budget.
- Ch.6's template regularity should make 172 of ~230 entities cheap and uniform. Chs.1–5,7 carry the real cost.
- Falsifiable claims carry exit-exam lines above.

## Config fragment

```yaml
# INPUT to schema/config sessions — not live config.
sources:
  - slug: loeliger-til
    type: book
    title: "Threaded Interpretive Languages: Their Design and Implementation"
    loc_grammar: "p:<printed>; pdf_page = printed + 15"
    text_path: "<derived in-session; not persisted>"
    media_notes: "scan_ocr, MRC container, InvisibleOCR text layer"
    # schema:v2-proposed
    ingest:
      container: scan_ocr
      ocr_engine: "unnamed (Internet Archive pipeline)"
      columns: 1
      zone_model: "single column; 4-zone code rows (label/opcode/operand/comment)"
      hyphenation: {style: justified_eol, marker: "-"}
      repair_vocab: ["{REG}->(REG) closed list", "(IX—n)->(IX-n)"]
      preserve_patterns: ["■ = one ASCII space (author's printed symbol)"]
      code_detection: "opcode density + ;-comment column"
      table_mode: "label:value rows (Ch.6 template)"
      fidelity_canaries: ["LD (LBP),HL", "RES 5,(HL)", "JP (IY)", "CP \"LD\""]
      figure_manifest: {method: caption_derived, figures: 21, tables: 7, listings: 13}
      caption_pattern: "Figure N.M:"
      source_of_record: raw_pdf
    # schema:v2-proposed
    chunk_boundary: ["ch6:convention(entry)", "else:section"]
    chunk_fallback_max: {unit: tokens, value: 1200}
    chunk_overrides: []
engagement:
  domain: threaded_interpretive_languages
  content_license: licensed
entity_model:
  types: [keyword, concept]
  role_split: null
registry:
  authority_anchors: ["ch6_dictionary_entry", "z80_6800_code_body"]
  community_arbitration: true
# schema:v2-proposed
native_seed: {subject_index: "p:249-251 (45 entries)", ch6_dictionary: "172 entries"}
scope: {in: "p:1-244", out: ["p:245-248 bibliography", "p:249-251 index", "front matter i-xii"]}
visual_policy: describe
arbitration_mode: [codified, community]
web_policy: in-tradition
single_artifact: false
arbitration:
  tiebreak_preferences: {english_derived_keyword: reservation_tolerant}
  seed_path: arbitration_seed_loeliger-til.md
```

## Kit nominations

Hard spans, each naming the harvest-stage failure mode it tests (topology-neutral):
1. **p:22** — `HEX ■ CREATE ■ DROP ■ E1 ■ C, ■ NEXT ■■OK`. Tests: does the worker preserve `■` as a space symbol, and does it read `NEXT` here as a keyword rather than the routine? Failure mode: **preserve-pattern loss + premature sense assignment**.
2. **p:89** — the INLINE listing containing `CP "LD"`. Tests: does the worker read `"LD"` as the Line-Delete ASCII code, not the LD opcode? Failure mode: **surface-form collision inside a code listing**.
3. **p:120** — the `+LOOP` entry with `END,` in its code body. Tests: does the worker distinguish `END,` from `END`? Failure mode: **suffix-bearing distinct word merged as alias**.
4. **p:60** — "the loop is available to the operator through the BEGIN and END". Tests: `END` as loop keyword vs. the English word two lines later. Failure mode: **English-derived keyword false positive**.

## Sidecar manifest

- `harvest_brief_loeliger-til.md` — worker-facing, 23 lines
- `content_mode_map_loeliger-til.csv` — packet-builder-facing, 10 rows
- `loc_anchors_loeliger-til.csv` — driver/merge-facing, 251 rows
- `arbitration_seed_loeliger-til.md` — arbitration-layer boot state, 2 seeded terms
- `chunk_plan_loeliger-til.csv` — packet-builder/driver-facing, 179 rows
- `watchlist.csv` — the probe's raw ranked output, 20 rows [mechanical]

## Deviations

1. **Figure manifest method** [operator-decided]. The prompt specifies `pdfimages -list` + page objects. This container defeats it: 264 of 266 pages carry exactly 3 image objects (MRC background + foreground + JBIG2 mask), so figure-bearing pages are indistinguishable from prose pages. Ruled: caption-derived manifest from the 21 `Figure N.M:` matches. Semantic verification still belongs to downstream figure workers.
2. **Caption pattern differs from the prompt's example.** The prompt illustrates `Figure N-M:`; this source uses `Figure N.M:`. Derived from the source, as specified.
3. **Ambiguity probe implemented in-session.** No shipped script matching v2.5 was present (expected, never a blocker). Throwaway written against the fixed interface; same watchlist columns. Method `[mechanical]`, script retained at `/home/claude/probe/ambiguity_probe.py`.
4. **Raster rule satisfied for the code_listing MARGINAL verdict** (p:89 confirmed). For the `■` glyph, rasters at two further pages failed to composite under this MRC container; the question was instead settled by in-source textual proof ("The only token separator is an ASCII space (■)"), which is stronger evidence than a raster. Recorded rather than ground on — per "do not grind; split".
5. **Chunk-plan Ch.6 rows** anchor on the `Class:` marker rather than the centered keyword header. First attempt matched only 156 of 172 entries (page-top keywords lack a preceding blank line). Re-anchoring on `Class:` gives exact 172/172 coverage. Keyword names in the `notes` column carry light OCR wear (`f` for `!`, `SISIGN` for `$SIGN`); locations are sound.
6. **Convention-line count exceeds the ≤45 bound: 88 lines.** Collision doctrine invoked — the excess is exhibits, counts, and per-class verdicts; cutting to 45 would delete the evidence that makes these conventions traceable rather than asserted. Total doc is 260 lines, inside the ≤300 bound. Residual reported for your ruling.
   (An earlier draft of this section claimed a ≤300 overage; the lint disproved it and the claim was withdrawn.)

## Changelog

(empty — starts at ratification)

---
`- loeliger-til | book | Threaded Interpretive Languages: Their Design and Implementation / R. G. Loeliger / 1981 | loc-grammar: p:<printed>, pdf = printed + 15`
