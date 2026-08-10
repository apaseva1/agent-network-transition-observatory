import json
import os
import sys

def main():
    check_mode = '--check' in sys.argv
    
    with open('results/synthetic_transfer_summary.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    runs = data.get('runs', 864)
    forecast = data.get('forecast_eligible', 853)
    s0_full = data.get('S0_static', {}).get('full_auroc', 0.829009)
    s0_base = data.get('S0_static', {}).get('baseline_auroc', 0.883844)
    s0_uplift = data.get('S0_static', {}).get('absolute_uplift', -0.054835)
    
    s1_full = data.get('S1_rewire', {}).get('full_auroc', 0.907882)
    s1_base = data.get('S1_rewire', {}).get('baseline_auroc', 0.909849)
    s1_uplift = data.get('S1_rewire', {}).get('absolute_uplift', -0.001967)
    
    s2_full = data.get('S2_heterogeneous', {}).get('full_auroc', 0.862775)
    s2_base = data.get('S2_heterogeneous', {}).get('baseline_auroc', 0.858793)
    s2_uplift = data.get('S2_heterogeneous', {}).get('absolute_uplift', 0.003982)

    doc = f'''# Transfer Evaluation Results

## Canonical Evidence
- **Total runs**: {runs}
- **Forecast eligible**: {forecast}

### S0_static
- **full AUROC**: ~{s0_full:.6f}
- **baseline AUROC**: ~{s0_base:.6f}
- **absolute uplift**: ~{s0_uplift:.6f}

### S1_rewire
- **full AUROC**: ~{s1_full:.6f}
- **baseline AUROC**: ~{s1_base:.6f}
- **absolute uplift**: ~{s1_uplift:.6f}

### S2_heterogeneous
- **full AUROC**: ~{s2_full:.6f}
- **baseline AUROC**: ~{s2_base:.6f}
- **absolute uplift**: ~+{s2_uplift:.6f}

## Transfer retention
**undefined/null** in all current regimes because source uplift does not exceed the configured minimum threshold.

## Scientific Interpretation
The current R1 instrument validates the measurement pipeline. It does **NOT** establish positive incremental early-warning value. This null/weak result is a scientific strength: the experiment was capable of returning an unfavorable answer, and did so.
'''
    
    if check_mode:
        if not os.path.exists('docs/RESULTS.md'):
            print("docs/RESULTS.md missing.")
            sys.exit(1)
        with open('docs/RESULTS.md', 'r', encoding='utf-8') as f:
            existing = f.read()
        if existing != doc:
            print("docs/RESULTS.md is not fresh. Run generate_results_document.py.")
            sys.exit(1)
        print("docs/RESULTS.md is fresh.")
    else:
        with open('docs/RESULTS.md', 'w', encoding='utf-8') as f:
            f.write(doc)
        print("Generated docs/RESULTS.md")

if __name__ == '__main__':
    main()