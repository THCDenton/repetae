# Roadmap — close out discovery, freeze it, make first harvest contact

Written 2026-07-18 by an assisting ctx (repo verified against repetae.zip,
commit 90cfab2). Five sessions, each with one job. Proposed home:
`reference/` (operator's call — this is planning, not law).

Standing rule for every session below: **one job per session. Anything
discovered mid-session that is not that job gets docketed, not done.**
Scope creep is the recorded killer of prior sessions.

---

## Session A — Pay the clerical debt (everything filed, nothing designed)

**The job:** make the repo match reality. No design decisions.

Attach at boot: this roadmap, `checkpoints/session_checkpoint_2026-07-18.md`,
`law/primer_amendment_proposals_v4.md`, `law/workshop_lexicon_r18.md`,
`reference/system_diagram_r13.html`.

Deliverables:
1. **File the v2.7 vindication evidence** — the Loeliger re-run family
   (6 deliverables + session report from the "2.7 TIL test" ctx) and the
   third-ctx audit findings. If you downloaded the run's files, file those;
   if not, reconstruct from the transcripts and MARK each file
   `RECONSTRUCTION — recovered from transcript` (the audit-v1 lesson:
   unmarked reconstructions poison trust). Suggested home:
   `evidence/loeliger-til-run-2026-07-14/` (the re-run extends the family)
   or a sibling `-rerun-2026-07-18/` dir — operator's call.
2. **Register v5** — files P13, P14 (drafted 07-15b), the
   audit-generalization rule, the audit-is-not-schema-lockstep distinction.
   Three sessions overdue; this is the W10 pattern's test case.
3. **Lexicon r19** — owed entries: W15 (*a paste is not a file*),
   `meta artifact`, the three-names pair, `coverage by silence`,
   `confirmer→detector`.
4. **Diagram r14** — records discovery-v2.7-VALIDATED.

Done when: a close-state snippet shows all four in the repo.
Do NOT: touch the discovery prompt, the validator, or any pile.

---

## Session B — v2.8: the last accretive version before the freeze

**The job:** four small, evidenced, patch-scripted changes. Nothing else.

Attach at boot: `pipeline/discovery_prompt_v2_7.md` (md5 `1a19649f…`, 723L —
verify on disk before patching), `evidence/docket_chunk_coverage_reverify_v1.md`,
`pipeline/pipeline_config_schema_v2.md`.

The four changes:
1. **Coverage rule lands** (from the docket): chunk-plan coverage verified by
   arithmetic; any gap/overlap triggers mandatory re-verification of the
   affected pages; *a page may not be dropped by silence — only by a stated,
   page-checked reason.* Homes ruling: **both** (prompt rule here, lint twin
   in Session C) — the schema-lockstep precedent, decided this session by
   button.
2. **Fossil-layer move**: the ~85 lines of stacked version notes move to
   `pipeline/discovery_prompt_changelog.md`; the prompt keeps a pointer.
   (Pointer-not-copy, applied to itself.)
3. **Template fix, line 553**: `discovery_prompt_v2.6` → "this prompt's
   version" phrasing. A hardcoded self-fact rots on every re-version.
4. **Raster-rule dedupe**: currently stated in Probe discipline AND the
   version note; one authoritative statement, one pointer.

No dedicated test run for v2.8: changes 2–4 are non-behavioral, and change 1
is arithmetic-checkable and gets an independent lint twin in Session C.
Do NOT: refactor, reorganize sections, or "improve wording while in there."

---

## Session C — Validator rebuild: bank the mine

**The job:** the free checker finally learns everything the expensive
audits discovered. Unblocks P11; makes the mandatory-gate rule adoptable.

Attach at boot: `tools/discovery-validator/` (whole dir), v2.8 from Session B,
the two real run piles.

Deliverables:
1. **Fixtures + rules rebuilt against v2.8** (rules.py still cites v2.5 —
   two versions stale). Fix the two red selftests found 07-18 in a fresh
   environment (TAG_MECHANICAL_NO_METHOD passes when it should fail;
   TAG_ILLEGAL is non-specific).
2. **New lints, one per banked discovery:**
   - graded-tag grammar (`[mechanical: <method>; <grade>]`, grade ∈ 3)
   - partial-graded universal = defect (the rap-book class)
   - chunk deferral arithmetic (`boundary_type: section` with `est_size` >
     ruled bound)
   - **coverage partition**: every in-scope page in exactly one chunk;
     gap or overlap = hard fail (the docket's lint twin)
   - convention-line count vs container-class bound (the mechanical
     definition, v2.6)
3. **Run the rebuilt validator on both real piles.** Expect failures on the
   old piles (span-era fragments, known defects) — record them as findings,
   do not silently fix the piles.
4. **The test-logging rule** (operator request, 07-18) — filed as a register
   proposal: *every audit finding must terminate in exactly one of: a lint,
   a prompt rule, or an explicitly-rejected docket entry.* Audits mine;
   the validator banks. No finding may simply evaporate.

Done when: selftest green, real-pile results recorded, proposal filed.

---

## Session D — The freeze, and harvest prep

**The job:** write the freeze into law; ready one pile for feeding.

1. **Freeze ruling → register**: no discovery v2.9 and no refactor until a
   harvest run has produced evidence. Unlock condition written into the
   ruling itself, so "one more version?" stops being re-litigated.
2. **Pick the test pile** (button): recommend **rappers-handbook** —
   born_digital, simpler ingest. Requires an ops amendment session first:
   its 4 known defects are still `ratified`. (Loeliger alternative requires
   the p174–179 chunk patch + PDF.) Amend the chosen pile per the amendment
   protocol: changelog line per fix.
3. **Read `pipeline/harvester_prompt_v1.md` against everything learned
   since 07-11** — not to rewrite it (that's speculation), but to list its
   known-stale assumptions so the test run's failures are legible.

Do NOT: fix the harvester prompt preemptively. It earns its v2 from a run,
the same way discovery did.

---

## Session E — First contact: a small harvest

**The job:** feed the machine a handful of chunks and watch it break.

- Scope: 3–5 chunks from the chosen pile, a few workers, one merge attempt.
  Not the whole book. The deliverable is EVIDENCE, not a wiki.
- Three-role where affordable: run ctx ≠ design ctx; audit the output cold
  if budget allows.
- The session report's "friction worth reporting upstream" section is the
  most valuable artifact this roadmap produces. Everything downstream of
  discovery gets its first real docket here.
- Expected outcome per the project's own history: harvester_prompt_v1
  breaks everywhere it obeys something it never defined. That is success.

Done when: the run family + report are FILED (Session A's lesson — same
session, not later), and a docket exists for the harvest stage.

---

## After E

The next design session triages the harvest docket. Discovery reopens only
if harvest evidence names it — that's the freeze's unlock working as
designed. The refactor question (v3.0) waits for: validator green (C),
rule inventory built, regression baseline chosen. All three are cheap once
C is done.
