# Discovery Output Audit — v1

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

The pile is one master document (for humans and future sessions to consult) plus
a small family of sidecars, **each with exactly one downstream consumer**:

- **the harvest brief** — ≤25 lines. **The only artifact a worker ever sees.**
  Stapled verbatim to every slice.
- **a location decoder** — the book's printed page numbers vs. the file's, proven
  and tabulated, so every citation anyone writes resolves.
- **a chunk plan** — where to cut, at the book's own seams, so no lesson gets
  sawed in half.
- **a mode map** — per section: prose, tabular, dialogic, code listing, mixed.
  Selects the reading instructions.
- **an arbitration seed** — words predicted to cause fights later, pre-opened for
  a downstream judging stage. **Forbidden from reaching workers** — contaminating
  readers with expectations is the cardinal sin here.

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
