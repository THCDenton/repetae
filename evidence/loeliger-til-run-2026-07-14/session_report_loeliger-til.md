# Session Report — discovery_prompt_v2.5 on `loeliger-til`

**To:** the Claude agent assisting this operator
**From:** the agent that ran the discovery session, 2026-07-14
**Re:** what this source threw at me, how I got past it, and what I'd want known before a re-run

---

## 1. The source, briefly

R. G. Loeliger, *Threaded Interpretive Languages: Their Design and Implementation* (Byte Books, 1981). 266 PDF pages / 251 printed. An Internet Archive scan, MRC-recoded by LuraDocument. Structure: five chapters of design prose interleaved with annotated Z80/6800 assembly; one 77-page rigidly-templated 172-keyword dictionary (Ch. 6); an extensions chapter; a practice chapter; then bibliography and subject index.

The short version of what makes it hard: **it is an OCR'd scan of a book whose payload is column-aligned code, and whose keyword vocabulary is drawn from ordinary English.** Both are traps a fast session walks straight into.

---

## 2. The five real challenges

### 2.1 `-raw` silently destroys the book

The single highest-consequence finding, and it would have been invisible without the prompt's "compare at least two methods" rule.

On p:89, `pdftotext -raw` reads the label/opcode column top-to-bottom, then dumps **all forty comments as a trailing block**. Every instruction is severed from its explanation. The text still *looks* fine — it's clean, well-formed, plausible English and mnemonics. Nothing errors. A session that ran `-raw` and glanced at the output would ratify conventions against rubble and never know.

`-layout` preserves the four-zone row (label / opcode / operand / `;`comment). It won decisively.

**Transferable lesson:** on any source where meaning lives in *horizontal adjacency* — code, ledgers, dialogic frames, spec tables — `-raw` is not a candidate, it's a hazard. The comparison is not a box to tick. Do it on the densest page you can find, not a random one.

### 2.2 The text layer lies politely — `(HL)` → `{HL}`

The OCR renders Z80 parentheses as braces. `LD (HL),20` becomes `LD {HL},20`. In Z80, `(HL)` means *the byte at the address in HL*; `HL` means the register pair. The paren is load-bearing, and the corruption is uniform, quiet, and semantically invisible to anything that isn't reading the assembly as assembly.

The prompt's **raster rule** is what caught it (`pdftoppm` + view on p:89, the page image plainly showing parens). I want to stress that the rule earned its keep here: I would not have escalated a MARGINAL verdict on a text layer that reads this cleanly without being *forced* to look at the page.

The census then made it a cheap ruling rather than an open question: all 210 brace-pairs contained register names, index expressions, or TIL variables (`{HL}` 59, `{IY}` 16, `{IX+0}` 12…), while parens contained prose material (`(8)`, `(16)`, `(Immediate)`). Two non-overlapping populations ⇒ **closed substitution list** ⇒ a ten-second button. 176/210 repaired; the 34 residuals are mostly *correct rejections* (`{MODE = 0}`, `{0,...,9}`, `{A DIGIT}` are genuine prose braces).

**Transferable lesson:** the gap between "I suspect damage" and "here is a closed list, 176 sites, here are the two populations" is the difference between an escalation and a button. Census before you ask.

### 2.3 Two falsified priors — both my own, both killed by evidence

This is the part I'd most want a successor to internalize, because in both cases my instinct was **wrong in the direction of seeing damage that wasn't there**.

**Prior 1: `CP "LD"` is OCR damage.** It isn't. The raster shows `CP "LD"` in the original. Loeliger's own notation: a quoted mnemonic denotes *that key's ASCII code* — `"LD"` is the Line-Delete character, not the LD opcode. Same for `"BS"`, `"CR"`. Had I "repaired" this, I'd have corrupted real content while congratulating myself on fidelity. It's now kit nomination #2, because a harvest worker will make exactly the same mistake.

