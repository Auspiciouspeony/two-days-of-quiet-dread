"""two-days-of-quiet-dread — program/v1 entry.

One fixed one-line code review comment that approves a pull request
while carrying quiet existential dread, written to entry.txt in the
output directory. The grader reads exactly the bytes written: no
trailing newline, no second line.

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py

Deterministic: a single constant string; no randomness, no network,
no clock. Python 3.13, standard library only.
"""

import os
from pathlib import Path

# v1 (tested first): "LGTM — I have approved 400 of these and cannot remember
# a single one." Flat and real, but the "approved many, remember none"
# angle is a known meaningless-work shape.
#
# Iteration round (v1 -> v2), judged on the brief's criteria in order:
# 1. approves ("Approved.") + dread — both pass. 2. the laugh comes from
# the dread itself — v2's punch IS the dread (the reviewer, like the
# code, will one day be deprecated). 3. quiet understatement, flat
# tone — both flat. 4. reads like a real tired engineer before clicking
# approve — v2's "The code is good, the tests are green" sounds like a
# genuine approval, v1's bare "LGTM" less so. 5. fresh turn of phrase —
# v2 wins outright: "deprecated" is engineer vocabulary turned on the
# human, an unexpected word where the obvious line would say "retire"
# or "die". Closest other challengers: "I have stopped asking what any
# of it is for" (punch too abstract) and "still reviewing this file
# when I am sixty" (familiar aging shape).
COMMENT = (
    "Approved. The code is good, the tests are green, and I will be "
    "maintaining this until one of us is deprecated."
)


def _best_effort_chmod(path: Path, mode: int) -> None:
    """Chmod when the path is ours; never fail the run when it is not.

    In the grader the output directory is mounted by the grader and not
    owned by us, so chmod there raises PermissionError. The entry file
    itself is created by us, so its own chmod still applies.
    """
    try:
        path.chmod(mode)
    except OSError:
        pass


def run(output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    _best_effort_chmod(output_dir, 0o755)
    entry = output_dir / "entry.txt"
    entry.write_text(COMMENT, encoding="utf-8")
    # Outputs are collected by another user than the one running this
    # program, so the file must be world-readable.
    entry.chmod(0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))))
