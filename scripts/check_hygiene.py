import os
import re
import sys

DANGEROUS_PATTERNS = [
    r"BEGIN PRIVATE KEY",
    r"BEGIN RSA PRIVATE KEY",
    r"(?i)api[_-]?key\s*=\s*['\"][A-Za-z0-9\-_]{16,}['\"]",
    r"(?i)bearer\s+[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+"
]

DANGEROUS_FILES = [
    ".env",
    ".env.local",
    "credentials.json"
]

def main():
    failed = False
    print("Running bounded repository hygiene scan...")
    for root, dirs, files in os.walk("."):
        if ".git" in root or "__pycache__" in root or "node_modules" in root:
            continue
            
        for f in files:
            if f in DANGEROUS_FILES:
                print(f"[ERROR] Suspicious file found: {os.path.join(root, f)}")
                failed = True
                continue
                
            if not f.endswith(".md") and not f.endswith(".py") and not f.endswith(".json") and not f.endswith(".csv") and not f.endswith(".txt"):
                continue
                
            if f == "check_hygiene.py":
                continue
                
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8") as file_obj:
                    lines = file_obj.readlines()
                for i, line in enumerate(lines):
                    for pattern in DANGEROUS_PATTERNS:
                        if re.search(pattern, line):
                            print(f"[ERROR] Suspicious pattern found in {path}:{i+1}")
                            failed = True
            except Exception:
                pass
                
    if failed:
        print("Hygiene check failed.")
        sys.exit(1)
    else:
        print("Hygiene check passed.")

if __name__ == "__main__":
    main()
