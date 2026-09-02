# Statistical tests

This project compares model configurations when each configuration contains independent runs with randomly chosen seeds. It performs:

- a two-sided omnibus permutation test for every question and metric;
- two-sided pairwise permutation tests based on differences in means;
- Hedges' g effect sizes; and
- Holm correction across pairwise comparisons within each question and metric.

Pairwise tests with only two groups of five runs are exact (all 252 label assignments). Larger omnibus tests use reproducible Monte Carlo permutations.

## Run the analysis

Install the dependency in a virtual environment:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

```bash
.venv/bin/python -m statistical_tests data/sep_2_aleksey.json
```

The command automatically creates:

```text
results/
└── sep_2_aleksey/
    ├── report.md
    └── results.json
```

To select another destination:

```bash
.venv/bin/python -m statistical_tests data/sep_2_aleksey.json --output-dir my_results/run_1
```

Use `--permutations` to change the default of 100,000 random assignments and `--seed` to change the reproducibility seed.

## Interpretation

The omnibus test asks whether any configuration differs for a metric. Pairwise results identify which configurations differ. Use the Holm-adjusted p-value (`Holm p`) for the usual 0.05 significance decision. Statistical significance does not measure practical importance, so interpret it alongside the mean difference and Hedges' g.

Because the random seeds do not correspond across configurations, all tests treat runs as independent rather than paired.