**Prior 2: `■` (U+25A0, 613 occurrences) is OCR noise.** It isn't. The book says so itself, in prose I found by grepping the glyph's own contexts:

> *"The only token separator is an ASCII space (■)"*
> *"This command will enter a space (■) at the cursor point"*

Loeliger prints a black square wherever a space is semantically significant, so readers can count spaces in Forth source. The OCR preserved it faithfully. It is the prompt's `preserve_patterns` category exactly: **noise-looking content that is content**.

Note *how* prior 2 died. Two rasters failed to composite under the MRC container. Rather than grind on the toolchain — the prompt is explicit, *do not grind; split* — I asked the text what the glyph meant and the book answered in a complete sentence. **In-source textual proof beat the raster, and was stronger evidence than the raster would have been.** That's recorded as Deviation #4.

**Transferable lesson:** when a glyph looks like noise, grep its contexts before you filter it. A book about a language will often define its own notation in prose. Also: your priors about OCR damage are biased toward false positives, because damage is what you're looking for.

### 2.4 The probe's top ranks are page furniture

The ambiguity probe's highest-ranked terms were `THREADED`, `INTERPRETIVE`, `LANGUAGES` — freq 124–125, dispersion 10, identical scores. They are the **verso running head on every even page**. `TIL` (227, disp 10) is the book's subject; ubiquity there carries zero ambiguity signal.

Dispersion rewards ubiquity, and in a scanned book ubiquity means furniture. The signal wasn't wrong — it was doing exactly what it does — but it required a human-legible sentence saying *these four rows are artifacts, here's why* rather than being quietly dropped. Signals rank; they never rule. This was the live demonstration.

Strip the artifacts and the probe was genuinely good: `END` (78, ch6:26|ch4:25), `NEXT` (116, four homes), then the whole English-derived keyword class. It found the real thing.

**Transferable lesson:** budget for a de-furniture pass on any scanned source with running heads. And say the artifacts out loud in the master doc — a successor reading the watchlist cold will otherwise think `LANGUAGES` is a term worth arbitrating.

### 2.5 `pdfimages` is defeated by the container

264 of 266 pages carry **exactly 3 image objects** — the MRC triple (background JPX + foreground JPX + JBIG2 mask). Figure-bearing pages are indistinguishable from pure-prose pages. The prompt names `pdfimages -list` + page objects as the figure-manifest method; that method carries *zero information* here.

I could have produced a 794-row "figure manifest" that was really a page-scan census, and it would have looked plausible. Instead: report the impossibility, offer the alternatives (caption-derived / full-page raster CV / defer to a dedicated ingest session), take the ruling, log the deviation. Operator chose caption-derived; 21 figures via `Figure N.M:`.

**Transferable lesson:** when the prompt's named method returns a constant, that constant *is* the finding. Say so. Don't ship the constant as data.

---

## 3. What went right, and why

**The book handed me gifts that offset the OCR pain — but only because I counted instead of assuming.**

- **Pagination offset is a constant 15** across 247 of 250 numbered pages. Zero drift, p:1 → p:251. That's rare in a scan and it made the anchor table trivially exact (251 rows, no interpolation). The grammar proof landed `p:89 → pdf 104` on the very page I'd raster-verified — independent corroboration for free.
- **Ch. 6 is machine-regular:** `Class:` = `Function:` = **172**, exactly. So the effort forecast's keyword count isn't a density extrapolation, it's a census. Rare luxury; say so when it happens.
- **`Class:` gives a free source-native taxonomy** (I/O 21, Arithmetic 21, System 20, …) that maps onto the TOC's §6.2.x categories.
- **The template maps almost 1:1 onto the prompt's core slots:** Function→`definition`, Z80 Code→`mechanism`, Usage→`options`, Input/Output→`cues`, Notes→`dangers`.

But: **`BYTES:` appears 3 times in 172 entries.** My p:105 sample showed it, and if I'd generalized from that one sample I'd have modelled a required slot that's 98% absent. Counting caught it. The lesson generalizes — one beautiful sample is a hypothesis, not a template.

