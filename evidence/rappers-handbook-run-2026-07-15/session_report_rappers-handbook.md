# Session report — `rappers-handbook` discovery run (v2.6)

**To:** the Claude assisting the operator
**From:** the Claude that ran it
**Date:** 2026-07-15
**Terminal state:** ratified
**Source:** *The Rapper's Handbook, 2nd Ed.* (Flocabulary, 2009), 230pp, born-digital InDesign CS2

---

## 1. What this source is, and why it isn't what it looks like

Uploaded as `rapper.pdf` — **the filename is a red herring.** It matches co-author Alexander Rappaport's surname, not the title. Identity came from the copyright page. If you inherit this source, don't let the slug come from the filename.

It reads like a soft source (a fun book about rapping) and behaves like a hard one. The hardness is not where you'd look for it.

---

## 2. The challenges, in the order they bit

### 2.1 The core finding: the text layer destroys the teaching

**This is the one thing to carry forward.** This book teaches by **bolding the rhyming syllables inside real lyric excerpts**. The bold *is* the pedagogy.

`pdftotext -layout` and `-raw` — the two tools anyone reaches for first — **silently drop the bold** and emit clean, plausible, undifferentiated text. Nothing errors. Nothing looks wrong. A downstream worker would read two ordinary lines and never know the book was pointing at something.

| Strategy | Verdict |
|---|---|
| `pdftotext -layout` | **FAIL** — bold lost silently |
| `pdftotext -raw` | **FAIL** — bold lost silently |
| pdfplumber + `fontname` | **PASS** |

How I caught it: **the raster rule.** The v2.6 prompt mandates that any MARGINAL/FAIL per-class verdict be confirmed against a rasterized page. I had no FAIL yet — the text looked fine. I rasterized anyway, on the theory that *a scansion book must be marking syllables somehow, and I can't see any marks*. The raster showed `The **fact** is I kick **phat raps**, so know **that**`. The text layer had shown me none of it.

**Advice:** the raster rule is written as a confirmation step for suspected failures. Treat it as a **detection** step when the source's pedagogy has a visual channel. Ask "how does this book point at things?" before trusting any extraction. Silent fidelity loss doesn't announce itself — that's the definition.

### 2.2 Measure, don't guess — twice, and the second one caught *me*

**Gap threshold.** Font-aware extraction initially shredded lines: bold words dropped onto their own rows because the bold subset sits fractionally off-baseline. I could have guessed a threshold. I measured instead: intra-line jitter **≤0.9pt**, true line breaks **≥12.7pt**, no overlap. Ruled `gap_threshold_pt: 3.0` — enormous margin, defensible, reproducible.

**Chunk sizes — where I was wrong.** I estimated max chapter ≈4,000 tok from a page average and asked the operator to rule a 4,500 fallback on that basis. They took my lean. Then I ran the real per-chapter census: **`Guide to Battling` = 4,903 tok — over the bound I'd just gotten ruled on my own bad number.**

I did *not* quietly widen the bound or quietly split. The plan takes a `fallback_split` at the book's own heading (p147), and I surfaced the error in the read-back with the option to re-rule to 5,000.

**Advice:** run the expensive measurement **before** the button group that depends on it. Page-averages lie about the tail, and the tail is exactly what a fallback bound is for. I got the right outcome by the wrong route.

### 2.3 The bound blew, and the honest move was to audit myself first

Final lint: **61 convention lines against the ≤50 born_digital bound.**

v2.6 explicitly warns against reaching for the collision doctrine before auditing your own line discipline. So I linted myself with a script rather than eyeballing it, and **the lint was right and I was wrong** — 11 lines were genuine defects:

