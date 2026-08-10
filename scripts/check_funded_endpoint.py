import sys
from pathlib import Path

def main():
    required_string = "DETERMINISTIC/SYNTHETIC R1 = FUNDED HIGH-FIDELITY ENDPOINT"
    
    docs_to_check = [
        "docs/WHITEPAPER.md",
        "docs/GRANT_REVIEW_PACKET.md"
    ]
    
    found = False
    for doc_path in docs_to_check:
        p = Path(doc_path)
        if p.exists():
            content = p.read_text(encoding="utf-8")
            if required_string in content:
                found = True
                break
                
    if not found:
        print(f"Error: The mandated funded endpoint string was not found in any of the checked documents.")
        print(f"Missing string: {required_string}")
        sys.exit(1)
        
    print("FUNDED HIGH-FIDELITY ENDPOINT string is present.")
    
if __name__ == "__main__":
    main()
