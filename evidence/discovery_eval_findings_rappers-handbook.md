# Discovery evaluation — rappers-handbook

Adversarial read of the 2026-07-15 discovery output (discovery_prompt_v2.6) against the source
binary. Purpose: inform future discovery prompt revisions. Findings are ordered by portability —
what generalizes to the next source first, what's local to this one last.

Method: verified every mechanical claim that could be re-run against `rapper.pdf`; ran the two
seeded exit exams to their stated conditions; ran a cold-read goldfish test (harvest brief + one
chunk, no other context) on the Hand Gestures chapter (p122–p134).

**Verdict: ships, with one real defect.**

---

## 1. Findings that should change the discovery prompt

### 1.1 A census that counts occurrences is not a census that tests a frame — PROMPT DEFECT

The brief asserts: *"Gestures are always 'The <Name>'"*. The discovery doc backs this with
`[mechanical: heading census in p122–p134]`.

The headings in that exact range:

| loc | heading | fits `The <Name>`? |
|---|---|---|
| p124 | The Ninja Star | yes |
| p125 | Variation: The Kweli Finger Wag | child frame |
| p126 | The Poppin-Off-of-the-Top-of-the-Dome Finger Flick | yes |
| p128 | The Mos Def You-Don't-Wanna-Mess Wave | yes |
| p130 | The Slim Shady Chop | yes |
| p132 | The Tonedeff Fast-Finger-Piano-Playa | yes |
| p133 | **Other Techniques: The Bob and Point** | **no — prefixed** |
| p134 | **Pantomiming** | **no — no article, no name-frame** |

Two of eight break the frame. The census found the headings and did not test the rule against them.
The mechanical tag is doing work it didn't earn: it certifies that counting happened, not that the
generalization survived the count.

**Consequence, observed:** on cold read, `Pantomiming` was nearly skipped. It is a taught, named
technique with a procedure and a failure mode ("you'll look like a French mime"). A worker holding
"gestures are always `The <Name>`" has an active reason to discard it. The brief's most confident
line is the line that loses an entity.

**Generalizable rule for the prompt:** when an alias/frame convention is asserted with a universal
("always", "fixed frame", "invariant"), the mechanical evidence must be the *exceptions column* —
the enumeration of members that do NOT fit — not the count of members that do. A frame claim with
no exception census is unverified. If the exception set is non-empty, the convention line must
carry the exception, or the universal must be downgraded to "usually" and the worker instruction
must not depend on the frame.

**Suggested prompt language:** *For each frame/alias convention, emit the count of conforming
members AND the enumerated list of non-conforming members. A frame convention may not ship with a
universal quantifier unless the non-conforming list is empty and that emptiness was tested.*

### 1.2 Dispersion measures ubiquity, not ambiguity — CONFIRM AND PROMOTE

The session's own probe finding, restated because it is the most portable thing it produced:

- `verse` (dispersion 21, count 86) — DOWNGRADED, single stable sense
- `spit` (dispersion 20, count 86) — DOWNGRADED, single stable sense
- `flow` (dispersion 17, count 110) — SEEDED, collision YES → **exam CONFIRMED**

The two top-ranked rows by dispersion were both false positives. The signal that predicted real
trouble was **collision** (distinct local contexts in distant ranges), not spread.

This evaluation supplies the second data point the session asked for. It is a *confirming* data
point but from the same source, so it does not discharge the "one source is not a class" caveat —
what it does show is that the mechanism is understood well enough to be predictive: `flow` was
seeded on collision and its exam confirmed; `bar` was seeded on collision and its exam killed
(see 1.3). Collision predicted the *interesting* cases in both directions. Dispersion predicted
nothing.

**Recommendation:** rank the ambiguity watchlist on collision. Demote dispersion to a tiebreak.
Do not wait for a third source — the failure mode of the current ranking is that it puts house
vocabulary at the top of every list on every source that has house vocabulary, which is most of
them. The cost of the change is low; the cost of the status quo is an operator asked to rule on
two false positives before reaching the real one.

### 1.3 A seed whose own exit exam has already failed should carry the result — PROMPT GAP

`bar` was seeded as a fan-out. Its stated KILLED condition:

> KILLED if the book consistently uses one sense and the other reading came only from quoted
> lyrics rather than the book's own teaching voice.

Run against the source:

- **p199–p208** (unit-of-song-structure sense) — present, repeatedly, in the book's teaching voice:
  "There are the intro and outro bars", "of 16 to 32 bars each", "or 8 bars before the rapper spits".
- **p39–p53** (claimed single-lyric-line sense) — **one** hit, book-wide, in that entire range:
  *"their bars rhyming multisyllabically"* — inside a `droppin' knowledge` sidebar. Practitioner
  quotation, not the book's own teaching voice.

That is the KILLED condition, matched verbatim. The seed's second home range is a quotation
artifact.

