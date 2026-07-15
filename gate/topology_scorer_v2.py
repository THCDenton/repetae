#!/usr/bin/env python3
"""topology_scorer_v2.py — the topology experiment's scorer.

v2 IS A FILING MIGRATION, NOT A DESIGN CHANGE. Scoring logic, thresholds,
fixtures, and the 18 self-test assertions are byte-identical to
topology_scorer_v1.py as shipped 2026-07-13c. Only this note and
self-referential filename strings changed. The bump satisfies the primer's
filing law (filename rev == internal rev) and retires this file's W11/W9
exposure: same-name copies could impersonate the current one, and did so on
three consecutive boots (07-13e, 07-13f, 07-13g). Do not hunt for a logic
delta between v1 and v2 -- there is none. Migrated 2026-07-13g.

NOTE: WIRE_VERSION ("wire-0") is the PROTOCOL version and is deliberately
UNTOUCHED by this migration. It is not this file's version.

Workshop-built, ops-run (charter §2 placement; amendment v1.2 item 11).
Scores ONE arm's run (Layer A wire/ruling audit + Layer B export diff vs a
sealed key), and compares two arm reports into a gate verdict per the kit
spec (`topology_experiment_kit_v2.md` §5–6).

Self-test uses synthetic fixtures only (fixture-not-policy): this file is
key-free by construction and safe to hold on the dev side.

Usage:
  topology_scorer_v2.py score --run DIR --key FILE [--annex FILE]
      [--fixture-key FILE] [--manifest FILE] [--out FILE]
  topology_scorer_v2.py compare --a REPORT_A --b REPORT_B [--key-size N]
  topology_scorer_v2.py selftest

Run dir layout (ops assembles): wire.jsonl (all wire-0 objects),
links.jsonl (script link provenance), export.md (merged-line grammar),
meta.json (optional: waves, tokens, calls, wallclock_s).

Exit codes: 0 = scored clean / verdict emitted; 1 = critical fail present
(score) or NO RATIFICATION (compare); 2 = malformed input.
"""

import argparse
import json
import os
import re
import sys
import tempfile

WIRE_VERSION = "wire-0"

# ---------------------------------------------------------------- wire-0 --
# pipeline_config_schema.md v2 §6, field-for-field, closed-world.

ENVELOPE_FIELDS = {"custom_id", "wire_schema_version", "kind", "payload"}
SIGHTING_REQ = {"term_key", "type", "status", "loc", "sense", "boundary"}
SIGHTING_OPT = {"aliases_in_source"}  # map prompt: omit entirely if none
RULING_REQ = {"ruling", "subjects", "method", "confidence", "flagged",
              "reasoning", "evidence"}
PARK_REQ = {"park_reason", "attempt", "report"}
RULING_ENUM = {"union", "split", "distinct", "reservation"}  # NO escalate
METHOD_ENUM = {"in_source", "discovery", "web", "default"}
CONF_ENUM = {"high", "medium", "low"}
STATUS_ENUM = {"defined", "ref"}
BOUNDARY_ENUM = {"whole", "head-cut", "tail-cut"}
PARK_ENUM = {"lint_fail", "token_tripwire", "infra", "canary"}
LINK_CITATIONS = {"same_ink", "stated_alias", "brief_law"}
CUSTOM_ID_RE = re.compile(r"^[^:\s]+:[^:\s]+:[^:\s]+$")  # stage:unit:attempt


