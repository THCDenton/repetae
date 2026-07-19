# Session report — loeliger-til discovery run
To: the Claude agent assisting this operator
From: the discovery-session Claude that ran Loeliger *Threaded Interpretive Languages* against discovery_prompt_v2.7
Date: 2026-07-18
Terminal state: ratified. Six deliverables + this report.

This is written for you, a fellow agent, not for a validator. It covers what
the book threw at me, how I handled it, what I'd do differently, and the full
operator interview verbatim so you don't have to reconstruct it from the docs.

---

## The one-paragraph version

The book is an OCR scan whose text layer is *clean enough to trust and wrong
in exactly the places that matter*. It teaches a Forth-family programming
language whose word-names are made of punctuation (`$ * : ; @ ! #`), and the
OCR quietly corrupts that punctuation. So the central discipline of the run
was: don't believe the text layer, rasterize and read pages with your eyes,
and treat every "clean extraction" as a lie until a raster confirms it. Almost
every good decision downstream traces back to that one habit.

---

## Challenges the book posed, and how I got past them

### 1. The text layer lies politely (the headline problem)
`pdffonts` shows the text-layer font is literally named `InvisibleOCR` — an OCR
overlay on scanned page images. `pdftotext` output *looks* immaculate for
prose. It is not. The book's core content is a 172-entry keyword dictionary,
and inside those entries the OCR does things like:
- render the Forth token-separator glyph (`■`) as the letter **`B`**, so a
  formal definition `: ■APART■SPACE■8■...` comes out `:BAPARTBSPACEB8B...`.
  `B` is also a hex digit, so this is genuinely ambiguous, not obviously-broken.
- turn Z80 indirect addressing `(HL)` into `{HL}`
- turn assembly comment `;` into a bullet or asterisk
- corrupt the sigils that ARE the word names: `*STACK`→`'STACK`, `$PATCH`→`SPATCH`

**How I overcame it:** I followed the prompt's raster-rule *as a detector, not
a confirmer*. I rasterized sample pages (`pdftoppm -r 100 -gray`) up front and
read them against the text layer BEFORE forming any verdict. The block-glyph
substitution is invisible in the text stream and obvious the instant you look
at page 135. That single raster pass is what let me write a real repair
vocabulary instead of certifying a clean-looking corruption.

**Advice:** on any Internet Archive / LuraDocument scan, rasterize first, every
time. The `%PDF` magic + `InvisibleOCR` font + full-page raster images
(`pdfimages -list` shows one big image per page) is the signature. Budget for
it; don't wait for a MARGINAL verdict to look.

### 2. `splitlines()` will silently scramble this file
The page running-headers are separated by form-feed (`\f` / `\x0c`) characters,
and Python's `str.splitlines()` splits on form-feed. That detached every page
number from its header and made my first anchor-extraction pass return zero
anchors while looking like a logic bug. `cat -A` on the raw text revealed the
`\f` sitting inline.

**How I overcame it:** switched every reader to `raw.split('\n')` and never
used `splitlines()` on this source again. Recorded it as a falsified prior.

**Advice:** for this book (and probably any LuraDocument scan), read with
`split('\n')`, not `splitlines()`. If your anchor/citation logic mysteriously
finds nothing, this is the first thing to check.

### 3. Triple-status terms (the interesting semantic problem)
Terms like `NEXT`, `DUP`, `EXECUTE`, `SEMI`, `TOKEN` each appear in THREE
distinct roles across 5–6 chapters: (a) a concept discussed in prose, (b) a Z80
assembly mnemonic inside Code blocks, and (c) a defined keyword_entry in the
Chapter-6 dictionary. A naive harvest will either merge them into mush or mint
duplicate entities.

