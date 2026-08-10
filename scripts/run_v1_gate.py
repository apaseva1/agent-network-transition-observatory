import subprocess
import sys

def run_step(name, command):
    print(f"--- Running {name} ---")
    try:
        subprocess.run(command, check=True)
        print(f"[OK] {name}")
    except subprocess.CalledProcessError:
        print(f"[FAIL] {name} failed.")
        sys.exit(1)

def main():
    run_step("Tests", [sys.executable, "-m", "pytest", "-q"])
    run_step("Canonical Reproduction Verification", [sys.executable, "scripts/verify_reproduction.py"])
    run_step("Claim Scan", [sys.executable, "scripts/check_claim_boundary.py"])
    run_step("Bounded Hygiene Check", [sys.executable, "scripts/check_hygiene.py"])
    run_step("Funded Endpoint Check", [sys.executable, "scripts/check_funded_endpoint.py"])
    
    print("\n=== V1 GATE PASSED ===")

if __name__ == "__main__":
    main()
