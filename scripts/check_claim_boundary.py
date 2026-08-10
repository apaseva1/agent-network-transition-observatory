import sys
import re

ACTIVE_DOCS = [
    "README.md",
    "CLAIM_BOUNDARY.md",
    "docs/WHITEPAPER.md",
    "docs/GRANT_REVIEW_PACKET.md",
    "docs/RESULTS.md"
]

FORBIDDEN_PHRASES = [
    r"\bproven safe\b",
    r"\bfrontier validated\b",
    r"\bproduction-ready\b",
    r"\buniversal safety\b",
    r"\bguaranteed safety\b",
    r"\bgeneral solution\b"
]

def main():
    failed = False
    for doc in ACTIVE_DOCS:
        try:
            with open(doc, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                for phrase in FORBIDDEN_PHRASES:
                    if re.search(phrase, line, re.IGNORECASE):
                        print(f"OVERCLAIM DETECTED in {doc}:{i+1}: {line.strip()} (matches '{phrase}')")
                        failed = True
        except FileNotFoundError:
            print(f"Warning: {doc} not found. Skipping.")
            
    if failed:
        print("Claim boundary check failed.")
        sys.exit(1)
    else:
        print("Claim boundary check passed.")

if __name__ == "__main__":
    main()
