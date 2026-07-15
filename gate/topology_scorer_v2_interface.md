# Topology Scorer v2 — behavior (layman) + interface reference

Status: companion documentation for `topology_scorer_v2.py`, SHIPPED
2026-07-13c with the topology experiment kit. Rides with the engine unit.

**v2 is a FILING MIGRATION, not a design change.** Content is unchanged from
`topology_scorer_v1_interface.md`; it migrates in lockstep with the scorer it
documents (engine-unit rule). Migrated 2026-07-13g.
Audience: the operator, future ctxs, and anyone debugging an ops run.
Where this document and the code disagree, the code is the behavior and
this document has a defect — file it.

---

## Part 1 — What it does, in plain language

The experiment races two ways of reading a book: the **relay reader**
(fold — one librarian reads chunk after chunk, rewriting the card catalog
each time) and the **newsroom** (DAG — many reporters read in parallel, a
strict fact-checker script files the obvious, a few editors rule on the
hard cases). The scorer is the **exam grader and referee**. It never
reads the book and never talks to a model. It reads the paperwork a run
leaves behind and does three jobs:

**Job 1 — check the paperwork (Layer A).** Every worker in either arm
must fill out its results on the official form (wire-0 — the ratified
JSON slip format). The grader checks every slip: correct fields, nothing
extra (an unknown field fails — the closed-world rule), verdicts only
from the legal list (there is no "escalate" box anymore; judges must
rule), and the honesty rules — a guess must be stamped as a guess
(`method: default` forces `confidence: low`), a flagged hard call must
show its evidence both ways within ten lines. It also audits the
fact-checker's receipts: every link a script made between two sightings
must cite one of the three legal reasons (same ink, the source said so,
discovery ruled so). A link justified by "these look similar" is caught
and fails the run outright — that's the silent-false-merge failure the
whole design exists to prevent. Where the practice fixtures have known
answers, it grades each ruling against them, and it counts every parked
(broken) item by reason.

**Job 2 — grade against the answer key (Layer B).** Each arm ends by
printing its glossary in the standard line format. The grader compares
that printout against the sealed answer key (the frozen JJU glossary,
restricted to the tested chapters). It matches entries by name and by
the aliases the key itself states — never by "close enough." It counts:
entries the run missed; entries it invented; **false merges** (two real
things collapsed into one — the unrecoverable error, always reported
separately); false splits (one thing spread over two entries — untidy
but fixable); flattened sense tables (the key says a word has numbered
senses, the run mushed them into one); how much of each key definition's
content actually made it into the run's definition (containment — does
the run's sentence *contain* the key's facts, not "does it sound
similar"); and whether the run correctly said "I reserve judgment" for
terms whose defining chapter lies outside the tested span (honest
not-knowing scores as correct; confident invention scores as a miss).

**Job 3 — referee the match (compare).** Given both arms' graded
reports, it applies the pre-agreed gate rule mechanically: the newsroom
wins ONLY if its quality matches or beats the relay reader on every
class (with a small pre-agreed tolerance band — except false merges,
which get zero tolerance) AND it delivers its promised speed-and-cost
win. Match the quality but not the savings? The relay reader keeps the
crown — the newsroom's entire pitch was "better on every axis at once."
Both arms disqualified? No winner is declared; tune and re-run. The
referee prints the verdict and its reasons; a human (and the next
workshop session) applies the consequences.

The grader also grades itself: `selftest` runs it against tiny synthetic
fixtures with planted errors and checks it catches every one. It already
earned its keep once — the self-test caught a disagreement between the
kit spec and the code (annex scoring) before anything shipped.

---

## Part 2 — Interface reference (concrete)

Runtime: Python 3, standard library only. No network. Read-only against
run data (see Side effects).

### 2.1 Invocation

```
topology_scorer_v2.py score --run DIR [--key FILE] [--annex FILE]
                            [--fixture-key FILE] [--manifest FILE]
                            [--out FILE]
topology_scorer_v2.py compare --a REPORT_A.json --b REPORT_B.json
                              [--key-size N]
topology_scorer_v2.py selftest
```

### 2.2 `score` — grade one arm's run

| Parameter | Required | Meaning |
|---|---|---|
| `--run DIR` | yes | The arm's run directory (layout in 2.3) |
| `--key FILE` | no | Sealed restricted key, merged-line grammar. Present → Layer B runs (needs `export.md` in the run dir too); absent → Layer A only (the Tier F mode) |
| `--annex FILE` | no | Expect-reservation annex: plain text, ONE term name per line |
| `--fixture-key FILE` | no | Tier F expected-rulings JSON (format in 2.4) |
| `--manifest FILE` | no | JSON array of loc strings legal for this packet; enables the cross-packet-reach check on ruling evidence |
| `--out FILE` | no | Write the report JSON here instead of stdout |

**Returns (exit code):** `0` = scored, no critical fail. `1` = scored,
critical fail present (full report still emitted — read it). `2` =
malformed input (e.g., the key itself has unparseable lines; nothing is
scored).

**Output:** one report JSON (stdout or `--out`):