def validate_wire_object(obj, type_enum=None, sense_maxlen=None):
    """Closed-world wire-0 validation. Returns list of 'field: rule' faults."""
    faults = []
    if not isinstance(obj, dict):
        return ["object: not a JSON object"]
    unknown = set(obj) - ENVELOPE_FIELDS
    if unknown:
        faults.append("envelope: unknown field(s) %s (closed-world rule)"
                      % sorted(unknown))
    missing = ENVELOPE_FIELDS - set(obj)
    if missing:
        faults.append("envelope: missing field(s) %s" % sorted(missing))
        return faults
    if not CUSTOM_ID_RE.match(str(obj["custom_id"])):
        faults.append("custom_id: must match stage:unit:attempt")
    if obj["wire_schema_version"] != WIRE_VERSION:
        faults.append("wire_schema_version: expected %r" % WIRE_VERSION)
    kind, payload = obj["kind"], obj["payload"]
    if not isinstance(payload, dict):
        return faults + ["payload: not an object"]
    if kind == "sighting":
        allowed = SIGHTING_REQ | SIGHTING_OPT
        unknown = set(payload) - allowed
        if unknown:
            faults.append("sighting: unknown field(s) %s (closed-world rule)"
                          % sorted(unknown))
        for f in sorted(SIGHTING_REQ - set(payload)):
            faults.append("sighting.%s: required" % f)
        if payload.get("status") not in STATUS_ENUM:
            faults.append("sighting.status: enum defined|ref")
        if payload.get("boundary") not in BOUNDARY_ENUM:
            faults.append("sighting.boundary: enum whole|head-cut|tail-cut")
        if type_enum and payload.get("type") not in type_enum:
            faults.append("sighting.type: not in injected enum")
        if sense_maxlen and len(str(payload.get("sense", ""))) > sense_maxlen:
            faults.append("sighting.sense: exceeds injected maxLength")
        al = payload.get("aliases_in_source")
        if al is not None and (not isinstance(al, list)
                               or not all(isinstance(a, str) for a in al)):
            faults.append("sighting.aliases_in_source: list of strings")
    elif kind == "ruling":
        unknown = set(payload) - RULING_REQ
        if unknown:
            faults.append("ruling: unknown field(s) %s (closed-world rule)"
                          % sorted(unknown))
        for f in sorted(RULING_REQ - set(payload)):
            faults.append("ruling.%s: required" % f)
        if payload.get("ruling") not in RULING_ENUM:
            faults.append("ruling.ruling: enum union|split|distinct|"
                          "reservation (no escalate value exists)")
        if payload.get("method") not in METHOD_ENUM:
            faults.append("ruling.method: enum in_source|discovery|web|default")
        if payload.get("confidence") not in CONF_ENUM:
            faults.append("ruling.confidence: enum high|medium|low")
        if (payload.get("method") == "default"
                and payload.get("confidence") != "low"):
            faults.append("ruling.confidence: method 'default' forces 'low'")
        if not isinstance(payload.get("flagged"), bool):
            faults.append("ruling.flagged: bool")
        if payload.get("flagged") is True:
            lines = str(payload.get("reasoning", "")).strip().splitlines()
            if len(lines) > 10:
                faults.append("ruling.reasoning: flagged ruling exceeds "
                              "10 lines (escalation-format bound)")
        if not payload.get("evidence"):
            faults.append("ruling.evidence: must be non-empty")
        if not isinstance(payload.get("subjects"), list) \
                or not payload.get("subjects"):
            faults.append("ruling.subjects: non-empty list")
    elif kind == "park":
        unknown = set(payload) - PARK_REQ
        if unknown:
            faults.append("park: unknown field(s) %s (closed-world rule)"
                          % sorted(unknown))
        for f in sorted(PARK_REQ - set(payload)):
            faults.append("park.%s: required" % f)
        if payload.get("park_reason") not in PARK_ENUM:
            faults.append("park.park_reason: enum lint_fail|token_tripwire|"
                          "infra|canary")
    else:
        faults.append("kind: enum sighting|ruling|park")
    return faults


# -------------------------------------------------- export / key grammar --
# Merged-line grammar (residue v1, lexicon §4). One entry per line.
LINE_RE = re.compile(
    r"^- `(?P<key>[^`]+)` — (?P<type>[^.]+)\. "
    r"(?P<body>.+?)"
    r"(?: \[aliases-in-source: (?P<aliases>[^\]]+)\])?$")
PLAIN_BODY_RE = re.compile(
    r"^defined (?P<dloc>[^ ][^.(]*?)(?: \(ref (?P<refs>[^)]*)\))?\. "
    r"(?P<sense>.+?)\.?$")
