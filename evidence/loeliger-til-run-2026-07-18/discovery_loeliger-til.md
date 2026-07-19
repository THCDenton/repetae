# Discovery — loeliger-til (Threaded Interpretive Languages: Their Design and Implementation)
Status: conventions ratified 2026-07-18, discovery_prompt_v2.7.

## Conventions

### Identity
- slug `loeliger-til`; type `book` [operator-decided]
- R.G. Loeliger, *Threaded Interpretive Languages: Their Design and Implementation*, Byte Books, 1981, 266pp [mechanical: pdfinfo + title page; exhaustive]
- Domain contribution: a from-scratch design/implementation manual for Forth-family threaded interpretive languages on a Z80, built around the author's reference TIL "ZIP"; teaches inner-interpreter design, vocabularies, defining words, and a full keyword dictionary. [inferred-confirmed]
- Preflight attestation recorded: environment contains only prompt + source (no companions present). [operator-decided]

### Ingest
- container `scan_ocr`; Internet Archive scan, LuraDocument producer, InvisibleOCR text layer over full-page rasters (3390x5300 gray + JBIG2 mask) [mechanical: pdffonts + pdfimages -list; exhaustive]
- per-class verdict: prose PASS; code/tabular MARGINAL (repaired); confirmed against rasterized pp.135/150/40 [mechanical: raster vs text-layer at 3 sites; sampled]
- repair vocabulary (closed list): block-glyph -> token separator (space); "B" between caps in Formal-Definition lines -> token separator, not hex; `{HL}` -> `(HL)`; trailing `not-sign` -> soft hyphen (de-hyphenate); stray bullet/asterisk in Code -> `;` comment [mechanical: symptom census in text layer; sampled]
- accept-scan-with-repair ruling [operator-decided]
- fidelity canaries (must reconstruct): `: <sep>APART<sep>SPACE<sep>8<sep>0<sep>CDO ...`; `$KEY`, `$ECHO`, `$CRLF`; `*STACK`, `$PATCH` [mechanical: exhibits pulled from source; sampled]
- figure manifest: 19 distinct figures, caption pattern `Figure N.M: <italic title>`; distribution ch2:6 ch3:2 ch4:1 ch5:8 ch7:2; figures baked into page rasters (scan) [mechanical: caption census; exhaustive]
- second caption class present: `Listing N.M: <title>` (pseudo-code / Z80 listings), distinct from figures [mechanical: grep listing captions; sampled]

### Location grammar
- grammar: `page N` (arabic body, roman front matter i-xiii) + `§N.M[.K]` section numbering (up to 4 levels, e.g. §7.2.4.1); figures `fig:N-M`, listings `listing:N-M` [inferred-confirmed]
- PROVEN: 250 unique page anchors span printed pp.1-251; 3 random citations (p25/p92/p135) resolved to text-line offsets [mechanical: anchor build + 3-citation proof; exhaustive]
  - anchor table shipped as `loc_anchors_loeliger-til.csv` (page->line index; interpolate gap pages)
- anchor caveat: even-page running headers sometimes carry the BOOK title, odd pages the CHAPTER title; anchor table keys on page number regardless [mechanical: header format inspection; sampled]

### Entity types
- `keyword_entry` — a dictionary word: centered ALLCAPS name + labeled template (Class/Function/Input-Output/Usage/Code/Bytes[/Formal Definition]); ~172 in ch6; unit-weight small/uniform (~221 tok) [mechanical: Class:=Function:=172; exhaustive]
- `concept` — a named TIL mechanism taught in prose (threading, inner interpreter, vocabularies, defining words, virtual memory); slots: definition/mechanism/connections [inferred-confirmed]
- `figure` — captioned line-art diagram; slot: description (never embed) [operator-decided]
- `listing` — captioned code block (pseudo-code or Z80); slot: code_block [operator-decided]
- entity set ruling: keyword_entry + concept + figure + listing [operator-decided]

### Mention classes
- Z80 assembly mnemonics (POP PUSH LD INC AND OR GET DE HL) are reference-only mentions, never TIL entities [mechanical: dispersion shows GET=234/PUSH=158 concentrated in Code blocks; sampled]
- dual-status: NEXT, DUP, EXECUTE, SEMI, TOKEN are BOTH prose concepts AND ch6 keyword_entries (see Ambiguity forecast) [mechanical: cross-chapter dispersion; exhaustive]

