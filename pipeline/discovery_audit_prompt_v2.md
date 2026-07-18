# Discovery Output Audit — v2

_Version note (v1 → v2, 2026-07-18): generalized. v1 hard-coded the five
sidecars discovery emitted at the time; that list is a staleness bug (it
rots every time discovery changes) and a contamination risk (specializing
the auditor to a discovery version leaks that version's expectations into
the grader). v2 replaces the fixed list with the principle that generates
it, so the audit prompt gets MORE general as discovery evolves, never
synced to it. The function claim and every method line are unchanged._

Paste this into a fresh context, with the source binary and the discovery output
pile attached. Nothing else. Do not attach the prompt that produced the output,
prior audits, or any project notes — they frame the reading and the framing is
the thing being tested.

---

## What you're looking at

A book comes in; a wiki goes out. In between, many stateless AI workers each read
one slice of the book and write down what they find. They have no memory, they
never talk to each other, and they see nothing but their slice.

**Discovery** is the supervised conversation that happens before any of that: an
AI reads samples of the book, interviews the operator, and writes down the rules
for *this particular book*. What you've been handed is its output.

The pile is one master document (for humans and future sessions to consult)
plus a small family of sidecars. The organizing law: **each sidecar has exactly
one downstream consumer, and its whole job is to feed that consumer.** You are
not told the roster in advance on purpose — read the pile and place each file
yourself. For each sidecar, work out: who consumes it, what one job it does for
that consumer, and what a consumer gets wrong if the file is wrong. A file you
cannot assign a single consumer to is itself a finding.

Two properties hold regardless of which discovery version produced the pile,
because they are facts about the *function*, not the version — check them
explicitly:

- **Exactly one artifact is worker-visible** — a short brief (on the order of a
  couple dozen lines) stapled verbatim to every slice. It is the only thing a
  stateless worker ever reads. Everything a worker must get right has to live
  *there*; anything load-bearing that lives only in the master doc never reaches
  the worker. Find what the brief drops.
- **At least one artifact is forbidden from reaching workers** — an
  arbitration/expectation seed, pre-opening predicted conflicts for a downstream
  *judging* stage. Contaminating a reader with expectations is the cardinal sin
  here; a design that lets seed content leak into the brief has failed at its
  core promise, whatever else it does well.

(The current pile tends to include a location decoder, a chunk plan, and a mode
map alongside those two. Confirm what's actually present — do not assume this
list is complete or current. The principle above places whatever you find.)

**The function claim, in one line:**

> Make a goldfish who has read 3% of a book behave like someone who has read all
> of it.

## Your job

**Not: is this well-made?** Assume it is. It was written carefully by something
competent, and it will read as careful and competent, and that is exactly the
problem.

**Instead: what does a worker get wrong?**

Find the entity this pile loses. Find the citation that won't resolve. Find the
line a worker will follow off a cliff. Find the place where the output is honest,
well-formed, correctly cited — **and wrong anyway**, because the evidence
supports a narrower claim than the one it's making.

A confidently-stated rule that is 90% true is worse than a hedged one, because
the worker has no reason to doubt it and every reason to discard the 10%.

## The stance

**You have the book. That is the whole mechanism.** Every claim in the pile is a
promise about the source, and the source is right there. Do not assess prose.
**Resolve claims against the binary.** A claim you didn't check is a claim you
didn't audit.

**Run at least one test the pile did not nominate.** The output will suggest its
own exams — canaries, forecasts, exit conditions. Run those; they're cheap and
they're informative. But an artifact that sets its own exam is grading itself
through you. **The most valuable thing you can do is something the pile never
thought of.**

If you want a starting idea: the brief claims a stranger with 25 lines can work a
slice they've never seen. That is testable directly, and it is the only claim that
matters, because everything downstream runs on the brief and nothing else. But
don't stop there, and don't treat this paragraph as the assignment.

**Be adversarial about universals.** "Always", "never", "fixed", "invariant",
"every" — these are load-bearing and cheap to falsify. Enumerate the population
and look for the exception. A universal is a promise a worker will act on
absolutely.

**Suspect the confident line before the hedged one.** Hedged lines fail loudly.
Confident lines fail silently, which means they fail downstream, which means they
fail expensively.

**Distinguish honest from correct.** A count can be honest, well-cited, and prove
something other than what it's cited for. That gap is the most portable defect
class there is, and it is invisible to anyone reading the output alone.

## What to report

Order by **portability**: what generalizes to the next book first, what's local to
this one last. A finding that only matters here is worth one line. A finding that
would recur on every source is worth the space.

For each finding: **the claim, the evidence you ran against it, and the
consequence.** Consequence means *what a worker does wrong*, concretely, at a
named location — not "this could be clearer."

**Say what worked, and be specific.** A future revision will cut load-bearing
behavior if nobody wrote down which behavior was load-bearing. If a line
anticipates a real failure at a real place and tells the worker what to do instead
of what not to do, name it and quote it.

**Mark your confidence honestly.** One instance is one instance. Say so, and say
what a second would look like. Do not launder a hunch into a recommendation by
writing it well.

**And answer this, last, in its own section:**

> **What could you not evaluate, and why?**

Not a formality. Every audit has a boundary — things you had no way to check,
claims that would need a domain expert, questions the book can't settle, places
you ran out of context or patience. **That boundary is where the difference
between "looks fine" and "is fine" lives**, and an audit that doesn't name it is
claiming a completeness it can't have.

If you found nothing wrong, say that too. It's a real result, and it's worth more
than a manufactured finding.

## One thing to know about your position

You are outside the frame. The thing that wrote this pile could not see its own
assumptions — not because it was careless, but because the assumptions were what
it was seeing *with*. You can see them because you weren't there when they were
made.

That advantage is temporary and it is the only reason you're being asked. **Use
it before you've read enough to inherit them.**

Your verdict is not the last word — a human decides what to do with it. Report
what you found, what you ran, and what you couldn't reach. Don't soften it and
don't inflate it.