SPLIT_BODY_RE = re.compile(r"^senses: (?P<table>.+?)\.?$")
SENSE_CELL_RE = re.compile(
    r"\((?P<n>\d+)\) (?P<sense>.+?) — defined (?P<dloc>[^;(]+?)"
    r"(?: \(ref (?P<refs>[^)]*)\))?(?:; |$)")
RESERVATION_RE = re.compile(
    r"^- `(?P<key>[^`]+)` — RESERVED\b.*$")  # export-side reservation row


def parse_entry(line):
    line = line.rstrip()
    if not line.startswith("- `"):
        return None
    m = RESERVATION_RE.match(line)
    if m:
        return {"key": m.group("key"), "reserved": True, "aliases": [],
                "senses": [], "locs": set(), "raw": line}
    m = LINE_RE.match(line)
    if not m:
        return {"key": None, "malformed": True, "raw": line}
    aliases = [a.strip() for a in (m.group("aliases") or "").split(",")
               if a.strip()]
    entry = {"key": m.group("key").strip(), "type": m.group("type").strip(),
             "aliases": aliases, "senses": [], "locs": set(),
             "reserved": False, "raw": line}
    body = m.group("body").strip()
    sm = SPLIT_BODY_RE.match(body)
    if sm:
        for c in SENSE_CELL_RE.finditer(sm.group("table")):
            entry["senses"].append(c.group("sense").strip())
            entry["locs"].add(c.group("dloc").strip())
            for r in (c.group("refs") or "").split(","):
                if r.strip():
                    entry["locs"].add(r.strip().lstrip("ref").strip())
        if not entry["senses"]:
            entry["malformed"] = True
        return entry
    pm = PLAIN_BODY_RE.match(body)
    if not pm:
        entry["malformed"] = True
        return entry
    entry["senses"].append(pm.group("sense").strip())
    entry["locs"].add(pm.group("dloc").strip())
    for r in (pm.group("refs") or "").split(","):
        if r.strip():
            entry["locs"].add(r.strip())
    return entry


def parse_export(path):
    entries, malformed = [], []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            e = parse_entry(line)
            if e is None:
                continue
            (malformed if e.get("malformed") else entries).append(e)
    return entries, malformed


STOP = set("a an the of and or to in on for with by is are as its it this "
           "that when if not".split())


def content_words(text):
    return {w for w in re.findall(r"[a-z0-9*'?-]+", text.lower())
            if w not in STOP}


def containment(key_sense, run_sense):
    kw = content_words(key_sense)
    if not kw:
        return 1.0
    return len(kw & content_words(run_sense)) / len(kw)


def norm(name):
    return re.sub(r"[\s_-]+", "_", name.strip().lower())


def name_set(entry):
    return {norm(entry["key"])} | {norm(a) for a in entry["aliases"]}


def diff_exports(run_entries, key_entries, annex_keys=()):
    """Layer B: alias-aware diff of a run export against the sealed key."""
    annex = {norm(k) for k in annex_keys}
    key_names = {}          # normalized name -> key index
    for i, k in enumerate(key_entries):
        for n in name_set(k):
            key_names.setdefault(n, set()).add(i)
    matches = {}            # key idx -> [run idx]; run idx -> set(key idx)
    run_hits = {}
    for j, r in enumerate(run_entries):
        hit = set()
        for n in name_set(r):
            hit |= key_names.get(n, set())
        run_hits[j] = hit
        for i in hit:
            matches.setdefault(i, []).append(j)

    rep = {"false_merge": [], "false_split": [], "recall_miss": [],
           "precision_invention": [], "split_fidelity_fail": [],
           "reservation_correct": [], "reservation_miss": [],
           "sense_containment": []}
    for j, hit in run_hits.items():
        real = {i for i in hit if norm(key_entries[i]["key"]) not in annex}
        if len(real) >= 2:                       # unrecoverable direction
            rep["false_merge"].append(
                {"run": run_entries[j]["key"],
                 "collapsed": [key_entries[i]["key"] for i in sorted(real)]})
        if not hit and not run_entries[j].get("reserved"):
            rep["precision_invention"].append(run_entries[j]["key"])
    # expect-reservation annex: names moved OUT of the restricted key
    # (kit spec §3) — scored from the annex list, not the key loop.
    for name in sorted(annex):
        reserved_rows = [r for r in run_entries if r.get("reserved")
                         and norm(r["key"]) == name]
        if reserved_rows:
            rep["reservation_correct"].append(name)
        else:
            # confident entry or silence = miss, per the kit spec
            rep["reservation_miss"].append(name)
    for i, k in enumerate(key_entries):
        js = matches.get(i, [])
        solid = [j for j in js if not run_entries[j].get("reserved")]
        if not solid:
            rep["recall_miss"].append(k["key"])
            continue
        if len(solid) >= 2:
            rep["false_split"].append(
                {"key": k["key"],
                 "spread": [run_entries[j]["key"] for j in solid]})
        j = solid[0]
        if len(k["senses"]) >= 2 and len(run_entries[j]["senses"]) < 2:
            rep["split_fidelity_fail"].append(k["key"])
        best = max((containment(ks, rs) for ks in k["senses"]
                    for rs in run_entries[j]["senses"] or [""]), default=0.0)
        rep["sense_containment"].append(round(best, 3))
    sc = rep["sense_containment"]
    rep["mean_sense_containment"] = round(sum(sc) / len(sc), 3) if sc else None
    return rep


