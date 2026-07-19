# Session checkpoint — 2026-07-19c (roadmap Session C, CHUNK 2 — lints 1–2 of 5)

Purpose: boot file for the next session. **Files are the only memory.** Written
under checkpoint schema v2.1 (slots below, boot manifest last). Reads alongside
07-19b (Session C chunk 1) and the roadmap. **Model this session: Claude Opus** —
a workshop code session inside the claude.ai project. NORMAL derivation/code
session, NOT a Fable capability probe; keep it out of the Fable model series.
This ctx worked against the operator's uploaded `repetae.zip` (git tree,
commit-clean at `481b0fa`), verified against the live-machine handshake; all
scripting ran on the on-disk unzip. A CODE session (Python), same rhythm as
chunk 1 — the deliverable is a green test suite, larger by two lints.

## What this session was

**Roadmap Session C, chunk 2 — but only the FIRST TWO of its five lints.**
Context budget was checked mid-session: after lint 2 the ctx judged it did not
have room to safely land the two reading-logic lints (coverage-partition,
convention-count vs container-bound, the latter needing container-class
detection first) without risking the worst stop-state — running out mid-lint
with fixtures half-built. Per the project's chunking discipline, we stopped at a
clean save-point: **two lints green, nothing half-finished.** The remaining
three lints are the next session (chunk 2 continued).

## Verified state changes

All inside `tools/discovery-validator/`. Baseline reproduced BEFORE any edit:
selftest **19/19 GREEN** on the merged chunk-1 tree (handshake md5s all matched
the live machine: rules.py `d7d429fd`, validate.py `c2ef517e`, build_invalid
`c2c808e5`, valid fixture `c4c9cbfb`). Final: **21/21 GREEN, exit 0.**

**LINT 1 — graded-tag grammar (`TAG_NO_GRADE`).** Option-1 scope (operator
button): both no-grade AND illegal-grade-word fail.
1. `src/rules.py`: added `LEGAL_GRADES = {exhaustive, sampled, partial}` and
   `MECHANICAL_GRADE_SEPARATOR = ";"`, sourced to v2.8 Provenance-tags §.
2. `src/validate.py`: new `tag_grade(token)` — grade is the LAST `;`-delimited
   clause, split from the RIGHT so a method clause containing `:`/`,` (e.g.
   `[mechanical: Class: = Function: = 172, exact; exhaustive]`) is safe.
   Returns the grade iff legal, else None. Wired `TAG_NO_GRADE` into the
   tag-check loop AFTER the method check, guarded by `continue` so a
   method-less tag raises only `TAG_MECHANICAL_NO_METHOD` (specificity contract).
3. **Valid fixture upgraded with HONEST grades** (chunk-1 deferred this):
   line 11 `exhaustive` (14/14 covers the claim), line 12 `exhaustive`
   (census = full population), line 32 `exhaustive` (full transcription),
   line 35 `sampled` (one item named from the watchlist). Grades assigned by
   claim, not cosmetically. This changed the valid fixture md5.
4. New fixture `fixtures/invalid/tag_no_grade/`.
5. **Two lockstep anchors fixed** (W12 trap): `TAG_MECHANICAL_NO_METHOD`'s
   generator anchor updated to the graded wording; `TAG_MULTIPLE`'s injected
   second tag given a grade (`[mechanical: x count; sampled]`) so only
   `TAG_MULTIPLE` fires. The second was a PREDICTED-class failure — the suite
   went 19/20 with `TAG_MULTIPLE also raised TAG_NO_GRADE`, correctly diagnosed
   as fixture-data authored to the old gradeless spec, fixed at source not in
   the checker.

**LINT 2 — partial-on-universal (`TAG_PARTIAL_UNIVERSAL`).** The
rappers-handbook class.
1. `src/rules.py`: added `UNIVERSAL_QUANTIFIERS = (always, every, never,
   invariant, "fixed frame")`. Scope deliberately TIGHT — bare `fixed` and
   `throughout` EXCLUDED (they appear in innocent prose; the valid fixture's
   `title case throughout` is exhaustive-graded and true). Sourced to v2.8 +
   the audit's generalizable rule (findings lines 44–53).
