#!/usr/bin/env python3
"""
Self-test: the valid fixture passes clean; each negative fixture fails with
its OWN code and no other.

The specificity assertion matters. A validator that fails everything is
useless in the same way as one that fails nothing -- if breaking the mode
enum also trips the tag check, the codes are lying and a real operator will
chase the wrong defect.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.validate import validate_run  # noqa: E402

SLUG = "synth"
VALID = ROOT / "fixtures" / "valid" / "sample_run"
INVALID = ROOT / "fixtures" / "invalid"


def run():
    results = []

    # --- the valid run must be clean -------------------------------
    rep = validate_run(VALID, SLUG)
    if rep.passed:
        results.append(("PASS", "valid fixture -> ENVELOPE GREEN"))
    else:
        codes = [c for c, _ in rep.violations]
        results.append(("FAIL", f"valid fixture raised {codes}"))

    # --- each negative must fail with its own code -----------------
    if not INVALID.is_dir():
        print("ERROR: no negative fixtures. Run tests/build_invalid.py")
        return 2

    for case_dir in sorted(INVALID.iterdir()):
        if not case_dir.is_dir():
            continue
        expected = case_dir.name.upper()
        rep = validate_run(case_dir, SLUG)
        codes = {c for c, _ in rep.violations}

        if rep.passed:
            results.append(("FAIL", f"{expected}: passed but should fail"))
        elif expected not in codes:
            results.append(
                ("FAIL", f"{expected}: raised {sorted(codes)}, not its own code")
            )
        elif len(codes) > 1:
            extra = sorted(codes - {expected})
            results.append(
                ("FAIL", f"{expected}: also raised {extra} -- not specific")
            )
        else:
            results.append(("PASS", f"{expected} -> caught, specific"))

    # --- report ----------------------------------------------------
    for status, msg in results:
        print(f"  [{status}] {msg}")

    failed = [r for r in results if r[0] == "FAIL"]
    print()
    print(f"{len(results) - len(failed)}/{len(results)} PASS")

    if failed:
        print("\nSELF-TEST RED")
        return 1

    print("\nSELF-TEST GREEN")
    print()
    print("Fixtures are SYNTHETIC -- authored from the prompt spec, never")
    print("run against real discovery output. Green here means the code")
    print("implements the spec, not that the spec matches reality.")
    return 0


if __name__ == "__main__":
    sys.exit(run())
