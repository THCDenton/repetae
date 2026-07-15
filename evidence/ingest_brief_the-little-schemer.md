# Ingest Session Brief — the-little-schemer

Status: SPLIT from discovery, 2026-07-09, by operator button ruling
(`B — Split to dedicated ingest session`), under discovery_prompt_v2.2
invariant *"Do not grind; split."*

Discovery is **halted at Stage 1 (ingest fidelity gate)** pending this
session's deliverable. No conventions were ratified. No axis was defaulted.

---

## Deliverable

1. `text_path` — a clean extraction of the source.
2. `extraction_report.md` — methods, verdicts, residues.

Discovery then re-runs against (1), recording the whole of this as a single
`[mechanical]` convention line in its Ingest axis.

---

## Source

`/mnt/user-data/uploads/The_Little_Schemer.pdf`

- 2,359,953 bytes. PDF 1.6.
- *The Little Schemer*, 4th Edition. Friedman & Felleisen. MIT Press.
  ISBN-13 9780262560993.
- 211 pages; 201 carry text.
- **Producer: `Adobe Acrobat 10.0 Paper Capture Plug-in with ClearScan`.**
  This is a **scan**. The text layer is OCR with synthesized fonts.
  Letter-level error is irreducible; layout error is not.

### Do NOT use `/mnt/project/The_Little_Schemer.pdf`
Despite the extension it is **not a PDF** — it is 205 KB of pre-extracted
plain text, produced by `pdftotext` with **no flags** against this same
scan. Default mode discards column geometry and serializes the page
column-wise, so every answer precedes the question it answers. It is a
corrupt artifact. It is retained only as evidence.

---

## Layout model (established, reuse — do not re-derive)

Page width 461pt. Body pages are **two-column dialogue**: question left,
answer right, read across. Word `x0` is cleanly bimodal at `width * 0.5`
(verified p22 / p46 / p121).

A naive two-zone split is **wrong**, because centered full-width elements
(the Laws, the Ten Commandments, front matter, preface prose) straddle the
midpoint and get sliced. 41 of 201 pages contain straddling words.

The correct model is **three zones**, decided per visual row:

| Zone | Rule |
|---|---|
| `FULL` | any word crosses the midpoint, or the row spans it without a clean gap |
| `Q` | row's words all end left of midpoint |
| `A` | row's words all start right of midpoint |

`extract2.py` implements this and it is **correct**. Keep it.

---

## The one defect to fix

**ClearScan baseline jitter breaks fixed-bin row clustering.**

Words on a single visual line have `top` values differing by 0.1–0.5pt.
True line spacing is ~11pt. `extract2.py` groups rows with
`round(top / 6)`, whose bin boundaries fall *inside* those sub-point
clusters — splitting one line across two bins, which are then independently
re-sorted by `x0`.

Observed, p135 left column (one visual line, three bins):

```
top=56.71  x0= 69.8  '((4'
top=56.89  x0= 59.8  'is'
top=56.97  x0=119.7  '(7'
```

Gap census, same column: `[11.1, 11.1, 0.2, 0.1, 0.1, 0.3, 34.6, 0.5, 10.8, 11.1, ...]`
— i.e. inter-line gaps ~11pt, intra-line gaps <0.5pt. Trivially separable.

### Symptom

p135 should read:

```
rel is ((4 3) (4 2) (7 6) (6 2) (3 4))
```

`extract2.py` emits:

```
is ((4 (4 2) (7 6) (6 2) 4))
rel 3) (3
```

Scope: **5,043** short `[A]` fragments file-wide. Systematic, not local.

### Why this is the blocking defect

An S-expression is this book's atomic unit of meaning. Shuffled parentheses
are worse than missing text: they are **silently plausible**. A downstream
harvester cannot detect the corruption.

### Fix

Replace `round(top / 6)` with **gap-based clustering**: sort word tops; start
a new row wherever the gap to the previous top exceeds ~3pt. Within a row,
sort by `x0`. Nothing else in `extract2.py` changes.

---

## Ratified, carry forward unchanged

**OCR repair whitelist** — operator-ruled
(`Repair — whitelist substitutions, tag [mechanical]`). Verified: 0 real
misses. Closed vocabulary; the book defines ~50 functions.

