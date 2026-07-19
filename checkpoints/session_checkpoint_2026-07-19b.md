# Session checkpoint — 2026-07-19b (roadmap Session C, CHUNK 1 of 3 executed)

Purpose: boot file for the next session. **Files are the only memory.** Written
under checkpoint schema v2.1 (slots below, boot manifest last). Reads alongside
07-19 (Session B) and the roadmap. **Model this session: Claude Opus** — a
workshop code session inside the claude.ai project. NORMAL derivation/code
session, NOT a Fable capability probe; keep it out of the Fable model series.
This ctx had the operator's uploads (the whole repo as `repetae.zip`, git tree,
commit-clean); scripts ran ONLY against the on-disk unzip. This is a CODE
session (Python), a different rhythm from B's prose-diffing — the deliverable is
a green test suite, not a patched prompt.

## What this session was

**Roadmap Session C, chunk 1 of a planned 3.** Session C's full job (rebuild the
validator against v2.8, add five lints, run both real piles, file the
test-logging rule) was scoped by the operator into three chunks at session
start, after a context-budget check. **Only chunk 1 was executed** — deliberately,
as the safe save-point. Chunk 1: fix the two red selftests + re-ground rules.py
v2.5→v2.8, get the EXISTING 19-fixture suite green. Chunks 2 (the five new lints
+ container-class detection) and 3 (real-pile runs + findings + register
proposal) are the next one or two sessions.

The session also exercised the newly-agreed BOOT PROTOCOL (orient → requisition
→ attach → work) end to end for the first time — see below.

## Verified state changes

All inside `tools/discovery-validator/`. Baseline reproduced BEFORE any edit:
selftest 17/19 RED, exit 1, with exactly the two failures the roadmap named
(`TAG_ILLEGAL` non-specific; `TAG_MECHANICAL_NO_METHOD` false pass). Final:
**19/19 GREEN, exit 0.**

1. **`src/rules.py` RE-GROUNDED v2.5 → v2.8** (md5
   `d7d429fd69a2fffe3b669b1674031cd1`). Module docstring re-cited; all nine
   `Source:` comments moved v2.5→v2.8 by sed, THEN the enums were verified
   still-current against v2.8 (content modes, boundary types, chunk-plan
   columns, the six legal tags — all unchanged v2.5→v2.8, so the relabel is
   not a lie). Convention-line bound changed from the flat `~45` to
   container-keyed constants: `MASTER_MAX_CONVENTION_LINES_BORN_DIGITAL = 50`,
   `..._SCAN_OCR = 75`, with the born_digital value wired as the chunk-1
   default. **The scan_ocr branch is DEFINED but NOT APPLIED** — see deferrals.
2. **`src/validate.py` — TWO BUG FIXES** (md5
   `c2ef517e30465521eeb929fc59d7b88f`):
   - **`tag_has_method`**: v2.5 accepted the method in the line's PROSE; v2.8
     forbids it ("one with the method in the line's prose ... is a defect",
     v2.8 Provenance tags §). The old prose-fallback was always satisfied
     (every convention line has prose before its tag), which is why
     `TAG_MECHANICAL_NO_METHOD` never fired. Now requires non-empty content
     after a separator INSIDE the bracket. Chunk-1 scope: enforces
     method-in-bracket only, NOT the full `<method>; <grade>` grammar.
   - **`check_provenance_tags`**: `TAG_ILLEGAL` and `TAG_BARE` are now
     MUTUALLY EXCLUSIVE. Three cases: no brackets → BARE; a non-citation
     bracket that is not a legal tag → ILLEGAL only; only citations
     (`[p:89]`, `[fig:3.1]`) and no tag → BARE. The old code fired both,
     failing the selftest's specificity assertion.
3. **`tests/build_invalid.py` — generator anchors moved IN LOCKSTEP** (md5
   `c2c808e5a2cae4aca3e80556ad3bf09c`). Two cases referenced the old
   `[mechanical]`-prose wording as their string anchor; when the valid fixture
   was reworded they would have silently no-op'd (the W12/lockstep trap). Fixed:
   `TAG_MECHANICAL_NO_METHOD`'s anchor updated to the new wording; `TAG_MULTIPLE`'s
   injected second tag made well-formed (`[mechanical: x count]`) so ONLY
   `TAG_MULTIPLE` fires, not `TAG_MECHANICAL_NO_METHOD` too.
