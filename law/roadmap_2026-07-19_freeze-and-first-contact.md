# Roadmap r2 — freeze discovery, make first harvest contact

Written 2026-07-19 by an assisting ctx (**Claude Fable 5** — not a workshop
derivation ctx; keep out of the Opus series). Repo verified against
`repetae.zip` at commit `4fc81d7`; every claim below was re-checked by script
against that tree, not carried from checkpoints. **Supersedes
`roadmap_2026-07-18_close-and-first-contact.md`** (sediment — keep it; its
A–C sections are now a record of predictions that held). Proposed home: repo
root beside its predecessor (operator's call — planning, not law).

Standing rules, carried and extended:

1. **One job per session.** Anything discovered mid-session that is not that
   job gets docketed, not done. (Carried. Held at every level on 07-19,
   including recursively — chunking a session is permitted; it is this rule
   applied finer, not a violation of it.)
2. **NEW — no session insertion before E.** The list below is closed. Amending
   a session's contents with new evidence is maintenance; adding a session
   between here and E is the workshop-becomes-the-product failure mode wearing
   a planning costume. If work appears that seems to demand a new pre-E
   session, it goes to the docket and waits for E's evidence to justify it.
3. **NEW — sealed-checkpoint rule (to be filed, see §0).** Anything discovered
   after a session's checkpoint is sealed gets a filing act (docket line,
   amendment note) before the session ends — never only a chat assertion.
   Taught by the 07-19 retirement-gap incident, where a real finding nearly
   evaporated because the closing claim outran the files.

---

## Ledger — what the 07-18 roadmap already closed (verified, not trusted)

| Session | Closed as | Independent re-verification (07-19, assisting ctx) |
|---|---|---|
| A — clerical debt | ckpt 07-18c | register v5 / lexicon r19 / diagram r14 on disk, md5s match filing claims; Loeliger evidence dir present with coverage note |
| B — discovery v2.8 | ckpt 07-19 | v2.8 `7fb622ea…` 673L on disk (50L *shorter* than v2.7 — fossil layer extracted); changelog present |
| C — validator rebuild + shakedown | ckpts 07-19b/c/d/e | selftest **24/24 PASS** re-run; Loeliger fires exactly 1 red (`CHUNKPLAN_COVERAGE p174..179` — P16 live); rappers fires exactly 37 incl. `SECTION_ORDER`; findings v1/v2 filed; handshake md5s all match 07-19e |

Facts that postdate the old roadmap and govern the sessions below:
- **P16 is demonstrated live.** The validator mechanically catches the real
  Loeliger gap. The cheap check now carries load; P11's unblock condition met.
- **Rappers is ruled a pre-v2.8 pile** [operator, 07-19e]. Its era-mismatch
  reds are rejected-docket, not defects. Its REAL open items: F5 (section
  order, confirmed version-neutral by the F5 session) + the confirmed
  `CONVENTIONS_TOO_MANY 61 > 50` bound blow + the 4 `ratified` audit defects.
- **F3 retired; P17, P18 filed** (findings v2 terminus ledger — every finding
  terminates; nothing evaporated *in the findings record*).
- **The close protocol has a known retirement gap** (two-hash sync places and
  updates but cannot remove; a retired fixture dir stranded the live tree on
  07-19). Real, operator-observed, currently living ONLY in chat scrollback.
- **The stale `/mnt/project/` mount caused a real incident** (the un-booted
  07-19 checkpoint name collision). Root cause standing until cleared.

---

## §0 — In flight: kill F5 (assigned by ckpt 07-19e, not by this roadmap)