- **Pointers** failing condition 2 (`Sidecar: ...`, `see § Ambiguity forecast` — they point, they don't assert)
- **Engine-law restatements** failing condition 3 (the native-seeds law, the tiebreak ladder's status — true of the engine, not of this source)
- **Commentary** failing condition 4 (edition history, "cross-refs are edges")
- **A mis-nested `### Effort forecast` inside `## Conventions`** — inflating the count by 5. The spec says that section isn't counted; I'd made it countable by putting it in the wrong place.

Residual after cutting: 61, concentrated in **Ingest (12 lines)** — all mandated `ingest:` fields. Cutting to 50 means deleting the canaries and per-class verdicts, i.e. the evidence that makes the bold-loss finding *traced* rather than *asserted*. Doctrine invoked, residual reported, operator rules.

**And I recorded counter-evidence against my own overage:** v2.6 re-ruled ≤45→≤50/≤75 on the strength of *one* scan_ocr run, then warned that a doctrine firing on every run of a class is a mis-set constant. **This is one born_digital run. One run is not a class.** This source is atypical — its `ingest:` axis costs 12 lines because a font-level teaching signal had to be proven; a normal born_digital source lands near 45.

**Advice:** write the lint as a script and run it on yourself. I'd have defended those 11 lines in prose. The script didn't care. Also: when your run produces evidence that would conveniently re-rule a bound in your favor, say out loud why it isn't enough yet.

### 2.4 The spec assumed captions; the source has none

The Ingest phase mandates deriving a caption pattern (`Figure N-M:`) and proposing proximity pairings flagged `[mechanical: ...]`.

**This source has 70 images and zero captions.** The 11 hits for "Figure" are the ordinary verb ("figure out"). Verified mechanically across `Figure [0-9]`, `Fig.`, `Diagram`, `Table [0-9]` — all zero.

I emitted `caption_pattern: null` and **proposed no pairings**. A pairing count here would have been fabricated provenance — the critical defect class. Logged as a Deviation and docketed for v2.7.

**Advice:** when the spec mandates producing an artifact and the source can't support one, the null result *is* the finding. Write it down with its evidence. Don't manufacture the artifact to satisfy the checklist, and don't silently skip it either.

### 2.5 My own tooling failed twice — the source was fine both times

- **Running-head grep returned ~nothing.** I nearly recorded "no running heads." Cause: my regex missed the **curly apostrophe** in `RAPPER'S`. Source fine.
- **Two-column gutter detector found "single column"** on Appendix I — which I had *watched* interleave. Cause: wrapped continuation lines polluted the x0 histogram. The **raster overruled my script.**

Both recorded as falsified priors with what killed them.

**Advice:** when a mechanical probe contradicts what you've directly observed, **suspect the probe.** Cheap first, judgment second — but judgment *verifies*, and here judgment was right and the script was wrong. Also: curly quotes. Always curly quotes.

### 2.6 Genuine per-class heterogeneity

Verdicts are per class, not global, and this source proves why:

| Class | Verdict |
|---|---|
| Prose | PASS |
| **Lyric scansion (core)** | **PASS on strategy 3 only** |
| `droppin' knowledge` sidebar | PASS (ragged wrap = text flowing around drawn speech-bubble art, not corruption) |
| Gesture procedures | PASS as text / **teaching absent from text** |
| **Appendix I idiom list** | **FAIL until zone-scoped repair** |
| Appendix II/III | PASS |

Two subtleties worth stealing:

- **Appendix I is a *mixed zone***: single-column intro paragraph **above** a two-column list. Page-scoped bisection shreds the intro; no repair shreds the list. The repair must be **zone-scoped**. I only found this because I checked what my own fix broke.
- **Partial bolding is a source property, not extraction loss.** On p50 only `flow's cold` is bold while other multis in the same excerpt aren't. I rastered before asserting either way. Had I trusted the text layer I'd have reported a fidelity bug that doesn't exist.

### 2.7 Visual dependency that `ignore` would have deleted

Printed **p126** is a heading — `The Poppin-Off-of-the-Top-of-the-Dome Finger Flick` — plus a full-page illustration and **zero body text**. The entire instruction (hand position, motion arrows) is in the drawing.

The `Hand Gestures` chapter (p122–p134, 6 illustrations) is a genuine teaching chapter that text extraction reduces to a list of funny titles. This became the decisive exhibit for the visual-policy button.

### 2.8 The probe's top two rows were both false positives

The in-session ambiguity probe (no shipped script; companion 5 absent — expected, never a blocker) ranked:

| term | count | disp | collision | outcome |
|---|---|---|---|---|
| `verse` | 86 | **21** | none | **DOWNGRADED** |
| `spit` | 86 | **20** | none | **DOWNGRADED** |
| `flow` | 110 | 17 | **YES** | **SEEDED** |
| `bar` | 17 | 6 | **YES** | **SEEDED** |

**The finding worth carrying to the next source: on a house-vocabulary source, dispersion measures ubiquity, not ambiguity.** `verse` and `spit` outranked `flow` on dispersion while being completely unambiguous — they're the book's house words, so they're everywhere. The signal that actually predicted trouble was **collision** (distinct local contexts in distant ranges): `flow` as craft term (own 12pp chapter) vs. plain verb (*flow for as long as you can*) vs. physiological (*salvia flowing*) — three senses within six pages of "On the Mic."

Downgrades recorded, not deleted, with an exit exam: **if this repeats on a second source, rank on collision and demote dispersion to a tiebreak.**

---

## 3. The full interview (12 button groups, 4 passes)

Every ruling below is a button. Free-text was context only. Evidence and lean preceded every group.

### Preflight

**Q0 — Attestation.** *Does this environment contain anything besides this prompt, the source, and companions?*
→ **`Nothing else`** → recorded as a provenance line under Identity, proceeded.

*(Source integrity check passed without a button: `%PDF-1.6` magic bytes matched the claim — a raw binary, not a platform-mangled text extraction. No re-provisioning ruling needed.)*

### Pass 1 — license, visual, scope

**Q1 — License posture.**
Evidence: all-rights-reserved front matter; Discography carries **per-song clearances from EMI April Music, EMI Blackwood Music, Morley Music**, each marked *All Rights Reserved / International Copyright Secured*. ~21 lyric excerpts are third-party copyrights licensed to Flocabulary for this book only. We hold no license. Lean: `licensed`.
→ **`licensed`** — *took lean*

**Q2 — Visual policy.**
Evidence: p126 = heading + full-page drawing + zero body text; `ignore` deletes a teaching chapter; `embed` reproduces van Hée's artwork under an all-rights-reserved posture. Lean: `describe`.
→ **`describe`** — *took lean* (license-gated to describe-never-embed anyway)

**Q3 — Scope: Part Five (Setting up a Studio, p168–179).**
Evidence: 2009 gear advice, era-bound, arguably not craft. Against: promised part of a "comprehensive" handbook. Lean: exclude Studio, keep On the Mic.
→ **`Include both (full book in scope)`** — **OVERRODE MY LEAN**
*Consequence:* killed my "expected out-of-scope span" sampling assumption. Recorded as a falsified prior with the operator's ruling as what killed it.

### Pass 2 — ontology, web, chunking

**Q4 — Openness + arbitration mode.**
Evidence: living oral tradition; book defines its own terms but the community owns them; no academic canon. Lean: open + community.
→ **`open + community`** — *took lean*

**Q5 — `web_policy`.**
Evidence *for* `open`: living, heavily web-documented tradition. *Against*: 2009 snapshot, and hip-hop vocabulary drifts — judges could import 2026 senses into a 2009 source. Lean: `in-tradition`.
→ **`in-tradition`** — *took lean*

**Q6 — Chunk boundary + fallback.**
Evidence (from a page-average — **this is the one I got wrong**): max chapter ≈4,000 tok, median ≈1,200, 52.2k book. Lean: chapter / 4,500.
→ **`chapter / fallback 4,500 tok`** — *took lean*, **then the real census said 4,903. See §2.2.**

### Pass 3 — watchlist-driven arbitration

**Q7 — `flow` lean.** (disp 17, count 110, collision confirmed)
→ **`no opinion`** — **ABSTENTION**

**Q8 — `bar` lean.** (disp 6, count 17, `16 bars` vs one written line)
→ **`no opinion`** — **ABSTENTION**

> **The most important thing I did all session:** I recorded both as `lean: no opinion`. I did **not** map the abstention onto my own "expected fan-out" lean and tag it `[operator-decided]`. That's fabricated provenance — the defect class v2.6 calls critical. The seed blocks carry the abstention explicitly and let the mechanical evidence stand on its own. **If you take one behavioral lesson from this report, take this one.**

**Q9 — Tiebreak preference, craft-term-polysemy class.**
→ **`Split freely — pre-open fan-outs`** — *took lean*
This ruling did real work: it's what licensed seeding `flow` and `bar` on **mechanical evidence alone**, despite the operator having no opinion on either term.

### Pass 4 — entity model

**Q10 — Entity types.**
Evidence: named techniques (Multis, Slant Rhyme), named gestures (Ninja Star, Kweli Finger Wag), games/drills, ~17 reference-only artists. Lean: 3 types + artist as mention class.
→ **`technique / gesture / drill / artist`** — **OVERRODE MY LEAN**. Artist promoted to full entity type. Mention classes → **null**. Dual-status (entity + registry anchor) routed to the registry queue.

**Q11 — `droppin' knowledge` sidebars.** (25×, verbatim third-party quotes, under `licensed`)
Lean: skip on sight, registry anchor only.
→ **`Harvest as entity content`** — **OVERRODE MY LEAN**

**Q11-RE-ASK.** I re-asked once, with the license context explicit, offering `Harvest the claim, not the words` / `Harvest verbatim` / `Reverse: skip on sight`.
→ **`Harvest verbatim — quotes reproduced in entity content`** — **OVERRODE MY LEAN AGAIN**

> **How I handled the disagreement.** Ruled twice, with the license in view the second time → **it ships as ruled**, `[operator-decided]`. I did **not** ask a third time (that's badgering) and did **not** quietly write my own preference (that's the fabrication defect). I attached an **Escalations entry**: evidence both ways, my lean stated (*harvest the claim, attribute the speaker, don't reproduce the words*), flagged for whoever runs harvest with the license facts in hand.
>
> The tension is real: the same `licensed` posture that blocked embedding van Hée's drawings now permits reproducing EMI-cleared lyrics and interview text — same underlying rights, opposite treatment. The operator may hold license facts the session can't see. **The escalation is the honest exit: the ruling stands, the conflict is on the record.**

**Q12 — Appendix I (~90-idiom two-column list).**
→ **`Native seed only — not harvested as entities`** — *took lean*

### Interview scorecard

- **12 groups + 1 re-ask.** 8 took my lean, **3 overrode it**, 2 abstained.
- **~25% override rate is healthy** — it means the buttons were genuinely choosable, not theater. If everything takes your lean, you're probably not presenting options evenhandedly.
- **All 3 overrides had consequences I had to absorb**, not argue with: one killed a sampling assumption, one restructured the entity model, one required an escalation.

---

## 4. Advice for the next session

1. **Ask how the source *points*.** Before trusting any extraction, find the pedagogical marking channel. Bold, color, position, arrows. If it has one, the text layer may be lying politely — raster to *detect*, not just to confirm.
2. **Measure before the button, not after.** My chunk-bound estimate was wrong and the real census caught it *after* the operator had already ruled on my bad number. Right outcome, wrong route.
3. **Lint yourself with a script.** I'd have defended those 11 bad lines in prose all day. The script didn't care. Conditions 2–4 of the convention-line test catch real slop.
4. **Check your own tooling before blaming the source.** Two probes failed; the source was fine both times. Curly apostrophes; histogram pollution.
5. **A null result is a finding.** No captions → `caption_pattern: null` + evidence. Don't manufacture an artifact to satisfy a checklist; don't silently skip it either.
6. **`no opinion` means `no opinion`.** Never promote an abstention to your own lean. Not once.
7. **When a ruling conflicts with another ruling, escalate — don't re-ask forever and don't quietly override.** One re-ask with fresh framing, then the ruling ships with the conflict documented.
8. **Argue against your own convenient conclusions.** My overage would have been convenient evidence for re-ruling the bound. One run is not a class. Say so out loud.

---

## 5. Docketed for v2.7 (one evidence point each — recorded so nobody re-derives them cold)

- **The bounds may need a per-axis allowance, not just a container class.** ≤50 born_digital assumes `ingest:` costs ~3 lines. It cost **12** here because the source encodes teaching in a **font attribute** — a property of *how a source teaches*, not of its container, and container class is the only thing the bound keys on. **One data point.** Next born_digital run confirms or kills it.
- **The prompt assumes captioned figures.** Ingest mandates deriving a caption pattern and proposing pairings. This source: 70 images, zero captions. Both instructions inapplicable — not ambiguous, just unmet. Needs an explicit `caption_pattern: null` path rather than leaving the run to notice. **One artifact, one reader.**
- *(Prior-run docket item, independently supported here: **chunk-plan rows may defer instead of chunking.** This run did not defer — `Guide to Battling` took a real `fallback_split` at a real heading with a reason in `notes`. Offered as a second witness that the lint — `boundary_type: section` with `est_size` > `chunk_fallback_max`, detectable by arithmetic — is the right fix.)*

---

## 6. Deliverables

| File | Status |
|---|---|
| `discovery_rappers-handbook.md` | 244/300 lines PASS · **61/50 convention lines — doctrine invoked, reported** · 0 untagged · 0 bare `[mechanical]` |
| `harvest_brief_rappers-handbook.md` | 24/25 lines PASS · ~309/350 tok PASS · no seeds/forecasts/arbitration |
| `arbitration_seed_rappers-handbook.md` | 2 seeded, 2 downgraded · never enters a worker packet |
| `chunk_plan_rappers-handbook.csv` | 36 rows · 219/219 pages · exactly-once verified |
| `loc_anchors_rappers-handbook.csv` | 36 anchors · offset proven 203/203, zero exceptions |
| `content_mode_map_rappers-handbook.csv` | 35 rows · enum pinned |

**Registration line:**

```
- rappers-handbook | book | The Rapper's Handbook, Second Edition / Escher (Blake Harrison) with Alexander Rappaport / 2009 | loc-grammar: p<N>, N = printed page (printed = pdf − 10)
```

**The single highest-value artifact of this run is the bold-loss finding** (§2.1) — it's the canary, the kit's first nomination, and the reason `text_path` couldn't be a checkbox. Everything else is bookkeeping around it.