4. **Fixtures rewritten to v2.8 tag form** (valid `discovery_synth.md` md5
   `c4c9cbfb648038a375a5a4448471ee72`; all 18 invalid regenerated from it via
   `build_invalid.py`). Four `[mechanical]` tags converted from prose-method to
   method-in-bracket (`[mechanical: counted across the anchor table]` etc.).
   **These are the SINGLE SOURCE OF TRUTH** (`shutil.copytree(VALID, ...)`), so
   patching the valid fixture + regenerating propagates cleanly — no per-file
   hand-edit, no lockstep drift. **Grades NOT added yet** — chunk 2.

## Rulings (this session — operator free-text concurrence, not buttons)

- **Chunk the session; do chunk 1 only** [operator: "chunk 1", after the ctx
  reported it was NOT confident all three chunks fit one context budget].
  Recorded because it is the roadmap's "one job per session" discipline applied
  one level finer: Session C's job was itself too big for one context, and the
  ctx said so BEFORE starting rather than running out mid-chunk-2 with fixtures
  half-built (the worst stop state). The save-point chosen (selftest green on the
  existing fixtures) leaves the repo strictly better, nothing half-finished.
- **Container-class detection is chunk 2, not chunk 1** [ctx scope call, stated
  loudly, operator did not override]. v2.8's bound is container-keyed
  (born_digital ≤50 / scan_ocr ≤75), but the validator does not yet READ the
  class off a run. Wiring that is new reading logic with its own debug risk;
  deferred with an inline `TODO(chunk-2)`. Chunk 1 wires the born_digital
  default only. A scan_ocr pile checked this session would false-flag against
  the too-strict 50 — noted so chunk 3 does not mistake it for a real finding.
- **Fixtures speak v2.8 without grades, for now** [ctx scope call]. The chunk-1
  method check only requires SOMETHING in the bracket; grades arrive with the
  graded-tag lint in chunk 2, at which point these fixtures get their
  `; <grade>` suffix.

## Dependency ledger (verified-how)

| Dependency | Status | Verified how |
|---|---|---|
| whole repo (`repetae.zip`, git, commit-clean) | ✓ ON DISK | unzipped to `/home/claude/repo/repetae`; every requisitioned file md5-matched the pre-attach handshake EXACTLY (10/10 OK, no MISSING) |
| `discovery_prompt_v2_8.md` | ✓ FILE, ON DISK | md5 `7fb622ea…` EXACT, 673L — the rebuild authority; read the Provenance-tags § and Bounds § IN FULL before editing rules |
| `pipeline_config_schema_v2.md` | ✓ FILE, ON DISK | md5 `d3f866c4…` EXACT — enum cross-check (unchanged; schema-boundary still out of scope per README) |
| `tools/discovery-validator/` (whole dir) | ✓ ON DISK | selftest run as-is for baseline (17/19 RED) BEFORE editing; rules.py + validate.py + selftest.py + build_invalid.py read in full |
| roadmap `…close-and-first-contact.md` | ✓ ATTACHED | the session contract; Session C scope held (chunk 1 is a sub-scope, not a widening) |

## Propagation / blast radius

- **Chunk-1 outputs do not exist to the next session until synced.** The
  outbound sync ships the whole `tools/discovery-validator/` tree (22 modified
  files) + this checkpoint, as a git-aware apply (stage → diff → selftest-verify
  → operator commits). Once merged, `tools/discovery-validator/` is at "v2.8
  chunk-1: two red tests fixed, envelope re-grounded, 19/19 green."
- **P11 is NOT yet unblocked.** P11's unblock is the FULL validator rebuild
  (the mandatory-door rule needs a door that reads current spec). Chunk 1 is
  necessary but not sufficient — the five lints (chunk 2) are the substance of
  the "bank the mine" deliverable. Do not increment P11 or mark it unblocked on
  chunk 1 alone.