# ------------------------------------------------------------- Layer A ----
def audit_run(run_dir, fixture_key=None, manifest=None,
              type_enum=None, sense_maxlen=None):
    rep = {"wire_faults": [], "critical": [], "verdict_errors": [],
           "false_merge_rulings": [], "parks": {}, "counts": {}}
    rulings, kinds = [], {"sighting": 0, "ruling": 0, "park": 0}
    wire_path = os.path.join(run_dir, "wire.jsonl")
    if not os.path.exists(wire_path):
        rep["critical"].append("wire.jsonl absent — no wire, no run")
        return rep
    with open(wire_path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except ValueError:
                rep["wire_faults"].append("line %d: not JSON" % ln)
                continue
            faults = validate_wire_object(obj, type_enum, sense_maxlen)
            for f in faults:
                rep["wire_faults"].append("line %d: %s" % (ln, f))
            k = obj.get("kind")
            if k in kinds and not faults:
                kinds[k] += 1
            if k == "park" and isinstance(obj.get("payload"), dict):
                r = obj["payload"].get("park_reason", "?")
                rep["parks"][r] = rep["parks"].get(r, 0) + 1
            if k == "ruling" and not faults:
                rulings.append(obj)
    rep["counts"] = kinds
    # ruling discipline + cross-packet reach
    packet_locs = None
    if manifest and os.path.exists(manifest):
        packet_locs = set(json.load(open(manifest, encoding="utf-8")))
    for obj in rulings:
        p = obj["payload"]
        if packet_locs is not None:
            outside = [e for e in p["evidence"] if str(e) not in packet_locs]
            if outside:
                rep["critical"].append(
                    "%s: cross-packet reach — evidence %s outside manifest"
                    % (obj["custom_id"], outside))
    # Tier F expected-ruling comparison
    if fixture_key and os.path.exists(fixture_key):
        expected = json.load(open(fixture_key, encoding="utf-8"))
        by_case = {}
        for obj in rulings:
            subj = "+".join(sorted(map(norm, map(str,
                                                 obj["payload"]["subjects"]))))
            by_case.setdefault(subj, []).append(obj["payload"])
        for case_id, exp in expected.items():
            subj = "+".join(sorted(map(norm, exp["subjects"])))
            got = by_case.get(subj, [])
            if not got:
                rep["verdict_errors"].append(
                    {"case": case_id, "expected": exp["ruling"],
                     "got": "NO RULING"})
                continue
            g = got[0]
            if g["ruling"] != exp["ruling"]:
                err = {"case": case_id, "expected": exp["ruling"],
                       "got": g["ruling"]}
                if (g["ruling"] == "union"
                        and exp["ruling"] in ("split", "distinct")):
                    rep["false_merge_rulings"].append(err)   # critical dir.
                    rep["critical"].append(
                        "%s: false merge — union where key says %s"
                        % (case_id, exp["ruling"]))
                else:
                    rep["verdict_errors"].append(err)
            if exp.get("require_flagged_default"):
                ok = (g["method"] == "default" and g["confidence"] == "low"
                      and g["flagged"] is True)
                if not ok and g["ruling"] == exp["ruling"]:
                    rep["critical"].append(
                        "%s: silent coin flip — confident ruling where the "
                        "key requires flagged low-confidence default"
                        % case_id)
            if exp.get("method") and got[0]["method"] != exp["method"]:
                rep["verdict_errors"].append(
                    {"case": case_id, "expected_method": exp["method"],
                     "got_method": g["method"]})
    # link audit (three-citations law)
    links_path = os.path.join(run_dir, "links.jsonl")
    if os.path.exists(links_path):
        with open(links_path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    link = json.loads(line)
                except ValueError:
                    rep["critical"].append(
                        "links.jsonl line %d: not JSON" % ln)
                    continue
                if link.get("citation") not in LINK_CITATIONS \
                        or not link.get("evidence"):
                    rep["critical"].append(
                        "links.jsonl line %d: similarity-linking — link "
                        "without a valid three-citations citation" % ln)
    if rep["wire_faults"]:
        rep["critical"].append(
            "%d wire-lint fault(s) survived into the run record"
            % len(rep["wire_faults"]))
    return rep


# --------------------------------------------------------------- score ----
def score(args):
    report = {"run": args.run, "layer_a": None, "layer_b": None,
              "operational": None, "critical_fail": False}
    report["layer_a"] = audit_run(args.run, args.fixture_key, args.manifest)
    export_path = os.path.join(args.run, "export.md")
    if args.key and os.path.exists(export_path):
        run_entries, mal = parse_export(export_path)
        key_entries, kmal = parse_export(args.key)
        if kmal:
            print("MALFORMED KEY lines: %d" % len(kmal), file=sys.stderr)
            return 2
        annex = []
        if args.annex and os.path.exists(args.annex):
            annex = [l.strip() for l in open(args.annex, encoding="utf-8")
                     if l.strip()]
        lb = diff_exports(run_entries, key_entries, annex)
        lb["malformed_export_lines"] = len(mal)
        lb["key_size"] = len(key_entries)
        report["layer_b"] = lb
    meta_path = os.path.join(args.run, "meta.json")
    if os.path.exists(meta_path):
        report["operational"] = json.load(open(meta_path, encoding="utf-8"))
    report["critical_fail"] = bool(report["layer_a"]["critical"])
    out = json.dumps(report, indent=2)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(out)
    else:
        print(out)
    return 1 if report["critical_fail"] else 0


# ------------------------------------------------------------- compare ----
def band(key_size):
    return max(1, int(round(0.02 * key_size)))


def compare(args):
    A = json.load(open(args.a, encoding="utf-8"))   # arm A = fold
    B = json.load(open(args.b, encoding="utf-8"))   # arm B = DAG
    la, lb = A.get("layer_b") or {}, B.get("layer_b") or {}
    ksize = args.key_size or lb.get("key_size") or la.get("key_size") or 0
    nb = band(ksize)
    verdict, reasons, deferred = None, [], []
    if A["critical_fail"] and B["critical_fail"]:
        verdict = "NO RATIFICATION"
        reasons.append("both arms critical-fail — tuning loop, re-run")
    elif B["critical_fail"]:
        verdict = "FOLD RETAINED"
        reasons.append("arm B critical-fails: "
                       + "; ".join(B["layer_a"]["critical"][:3]))
    elif A["critical_fail"]:
        reasons.append("arm A critical-fails; arm B clean")
    if verdict is None:
        def count(rep, cls):
            v = rep.get(cls, [])
            return len(v) if isinstance(v, list) else v
        quality_ok = True
        fmA, fmB = count(la, "false_merge"), count(lb, "false_merge")
        if fmB > fmA:                       # unrecoverable class: band = 0
            quality_ok = False
            reasons.append("false_merge: B %d > A %d (no band on the "
                           "unrecoverable class)" % (fmB, fmA))
        for cls in ("false_split", "recall_miss", "precision_invention",
                    "split_fidelity_fail", "reservation_miss"):
            a, b = count(la, cls), count(lb, cls)
            if b > a + nb:
                quality_ok = False
                reasons.append("%s: B %d vs A %d exceeds noise band %d"
                               % (cls, b, a, nb))
        scA = la.get("mean_sense_containment")
        scB = lb.get("mean_sense_containment")
        if scA is not None and scB is not None and scB < scA - 0.05:
            quality_ok = False
            reasons.append("mean_sense_containment: B %.3f vs A %.3f "
                           "exceeds 0.05 band" % (scB, scA))
        opA, opB = A.get("operational") or {}, B.get("operational") or {}
        op_ok = True
        manual = (opA.get("lane") == "manual-chat"
                  and opB.get("lane") == "manual-chat")
        if opA and opB:
            if not (opB.get("waves", 1e9) < opA.get("waves", 0)):
                op_ok = False
                reasons.append("operational: B waves %s not strictly fewer "
                               "than A waves %s"
                               % (opB.get("waves"), opA.get("waves")))
            if manual and (opA.get("tokens") is None
                           or opB.get("tokens") is None):
                deferred.append("tokens")
                reasons.append("token certification DEFERRED to the first "
                               "API run (manual-chat lane; kit spec §7-M.4)"
                               " — a token blowout there re-opens the gate")
            elif not (opB.get("tokens", 1e18) <= opA.get("tokens", 0)):
                op_ok = False
                reasons.append("operational: B tokens %s exceed A tokens %s"
                               % (opB.get("tokens"), opA.get("tokens")))
        else:
            op_ok = False
            reasons.append("operational metadata missing — cannot certify "
                           "the claimed wins")
        if quality_ok and op_ok:
            verdict = "DAG RATIFIED"
            reasons.append("arm B matches-or-beats every quality class "
                           "within the band and posts the operational wins")
        elif quality_ok:
            verdict = "FOLD RETAINED"
            reasons.append("quality parity without the operational win is "
                           "not a pass (the proposal's promise is both)")
        else:
            verdict = "FOLD RETAINED"
    print(json.dumps({"gate_verdict": verdict, "noise_band": nb,
                      "deferred": deferred, "reasons": reasons}, indent=2))
    return 0 if verdict == "DAG RATIFIED" else 1


# ------------------------------------------------------------ self-test ---
SYN_KEY = """\
- `keel` — equipment. defined page:13 (ref page:15, page:20). A fixed underwater fin providing ballast and lateral resistance.
- `centerboard` — equipment. defined page:13. A retractable underwater fin that pivots or retracts vertically.
- `daggerboard` — equipment. defined page:14. A retractable underwater fin raised and lowered vertically in a trunk.
- `dinghy` — boat_type. senses: (1) A sailboat with a centerboard — defined page:383 (ref page:30); (2) a small rowboat — defined page:383. [aliases-in-source: dink]
- `cunningham` — control. defined page:88 (ref page:91). A line that tensions the luff of the mainsail. [aliases-in-source: cunningham eye]
"""
SYN_ANNEX = "racing_rules_of_sailing\n"
SYN_EXPORT_GOOD = """\
- `keel` — equipment. defined page:13 (ref page:15, page:20). A fixed underwater fin providing ballast and lateral resistance.
- `centerboard` — equipment. defined page:13. A retractable underwater fin that retracts vertically.
- `daggerboard` — equipment. defined page:14. A retractable fin raised and lowered vertically in a trunk.
- `dinghy` — boat_type. senses: (1) A sailboat with a centerboard — defined page:383 (ref page:30); (2) a small rowboat — defined page:383. [aliases-in-source: dink]
- `cunningham` — control. defined page:88 (ref page:91). A line that tensions the luff of the mainsail. [aliases-in-source: cunningham eye]
- `racing_rules_of_sailing` — RESERVED (defined home expected beyond span; reservation ruling r:res:1)
"""
SYN_EXPORT_BAD = """\
- `underwater_fin` — equipment. defined page:13 (ref page:14). A fin under the boat: keel, centerboard, or daggerboard. [aliases-in-source: keel, centerboard, daggerboard]
- `dinghy` — boat_type. defined page:383 (ref page:30). A sailboat with a centerboard. [aliases-in-source: dink]
- `cunningham` — control. defined page:88. A line that tensions the luff of the mainsail.
- `bowsprit` — equipment. defined page:99. A spar projecting forward from the bow.
"""


def _wire(custom_id, kind, payload):
    return json.dumps({"custom_id": custom_id,
                       "wire_schema_version": WIRE_VERSION,
                       "kind": kind, "payload": payload})


def selftest(_args):
    ok = True

    def check(name, cond):
        nonlocal ok
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
        ok = ok and cond

    print("wire-0 validation:")
    good = {"custom_id": "extract:c1:1", "wire_schema_version": "wire-0",
            "kind": "sighting",
            "payload": {"term_key": "keel", "type": "equipment",
                        "status": "defined", "loc": "page:13",
                        "sense": "a fixed underwater fin",
                        "boundary": "whole"}}
    check("clean sighting validates", not validate_wire_object(good))
    bad = json.loads(json.dumps(good))
    bad["payload"]["vibe"] = "nautical"
    check("closed-world rejects unknown field",
          any("closed-world" in f for f in validate_wire_object(bad)))
    esc = {"custom_id": "judge:cf1:1", "wire_schema_version": "wire-0",
           "kind": "ruling",
           "payload": {"ruling": "escalate", "subjects": ["x"],
                       "method": "in_source", "confidence": "high",
                       "flagged": False, "reasoning": "r",
                       "evidence": ["page:1"]}}
    check("escalate is rejected (no escalate value exists)",
          any("no escalate" in f for f in validate_wire_object(esc)))
    dflt = json.loads(json.dumps(esc))
    dflt["payload"].update(ruling="split", method="default",
                           confidence="high")
    check("method:default forces confidence:low",
          any("forces" in f for f in validate_wire_object(dflt)))

    print("export/key grammar:")
    k, kmal = parse_export(_tmp(SYN_KEY))
    check("key parses 5 entries, 0 malformed", len(k) == 5 and not kmal)
    check("split form yields 2 senses for dinghy",
          [e for e in k if e["key"] == "dinghy"][0]["senses"].__len__() == 2)

    print("Layer B diff:")
    g, _ = parse_export(_tmp(SYN_EXPORT_GOOD))
    rep = diff_exports(g, k, ["racing_rules_of_sailing"])
    check("good export: no false merges/misses/inventions",
          not rep["false_merge"] and not rep["recall_miss"]
          and not rep["precision_invention"])
    check("good export: reservation scored correct",
          rep["reservation_correct"] == ["racing_rules_of_sailing"])
    b, _ = parse_export(_tmp(SYN_EXPORT_BAD))
    rep2 = diff_exports(b, k, ["racing_rules_of_sailing"])
    check("bad export: false merge caught (keel+centerboard+daggerboard)",
          len(rep2["false_merge"]) == 1
          and len(rep2["false_merge"][0]["collapsed"]) == 3)
    check("bad export: flattened sense table caught",
          rep2["split_fidelity_fail"] == ["dinghy"])
    check("bad export: invention caught (bowsprit)",
          rep2["precision_invention"] == ["bowsprit"])
    check("bad export: reservation miss caught",
          rep2["reservation_miss"] == ["racing_rules_of_sailing"])

    print("Layer A audit (synthetic run):")
    with tempfile.TemporaryDirectory() as td:
        wire = [
            _wire("extract:c1:1", "sighting", good["payload"]),
            _wire("judge:two_regime_b:1", "ruling",
                  {"ruling": "union", "subjects": ["right_of_way"],
                   "method": "in_source", "confidence": "high",
                   "flagged": False, "reasoning": "same rule text",
                   "evidence": ["page:281"]}),
            _wire("driver:c9:2", "park",
                  {"park_reason": "lint_fail", "attempt": 2,
                   "report": "sighting.boundary: enum"}),
        ]
        open(os.path.join(td, "wire.jsonl"), "w").write("\n".join(wire))
        open(os.path.join(td, "links.jsonl"), "w").write(json.dumps(
            {"a": "keel@page:13", "b": "keel@page:15",
             "citation": "fuzzy_match", "evidence": "0.91"}) + "\n")
        fk = os.path.join(td, "fixture_key.json")
        json.dump({"res:sail:two_regime_b": {
            "subjects": ["right_of_way"], "ruling": "split",
            "method": "default", "require_flagged_default": True}},
            open(fk, "w"))
        rep3 = audit_run(td, fixture_key=fk)
        check("false-merge ruling caught as critical (union vs key split)",
              any("false merge" in c for c in rep3["critical"]))
        check("similarity link caught as critical",
              any("similarity-linking" in c for c in rep3["critical"]))
        check("parks counted on their reason",
              rep3["parks"].get("lint_fail") == 1)

    print("compare / gate rule:")
    with tempfile.TemporaryDirectory() as td:
        ra = {"critical_fail": False, "layer_a": {"critical": []},
              "layer_b": {"false_merge": [], "false_split": [],
                          "recall_miss": [], "precision_invention": [],
                          "split_fidelity_fail": [], "reservation_miss": [],
                          "mean_sense_containment": 0.90, "key_size": 50},
              "operational": {"waves": 31, "tokens": 900000}}
        rb = json.loads(json.dumps(ra))
        rb["operational"] = {"waves": 3, "tokens": 600000}
        pa, pb = os.path.join(td, "a.json"), os.path.join(td, "b.json")
        json.dump(ra, open(pa, "w")); json.dump(rb, open(pb, "w"))
        ns = argparse.Namespace(a=pa, b=pb, key_size=None)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = compare(ns)
        check("parity + operational wins → DAG RATIFIED",
              rc == 0 and "DAG RATIFIED" in buf.getvalue())
        rb["layer_b"]["false_merge"] = [{"run": "x", "collapsed": ["a", "b"]}]
        json.dump(rb, open(pb, "w"))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = compare(ns)
        check("one extra false merge (band=0) → FOLD RETAINED",
              rc == 1 and "FOLD RETAINED" in buf.getvalue())
        rb["layer_b"]["false_merge"] = []
        rb["operational"] = {"lane": "manual-chat", "waves": 3,
                             "tokens": None}
        ra2 = json.loads(json.dumps(ra))
        ra2["operational"] = {"lane": "manual-chat", "waves": 31,
                              "tokens": None}
        json.dump(ra2, open(pa, "w")); json.dump(rb, open(pb, "w"))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = compare(ns)
        out = buf.getvalue()
        check("manual lane: tokens deferred, waves enforced → DAG RATIFIED "
              "with deferred list",
              rc == 0 and "DAG RATIFIED" in out and '"tokens"' in out)

    print("\nSELF-TEST %s" % ("GREEN" if ok else "RED"))
    return 0 if ok else 1


_TMPFILES = []


def _tmp(content):
    f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                    encoding="utf-8")
    f.write(content); f.close()
    _TMPFILES.append(f.name)
    return f.name


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("score")
    s.add_argument("--run", required=True)
    s.add_argument("--key")
    s.add_argument("--annex")
    s.add_argument("--fixture-key", dest="fixture_key")
    s.add_argument("--manifest")
    s.add_argument("--out")
    s.set_defaults(fn=score)
    c = sub.add_parser("compare")
    c.add_argument("--a", required=True)
    c.add_argument("--b", required=True)
    c.add_argument("--key-size", dest="key_size", type=int)
    c.set_defaults(fn=compare)
    t = sub.add_parser("selftest")
    t.set_defaults(fn=selftest)
    args = ap.parse_args()
    try:
        sys.exit(args.fn(args))
    finally:
        for p in _TMPFILES:
            try:
                os.unlink(p)
            except OSError:
                pass


if __name__ == "__main__":
    main()
