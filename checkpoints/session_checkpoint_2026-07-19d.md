# Session checkpoint — 2026-07-19d (roadmap Session C, CHUNK 2 — lints 3–5 of 5: COMPLETE)

Purpose: boot file for the next session. **Files are the only memory.** Written
under checkpoint schema v2.1 (slots below, boot manifest last). Reads alongside
07-19c (Session C chunk 2, lints 1–2) and the roadmap. **Model this session:
Claude Opus** — a workshop code session inside the claude.ai project. NORMAL
derivation/code session, NOT a Fable capability probe; keep it out of the Fable
model series. This ctx worked against the operator's uploaded `repetae.zip` (git
tree, commit-clean at `ba92780`), verified on-disk; all scripting ran on the
on-disk unzip. A CODE session (Python), same rhythm as chunks 1–2 — the
deliverable is a green test suite, larger by three lints.

## ⚠ Boot note — a stale checkpoint is in circulation (read first)

The operator may boot a session with `session_checkpoint_2026-07-19.md` (no
suffix) attached. **That file is STALE and its plan is superseded.** It was
written by an un-booted design chat working off the OLD `/mnt/project/` mount,
BEFORE that chat discovered the 07-14 repo migration had landed. Its headline
instruction — "run a dirty Tier-F harvest next session" — predates the roadmap's
proper sequencing and skips Sessions C–D. The repo (this checkpoint's authority)
is the source of truth: the dirty run is roadmap **Session E**, gated behind
finishing C (done as of this checkpoint) and D (the freeze). If both files are
present, THIS one (and 07-19c) win; the no-suffix 07-19 is sediment. Flagged so
the next ctx doesn't re-litigate a decision the repo already sequenced.

## What this session was

**Roadmap Session C, chunk 2 — the FINAL THREE of its five lints.** Chunk 2
lints 1–2 landed in 07-19c (graded-tag grammar, partial-on-universal). This
session landed lints 3, 4, 5, completing Session C's validator rebuild. A code
session in the same rhythm as chunks 1–2: baseline-before-edit, spec read
verbatim before each lint, one lint at a time, suite kept green, defensive
sweep after each. **Result: 24/24 GREEN, exit 0.** No half-built state; all
five lints are in.

## Verified state changes

All inside `tools/discovery-validator/`. Baseline reproduced BEFORE any edit:
selftest **21/21 GREEN** on the uploaded tree (handshake md5s matched the
07-19c boot handshake exactly: rules.py `8927a005`, validate.py `4d13c303`,
build_invalid `0c855151`, valid fixture `d9cf75ea`). Final: **24/24 GREEN,
exit 0.** Three new fixtures, three new lints.

**LINT 3 — chunk-deferral arithmetic (`CHUNKPLAN_OVERSIZED`).** Source: v2.8 §6
chunk-plan axis — a size-bounded fallback for oversized units; "the bound is a
per-source button ruling MEASURED against this source's layout, never a global
constant."
1. `src/rules.py`: `FALLBACK_BOUNDARY_TYPE`, `NATURAL_BOUNDARY_TYPES`
   ({chapter, section, convention}). No global size constant introduced — the
   bound is witnessed by the plan's own data.
2. `src/validate.py`: `parse_est_size()` (int value + unit from "1180 lines");
   `_check_chunk_deferral()` — the smallest `fallback_split` est_size witnesses
   the ruled ceiling (a fallback exists BECAUSE a unit hit the bound); any
   NATURAL boundary at or above that witness should itself have been deferred.
   Silent when no fallback row exists (no witnessed bound in the plan).
   `CHUNKPLAN_SIZE_UNIT` guards a mixed-unit plan (comparison meaningless).
3. Fixture `chunkplan_oversized/`: c01 chapter bloated 1180→1500, above the
   c03 fallback witness (1400). Coverage and unit left intact so only
   `CHUNKPLAN_OVERSIZED` fires.

**LINT 4 — coverage partition (`CHUNKPLAN_COVERAGE`).** The P16 lint twin.
Source: v2.8 §6 coverage rule — "every in-scope range appears in exactly one
chunk … walk the chunk rows in loc order … any gap OR overlap." Enforced by
ARITHMETIC on the loc-grammar, never on the plan's self-narration.
1. `src/rules.py`: `LOC_PAGE_RE` (leading integer of a `page.line` location).
2. `src/validate.py`: `loc_page()`; `_check_chunk_coverage()` — sort spans by
   page, walk adjacent pairs. `next.start == prev.end` is a LEGAL shared-
   boundary page (v2.8's explicit "one page doing double duty" case, e.g. the
   Loeliger p174 back-matter/prose overlap); `start > prev.end + 1` is a GAP
   (the p174–179 class); `start < prev.end` is an OVERLAP. Unparseable locs are
   reported, not skipped — coverage that can't be computed isn't certified.
3. Fixture `chunkplan_coverage/`: c04 start shifted 70.13→72.1, leaving page 71
   unassigned. Only `CHUNKPLAN_COVERAGE` fires.
   - **Design note:** the valid fixture's c03 (55–70) and c04 (70–88) SHARE
     page 70. This is the shared-boundary case, and the lint is written to
     PERMIT it. Confirmed clean on the valid fixture — the lint distinguishes a
     legal shared boundary from an illegal overlap by the strict `<` test.

**LINT 5 — container-keyed convention bound (`CONVENTIONS_TOO_MANY` keyed;
`CONTAINER_CLASS_MISSING`).** The chunk-1 `TODO(chunk-2)` — the biggest debug
risk, per 07-19c. Source: v2.8 Bounds — born_digital ≤50, scan_ocr ≤75; "the
container class is known at Ingest … state it in the read-back."
1. **The wiring gap this surfaced:** the valid fixture had NO machine-readable
   container class — the ingest block was referenced ("emitted below") but the
   class itself was not a parseable line. The honest fix was to add the
   read-back to the valid fixture, not to guess the class from file contents.
2. `fixtures/valid/sample_run/discovery_synth.md`: added an Identity convention
   line — `Ingest read-back: container: born_digital … [mechanical: preflight
   container probe; exhaustive]`. Honestly graded. This changed the valid
   fixture md5.
3. `src/rules.py`: `CONTAINER_CLASS_MARKER`, `CONTAINER_BOUNDS` map; removed the
   chunk-1 `MASTER_MAX_CONVENTION_LINES` hardcoded default (clean removal — no
   dangling refs, verified).
4. `src/validate.py`: `read_container_class()` reads the class from the run's
   own read-back (never inferred); `check_master_bounds()` keys the bound to it.
   **Absent read-back = `CONTAINER_CLASS_MISSING`, NOT a silent strict default**
   — an unstated class was the exact ambiguity v2.6 killed.
5. Fixture `container_class_missing/`: read-back line removed; only
   `CONTAINER_CLASS_MISSING` fires.

## Defensive sweep (per chunk-1/2 discipline)

- Each of the three new fixtures raises EXACTLY its own code (verified by
  isolating violations per case). No co-firing — the specificity contract holds
  at 24/24.
- Valid fixture confirmed clean for the RIGHT reasons, not by luck: shared-
  boundary page 70 allowed; c01=1180 < fallback witness 1400; container reads
  `born_digital`; parsers spot-checked (`loc_page('70.13')→70`,
  `parse_est_size('1180 lines')→(1180,'lines')`).
- Both stale `TODO(chunk-2)` markers removed (rules.py rebuild note updated to
  chunks 1–2; `tag_has_method` docstring corrected — the grade grammar it
  described as owed already shipped in 07-19c via `tag_grade`).
- No new global constants smuggled in: lint 3's bound is witnessed by plan
  data, lint 4 is pure loc arithmetic, lint 5's bounds trace verbatim to v2.8.

## New handshake md5s (verify the merge next session)

| File | md5 | lines | expected_prior (07-19c) |
|---|---|---|---|
| `src/rules.py`        | `cf820125d3e704c2de2a47298ba73de0` | 260 | `8927a005952b71581d08f74ff5a12a08` |
| `src/validate.py`     | `e462fab9f64955811279b5e7bf82dddf` | 765 | `4d13c303c9f6968fafd0f9bfc20611ed` |
| `tests/build_invalid.py` | `73310ee378082dcd881896648955ceea` | 257 | `0c85515175845897dd68188e9050192d` |
| `fixtures/valid/sample_run/discovery_synth.md` | `3bd1287afd21a2bcdecd806840ffa014` | 47 | `d9cf75ead1950196cea3778a000ca5cb` |

All invalid `discovery_synth.md` fixtures + the three new case dirs regenerate
from the valid fixture via `build_invalid.py` (single source of truth); their
per-file md5s are derived, not shipped.

## Rulings (this session)

- **Deferral bound is witnessed, not constant** [ctx call]. v2.8 forbids a
  global size constant; the plan's own smallest fallback_split est_size is the
  legitimate in-band witness of the ruled ceiling. Silent when no fallback
  exists — the plan states no ceiling, so none is enforced.
- **Shared-boundary page is legal; overlap is not** [ctx call, spec-anchored].
  v2.8 explicitly names the shared-boundary case (one page doing double duty).
  `next.start == prev.end` permitted; `next.start < prev.end` fails. Encoded so
  the valid fixture's c03/c04 page-70 touch passes.
- **Absent container class HALTS, does not default** [ctx call, spec-anchored].
  v2.8 says the class is known and must be stated. A missing read-back raises
  `CONTAINER_CLASS_MISSING` rather than silently applying ≤50 — refusing to
  guess is the v2.6 lesson.
- **Valid fixture gains an honest read-back line** [ctx call]. Lint 5 is
  unwireable without a machine-readable class; the fixture lacked one. Added as
  a true, exhaustive-graded ingest line, not a cosmetic stub.

## Propagation / blast radius

- **Outputs do not exist to the next session until synced.** Ship the sources
  (2 src files, 1 generator, valid fixture, this checkpoint) as the standard
  CLOSE PROTOCOL zip; invalid fixtures regenerate on the far side. The sync is
  a paste snippet (no `.sh` file), delivered in the closing message.
- **P11 IS NOW UNBLOCKED (pending sync + commit).** Its unblock condition was
  the FULL validator rebuild — all five lints. That condition is met as of this
  checkpoint. The next design session may treat the mandatory-gate rule (P11) as
  adoptable; ratify-or-reject belongs on the board.
- **Session C chunk 3 is the next validator session:** run the rebuilt
  validator on the two REAL piles (Loeliger + rappers-handbook), record failures
  as findings (do NOT silently fix the piles), and file the test-logging rule
  (roadmap C.4) as a register proposal — *every audit finding terminates in
  exactly one of: a lint, a prompt rule, or an explicitly-rejected docket entry.*
  Expect the real piles to fail: they carry span-era fragments and known
  defects, and (per the scan_ocr note) any scan pile now needs a `container:`
  read-back line or it raises `CONTAINER_CLASS_MISSING` — that finding is
  legitimate signal about the piles, not a validator bug.
- **Then roadmap D** (freeze ruling + harvest prep), **then E** (first contact).

## Open design questions register — delta

NEW: none minted. CARRIED: the roadmap's C(chunk 3)→D→E sequence; register
pending set (P3-R, P4, P5–P7, P9, P10, **P11 now unblockable**, P12, P13, P14→
charter, P15, P16). **The test-logging rule (roadmap C.4) still owed** — chunk-3
deliverable. Boot-protocol + P13 zip riders still owed to register v6 — and the
P13 close rider now carries the 07-19d amendment: the sync is a **paste snippet,
not a shipped `.sh` file** (stateless, reads the zip's MANIFEST, nothing to reuse
across sessions). Ratify the snippet form, not the superseded script form.

## Session hygiene / corrections ledger

- **MODEL: Claude Opus** (normal code session). NOT a Fable probe.
- **Baseline-before-edit held.** 21/21 reproduced on the uploaded tree, handshake
  md5s matched the 07-19c boot handshake, BEFORE any edit.
- **Spec read verbatim before each lint**, not written from the roadmap
  one-liner — surfaced that lint 5 needed a fixture change (the missing container
  read-back), which the one-liner did not mention.
- **No predicted-class failures chased this session** — the three lints came in
  specific on first build (the coverage fixture needed one framing pass to pick a
  single-rule break, resolved before selftest, not a debug cycle).
- **Scope held.** Only lints 3–5. No real-pile runs (that is chunk 3), no
  refactor, no "improve while I'm in here." The two doc-comment corrections were
  removing now-false TODOs the edits made stale — housekeeping of this session's
  own footprint, not scope creep.
- **BOOT/CLOSE PROTOCOL exercised** per 07-19c: worked against the uploaded zip
  verified on disk; close is the standard sources-only zip + a paste-snippet
  sync (no `.sh` file, per the 07-19d ruling) + MANIFEST with two-hash fields.

## Boot manifest — request list (next session = Session C, CHUNK 3: real-pile runs + test-logging proposal)

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

### CLOSE PROTOCOL (burned in — standard for all subsequent checkpoints; snippet form as of 07-19d)

Every work session ends the same way. Deliverables travel as ONE zip; the
operator places them with a PASTE SNIPPET that verifies before it writes. **No
sync SCRIPT is shipped** — a `.sh` file is one more artifact to track and reuse
across sessions, and the sync is generic (it reads the zip's own MANIFEST), so
it lives as a stateless snippet the operator pastes and discards [operator
ruling, 07-19d]. The snippet form supersedes the earlier `close_sync.sh`-beside-
the-zip form; do NOT rebuild a script.

1. **Ship SOURCES, not derived artifacts.** The zip carries authored files —
   code, the valid fixture, the checkpoint — under repo-relative paths, plus
   `MANIFEST.txt`. Files a script regenerates (the invalid fixtures, from
   `build_invalid.py`) are NOT shipped; the sync regenerates them on the far
   side.
2. **Manifest in the zip.** `MANIFEST.txt` lists every shipped file as
   `path · md5 · bytes · lines · expected_prior_md5`. `expected_prior_md5` is
   `-` for new/unchanged files, or the md5 the file had at session boot for
   files this session edited.
3. **Two-hash placement** [operator ruling, 07-19c]. Per shipped file the sync:
   places if absent; skips if disk already equals the new md5 (idempotent);
   overwrites ONLY if disk equals `expected_prior_md5`; HALTS on any other
   difference as an unknown collision, clobbering nothing. Refuses a dirty tree.
4. **Regenerate + prove green.** After placement the sync runs
   `build_invalid.py` then the selftest; a sync that does not end green tells the
   operator NOT to commit. Only then does it print the commit line.

The sync is a paste snippet, delivered in the closing chat message (not a file).
The operator sets `ZIP=` to the downloaded zip's path and pastes the snippet
from `~/git/repetae`. The snippet is stateless — it reads the zip's MANIFEST, so
the same shape works for every session with no per-session script to maintain.

---

**READ THIS FIRST.** The repo is the source of truth: `~/git/repetae`,
operator's machine (Pop!_OS, X11, GNOME; `xclip` present). **Session C is
COMPLETE through the validator rebuild: all five lints are green (24/24). The
next session is Session C CHUNK 3** — the real-pile shakedown: run the rebuilt
validator on Loeliger + rappers-handbook, record (do NOT fix) the failures as
findings, and file the test-logging rule as a register proposal. Then roadmap D
(freeze), then E (first contact). Do NOT reopen lints without a real-pile
finding naming one — that is the freeze discipline arriving early.

Requisition snippet — run in `~/git/repetae`, paste output, then ATTACH the
validator dir + both full run piles:

```bash
cd ~/git/repetae && { echo "=== session-C-chunk-3-real-piles requisition $(date -u +%FT%TZ) ==="
req(){ [ -f "$1" ] && printf '%-52s OK md5=%s lines=%s\n' "$2" \
  "$(md5sum "$1"|cut -d' ' -f1)" "$(wc -l <"$1")" \
  || printf '%-52s MISSING: %s\n' "$2" "$1"; }
echo "--- TIER 1: REQUIRED (attach the whole validator dir) ---"
req tools/discovery-validator/src/rules.py           "rules.py (all 5 lints)"
req tools/discovery-validator/src/validate.py        "validate.py (all 5 lints)"
req tools/discovery-validator/tests/selftest.py      "selftest.py"
req tools/discovery-validator/tests/build_invalid.py "build_invalid.py"
req tools/discovery-validator/fixtures/valid/sample_run/discovery_synth.md "valid fixture (now container-graded)"
echo "--- TIER 1: the real piles (attach both, whole run dirs) ---"
req evidence/loeliger-til-run-2026-07-18/discovery_loeliger-til.md   "Loeliger pile (real-run test 1)"
req evidence/rappers-handbook-run-2026-07-15/discovery_rappers-handbook.md "rappers pile (real-run test 2)"
echo "--- expected handshake (this session's outputs, verify merged) ---"
echo "  rules.py        EXPECT cf820125d3e704c2de2a47298ba73de0"
echo "  validate.py     EXPECT e462fab9f64955811279b5e7bf82dddf"
echo "  build_invalid   EXPECT 73310ee378082dcd881896648955ceea"
echo "  valid fixture   EXPECT 3bd1287afd21a2bcdecd806840ffa014"
echo "--- verify GREEN before real-pile runs ---"
echo "  cd tools/discovery-validator && python3 tests/selftest.py   # EXPECT 24/24"
echo "=== end ==="; } | tee /dev/tty | xclip -selection clipboard
```

If the outputs' md5s do not match, the merge did not take — re-sync from this
session's zip FIRST, confirm `python3 tests/selftest.py` is 24/24, THEN run the
real piles.