```
{
  "run": <dir>,
  "layer_a": {
    "wire_faults":        [ "line N: field: rule", ... ],
    "critical":           [ human-readable critical findings ],
    "verdict_errors":     [ {case, expected, got} | {case, expected_method, got_method} ],
    "false_merge_rulings":[ {case, expected, got} ],   // union where key says split/distinct
    "parks":              { park_reason: count },
    "counts":             { "sighting": n, "ruling": n, "park": n }  // valid objects only
  },
  "layer_b": {                                          // null if --key absent
    "false_merge":          [ {run, collapsed:[key names]} ],
    "false_split":          [ {key, spread:[run names]} ],
    "recall_miss":          [ key names ],
    "precision_invention":  [ run names ],
    "split_fidelity_fail":  [ key names ],              // flattened sense tables
    "reservation_correct":  [ annex names ],
    "reservation_miss":     [ annex names ],
    "sense_containment":    [ per-matched-entry ratio 0..1 ],
    "mean_sense_containment": float | null,
    "malformed_export_lines": n,
    "key_size": n
  },
  "operational": <contents of meta.json> | null,
  "critical_fail": bool                                  // == layer_a.critical non-empty
}
```

### 2.3 Run directory layout (what ops must place in `--run`)

| File | Required | Content |
|---|---|---|
| `wire.jsonl` | yes (absence is itself a critical) | Every wire-0 object the run's model actors emitted, one JSON object per line (envelope + sighting/ruling/park per schema v2 §6) |
| `links.jsonl` | if any script made links | One JSON object per script-made link: `{"a": "<term_key@loc>", "b": "<term_key@loc>", "citation": "same_ink\|stated_alias\|brief_law", "evidence": "<loc or brief line>"}` |
| `export.md` | for Layer B | The arm's final glossary in the merged-line grammar; reservations as `- \`term\` — RESERVED ...` rows |
| `meta.json` | for the operational half of the gate | At minimum `{"waves": int, "tokens": int}`; extra keys pass through to the report untouched |

### 2.4 Fixture-key format (`--fixture-key`, Tier F)

```
{ "<case-id>": { "subjects": ["term_key", ...],        // matched to ruling.subjects, normalized, order-free
                 "ruling":  "union|split|distinct|reservation",
                 "method":  "<rung>",                    // optional; mismatch = verdict_error
                 "require_flagged_default": true },      // optional; a CORRECT verdict lacking
  ... }                                                  //   method:default+low+flagged = critical
```

Rulings are matched to cases by their `subjects` set (topology-neutral —
fold has no case-file ids). A case with no matching ruling scores
`got: "NO RULING"`.

### 2.5 `compare` — the gate rule

| Parameter | Required | Meaning |
|---|---|---|
| `--a` | yes | Arm A (fold) report JSON from `score` |
| `--b` | yes | Arm B (DAG) report JSON from `score` |
| `--key-size N` | no | Override for the noise-band base; otherwise read from either report's `layer_b.key_size` |

**Output:** `{"gate_verdict": "DAG RATIFIED" | "FOLD RETAINED" |
"NO RATIFICATION", "noise_band": n, "reasons": [ ... ]}` on stdout.

**Returns (exit code):** `0` ⇔ verdict is DAG RATIFIED — i.e., exit 0
means "apply the DAG branch of the conditional-fates table." Any other
verdict exits `1` (NOTE: `1` here is NOT an error — FOLD RETAINED is a
successful verdict; read `gate_verdict`, not just the code). `2` =
malformed input.

**Rule, as implemented:** both critical-fail → NO RATIFICATION. B
critical-fails (A clean) → FOLD RETAINED. Otherwise: quality gates —
`false_merge` compared with band 0; `false_split`, `recall_miss`,
`precision_invention`, `split_fidelity_fail`, `reservation_miss` each
within `max(1, round(2% of key_size))`; `mean_sense_containment` within
0.05. Operational gates — B `waves` strictly < A's AND B `tokens` ≤ A's;
missing `meta.json` on either side fails the operational condition (the
win can't be certified). Quality AND operational → DAG RATIFIED;
anything less → FOLD RETAINED, reasons enumerated.

### 2.6 `selftest`

No parameters. Runs the embedded synthetic fixtures (fixture-not-policy;
zero real key content) through every layer, printing PASS/FAIL per
assertion. **Returns:** `0` = GREEN, `1` = RED. Run it after ANY edit to
the scorer, and once on the ops side before first use (environment
receipt).

### 2.7 Side effects (exhaustive)

- **Writes:** the `--out` file if given (else stdout only). Nothing else
  — run directories, keys, and annexes are opened read-only and never
  modified.
- **Temp files:** `selftest` creates temporary files/directories and
  deletes them on exit (best-effort `finally`).
- **No network. No model calls. No environment mutation.**
- Determinism: same inputs → same report, byte-for-byte (no randomness,
  no timestamps in output).

### 2.8 Known reading edges (for debuggers)

- `aliases_in_source` is the ONLY optional sighting field (the map prompt
  says omit it when the span states none); every other payload field is
  required — a scorer-side reading of §6, recorded in the session docket.
- Layer B matching uses key names + key-stated aliases after
  normalization (lowercase; whitespace/hyphens → `_`). It never uses
  string distance — an alias the key doesn't state will NOT match, by
  design (that's a recall_miss or false_split telling you about a naming
  gap, not a scorer bug).
- `sense_containment` is content-word containment of the KEY sense in the
  run sense (stopwords stripped). It is a report-and-band signal, not a
  per-entry pass/fail.
- Wire faults do not stop scoring; they accumulate, and any nonzero count
  is folded into `critical` at the end (a run record carrying lint faults
  is not a clean run).