### Ontology openness & arbitration
- openness: near-closed (the keyword set is a fixed dictionary; concepts are bounded by the book) [inferred-confirmed]
- arbitration mode `codified` (the book is its own ground truth for ZIP's keyword semantics) [inferred-confirmed]
- `web_policy: in-tradition` — Forth/TIL is a living tradition the web documents; scope the harvest judges' web license to that tradition, not to ZIP-specific claims [operator-decided]
- tiebreak preference: aggressive fan-out pre-opening for triple-status terms (this source) [operator-decided]

### Role split
- n/a — no perspective-split entities; single authorial voice throughout. [default]

### Native seeds
- back-matter Index (2-col, `Term page[,page]` + sub-entries) — MERGE-level recall aid only, never per-span input [mechanical: tail-of-book inspection; exhaustive]
- §6.2 "A Classy Cross Reference" (keyword-by-class lists) — second recall seed [mechanical: TOC + p174; sampled]
- ch6 dictionary itself is a de-facto keyword glossary (172 headers) [mechanical: entry-header census; exhaustive]

### Scope & exclusions
- INCLUDE ch1-6 (core teaching + dictionary) [operator-decided]
- INCLUDE ch7 "EXTENSION PLEASE" (p180-243) as concept-teaching (assembler/editor/VM case study) [operator-decided]
- EXCLUDE Bibliography/Notes (p244) [operator-decided]
- EXCLUDE Index from harvest (retained as recall seed only) [operator-decided]

### Content-mode map
- per-section modes shipped in `content_mode_map_loeliger-til.csv`; ch5 = code_listing-dominant, ch6/6.2 = tabular, ch1 = prose, ch2-4/7 = mixed [mechanical: TOC + sampled pages; sampled]

### Chunk plan
- boundary ladder: chapter -> section (§N.M) -> one keyword_entry (ch6); oversized-section fallback bound ~1500 tokens, split at least-bad ruled boundary [operator-decided]
  - plan shipped as `chunk_plan_loeliger-til.csv`; every in-scope range in exactly one chunk
- dictionary units ~221 tok each and uniform -> one keyword_entry per chunk (172 units) [mechanical: avg chars between Class: markers; exhaustive]
- prose sections exceed the 1500-tok fallback (e.g. §4.1 ~14.5k tok); plan MATERIALIZES 85 page-bounded slices at §-boundaries rather than deferring the cut [mechanical: page-count x 560 tok/pg; exhaustive]

### Visual policy
- ruling `describe` for all 19 figures; license-gated (licensed -> describe-never-embed) [operator-decided]

### Alias & fan-out weather
- sigil-bearing names ($ * : ; @ ! # < > + .) are whole names; $ = machine-code subroutine per author's own statement p75 [mechanical: p75 self-statement + sigil census; sampled]
  - 2-3 hardest spans nominated in Kit nominations section

### Versioning/era
- era-bound: Z80 / 1981 microcomputer context; ZIP reference implementation; no pedagogical versioning within the book [inferred-confirmed]

### Single-artifact flag
- n/a — full multi-chapter book, not a single-artifact source. [default]

### External refs
- Bibliography present (p244) but excluded; internal cross-refs (figure/listing/section) are edges, not external refs [operator-decided]

### License posture
- `licensed` (1981 Byte Books commercial title) — gates visual policy to describe-never-embed [operator-decided]

### Falsified priors
- PRIOR "splitlines() safe for this text" — FALSE: form-feed splits header from its page number; use split('\n'). Killed by cat -A. [mechanical: byte inspection; exhaustive]
- PRIOR "all 172 entries carry Formal Definition" — FALSE: only ~43 do (primitives defined in Z80 only). Killed by field census. [mechanical: Formal Definition:=43 vs Class:=172; exhaustive]

## Ambiguity forecast
Watchlist (dispersion across 7 chapters; signals rank, never rule):
- NEXT | disp=116/6ch | collision: concept+asm+keyword | homes §2,§3,§5,§6 | [mechanical: dispersion; exhaustive] — exit: distinct §3 primitive-sense vs §6 entry confirms fan-out
- DUP | 63/6ch | keyword+stack-op mention | §6,§2,§3,§7 | [mechanical: dispersion; exhaustive] — exit: §6 entry + inline mentions in >=2 ch
- TOKEN | 55/6ch | routine+concept+keyword | §5,§6,§3 | [mechanical: dispersion; exhaustive] — exit: §5 "Token Extracting" sense vs §6 entry
- EXECUTE | 34/6ch | concept+keyword | §2,§3,§6 | [mechanical: dispersion; exhaustive] — exit: §3 prose-sense vs §6 entry
- SEMI | 40/6ch | return-primitive+keyword | §2,§3,§6 | [mechanical: dispersion; exhaustive] — exit: ";S" primitive defined + §6 listed
- DROP,COLON | ~37/6ch | keyword+concept | §6+prose | [mechanical: dispersion; sampled] — exit: ":" defining-word sense vs literal entry
Per-term operator lean: pre-open fan-outs (aggressive) [operator-decided].
Per-class tiebreak: split-appetite HIGH for triple-status terms [operator-decided].

## Escalations
- none blocking. One flagged for read-back: config schema not reachable this session (see Deviations).

## Registry queue
- [model-knowledge, unverified] "ZIP is Loeliger's Z80 Forth-family TIL; TIL ~ Forth lineage" — route to dossier for web verification under in-tradition policy.
- proposed anchors: NEXT, DUP, EXECUTE, SEMI, TOKEN (dual-status keyword/concept) — dossier to confirm senses.

## Effort forecast
- expected entities ~172 keyword_entry + ~30-45 concept + 19 figure + ~10-15 listing ~= 230-250 entities (heuristic).
- openness near-closed -> low arbitration volume EXCEPT the ~6 pre-opened fan-outs.
- judgment budget: dominated by ch6 dictionary verification (172 sequential entries); repair-vocabulary application is the expensive ingest tax. Falsifiable: if ch6 yields materially <150 or >200 entries, the 172 count (exhaustive) was mis-scoped.

## Config fragment
```
# NOTE: pipeline_config_schema_v2.md was NOT reachable this session.
# Fields below are written plain as contract per axes checklist; field STATUS
# unverified against schema (see Deviations). No v3-proposed minted (no field
# genuinely absent from a schema I could read).
sources[loeliger-til]:
  type: book
  title: "Threaded Interpretive Languages: Their Design and Implementation"
  author: "R.G. Loeliger"
  year: 1981
  loc_grammar: "page N + §N.M[.K]; fig:N-M; listing:N-M"
  content_license: licensed
  web_policy: in-tradition
  ingest:
    container: scan_ocr
    engine: InvisibleOCR (IA/LuraDocument)
    columns: single (dictionary = label+content two-zone)
    hyphenation: soft-hyphen (not-sign marker), de-hyphenate at line end
    repair_vocab: [blockglyph->sep, B-between-caps->sep, "{HL}->(HL)", bullet->semicolon]
    preserve_patterns: [sigil-names, token-separator]
    canaries: ["$KEY","$ECHO","*STACK","$PATCH",": <sep>APART<sep>SPACE<sep>8..."]
  entity_model:
    types: [keyword_entry, concept, figure, listing]
  chunk_plan:
    ladder: [chapter, section, keyword_entry]
    fallback_max_tokens: 1500
  registry:
    seeds: [index, cross_reference_6_2]
    arbitration_mode: codified
```

## Kit nominations
- p135 APART/ASCII entries — tests OCR block-glyph token-separator repair (Formal Definition reconstruction failure mode).
- p150 code entry with Z80 + Formal Definition — tests mention/entity boundary (asm mnemonic vs TIL keyword).
- §6 NEXT/DUP entries adjacent to §3 prose usage — tests fan-out arbitration (same surface, distinct sense).

## Sidecar manifest
- harvest_brief_loeliger-til.md
- content_mode_map_loeliger-til.csv
- loc_anchors_loeliger-til.csv
- arbitration_seed_loeliger-til.md
- chunk_plan_loeliger-til.csv

## Deviations
- Config schema (`pipeline_config_schema_v2.md`) was NOT reachable this session. Per the schema-boundary rule I did NOT reconstruct a remembered field list: config-fragment fields are written plain as contract, their schema STATUS is unverified, and no `v3-proposed` tag was minted (no field genuinely absent from a schema I could read). Operator/schema-session should verify field status. FLAGGED, not guessed.
- Run executed as a supervised interview to the extent the interface allows; all 12 operator rulings were captured via button groups. No free-text was mapped onto a lean.
- Chunk plan avoids the "defer instead of chunk" defect (v2.7 docket): oversized prose sections are materialized as 85 real page-bounded slices, not marked "split later."

## Changelog
(empty)

- loeliger-til | book | Threaded Interpretive Languages: Their Design and Implementation / R.G. Loeliger / 1981 | loc-grammar: page N + §N.M[.K]
