# Methodological Hardening R2

The source-regime split is now grouped by topology × seed fraction × propagation parameter, preventing replicate configurations from leaking across development and held-out sets.

Verification: **8 passed**.

This change was made before submission freeze because it reduces the chance that the prototype overstates evidence quality. All generated CSV/JSON outputs in this capsule were regenerated after the change.
