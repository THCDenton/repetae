# How the Machine Should Read a Book — A Proposal

**Status:** PROPOSAL — hypothesis, not proven practice. Nothing here has run
end-to-end. Ratify at the amendment session only after the cheap test at the
bottom passes. (Session: 2026-07-12 design chat, operator + ctx.)

---

## TL;DR

- We've been arguing about the order the machine reads a book in.
- All the designs so far shared one hidden assumption: that questions must be
  answered *while reading*.
- But we have the whole book on disk before we spend a cent. So: **read fast
  in parallel, then answer every question at the end, with the whole book
  available as evidence.**
- It's faster than the careful-reader design, cheaper too, and every decision
  gets made with maximum information.
- We prove it with one cheap experiment before betting the pipeline on it.

---

## The problem in one breath

Turn a book into a glossary. The hard part isn't finding the terms — it's
deciding **which mentions are the same thing**. Is "the mount" on page 30 the
same as "the mount" on page 370? (In the jiu-jitsu book: no. Two different
concepts sharing a name.)

Every design we've debated is really just an answer to one question:

> **When a judgment call has to be made — how much of the book has the
> decider actually seen?**

---

## The three designs we tried

**1. The assembly line** *(original plan)*
- Chop the book into chunks, workers read them all at once, a script glues
  the results, a judge cleans up the leftovers.
- ✅ Fast and cheap.
- ❌ The judge decided identity questions from one-line summaries, without
  the book. Starved of evidence.

**2. The careful reader** *(the JJU way — what we flipped to)*
- One reader goes front to back, keeping a notebook. Unsure about something?
  Write it down, carry it forward, resolve it when the answer chapter arrives.
- ✅ Proven — it built the JJU glossary.
- ❌ Slow: every step waits for the last one. Days per book on the discount
  lane.
- ❌ Hidden flaw: only the *deferred* questions get full-book evidence. Any
  call made early gets made on partial information.

**3. The bracket** *(your pairs idea)*
- Merge chunks in pairs, then pairs of pairs, until one document remains.
- ✅ Fast.
- ❌ Two mentions of the same term meet wherever their branches happen to
  join — often with neither the book nor full evidence present. Same
  starvation as design 1, at every level.

---

## The realization that unlocks it

The careful reader's notebook — all those "check this later" notes — exists
because a human-driven session **can't look ahead**. It reads page 30 before
page 370 exists to it.

**Our machine has no such limit. The whole book is on disk on day one.**

So "will this term show up again later?" isn't a note to carry for 27 steps.
It's a *lookup*. The notebook was solving a problem we don't have.

And your pairs instinct was one word away from right: don't pair chunks by
**position** — group mentions by **term**. Then every mention of "the mount"
lands on one desk, once, together.

---

## The proposal: four phases

Think of it as a newsroom.

**Phase 1 — READ** *(the reporters — parallel, one batch, half price)*
- One worker per chunk. All run at the same time.
- Chunks follow the **source's own natural boundaries** — chapters, or
  sections if chapters run huge, or whatever convention the book uses.
  Cutting at real teaching boundaries kills the "hanging page" problem.
- The **chunk plan is a discovery deliverable**: the discovery session
  already reads the TOC and maps sections to page ranges, so it draws the
  chunk borders per source. (Retires the old "global span size" question —
  it's measured per book now.)
- They only *report* what they see: term, meaning as stated, location.
- Hard rule (already law): reporters never decide whether two mentions are
  the same thing. They report; they don't rule.

**Phase 2 — SORT** *(the filing clerk — a script, costs $0)*
- Merges everything that's *provably* the same (same name, stated alias,
  overlapping location). Obvious stuff files straight into the glossary.
- Everything genuinely ambiguous becomes a **case file**: every mention of
  the term, plus the actual book text around each one, plus what you said
  about it at the discovery interview.

**Phase 3 — DECIDE** *(the editors — parallel, one batch, half price)*
- One editor per case file. All independent cases run at the same time.
- Each editor holds **everything**: every mention, the surrounding book
  text, your discovery preferences, the internet (per the source's web
  policy).
- Per your ruling: they decide — full stop — and write down *why*, so we
  can diagnose and tune later. No ties, no waiting on you.