**How I overcame it:** the mechanical ambiguity probe (dispersion across
chapter buckets) ranked these cleanly — high dispersion + collision across
distant ranges. I did NOT rule on them (senses are harvest verdicts, not
discovery's). I pre-opened them as fan-outs in the arbitration seed, each with
an exit-exam line so the harvest run confirms or kills the fan-out against the
actual text rather than inheriting my guess.

**Advice:** the probe's dispersion signal was reliable here because the book's
structure (prose chapters + a back-of-book dictionary) naturally produces the
concept-vs-entry split. Trust the ranking to *prioritize attention*; never let
it *rule*. The Z80 mnemonics (`GET`, `PUSH`, `POP`, `LD`) also show huge counts
but are mention-only noise — keep them out of the entity set; that mention/entity
boundary is a real convention line, not a footnote.

### 4. The "defer instead of chunk" trap (v2.7 docket item, live)
My first chunk plan marked oversized prose sections `fallback_split` with a note
"split at subsections later." That is precisely the deferral defect the v2.7
prompt dockets — a note saying "cut this," not a cut. The arithmetic lint caught
it: §4.1 alone is ~14,500 tokens against a 1,500-token fallback.

**How I overcame it:** materialized 85 real page-bounded slices (~2 pages each,
under the fallback) plus one-chunk-per-entry for the 172 dictionary words. Every
in-scope range now lands in exactly one concrete unit.

**Advice:** run the arithmetic lint yourself (`boundary_type == section` AND
`est_size > fallback` → defect) before read-back. Don't ship a plan whose rows
are IOUs.

### 5. The schema boundary — what NOT to do
`pipeline_config_schema_v2.md` was not in the environment. The tempting move is
to write the config fragment's field list from memory of "what the schema
probably says." The v2.7 prompt is emphatic that this is how the field list
rots. I wrote the fields the axes checklist explicitly names as plain contract,
flagged in the read-back that I could not verify field status, and minted NO
`v3-proposed` tags (you can't declare a field "genuinely absent" from a schema
you can't read).

**Advice:** if you inherit this doc for a schema/config session, the config
fragment's field STATUS is unverified — that's the one real open thread. Verify
against the live schema before it becomes live config. Don't let my plain-written
fields be mistaken for schema-confirmed ones.

---

## What went smoothly (so you can calibrate)
- The dictionary is a gift: `Class:` count == `Function:` count == 172 exactly.
  That's an exhaustive-grade entity count you can lean on. If a later run of
  ch6 yields materially <150 or >200, something's wrong with the scoping.
- Location grammar is clean and proved on the first try (250 anchors, 3/3
  citations resolved). The anchor CSV is solid; the only wrinkle is that
  even-page headers sometimes carry the BOOK title instead of the chapter
  title, so key on page number, not header text.
- Caption pattern is uniform (`Figure N.M:`), and there's a second caption
  class (`Listing N.M:`) worth remembering — they're different entity types.

---

## If you're picking up downstream work
- The Index is EXCLUDED from harvest but RETAINED as a MERGE-level recall seed.
  Don't let anyone "clean that up" as a contradiction; it's deliberate
  (native-seeds law: reduce-side recall aid, never per-span input).
- The arbitration seed is boot state for the arbitration layer ONLY. It must
  never be injected into the harvest brief or a worker packet. If you see it
  leaking into worker context, that's a bug.
- License is `licensed` → figures are describe-never-embed. No figure raster
  should ever end up reproduced in output.

---

## The full operator interview (verbatim)

I presented decisions as button groups, ≤3 per message, evidence + my lean
first. Twelve questions across four rounds. Operator answers are exactly as
given.

**Round 1 — ingest / license / visuals**

Q1. Ingest verdict — the code/tabular class is MARGINAL (OCR corrupts the ■
token-separator, (HL)→{HL}, sigils, and comment semicolons; prose is clean).
How do you want to proceed?
Options: [Accept scan + ruled repair vocabulary (my lean)] / [Commission
dedicated ingest session] / [Accept as-is, no repairs]
→ **Accept scan + ruled repair vocabulary**

Q2. License posture (gates visual policy). It's a 1981 Byte Books commercial
title by R.G. Loeliger. What's the posture?
Options: [licensed (my lean)] / [personal] / [client_owned]
→ **licensed**

Q3. Visual policy for the 19 embedded figures (line-art diagrams baked into
page rasters).
Options: [describe (my lean, if licensed)] / [ignore] / [embed]
→ **describe**

**Round 2 — entities / scope**

Q4. Entity types. The spine is 172 dictionary keyword-entries (structured
template). Prose chapters teach concepts (threading, inner interpreter,
vocabularies); there are also captioned Figures AND Listings. Which entity set?
Options: [keyword_entry + concept + figure + listing (my lean)] /
[keyword_entry + concept only] / [keyword_entry only (dictionary-centric)]
→ **keyword_entry + concept + figure + listing**

Q5. Chapter 7 'EXTENSION PLEASE' (p180-243) builds an assembler/editor/
virtual-memory ON TOP of a TIL — a big applied case study. Include in harvest
scope?
Options: [In scope as concept-teaching (my lean)] / [Out of scope (case study,
not core)] / [In scope but flagged low-priority]
→ **In scope as concept-teaching**

Q6. Back matter: Bibliography/Notes (p244) and the two-column Index. Scope?
Options: [Exclude both (my lean)] / [Include Bibliography as external-refs
only] / [Include both fully]
→ **Exclude both** (Index retained separately as a MERGE recall seed — not a
harvest-scope inclusion, so no conflict)

**Round 3 — chunk plan / web policy / arbitration lean**

Q7. Chunk-plan boundary. Dictionary entries are tiny & uniform (~221 tok) —
natural unit = one keyword_entry. Prose chapters split at §N.M sections. What
boundary ladder + oversized-section fallback bound (measured against ~560
tok/page)?
Options: [chapter→section→one-keyword-entry, fallback ~1500 tok (my lean)] /
[section only, fallback ~1200 tok] / [one-keyword-entry everywhere possible]
→ **chapter→section→one-keyword-entry, fallback ~1500 tok**

Q8. web_policy (scopes harvest judges' web license). TIL is the Forth family —
a living tradition the web documents — but Loeliger's specific 'ZIP' keyword
set is idiosyncratic to this 1981 book. Setting?
Options: [in-tradition (my lean)] / [off] / [open]
→ **in-tradition**

Q9. Watchlist lean. Terms like NEXT/DUP/EXECUTE/SEMI/TOKEN appear as (a) prose
concept, (b) Z80 mnemonic, (c) defined keyword across 5-6 chapters. How
aggressively should discovery pre-open these fan-outs?
Options: [Pre-open fan-outs for the triple-status terms (my lean)] / [Single
sense expected, reserve on contact] / [No opinion — leave to harvest]
→ **Pre-open fan-outs for the triple-status terms**

(Preflight attestation — "does the environment contain anything besides prompt
+ source + companions?" — was answered "Nothing else" and recorded under
Identity. Counting that, twelve operator touchpoints total; nine were the
substantive button groups above.)

**Note on interview shape:** every answer landed on my stated lean. That's a
good sign the evidence-first framing was doing its job, but be alert — an
operator who taps your lean every time could also mean your options weren't
genuinely choosable. I tried to keep the non-lean options real (e.g. the
dedicated-ingest-session option in Q1 was a live alternative, not a straw man).
Watch for that in your own runs.

---

## Bottom line
The book is not hard because it's complex; it's hard because it's *deceptive* —
a scan that reads clean and isn't, of a language made of the punctuation the
scan corrupts. The whole run rewards one habit: look at the pages, don't trust
the text. Everything else followed from that.
