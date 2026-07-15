# discovery-validator

Envelope conformance checker for discovery output. Hard-fail, binary verdict.

Implements **P-2 (forecast quarantine)**, **P-3 (provenance-tag lint)**, and
**P-4 (output-family conformance)** from `discovery_test_record_v1.md`.

## Run it

```bash
python3 -m src.validate check --run /path/to/run_dir --slug my-book
python3 tests/selftest.py
```

Exit codes: `0` pass, `1` fail, `2` error.

## What it certifies

The **envelope**: file family present, master doc's nine sections in order,
every convention line carrying exactly one legal provenance tag,
`[discovery-forecast]` confined to its two permitted files, the countable
bounds (watchlist ≤20, brief ≤25 lines, escalations ≤12, master ≤300),
pinned enums in the CSVs, the registration line's shape.

## What it does NOT certify

**The config fragment's field names.** Master doc section 7 is deliberately
out of scope: the schema boundary is under revision (`discovery_prompt_v2.6`
owed, `pipeline_config_schema_v2.md` owed) and one of the open docket
questions. This is why P-2/P-3/P-4 are stable across v2.5→v2.6 — they never
open section 7. A schema check bolts on here later as one more function.

**The truth of anything.** This checks shape. A fabricated
`[operator-decided]` tag on a ruling no operator made is perfectly
well-formed and passes clean. Per P-5 in the test record, fabricated
provenance is not detectable as a lint. **Never describe a green verdict
from this tool as provenance integrity.**

## Fixtures are synthetic

Every fixture in `fixtures/` was authored against the *stated rules* in
`discovery_prompt_v2_5.md`. None derives from a real discovery run — only
one ratified run exists (sailing, 2026-07-09) and it predates several rules
checked here.

This means the validator has **the same cell the topology scorer has**:
green against test cases its own author invented, never having met real
output. Green means *the code implements the spec*. It does not mean *the
spec matches reality*. The first real discovery run is the first honest
test.

## Design decisions

- **Hard fail, no tiers** [operator-ruled 2026-07-14]. Any violation fails
  the run. Tiering deferred until failure classes are understood in
  practice. A watchlist at 21 rows blocks the run — that is intended.
- **Logic lives here, not in Node-RED.** This is a plain script: greppable,
  testable, diffable, runnable from a terminal. Node-RED calls it via exec
  as one node. The flow is wiring, not brain.
- **Every rule traces to a prompt line.** `src/rules.py` carries the
  citation for each constant. If a rule is not written down in
  `discovery_prompt_v2_5.md`, it is not in here.
- **Negative fixtures break exactly one rule each.** The self-test asserts
  specificity: a case must raise its own code and no other. A validator
  whose codes lie sends operators chasing the wrong defect.

## Layout

```
src/rules.py       constants, each traced to its prompt line
src/validate.py    the checks + CLI
tests/selftest.py  19 assertions: valid passes, each negative caught
tests/build_invalid.py  regenerates fixtures/invalid/
fixtures/valid/    one clean synthetic run
fixtures/invalid/  18 runs, one broken rule each
```

## Known gaps

- Convention-line detection is heuristic (bulleted lines inside
  `## Conventions`). A convention written as prose is invisible to the tag
  lint.
- Exhibit ≤5 lines is specified but unimplemented — exhibit boundaries are
  not mechanically distinguishable from convention lines in the current
  format.
- `loc_anchors` coverage stats and interpolation rule are specified in the
  prompt but have no declared column contract, so only presence is checked.