**Phase 4 — PUBLISH** *(the printer — a script, costs $0)*
- Assembles verdicts + clean entries into the final index and shard files.
- Pure mechanics. Re-runnable any time.

---

## Why this wins

- **Fast:** 2–3 batch rounds total, instead of 31 waits in a row. Overnight,
  not days — even on the half-price lane.
- **Cheap:** cheaper than the careful reader, which re-reads its growing
  notebook at every step. Here, each piece of text is read only where a
  decision actually needs it.
- **Smarter:** *every* judgment is made with the entire book's evidence in
  hand. The careful reader only managed that for the questions it thought to
  defer.
- **Safe to re-run:** if a run produces garbage, we read the editors' written
  reasoning, tune the prompts, and re-run — exactly your tuning plan.

---

## Honest downsides

- **More plumbing.** Four phases and a script that builds case files, versus
  one loop. Real work, but it's script work — the kind we already planned to
  own.
- **Reporters read alone.** A chapter that leans on another chapter reads
  slightly blind. Mitigation: chapters are chopped at natural boundaries with
  overlap (this contained the problem in JJU), and anything unclear becomes a
  case file for an editor who *can* see everything.
- **It's unproven.** The careful reader has a finished glossary to its name.
  This has an argument. Which is why:

---

## The test before we bet on it

Cheap, and mostly already built:

1. Run Phase 1 on the JJU book's test chapters (the sealed test kit already
   exists for this).
2. Run Phases 2–3 on the output (the judge test cases already exist too).
3. **Diff the result against the finished JJU glossary** — a known-good
   answer key we already own.

- Matches or beats it → ratify this design. It wins on every axis at once.
- Loses something the careful reader wouldn't have → we'll see exactly what,
  and the careful reader takes the crown back with evidence.

---

## What this does NOT decide

These stand on their own, whatever topology wins:

- The **index + shard** file format (output shape, not reading order).
- Your **no-human-in-the-loop** ruling and the tiebreak ladder.
- The **intake screening** tiers and runbook.
- Discovery upgrades (ambiguity forecast, web policy, tiebreak preferences).

**Recommendation for the amendment session:** ratify all of the above now;
gate the reading-order decision on the test.

---

## Appendix: "Couldn't the bracket carry to-do lists?"

*(Asked by the operator, 2026-07-12 — and anyone reading this will ask too.)*

The idea: merge chunks in pairs, each pair carries a to-do list of open
questions, each merge checks its questions against its partner, unresolved
ones ride upward, and the final merge collapses the to-do into the index.

**It's viable — it's a real pattern** (it's how distributed systems merge
data too big to sit in one place). In fact the "careful reader" is just this
tree in its most lopsided form. But two things push it back into this
proposal:

- **Most merge work is clerical** (same name → combine). Paying an AI to do
  it at every tree level is paying editor rates for filing. Optimize that
  away — scripts merge, AI only judges when a question meets its answer —
  and the tree *becomes this proposal*, just run in five waves instead of
  one. Hierarchical merging exists for data that can't fit in one place;
  ours fits on **the driver's disk** — the scripts on our own machine see
  everything, so one script pass groups everything globally. (The AI
  workers still live in a vacuum, seeing only the packet we ship them —
  that never changes. The global view belongs to the scripts that *build*
  the packets, not to the workers that receive them.)
- **A tree node can't see around corners.** It never knows if more evidence
  for its question is still coming in an unmerged branch — so it either
  rules early on partial evidence (the careful reader's hidden flaw,
  inherited) or defers everything to the top, where the root becomes one
  overworked judge. The flat design avoids the dilemma: the free script
  pass is global, so every case file is born complete.

**Bottom line:** the to-do list survives in this proposal — it *is* the
case-file queue — and "the to-do collapses with the actual index" is
Phase 4. The only change from the bracket version: a free global pass
builds the to-do complete in one shot, instead of letting it trickle up
a tree meeting its answers piecemeal.

---

*Evidence label, per workshop law: synthesis hypothesis. The careful reader's
proof-of-life is real but proves the "can't look ahead" setting — which is
not our setting. This document supersedes the fold-vs-tree debate of
2026-07-12 and the abandoned `merge_script_laymans_guide.md`.*