2. `src/validate.py`: new `line_has_universal(line)` — whole-word match for
   single words, substring for the `fixed frame` phrase, case-insensitive.
   Wired `TAG_PARTIAL_UNIVERSAL`, fires only when `tag_grade(tok) == "partial"`
   AND `line_has_universal`. Cannot co-fire with `TAG_NO_GRADE` (partial is a
   LEGAL grade). `continue` guards make the mutual exclusion explicit.
3. New fixture `fixtures/invalid/tag_partial_universal/` — mirrors the real
   defect: `- Aliases ALWAYS appear ... [mechanical: census ...; partial]`.
4. Caught specific on first run, no debug cycle. Defensive sweep confirmed no
   other invalid case raises the new code.

## New handshake md5s (verify the merge next session)

| File | md5 | lines |
|---|---|---|
| `src/rules.py`        | `8927a005952b71581d08f74ff5a12a08` | 204 |
| `src/validate.py`     | `4d13c303c9f6968fafd0f9bfc20611ed` | 595 |
| `tests/build_invalid.py` | `0c85515175845897dd68188e9050192d` | 222 |
| `fixtures/valid/sample_run/discovery_synth.md` | `d9cf75ead1950196cea3778a000ca5cb` | (grades added) |

All 19 invalid `discovery_synth.md` fixtures + the two new case dirs regenerate
from the valid fixture via `build_invalid.py` (single source of truth); their
per-file md5s are derived, not hand-authored.

## Rulings (this session)

- **Option 1 for the graded-tag lint** [operator button]: no-grade AND
  illegal-grade-word both fail. Widest net.
- **Grade = last `;` clause, split from the right** [ctx call]: the method
  clause legally contains `:` and `,`; only `;` delimits the grade. Encoded so
  v2.8's own `Class: = Function: = 172, exact; exhaustive` example parses.
- **Universal vocabulary kept tight** [ctx call]: `always/every/never/
  invariant/"fixed frame"` only; `fixed` and `throughout` excluded to avoid
  false-flagging innocent prose. If a real pile shows a missed universal, widen
  from evidence (chunk 3), don't speculate now.
