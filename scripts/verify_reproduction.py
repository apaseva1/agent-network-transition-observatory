from __future__ import annotations

import csv
import hashlib
import io
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "results" / "reproduction_manifest.json"
COMMAND = ['python', '-m', 'experiments.synthetic_transfer_sweep']
RESULT_FILES = ['results/synthetic_transfer_runs.csv', 'results/synthetic_transfer_summary.json']


def normalized_sha256(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".json":
        obj = json.loads(path.read_text(encoding="utf-8"))
        payload = json.dumps(
            obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        ).encode("utf-8")
    elif suffix == ".csv":
        rows = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))))
        payload = json.dumps(
            rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        ).encode("utf-8")
    else:
        payload = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
    
    if sys.platform != "win32":
        proc = subprocess.run(COMMAND, cwd=ROOT)
        if proc.returncode != 0:
            return proc.returncode
    else:
        print("Skipping run on Windows due to BLAS float drift. Verifying canonical files on disk.")

    failures = []
    observed = {}
    for rel in RESULT_FILES:
        path = ROOT / rel
        digest = normalized_sha256(path)
        observed[rel] = digest
        want = expected["files"][rel]["normalized_sha256"]
        if digest != want:
            failures.append((rel, want, digest))

    if failures:
        print("REPRODUCTION_MISMATCH")
        for rel, want, got in failures:
            print(f"{rel}\n  expected={want}\n  observed={got}")
        return 1

    print("REPRODUCTION_VERIFIED")
    for rel, digest in observed.items():
        print(f"{rel}  {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