---

## 4. The full interview

Five button passes, thirteen decisions. Recorded verbatim, including the one that constrained me.

### Preflight — attestation
| Q | A |
|---|---|
| Does this environment contain anything besides this prompt, the source, and the listed companions? | **Nothing else** |

### Pass 1 — ingest rulings (after raster + census evidence)
| Q | Lean | A |
|---|---|---|
| Code-listing repair: raster confirms `(HL)`→`{HL}`, 210 sites, closed list, load-bearing | repair mechanically | **Repair to parens (mechanical, closed list)** |
| Figure manifest: `pdfimages` carries zero signal (264/266 pages = 3 MRC objects) | caption-derived | **Caption-derived manifest (cheap, in-source)** |

### Pass 2 — scope + entity types
| Q | Lean | A |
|---|---|---|
| Subject Index p:249–251 (45 entries, already consumed as native seed) | exclude | **Exclude — reference apparatus** |
| Bibliography and Notes p:245–248 | exclude | **Exclude — reference apparatus** |
| Entity types: 172 templated keywords + concepts in Chs.1–5,7–8 | keyword + concept | **keyword + concept (2 types)** |

### Pass 3 — license, visuals, web
| Q | Lean | A |
|---|---|---|
| License posture: 1981 Byte Books, in copyright | licensed | **licensed** |
| Visual policy: 21 memory-layout / control-flow diagrams; `embed` foreclosed by license | describe | **describe (all figure classes)** |
| `web_policy`: Forth is a living tradition, but Loeliger's TIL deliberately differs while borrowing vocabulary | in-tradition | **in-tradition** |

### Pass 4 — watchlist arbitration
| Q | Lean | A |
|---|---|---|
| `NEXT` (116, four homes): routine / keyword-that-compiles-jump / English | expected fan-out | **No opinion** |
| `END` (78): `BEGIN...END` keyword / `END,` distinct keyword / English | expected fan-out | **Expected fan-out** |
| Ambiguity class "TIL keyword drawn from ordinary English" (CONSTANT/DUP/EXECUTE/FORGET/CURRENT/CODE/IF/ELSE/OK) | — | **Reservation-tolerant — let harvest decide** |

### Pass 5 — chunk plan
| Q | Lean | A |
|---|---|---|
| `chunk_fallback_max`, measured (Ch.6 p90 144 tok; sections mean 632; page median 309) | 1200 tokens | **1200 tokens** |
| Confirm Ch.6 boundary is per-entry, not per-§6.2.x category | per-entry | **Yes — dictionary entry is the unit** |

### The one that mattered most: `NEXT` → "No opinion"

I had a lean. The operator declined to adopt it. **"No opinion" is not permission to install my lean and stamp it `[operator-decided]`** — that's the fabricated-provenance defect, the one the prompt calls critical.

So: the lean is recorded as **`none recorded`**, and `NEXT` is seeded as **`watch`** — flagged to the arbitration layer with its evidence and its exit-exam line, **no sense pre-opened**. The class preference (reservation-tolerant) did the rest of the work.

This is worth flagging to you specifically, because it's the failure mode with the most gravitational pull. You have the evidence, you have a defensible reading, the operator has effectively said "you decide" — and the tag sitting right there says `[operator-decided]`. It would feel like efficiency. It's fabrication. Twelve of thirteen answers matched my lean; the thirteenth is the only one that tested whether the provenance system means anything.

---

## 5. Advice for future sessions on this source (or ones like it)

**Do this early:**

1. **`pdffonts` first, always.** `InvisibleOCR` + JBIG2 masks told me *container = scan_ocr* in one command, before any extraction. It reframes the entire ingest phase from checkbox to deliverable.
2. **Find the densest adversarial page mechanically, then compare methods there.** I grepped opcode density to find p:89. Comparing `-layout`/`-raw` on a prose page would have shown no difference and I'd have flipped a coin.
3. **Census before escalating.** Every "should I ask?" moment resolved into either a cheap button (brace repair: closed list, two clean populations) or no question at all (`■`: the book explains itself).
4. **Grep the glyph's own contexts before calling it noise.** Twice this book defined its own notation in prose that a substring search found instantly.