- **The graded-tag grammar is the biggest owed piece.** v2.8 requires
  `[mechanical: <method>; <grade>]` with grade ∈ {exhaustive, sampled, partial}
  AND the partial-on-universal defect check. Chunk 1 enforces method-in-bracket
  but is BLIND to grades. A real pile run now would pass graded-tag defects
  silently. This is the first chunk-2 lint.

## Open design questions register — delta

NEW: none minted. The three deferrals above are roadmap-scoped chunk-2/3 work,
not new design questions. CARRIED unchanged from 07-19: the roadmap's C–E
sequence; register pending set (P3-R, P4, P5–P7, P9, P10, P11 blocked, P12, P13,
P14→charter, P15, P16). **The test-logging rule (roadmap C.4) is still owed** —
it is a chunk-3 deliverable (filed as a register proposal once the real-pile
runs give it evidence).

## Reference-doc debt — slot

**NONE re-issued this session** (a code session touches the tool, not the
reference layer). CARRIED, still owed:
- The BOOT PROTOCOL + its P13 rider (this session's other thread — see below).
  Drafted, handed to the operator as `boot_protocol_and_p13_rider.md`, NOT yet
  filed into a checkpoint manifest or the register. **This checkpoint's boot
  manifest below IS the protocol's first live home** (per the operator ruling
  to burn it into every subsequent checkpoint).
- The P13 outbound-zip rider (deliverables travel as one zip, unpack-verify-
  place, refuse collisions) — owed to the register from 07-18c, joins the boot-
  protocol rider in the next register rev (v6). Both are P13 riders.

## Session hygiene / corrections ledger

- **MODEL: Claude Opus** (normal code session). NOT a Fable probe.
- **Baseline-before-edit held.** The 17/19 RED baseline was REPRODUCED and read
  before a single line changed — the two red tests were confirmed present and
  their mechanism understood from the code, not assumed from the roadmap's
  one-liners. This is what surfaced that the bugs were deeper than the roadmap
  said (the method rule needed the full v2.8 grammar; chunk 1 does the method
  half).
- **A predicted fixture failure, chased not patched-around.** After the
  `tag_has_method` fix, the suite went to 1/19 — the valid fixture's own
  `[mechanical]` tags used the old prose form. This was PREDICTED aloud before
  running, and correctly diagnosed as a fixture-data problem (W12: fixtures
  authored from the same misreading as the code), not a code regression. Fixed
  at the source (the valid fixture) + regenerated, not worked around in the
  checker.