The seed survives only because the operator's class ruling (**split freely — pre-open fan-outs**)
licenses pre-opening on mechanical evidence alone. That is a legitimate, recorded ruling and it
stands. But the seed as written hands arbitration a live hypothesis whose exam was already
answerable at discovery time, with no note that it was answered.

**Generalizable rule for the prompt:** a seed's exit exam should be *run at discovery* whenever the
evidence to run it is already in hand, and the result recorded on the seed. A seed may still be
pre-opened by operator ruling after a negative exam — but the seed must say so:
`exam: pre-run at discovery, KILLED condition matched; seeded anyway per operator class ruling`.
An unrun exam and a failed-but-overridden exam are different objects and arbitration needs to tell
them apart.

**Sharper version of the same point:** the tiebreak preference (`split freely`) was ruled at the
*class* level before the *instance* evidence was examined. A class-level ruling that licenses
pre-opening will always produce seeds; it removes the seeding decision from evidence entirely. The
prompt should ask the operator for the class preference *and* still require per-instance exam
results, so the operator's ruling is applied to a known fact rather than an open question.

### 1.4 Sticky notes should cover string collisions in the *pile*, not just senses in the book

`Other Techniques:` appears as:

1. A **heading prefix** inside the Hand Gestures chapter (p133, `Other Techniques: The Bob and Point`).
2. The **book's own sub-group name** governing the p93 shared-page merge (`Alliteration`,
   `Personification`, `Repeating Words`, `Visual Wordplay`, `Rhyming Nonsense Words`), load-bearing
   in the chunk plan and the loc anchors.

Unrelated meanings, identical string, and only sense (2) exists anywhere in the pile. Nothing warns
a downstream consumer that a `Other Techniques` hit in p133 is not sub-group membership.

The arbitration seed's remit as currently scoped is *terms the book uses ambiguously*. This is a
term **the pile** uses ambiguously — the collision is between the book's text and the pile's own
structural vocabulary.

**Recommendation:** extend the ambiguity probe to run over the discovery pile's own structural
terms (boundary names, sub-group names, mode names, part names) against the source text. Any
structural term that appears in the source with a different meaning is a sticky note. This is cheap
— the term list is short and known — and it catches the class of error where the pile's own
scaffolding is mistaken for content.

### 1.5 The escalation pattern is correct and should be named as a prompt affordance

The session was ruled, twice, to harvest `droppin' knowledge` sidebars **verbatim**, under a
`content_license: licensed` posture that hard-gates visual policy to describe-never-embed on
identical rights reasoning. It recorded the ruling, followed it, and flagged the contradiction with
evidence on both sides rather than quietly resolving it in either direction.

This is the right behavior and the prompt should make it explicit rather than leave it to session
judgment. Note also that the tension is **not theoretical**: the first sidebar in the first gesture
chunk is The Coup, "Pimps" (p122) — quoted song dialogue, covered by exactly the EMI/Morley
per-song clearances the escalation names. A worker following the brief reproduces cleared
third-party lyric dialogue verbatim on its first chunk of that chapter.

**Recommendation:** the prompt should state that a ruled decision in tension with another ruled
decision is recorded as ruled AND escalated with evidence both ways; the session does not
re-litigate and does not silently reconcile. It should also state that an escalation naming a
rights tension must cite the first location where the tension actually fires, so the operator is
ruling on a concrete instance rather than an abstraction.

### 1.6 The `[mechanical:]` tag needs a strength grade

Across this pile the tag covers claims of very different quality:

| claim | evidence | actual strength |
|---|---|---|
| `printed = pdf − 10` | 211/211 head-bearing pages, 0 exceptions | exhaustive |
| bold-loss on naive extraction | 3 strategies × raster-adjudicated | comparative, sound |
| `gap_threshold_pt: 3.0` | measured, two non-overlapping populations | measured, sound |
| gestures always `The <Name>` | "heading census" | **falsified by its own range** |

Same tag, four evidence classes, one of them wrong. The tag currently means "a machine was
involved," which is not a claim about whether the conclusion follows.

**Recommendation:** grade the tag — `[mechanical:exhaustive]` (whole population enumerated, N
stated, exceptions stated), `[mechanical:sampled]` (N stated, sampling frame stated),
`[mechanical:measured]` (instrument + threshold + separation stated). A claim carrying a universal
quantifier requires `exhaustive`. This is the cheapest available fix for 1.1: under this rule the
gesture-frame line could not have shipped as written, because "heading census" with no exception
list doesn't reach `exhaustive`.

---

## 2. What worked — preserve these

Recorded so future prompt revisions don't cut load-bearing behavior while fixing the above.

**Every re-runnable mechanical claim held.** Independently verified against the binary:

- `printed_page = pdf_page − 10` — 211 head-bearing pages checked, 211 confirm, **zero exceptions**.
- Canary 1, p41 bold scansion — recovered exactly:
  `The **fact** is I kick **phat** **raps** , so know **that**`. The pdfplumber+fontname strategy
  does what the doc says it does.