**Watch for:**

- **`BYTES:` was in my first sample and in 3/172 entries.** Count every slot before templating.
- **Ch.6 keyword-header detection is fragile.** Anchoring on the centered keyword line got 156/172 — page-top keywords lack a preceding blank line. Anchoring on `Class:` gets 172/172. Use the marker that's structurally guaranteed, not the one that's visually obvious. (Keyword *names* in the chunk plan still carry OCR wear: `f` for `!`, `SISIGN` for `$SIGN`. Locations are sound; names are cosmetic since the worker reads the page.)
- **Rasters fail to composite on some pages in this MRC container** (p:89 worked, pp:22/120 didn't). Don't grind. Reach for in-source textual evidence — it's often stronger anyway.
- **Two CPUs, one keyword.** Z80 (204 hits) and 6800 both appear; same keyword, two code bodies. That's one entity. It's in the brief, but it's the kind of thing a worker gets wrong.

**Open residual for the operator:**

**88 convention lines against a ≤45 bound.** I invoked the collision doctrine and did not cut. The excess *is* the evidence — the 172/172 census, the p:89 raster proof, the brace-population split, the offset verification across 247 pages. Cutting to 45 leaves conventions asserted rather than traced, which inverts the point of the bound. Total doc is 260 lines, inside ≤300. (An earlier draft claimed a ≤300 overage too; the lint disproved it and I withdrew the claim rather than ship a false deviation. Worth doing — lint your own Deviations section against reality.)

---

## 6. Prompt feedback (v2.5)

Things that earned their keep, unambiguously:

- **The raster rule.** Caught the brace corruption. A clean-reading text layer will not volunteer that it's wrong.
- **"Compare at least two methods."** Caught the `-raw` catastrophe. Would not have looked otherwise.
- **"Signals rank, never rule."** The probe put running heads in the top three. The doctrine had the answer pre-loaded.
- **"Do not grind; split."** Two failed rasters, and instead of a toolchain rabbit hole I got a better answer from the text in one grep.
- **"Re-ask, never map."** See `NEXT`, above.

Friction worth reporting upstream:

- **The ≤45 convention-line bound may be structurally wrong for scanned sources.** Per-class verdicts, repair vocabularies, canaries, and figure-manifest stats are individually irreducible and collectively blow the budget before you reach the interesting axes. The bound seems calibrated for born-digital sources where `ingest:` is three lines. The collision doctrine absorbs it, but if scans are common, the bound will collide *every time* — and a doctrine that fires on every run is a mis-set constant, not a safety valve.
- **The prompt's caption example (`Figure N-M:`) doesn't match this source (`Figure N.M:`).** Harmless — the prompt says derive it — but a hurried session might pattern-match the example instead of the source.
- **`pdfimages -list` as the named figure-manifest method has a whole container class where it returns a constant.** Worth a parenthetical in the prompt: *if every page shows an identical object count, you're looking at an MRC scan; the method is defeated, escalate.*

---

## 7. Bottom line

Terminal state: **ratified**. Seven deliverables. Thirteen operator rulings, all button-sourced. Two falsified priors recorded rather than buried. Six deviations logged, one of them withdrawn under lint.

The book's real difficulty wasn't the OCR — OCR damage is loud once you look. It was that **the damage and the content look alike**: `{HL}` is damage, `■` is content, `CP "LD"` is content, `END,` is a distinct word and not a typo. Every one of those is a coin-flip if you decide from priors, and every one is decisive if you count or look at the page.

The prompt's discipline is what made those four calls come out right. I'd run it again on this source unchanged, minus the ≤45 bound.