```
zub1 | subl | sub l   -> sub1        (but NOT `sublists`)
addl | add l          -> add1
atom ?  lat ?  null ?  zero ?  eq ?  number ?  member ?  eqan ?
eqlist ?  eqset ?  pair ?  fun ?  set ?  subset ?  revrel ?
fullfun ?  will-stop ?  equal ?      -> collapse the space
"(  car"  "(  cdr"  etc.            -> "(car"  "(cdr"
```

Census on the raw text layer: `add1` 62 / `addl` 4 (94% clean);
`sub1` 44 / `subl` 8 + `zub1` 4 (79% clean).

Emit **both** a repaired `text_path` and an unrepaired faithful copy.

---

## Acceptance tests

1. **S-expression integrity.** 20 randomly sampled S-expressions parse with
   balanced parens through a Scheme reader.
2. **The p135 canary.** Reconstructs exactly:
   `rel is ((4 3) (4 2) (7 6) (6 2) (3 4))`
3. **Q/A pairing.** p22 yields `What is (cdr l)` → `No answer.1`, and
   `where l is ()` → `You cannot ask for the cdr of the null list.`
4. **Repair, no over-reach.** `grep -c`: `addl` = 0, `zub1` = 0,
   `sublists` = 2 (untouched).
5. **Boxes intact.** `The Law of Cdr` appears as one contiguous `FULL`
   block, not split across `Q`/`A`.

---

## Known residues — record, do not chase

- Italic glyphs inside display boxes (e.g. `cdr` in *The Law of Cdr*) sit on
  a slightly different baseline and may emit as a stray one-word block.
  Cosmetic; does not affect Q/A pairing.
- Page 1 (cover art, a JPEG) OCRs as garbage:
  `Foreword bf GenW J. s-.n.a`. The true TOC line
  `Foreword by Gerald J. Sussman` is present and correct on its own page.
  Do not "repair" the cover.
- Footnote convention: `1 L: nil` — `L:` marks Lisp-vs-Scheme marginalia,
  numbered per page. Preserve; it is content.

---

## Structure confirmed present (for Discovery's later use — do not act on it here)

- 10 chapters + Intermission + Index. TOC on its own page.
- Running heads alternate `Chapter N` (verso) / chapter title (recto).
- 170 bare page-number lines.
- Front matter: *The Ten Commandments* block, copyright
  (*The Little LISPer* 1986, 1974; MIT 1996), preface with `(define atom? ...)`.
- Back matter: Index.

Location grammar is **Discovery's** call, not this session's. Observe only.

---

## Files

| Path | What |
|---|---|
| `/home/claude/extract.py` | S1, two-zone. Superseded — boxes sliced. |
| `/home/claude/extract2.py` | S2, three-zone. **Correct except row clustering.** Start here. |
| `/home/claude/schemer_text.txt` | S2 output, repaired. Has the shuffle defect. |
| `/home/claude/schemer_text_unrepaired.txt` | S2 output, faithful. Has the shuffle defect. |
| `/home/claude/scratch_notes.md` | Full session findings, both halts, provenance. |

---

## Provenance carried into Discovery's Ingest axis

```
[operator-decided] environment attestation = "Nothing else"
[operator-decided] OCR repair = whitelist substitutions, tag [mechanical]
[operator-decided] extraction = dedicated ingest session (split)
```

An earlier ruling, `extraction location = inline`, was **superseded by a
re-ask** after the inline attempt hit the two-strategy ceiling. It was not
silently remapped. Both the ruling and its supersession are recorded.

---

## Falsified priors (record, do not delete)

1. **"The Little Schemer's dialogic column structure is unrecoverable."**
   Killed by: word-coordinate bimodality in the real PDF
   (p22 117/118, p46 18/6, p121 36/96). The columns were never lost — only
   the upstream extraction lost them.

2. **"The source is corrupt."**
   Killed by: `pdfinfo` on the uploaded PDF. The *source* is a clean scan
   with an intact OCR text layer. The **artifact in project files** was
   corrupt. These are different objects, and conflating them nearly cost a
   correct source.
