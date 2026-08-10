import sys
from pathlib import Path
import re

def main():
    required_string = "DETERMINISTIC_SYNTHETIC_R1 != FUNDED_HIGH_FIDELITY_ENDPOINT"
    
    docs_to_check = [
        "README.md",
        "CLAIM_BOUNDARY.md",
        "docs/WHITEPAPER.md",
        "docs/GRANT_REVIEW_PACKET.md",
        "docs/GRANT_ALIGNMENT.md",
        "docs/REVIEWER_GUIDE.md",
        "docs/RFP_SCOPE_CONTRACT.md"
    ]
    
    # Regexes for equality formulations that must be rejected
    equality_patterns = [
        re.compile(r"DETERMINISTIC/SYNTHETIC R1 = FUNDED HIGH-FIDELITY ENDPOINT", re.IGNORECASE),
        re.compile(r"DETERMINISTIC_SYNTHETIC_R1 = FUNDED_HIGH_FIDELITY_ENDPOINT", re.IGNORECASE),
        re.compile(r"\bR1 = FUNDED\b", re.IGNORECASE),
        re.compile(r"synthetic R1 = funded", re.IGNORECASE),
        re.compile(r"deterministic R1 = funded", re.IGNORECASE),
    ]

    has_error = False
    
    for doc_path in docs_to_check:
        p = Path(doc_path)
        if not p.exists():
            continue
            
        lines = p.read_text(encoding="utf-8").splitlines()
        has_contract = False
        
        for i, line in enumerate(lines):
            # Check for forbidden equality
            for pattern in equality_patterns:
                if pattern.search(line):
                    print(f"Error: Forbidden equality formulation found in {doc_path}:{i+1}")
                    print(f"  Line: {line.strip()}")
                    has_error = True
                    
            # Check for required contract presence
            if required_string in line:
                has_contract = True

        if doc_path == "docs/RFP_SCOPE_CONTRACT.md" and not has_contract:
            print(f"Error: {doc_path} is missing the required canonical inequality contract: {required_string}")
            has_error = True

    if has_error:
        print("FUNDED ENDPOINT CHECK FAILED.")
        sys.exit(1)
        
    print("FUNDED ENDPOINT CHECK PASSED.")
    
if __name__ == "__main__":
    main()
