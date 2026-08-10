import os
import re
import sys

ACTIVE_DOCS = [
    "README.md",
    "docs/INDEX.md",
    "docs/WHITEPAPER.md",
    "docs/GRANT_REVIEW_PACKET.md",
    "docs/REVIEWER_GUIDE.md",
    "docs/REPOSITORY_STATUS.md",
    "docs/RFP_SCOPE_CONTRACT.md"
]

def check_links():
    failed = False
    for doc in ACTIVE_DOCS:
        if not os.path.exists(doc):
            print(f"Warning: {doc} not found. Skipping.")
            continue
            
        with open(doc, "r", encoding="utf-8") as f:
            content = f.read()
            
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        doc_dir = os.path.dirname(doc)
        
        for text, link in links:
            if link.startswith("http://") or link.startswith("https://"):
                print(f"[INFO] External URL reported in {doc}: {link}")
                continue
            if link.startswith("#"):
                continue
                
            # Remove hash anchor from local file link
            file_link = link.split("#")[0]
            if not file_link:
                continue
                
            target_path = os.path.join(doc_dir, file_link)
            if not os.path.exists(target_path):
                print(f"[ERROR] Broken link in {doc}: {link} (resolved to {target_path})")
                failed = True
                
    if failed:
        print("Link check failed.")
        sys.exit(1)
    else:
        print("Link check passed.")

if __name__ == "__main__":
    check_links()