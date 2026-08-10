from __future__ import annotations

import subprocess
import sys


def run(cmd: list[str]) -> None:
    print("$", " ".join(cmd))
    proc = subprocess.run(cmd)
    if proc.returncode:
        raise SystemExit(proc.returncode)


run([sys.executable, "-m", "pytest", "-q"])
run([sys.executable, "scripts/verify_reproduction.py"])
print("ALL_GATES_PASS")
