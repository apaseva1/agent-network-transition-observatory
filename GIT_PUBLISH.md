# Git Publication Bootstrap — v0.3.0

This source tree is repository-ready but intentionally has no remote bound to it.

Recommended publication sequence:

```bash
git init -b main
git add .
git commit -m "v0.3.0 post-freeze repository hardening"
git remote add origin <REMOTE_URL>
git push -u origin main
git tag -a v0.3.0 -m "v0.3.0 post-freeze repository hardening"
git push origin v0.3.0
```

Before the first public push:

1. choose repository visibility;
2. choose licensing explicitly;
3. confirm `python scripts/run_all.py` passes;
4. confirm the frozen submission linkage is correct;
5. do not add an application ID to the repository unless intentionally documenting the post-submission receipt.