- Canary 2, p215 Appendix I — the two-column interleave is real and reproduces as predicted
  (`An ax to grind` / `Cup of Joe` on one visual row); the single-column intro paragraph above it
  is real; zone-scoped repair is genuinely necessary and page-scoped bisection genuinely shreds
  the intro.
- Canary 3, p126 — extracts a bold heading and **zero** body text. Confirmed.

The canaries are well-chosen: each one fails loudly and specifically if the ingest strategy drifts.
The canary-as-deliverable pattern should be kept and required.

**The p126 brief line is the single highest-value line in the pile.**

> *A gesture heading with no body text is not truncation — the instruction is in the illustration.
> Flag for a figure worker; never invent the procedure.*

On cold read this line worked exactly as designed. Without it a worker either drops a teaching
chapter or hallucinates a procedure — both silent failures. It anticipates a specific failure at a
specific location and tells the worker what to do instead of what not to do. This is the shape a
brief line should have.

**The goldfish test mostly passed.** Cold, with 25 lines and one chunk:

- correctly took `droppin' knowledge` (The Coup, "Pimps") as content with attribution, not noise
- correctly read `Variation: The Kweli Finger Wag` as a child of The Ninja Star, not a sibling
- correctly flagged p126 rather than inventing
- correctly declined to force a sense on "flowing" (p123, "stay flowing")
- **failed** on `Pantomiming` (per 1.1), and had no tiebreak for gesture-vs-technique on it

Four of five traps cleared by a reader with no other context. The function claim — *make a goldfish
who's read 3% of a book behave like someone who's read all of it* — is substantially met.

**The negative result was reported as a result.** `caption_pattern: null` with the method stated
(0 matches for `Figure [0-9]`, `Fig.`, `Diagram`, `Table [0-9]`; the 11 "Figure" hits are the
ordinary verb) and the consequence drawn (`fig:` references use printed page, not `fig:N-M`), plus
a Deviations entry explaining that a pairing count would have been fabricated. This is the correct
handling of an axis whose answer is "the source doesn't have one" and the prompt should keep
demanding it.

**The falsifiable exit exams on the effort forecast are well-built.** Both name a threshold, a
cause, and a place to look:

- *if `technique` < 20 → the type is over-specified and `drill` absorbed it; check Freestyle Rap Games*
- *if `gesture` > 15 → the `Variation:` frame is being read as sibling; check `children_list` on The Ninja Star*

The second will catch the failure it names. Note it does **not** catch 1.1 — a `Pantomiming`-class
miss makes `gesture` come in *low*, and no exam watches that direction. Forecast exams should be
written in both directions where the type has both an over- and under-count failure mode.

**Line-discipline audited before invoking collision doctrine.** The session checked conditions 2–4
first, found real defects, cut 11 lines (pointers, engine-law restatements, commentary no consumer
acts on), fixed a mis-nesting that inflated the count by 5, and only then reported the residual
overage (61 vs ≤50) with the reason it's irreducible: the `ingest:` axis costs 12 lines on this
source because a font-level teaching signal had to be proven rather than asserted. It then recorded
counter-evidence *against* its own overage being grounds for re-ruling the bound ("one born_digital
run is not a class"). Arguing against the conclusion that favors you is the behavior to preserve.

---

## 3. Local to this source

- **`flow` seed: CONFIRMED, cleanly.** p182 yields *"it gets the salvia flowing"* and *"in order to
  keep flowing easily on a track"* — physiological/plain-verb, unresolvable to the craft sense
  taught at p98–p109. The fan-out is real. Arbitration should expect at least two senses, likely
  three (craft delivery / plain verb "to rap continuously" / physiological).
- **`bar` seed: KILLED condition matched** (see 1.3). Carry the negative result onto the seed
  before harvest.
- **Gesture-vs-technique tiebreak is missing** for `Pantomiming` and `The Bob and Point`. Both are
  named, taught, and procedural; both sit in the Hand Gestures chapter; neither takes the gesture
  name-frame. Needs an operator ruling or a brief line before harvest.
- **The Coup / "Pimps" (p122)** is the first live instance of the license escalation. If the
  verbatim-sidebar ruling is revisited, this is the page to revisit it on.

### Minimum changes before harvest

1. **Replace the gesture-naming brief line.** Suggested: *Gesture headings are bold 14pt; most but
   not all use "The <Name>". Take the heading verbatim whatever its shape. "Variation: ..." = child.*
   This removes the discard reason that loses `Pantomiming` without adding lines.
2. **Add an `Other Techniques` sticky note** to the arbitration seed (heading prefix vs. book
   sub-group; the latter is load-bearing in the chunk plan).
3. **Annotate the `bar` seed** with its pre-run exam result and the ruling that keeps it alive.
4. **Rule gesture-vs-technique** for the two non-frame-conforming headings.

Items 1 and 2 are the only ones that touch worker-facing artifacts. The brief has 1 line of headroom
against its 25-line budget; the replacement in (1) is a swap, not an addition.