- **Stop at two lints** [ctx budget call, operator concurred "finish that and
  checkout"]: the two reading-logic lints carry container-class detection's
  deferred debug risk; landing them on a tired context risked the half-built
  stop-state. Save-point chosen leaves the repo strictly better.

## Propagation / blast radius

- **Outputs do not exist to the next session until synced.** Ship the whole
  `tools/discovery-validator/` tree (2 src files, 1 generator, valid fixture +
  all regenerated invalids, 2 new case dirs) as a git-aware apply
  (stage → diff → selftest-verify → operator commits). `__pycache__` excluded.
- **P11 still NOT unblocked.** Its unblock is the FULL rebuild (all five lints +
  container detection). Two of five is progress, not the door.
- **Three lints still owed in chunk 2:** chunk-deferral arithmetic
  (`boundary_type: section` with oversized `est_size`); coverage-partition (the
  P16 lint twin, gap/overlap = hard fail); convention-count vs container-bound
  (REQUIRES wiring container-class detection first — chunk-1's deferred
  `TODO(chunk-2)`, the biggest single risk left). Then chunk 3 (real-pile runs +
  findings + the test-logging register proposal) is the session after.

## Open design questions register — delta

NEW: none minted. CARRIED from 07-19b: the roadmap's C–E sequence; register
pending set (P3-R, P4, P5–P7, P9, P10, P11 blocked, P12, P13, P14→charter, P15,
P16). **The test-logging rule (roadmap C.4) still owed** — chunk-3 deliverable.
Boot-protocol rider still owed to register v6.

**P13 outbound-zip rider — IMPLEMENTED this session (operator directive: make
the zip+shell close standard for all subsequent checkpoints).** Owed since
07-18c, shipped as a bare snippet in 07-19; now realized in its true zip form
and burned into the CLOSE PROTOCOL below. The rider text should still land in
register v6 as ratified law, but it is no longer just owed — it is running. Its
shape, decided this session: **sources-only zip + regenerate on place** (ship
the code + valid fixture + checkpoint; the invalid fixtures regenerate from
`build_invalid.py` on the far side, matching the tool's single-source-of-truth
model — do NOT ship 130 derived fixtures), and the **two-hash collision rule**
[operator button]: overwrite a differing file ONLY if disk == the expected-prior
md5 the manifest declares; any other difference HALTS as an unknown collision.
The manifest carries `path, md5, bytes, lines, expected_prior_md5` (the `bytes`
field is the one 07-18c shipped without).

## Session hygiene / corrections ledger

- **MODEL: Claude Opus** (normal code session). NOT a Fable probe.
- **Baseline-before-edit held.** 19/19 reproduced on the merged tree, handshake
  md5s matched live machine, BEFORE any edit.
- **Spec read verbatim before each lint**, not written from the roadmap
  one-liner — surfaced that the partial-on-universal rule is a SEPARATE lint
  from graded-tag grammar (the roadmap lists them separately; confirmed against
  v2.8 §Provenance + the audit's generalizable rule).
- **One predicted-class failure, chased not patched-around** (TAG_MULTIPLE ×
  TAG_NO_GRADE) — fixed at the fixture source, W12 discipline.
- **Scope held.** The three remaining lints and container-class detection
  explicitly NOT started. No "improve while I'm in here."
- **BOOT PROTOCOL exercised** (orient → requisition → attach → work): operator
  pasted tree + git status + live handshake; ctx verified the uploaded zip
  against it (7/8 direct matches + the 8th resolved as a path-guess error on the
  ctx's side, not a file problem — fixture lives at `fixtures/valid/sample_run/`,
  not `tests/fixtures/`). Whole-repo zip satisfied requisition in one shot.
- **CLOSE PROTOCOL exercised and standardized** (operator directive). The
  outbound sync was dry-run against a clean clone (4 files UPDATED via the
  two-hash rule, invalids regenerated, selftest 21/21) AND a tampered clone (a
  rogue local edit to `validate.py` correctly HALTED as an unknown collision,
  nothing clobbered). Both behaviors verified before shipping. Now burned into
  the boot manifest as the standing close, per the operator's instruction to
  make it standard for all subsequent checkpoints.

## Boot manifest — request list (next session = Session C, chunk 2 continued: lints 3–5)

### BOOT PROTOCOL (burned in until ratified — P13 rider owed to register v6)

Every work session opens the same way. No real work begins until it completes.

1. **Orient.** Ctx asks the operator to paste current repo state (`tree`, git
   hash/status), scoped to fit `xclip`. No guessing from a stale mount.
2. **Requisition, then loop.** Ctx emits a bash requisition snippet (probe
   declared paths, print md5 + line counts, loud `MISSING:` branch, `| tee
   /dev/tty | xclip -selection clipboard`). Operator runs it, pastes back. Loop
   until the ctx has everything.
3. **Attach for scripting.** Anything scripted against is ATTACHED (paperclip)
   or supplied as the whole-repo zip — never pasted. Paste-for-reading,
   attach-for-scripting.
4. **Then, and only then, work begins.**

### CLOSE PROTOCOL (burned in — standard for all subsequent checkpoints, 07-19c)

Every work session ends the same way. Deliverables travel as ONE zip; the
operator places them with one snippet that verifies before it writes.

1. **Ship SOURCES, not derived artifacts.** The zip carries authored files —
   code, the valid fixture, the checkpoint — under repo-relative paths. Files
   that a script regenerates (the invalid fixtures, from `build_invalid.py`) are
   NOT shipped; the sync regenerates them on the far side. This matches the
   tool's single-source-of-truth model and keeps the manifest small enough to
   eyeball.
2. **Manifest in the zip.** `MANIFEST.txt` lists every shipped file as
   `path · md5 · bytes · lines · expected_prior_md5`. `expected_prior_md5` is
   `-` for new/unchanged files, or the md5 the file had at session boot for
   files this session edited (from the boot handshake).
3. **Two-hash placement** [operator ruling, 07-19c]. Per shipped file the sync:
   places if absent; skips if disk already equals the new md5 (idempotent);
   overwrites ONLY if disk equals `expected_prior_md5` (a known, intended
   update); HALTS on any other difference as an unknown collision, clobbering
   nothing. It also refuses to run on a dirty working tree.
4. **Regenerate + prove green.** After placement the sync runs
   `build_invalid.py` then `selftest.py`; a sync that does not end green tells
   the operator NOT to commit. Only then does it print the commit line.

The outbound zip and its `close_sync.sh` ship as SEPARATE deliverables —
`close_sync.sh` lives BESIDE the zip, never inside it (a sync script sealed in
the archive it must unpack is unusable). Running it is:
`bash close_sync.sh /path/to/<session>.zip` from
`~/git/repetae`.

---

**READ THIS FIRST.** The repo is the source of truth: `~/git/repetae`,
operator's machine (Pop!_OS, X11, GNOME; `xclip` present). **Session C chunk 2
lints 1–2 are DONE; the next session is lints 3–5.** Lint 3: chunk-deferral
arithmetic. Lint 4: coverage-partition (P16 twin, gap/overlap = hard fail).
Lint 5: convention-count vs container-bound — **do this last; it requires wiring
container-class detection (reading `content_class` off the run) first, which is
the deferred `TODO(chunk-2)` and the biggest debug risk.** Each lint: one
`build_invalid.py` case + a selftest assertion, suite kept green, one job.
Anything else → docket. (Chunk 3 — real-pile runs + findings + test-logging
register proposal — is the session after.)

Requisition snippet — run in `~/git/repetae`, paste output, then ATTACH the
validator dir (or the whole-repo zip):

```bash
cd ~/git/repetae && { echo "=== session-C-chunk-2-lints-3to5 requisition $(date -u +%FT%TZ) ==="
req(){ [ -f "$1" ] && printf '%-52s OK md5=%s lines=%s\n' "$2" \
  "$(md5sum "$1"|cut -d' ' -f1)" "$(wc -l <"$1")" \
  || printf '%-52s MISSING: %s\n' "$2" "$1"; }
echo "--- TIER 1: REQUIRED (attach the whole validator dir) ---"
req tools/discovery-validator/src/rules.py           "rules.py (lints 1-2 output; add lints 3-5 here)"
req tools/discovery-validator/src/validate.py        "validate.py (lints 1-2 output)"
req tools/discovery-validator/tests/selftest.py      "selftest.py"
req tools/discovery-validator/tests/build_invalid.py "build_invalid.py (fixture generator)"
req tools/discovery-validator/fixtures/valid/sample_run/discovery_synth.md "valid fixture (now graded)"
req tools/discovery-validator/fixtures/valid/sample_run/chunk_plan_synth.csv "valid chunk plan (deferral+partition source)"
req pipeline/discovery_prompt_v2_8.md                "discovery v2.8 (lint authority)"
req pipeline/pipeline_config_schema_v2.md            "schema v2 (field authority: content_class, boundary_type)"
req evidence/docket_chunk_coverage_reverify_v1.md    "coverage docket (partition-lint source)"
echo "--- expected handshake (lints 1-2 outputs, verify merged) ---"
echo "  rules.py        EXPECT 8927a005952b71581d08f74ff5a12a08"
echo "  validate.py     EXPECT 4d13c303c9f6968fafd0f9bfc20611ed"
echo "  build_invalid   EXPECT 0c85515175845897dd68188e9050192d"
echo "  valid fixture   EXPECT d9cf75ead1950196cea3778a000ca5cb"
echo "--- verify GREEN before adding lints ---"
echo "  cd tools/discovery-validator && python3 tests/selftest.py   # EXPECT 21/21"
echo "=== end ==="; } | tee /dev/tty | xclip -selection clipboard
```

If the lints-1–2 md5s do not match, the merge did not take — re-sync from this
session's zip FIRST, confirm `python3 tests/selftest.py` is 21/21, THEN write
lint 3.
