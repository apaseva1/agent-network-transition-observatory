import subprocess
import sys
from pathlib import Path

def run_check(command, allow_code=None):
    try:
        proc = subprocess.run(command, capture_output=True, text=True)
        if proc.returncode == 0:
            return "PASS"
        if allow_code is not None and proc.returncode == allow_code:
            return "NOT_VERIFIED_ON_THIS_PLATFORM"
        print(f"Command failed: {' '.join(command)}")
        print(proc.stdout)
        print(proc.stderr)
        return "FAIL"
    except Exception as e:
        print(f"Error executing {' '.join(command)}: {e}")
        return "FAIL"

def main():
    print("=== RC.2 LOCAL GATES ===")
    
    # 1. CANONICAL_ARTIFACT_INTEGRITY
    print("Running Artifact Integrity...")
    integrity = run_check([sys.executable, "scripts/verify_reproduction.py", "--integrity"])
    
    # 2. CANONICAL_EXACT_REPRODUCTION
    print("Running Exact Reproduction...")
    exact = run_check([sys.executable, "scripts/verify_reproduction.py", "--exact"], allow_code=2)
    
    # 3. CROSS_PLATFORM_NUMERICAL_REPRODUCTION
    print("Running Numerical Reproduction...")
    numerical = run_check([sys.executable, "scripts/verify_reproduction.py", "--numerical"])
    
    # 4. RFP_ENDPOINT_BOUNDARY
    print("Running RFP Endpoint Check...")
    rfp = run_check([sys.executable, "scripts/check_funded_endpoint.py"])
    
    # 5. RESULTS_FRESHNESS
    print("Running Results Document Freshness...")
    freshness = run_check([sys.executable, "scripts/generate_results_document.py", "--check"])
    
    # 6. UNIT_REGRESSION_TESTS
    print("Running Unit Tests...")
    tests = run_check([sys.executable, "-m", "pytest", "-q"])
    
    # 7. CLAIM_BOUNDARY
    print("Running Claim Boundary Check...")
    claim = run_check([sys.executable, "scripts/check_claim_boundary.py"])
    
    # 8. LINK_CHECK
    print("Running Link Check...")
    link = run_check([sys.executable, "scripts/check_links.py"])
    
    # 9. BOUNDED_HYGIENE
    print("Running Bounded Hygiene Check...")
    hygiene = run_check([sys.executable, "scripts/check_hygiene.py"])
    
    print("\n=== GATE REPORT ===")
    print(f"CANONICAL_ARTIFACT_INTEGRITY: {integrity}")
    print(f"CANONICAL_EXACT_REPRODUCTION: {exact}")
    print(f"CROSS_PLATFORM_NUMERICAL_REPRODUCTION: {numerical}")
    print(f"RFP_ENDPOINT_BOUNDARY: {rfp}")
    print(f"RESULTS_FRESHNESS: {freshness}")
    print(f"UNIT_REGRESSION_TESTS: {tests}")
    print(f"CLAIM_BOUNDARY: {claim}")
    print(f"LINK_CHECK: {link}")
    print(f"BOUNDED_HYGIENE: {hygiene}")
    print("CI:")
    print("CI_CONFIGURED")
    print("CI_REMOTE_VERIFICATION: NOT_DETERMINED_BY_LOCAL_GATE")
    
    # Evaluate Pass Condition
    if exact == "FAIL":
        print("\n=== OVERALL STATUS: FAIL ===")
        sys.exit(1)
        
    required_passes = [integrity, numerical, rfp, freshness, tests, claim, link, hygiene]
    if all(x == "PASS" for x in required_passes):
        if exact == "NOT_VERIFIED_ON_THIS_PLATFORM":
            print("\n=== OVERALL STATUS: PASS_WITH_EXACT_REPRODUCTION_NOT_VERIFIED ===")
            sys.exit(0)
        else:
            print("\n=== OVERALL STATUS: PASS ===")
            sys.exit(0)
    else:
        print("\n=== OVERALL STATUS: FAIL ===")
        sys.exit(1)

if __name__ == "__main__":
    main()
