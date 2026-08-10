import argparse
import csv
import hashlib
import io
import json
import math
import shutil
import subprocess
import sys
import tempfile
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

def check_integrity():
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = []
    
    for rel in RESULT_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append((rel, expected["files"][rel]["normalized_sha256"], "FILE_MISSING"))
            continue
        
        digest = normalized_sha256(path)
        want = expected["files"][rel]["normalized_sha256"]
        if digest != want:
            failures.append((rel, want, digest))
            
    if failures:
        print("CANONICAL_ARTIFACT_INTEGRITY: FAIL")
        for rel, want, got in failures:
            print(f"  {rel}\n    expected={want}\n    observed={got}")
        return False
        
    print("CANONICAL_ARTIFACT_INTEGRITY: PASS")
    return True

def run_isolated_reproduction():
    temp_dir = tempfile.mkdtemp(prefix="anto_repro_")
    temp_path = Path(temp_dir)
    try:
        shutil.copytree(ROOT / "observatory", temp_path / "observatory")
        shutil.copytree(ROOT / "experiments", temp_path / "experiments")
        (temp_path / "results").mkdir(exist_ok=True)
        
        proc = subprocess.run(COMMAND, cwd=temp_path)
        if proc.returncode != 0:
            print("Reproduction subprocess failed.")
            return None
            
        return temp_path
    except Exception as e:
        print(f"Reproduction setup failed: {e}")
        shutil.rmtree(temp_dir, ignore_errors=True)
        return None

def check_exact():
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
        
    temp_path = run_isolated_reproduction()
    if not temp_path:
        print("CANONICAL_EXACT_REPRODUCTION: FAIL (Execution Error)")
        return False
        
    failures = []
    for rel in RESULT_FILES:
        path = temp_path / rel
        if not path.exists():
            failures.append((rel, "FILE_MISSING"))
            continue
            
        digest = normalized_sha256(path)
        want = expected["files"][rel]["normalized_sha256"]
        if digest != want:
            failures.append((rel, want, digest))
            
    shutil.rmtree(temp_path, ignore_errors=True)
    
    if failures:
        print("CANONICAL_EXACT_REPRODUCTION: NOT_VERIFIED_ON_THIS_PLATFORM (Byte-exact mismatch)")
        for f in failures:
            print(f"  {f[0]}: Mismatch")
        return 2
        
    print("CANONICAL_EXACT_REPRODUCTION: PASS")
    return True

def compare_json(expected, observed, path=""):
    if isinstance(expected, dict):
        if not isinstance(observed, dict):
            return False
        if expected.keys() != observed.keys():
            return False
        for k in expected:
            if not compare_json(expected[k], observed[k], path=f"{path}.{k}"):
                return False
        return True
    elif isinstance(expected, list):
        if not isinstance(observed, list):
            return False
        if len(expected) != len(observed):
            return False
        for i, (e, o) in enumerate(zip(expected, observed)):
            if not compare_json(e, o, path=f"{path}[{i}]"):
                return False
        return True
    elif isinstance(expected, float):
        if not isinstance(observed, float) and not isinstance(observed, int):
            return False
        # Relative tolerance of 1e-9 for BLAS/LAPACK float drift
        return math.isclose(expected, observed, rel_tol=1e-9, abs_tol=1e-9)
    else:
        return expected == observed

def compare_csv(expected_path, observed_path):
    expected_rows = list(csv.DictReader(io.StringIO(expected_path.read_text(encoding="utf-8"))))
    observed_rows = list(csv.DictReader(io.StringIO(observed_path.read_text(encoding="utf-8"))))
    
    if len(expected_rows) != len(observed_rows):
        return False
        
    for i, (e_row, o_row) in enumerate(zip(expected_rows, observed_rows)):
        if e_row.keys() != o_row.keys():
            return False
        for k in e_row:
            try:
                e_val = float(e_row[k])
                o_val = float(o_row[k])
                # Relative tolerance of 1e-9 for BLAS/LAPACK float drift
                if not math.isclose(e_val, o_val, rel_tol=1e-9, abs_tol=1e-9):
                    return False
            except ValueError:
                if e_row[k] != o_row[k]:
                    return False
    return True

def check_numerical():
    temp_path = run_isolated_reproduction()
    if not temp_path:
        print("CROSS_PLATFORM_NUMERICAL_REPRODUCTION: FAIL (Execution Error)")
        return False
        
    failures = []
    
    # Check JSON
    expected_json = json.loads((ROOT / "results" / "synthetic_transfer_summary.json").read_text(encoding="utf-8"))
    observed_json = json.loads((temp_path / "results" / "synthetic_transfer_summary.json").read_text(encoding="utf-8"))
    
    if not compare_json(expected_json, observed_json):
        failures.append("synthetic_transfer_summary.json")
        
    # Check CSV
    expected_csv_path = ROOT / "results" / "synthetic_transfer_runs.csv"
    observed_csv_path = temp_path / "results" / "synthetic_transfer_runs.csv"
    
    if not compare_csv(expected_csv_path, observed_csv_path):
        failures.append("synthetic_transfer_runs.csv")
        
    shutil.rmtree(temp_path, ignore_errors=True)
    
    if failures:
        print("CROSS_PLATFORM_NUMERICAL_REPRODUCTION: FAIL")
        for f in failures:
            print(f"  {f}: Numerical mismatch beyond tolerance")
        return False
        
    print("CROSS_PLATFORM_NUMERICAL_REPRODUCTION: PASS")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--integrity", action="store_true")
    parser.add_argument("--exact", action="store_true")
    parser.add_argument("--numerical", action="store_true")
    args = parser.parse_args()
    
    if args.integrity:
        res = check_integrity()
        sys.exit(0 if res else 1)
    elif args.exact:
        res = check_exact()
        sys.exit(0 if res is True else (1 if res is False else 2))
    elif args.numerical:
        res = check_numerical()
        sys.exit(0 if res else 1)
    else:
        print("Specify --integrity, --exact, or --numerical")
        sys.exit(1)

if __name__ == "__main__":
    main()
