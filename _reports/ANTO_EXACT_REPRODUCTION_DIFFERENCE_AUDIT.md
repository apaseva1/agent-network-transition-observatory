# ANTO Exact Reproduction Difference Audit

- **Which fields differ?** algebraic_connectivity
- **How many values differ?** 770 out of 14688 total values across 864 rows.
- **Maximum absolute difference:** 2.1316282072803006e-14
- **Maximum relative difference:** 5.062424165741393e-14
- **Whether differences are confined to algebraic_connectivity:** True
- **Whether strings / integers / row identity differ:** False

### Conclusion
The mismatch is entirely driven by subtle floating-point drift in specific algebraic calculations (eigenvalue decompositions in networkx/scipy) across different BLAS/LAPACK backends (e.g., OpenBLAS vs MKL vs Accelerate). The integers, strings, and categorical invariants remain 100% exact.