**The job (unchanged):** reorder the rappers pile's `## Effort forecast` into
its canonical slot (after Registry queue, before Config fragment) under the
amendment protocol — one changelog line; the pile moves from as-is evidence to
a patched rev. **It is a PILE PATCH: honor the isolation rule** — a fresh ops
ctx or the operator edits the pile; a workshop ctx emits only the patch
instruction. Confirmed real and version-neutral (v2.6's own mandated order
matches the validator's); everything AROUND it on the rappers red list is
fenced off as era-mismatch — do not clean up while in there.

**Two riders added to this session's CLOSE (cheap filings, not scope):**
1. **File the retirement gap** — docket entry or close-protocol amendment
   note: the MANIFEST needs a `remove:` section, or the sync reconciles the
   fixtures dir against `build_invalid.py`'s case list. Gets it out of
   scrollback; the fix itself can wait for the next protocol touch.
2. **File the sealed-checkpoint rule** (standing rule 3 above) as a register
   proposal, evidence: the retirement-gap incident.

Optional third, zero-cost: the next commit message may note that `4fc81d7
"1 more bug left on validator"` mislabels F5 — it is a pile defect; the
validator is correct. (Do not rewrite history; just stop the label spreading.)

Done when: rappers re-run shows `SECTION_ORDER` gone and **exactly** the
expected residual red set (the bound blow + era-mismatch classes — no new
reds, no vanished ones beyond F5). The validator is the amendment gate.

---

## Session D — The freeze, the ratification batch, harvest prep

**The job:** write the freeze into law, clear the law backlog while the
register is open, ready one pile for feeding. D touches the register anyway;
that makes it the ONE legitimate home for the accumulated law debt — this is
amended scope, not new scope. **If budget is tight, chunk D per the C
precedent** (D.1+D.2 = the law chunk; D.3+D.4 = the prep chunk). Chunking is
permitted; a new session is not.

**D.1 — Freeze ruling → register.** No discovery v2.9 and no refactor until a
harvest run has produced evidence naming discovery; unlock condition written
into the ruling itself. **NEW — the ruling must state P18's disposition
explicitly:** the `ruled_bound` machine-readable witness is a SCHEMA change,
and P14 (schema lockstep) says schema and prompt move together — so either
the freeze covers the schema too (P18 deferred to unlock; the honest default)
or the ruling carves a named exception. Silence here guarantees the first
post-freeze session re-litigates it.

**D.2 — Ratification batch → register v6 (+ charter v1.3 if P14 ratifies).**
The full pending board, each to ratify / reject / renumber:
P3-R, P4, P5–P7, P9, P10, **P11** (unblock condition now met and demonstrated
— the mandatory-gate rule is adoptable), P12, **P13 + both riders** (boot
protocol; zip-close in its 07-19d *snippet* form — ratify the snippet, not the
superseded `.sh`), **P14 → charter amendment v1.3** (it leaves the register),
P15, **P16** (now with live-fire evidence), **P17**, **P18** (disposition per
D.1), plus §0's sealed-checkpoint proposal. The boot/close protocols stop
being burned-in checkpoint text and become law. This backlog is the one
genuine omission of the 07-18 roadmap; it does not survive into a third
roadmap.

**D.3 — Pick the test pile (button) — pressed on 07-19 numbers, not 07-18
ones.** Both columns changed on 07-19; the old recommendation's premises are
stale even if its conclusion survives:

| | rappers-handbook | loeliger-til |
|---|---|---|
| ingest | **born_digital — simpler; E's failures stay legible as harvester failures** | scan_ocr — needs the PDF + extraction care |
| version | pre-v2.8 (v2.6); era fence must hold during amendment | **v2.7 — version-current** |
| amendment bill | F5 (in flight) + confirmed 61>50 bound blow + 4 ratified audit defects | **one located defect: the p174–179 chunk patch** |
| gate | validator red-set delta checkable, era classes excluded | **validator mechanically confirms the patch (P16 live)** |

Either is defensible; the button is the operator's. Whichever pile: amend it
under the amendment protocol (changelog line per fix), **with the validator as
the amendment gate** — run before and after; the delta must be exactly the
intended fixes and nothing else. The 07-18 roadmap could not say this (no
working validator existed); this one can, and does.

**D.4 — Read `pipeline/harvester_prompt_v1.md` (75L, md5 `9d2085ab…`) against
everything learned since 07-11.** Unchanged from the 07-18 roadmap: NOT a
rewrite — a list of its known-stale assumptions so the test run's failures
are legible. It earns its v2 from a run, the same way discovery did.

Do NOT: fix the harvester preemptively; reopen validator lints (F1/F2 fixes,
F3 retirement) without a real finding naming one; touch the discovery prompt
(the freeze you are writing applies to the session writing it).

---

## Session E — First contact: a small harvest

**Deliberately unchanged from the 07-18 roadmap — its wording was right.**

- Scope: 3–5 chunks from the chosen pile, a few workers, one merge attempt.
  Not the whole book. The deliverable is EVIDENCE, not a wiki.
- Three-role where affordable: run ctx ≠ design ctx; audit the output cold if
  budget allows.
- The session report's "friction worth reporting upstream" section is the most
  valuable artifact this roadmap produces. Everything downstream of discovery
  gets its first real docket here.
- Expected outcome per the project's own history: harvester_prompt_v1 breaks
  everywhere it obeys something it never defined. **That is success.**
- Done when: the run family + report are FILED (same session, not later — the
  Session-A lesson), and a docket exists for the harvest stage.

---

## Ops chores — operator tasks, no session needed

1. **Clear the stale `/mnt/project/` mount** (or reduce it to the primer + a
   single pointer file: "the repo is truth"). It is frozen at the 07-13 era,
   already caused one checkpoint collision, and every un-booted chat in the
   project remains one bad boot away from another. This executes the P9/P10
   ruling's second half, which was decided 07-14 and never performed.
2. When convenient: sync this roadmap + the F5 session's close into the repo
   so they exist to the next ctx.

## After E

Unchanged: the next design session triages the harvest docket. Discovery
reopens only if harvest evidence names it — the freeze's unlock working as
designed. The refactor question (v3.0) waits for: validator green (**met,
24/24**), rule inventory built, regression baseline chosen.

---

## Boot handshake for Session D (verify on disk before working)

```
law/primer_amendment_proposals_v5.md   EXPECT 20f11cf6650233f68acde92dddf3c6f7  237L
law/workshop_lexicon_r19.md            EXPECT 724ea572699db099cc73c8ec1f666067  1366L
law/engine_charter_amendment_v1_2.md   EXPECT 2bb378a214707a4aa009e61dc08e45ae  275L
pipeline/discovery_prompt_v2_8.md      EXPECT 7fb622eab071b99f4314a759c0f4a33a  673L
pipeline/harvester_prompt_v1.md        EXPECT 9d2085ab40bb6bb92706747821ec3d4e   75L
evidence/validator_real_pile_findings_v2.md EXPECT 806c05354fe3565f6e1e89635a618649  184L
tools/…/src/rules.py                   EXPECT 6996b2d962bc0cb78c167603abae535c
tools/…/src/validate.py                EXPECT 7cd3bb3eae5301ae1c2c1cbf3e3cb597
selftest                               EXPECT 24/24 PASS
```

Plus the F5 session's closing checkpoint (newest at D's boot — name unknown to
this roadmap; highest suffix wins) and the post-F5 rappers red set as the
amendment baseline if rappers is chosen in D.3. If any row differs, stop and
reconcile before D does anything — the repo is the source of truth.