- **Lockstep caught before it bit.** The generator's string anchors referenced
  the wording being changed; noticed BEFORE regenerating (which would have
  silently no-op'd two cases). Fixed in the same pass. Same organ as P14.
- **Scope held.** Container-class detection, the five lints, and the real-pile
  runs were all explicitly NOT done and marked `TODO(chunk-2)` / deferred to
  chunk 3 — no "improve while I'm in here." The `## `/enum surfaces were read,
  not rewritten.
- **BOOT PROTOCOL exercised.** Orient (operator pasted tree + git status) →
  requisition snippet (10/10 OK) → attach (whole repo zip) → verify md5s → work.
  First full run of the just-agreed protocol; it worked, and the whole-repo
  attach satisfied the requisition in one shot (no loop needed).
- Deliverables: the modified validator tree, this checkpoint, and the outbound
  git-sync snippet. Backups of the four hand-edited files kept in the ctx during
  the session (not shipped).

## Boot manifest — request list (next session = roadmap Session C, CHUNK 2)

### BOOT PROTOCOL (burned in until ratified — see the P13 rider owed to register v6)

Every work session opens the same way. No real work begins until it completes.

1. **Orient.** The ctx asks the operator to paste current repo state — a
   `tree`, a git hash/status listing, or whatever single command captures the
   layout and currency of what matters, scoped to fit `xclip`. The ctx does NOT
   guess the repo's shape from memory or from a stale mount.
2. **Requisition, then loop.** The ctx emits a bash requisition snippet (P13
   inbound shape: probe declared dependency paths, print md5 + line counts, loud
   `MISSING:` branch, tailed `| tee /dev/tty | xclip -selection clipboard`). The
   operator runs it; pastes the output back. If that output reveals more that is
   needed, the ctx emits another snippet. This loops until the ctx has everything.
3. **Attach for scripting.** Anything scripted against is ATTACHED via paperclip,
   never pasted (a pasted blob lands in context, not on disk at
   `/mnt/user-data/uploads`). Paste-for-reading, attach-for-scripting.
4. **Then, and only then, work begins.** A session does not start its job until
   orientation and requisition are complete.

---

**READ THIS FIRST.** The repo is the source of truth: `~/git/repetae`,
operator's machine (Pop!_OS, X11, GNOME; `xclip` present); a ctx cannot read it.
This manifest is a request list. **Session C chunk 1 is DONE; the next session
is Session C chunk 2 — the five lints + container-class detection.** Chunk 2's
job: add one lint per banked discovery to the now-v2.8 validator —
graded-tag grammar (`[mechanical: <method>; <grade>]`, grade ∈ {exhaustive,
sampled, partial}); partial-on-universal = defect; chunk-deferral arithmetic
(`boundary_type: section` with oversized `est_size`); coverage-partition (the
P16 lint twin, gap/overlap = hard fail); convention-count vs container bound
(which requires wiring container-class detection first). Each lint gets its own
fixture(s) via `build_invalid.py` + a selftest case, kept green. One job.
Anything else → docket. (Chunk 3 — real-pile runs + findings + the test-logging
register proposal — is the session after.)

Requisition snippet — run in `~/git/repetae`, paste output, then ATTACH the
Tier-1 files (scripts run only against attachments on disk):

```bash
cd ~/git/repetae && { echo "=== session-C-chunk-2 requisition $(date -u +%FT%TZ) ==="
req(){ [ -f "$1" ] && printf '%-52s OK md5=%s lines=%s\n' "$2" \
  "$(md5sum "$1"|cut -d' ' -f1)" "$(wc -l <"$1")" \
  || printf '%-52s MISSING: %s\n' "$2" "$1"; }
echo "--- TIER 1: REQUIRED (attach the whole validator dir) ---"
req tools/discovery-validator/src/rules.py           "rules.py (chunk-1 output; add lints here)"
req tools/discovery-validator/src/validate.py        "validate.py (chunk-1 output)"
req tools/discovery-validator/tests/selftest.py      "selftest.py"
req tools/discovery-validator/tests/build_invalid.py "build_invalid.py (fixture generator)"
req pipeline/discovery_prompt_v2_8.md                "discovery v2.8 (lint authority)"
req pipeline/pipeline_config_schema_v2.md            "schema v2 (field authority)"
req evidence/docket_chunk_coverage_reverify_v1.md    "coverage docket (partition-lint source)"
req evidence/discovery_eval_findings_rappers-handbook.md "rappers audit findings (lint mine)"
echo "--- expected handshake (chunk-1 outputs, verify merged) ---"
echo "  rules.py        EXPECT d7d429fd69a2fffe3b669b1674031cd1"
echo "  validate.py     EXPECT c2ef517e30465521eeb929fc59d7b88f"
echo "  build_invalid   EXPECT c2c808e5a2cae4aca3e80556ad3bf09c"
echo "  valid fixture   EXPECT c4c9cbfb648038a375a5a4448471ee72"
echo "--- verify selftest is GREEN on the merged tree before adding lints ---"
echo "  cd tools/discovery-validator && python3 tests/selftest.py   # EXPECT 19/19"
echo "=== end ==="; } | tee /dev/tty | xclip -selection clipboard
```

**Chunk 2's one job:** the five lints + container detection, each fixture-backed,
suite kept green. The roadmap is the contract; hold to it. If the chunk-1 md5s
above do not match, the merge did not take — re-sync from this session's zip
FIRST, and confirm `python3 tests/selftest.py` is 19/19 before writing any lint.
