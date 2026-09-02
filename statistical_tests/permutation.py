"""Run independent permutation tests for experiment JSON files."""

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.stats import permutation_test


def holm(ps):
    """Holm-adjust p-values while preserving their original order."""
    order = np.argsort(ps)
    adjusted = np.empty(len(ps))
    running = 0.0
    for rank, index in enumerate(order):
        running = max(running, (len(ps) - rank) * ps[index])
        adjusted[index] = min(running, 1.0)
    return adjusted


def hedges_g(a, b):
    """Bias-corrected standardized difference: mean(a) - mean(b)."""
    na, nb = len(a), len(b)
    pooled = np.sqrt(((na - 1) * np.var(a, ddof=1) + (nb - 1) * np.var(b, ddof=1)) / (na + nb - 2))
    return 0.0 if pooled == 0 else (np.mean(a) - np.mean(b)) / pooled * (1 - 3 / (4 * (na + nb) - 9))


def unpaired_permutation_test(a, b, permutations, rng):
    """Two-sided independent-sample test of the difference in means."""
    statistic = lambda x, y: np.mean(x) - np.mean(y)
    result = permutation_test(
        (a, b), statistic, permutation_type="independent", alternative="two-sided",
        n_resamples=permutations, rng=rng,
    )
    exact = math.comb(len(a) + len(b), len(a)) <= permutations
    return {
        "mean_difference": float(result.statistic), "hedges_g": float(hedges_g(a, b)),
        "p_value": float(result.pvalue), "method": "exact" if exact else "monte_carlo",
    }


def omnibus(groups, permutations, rng):
    """Independent-sample omnibus test using between-group variation."""
    def statistic(*samples):
        grand = np.mean(np.concatenate(samples))
        return sum(len(x) * (np.mean(x) - grand) ** 2 for x in samples)

    result = permutation_test(
        tuple(groups), statistic, permutation_type="independent", alternative="greater",
        n_resamples=permutations, rng=rng,
    )
    return {"statistic": float(result.statistic), "p_value": float(result.pvalue)}


def analyze(data, permutations=100_000, seed=20260902):
    rng, output = np.random.default_rng(seed), {}
    for q_name, question in data["runs"].items():
        metrics = {}
        for metric, raw in question["runs"].items():
            groups = {name: np.asarray(values, dtype=float) for name, values in raw.items()}
            comparisons = []
            for a, b in itertools.combinations(groups, 2):
                comparisons.append({"groups": [a, b], **unpaired_permutation_test(groups[a], groups[b], permutations, rng)})
            for row, adjusted in zip(comparisons, holm([x["p_value"] for x in comparisons])):
                row["p_holm"] = float(adjusted)
            metrics[metric] = {
                "summary": {name: {"n": len(x), "mean": float(np.mean(x)), "sd": float(np.std(x, ddof=1))} for name, x in groups.items()},
                "omnibus": omnibus(groups.values(), permutations, rng), "comparisons": comparisons,
            }
        output[q_name] = {"description": question.get("description", ""), "metrics": metrics}
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--permutations", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=20260902)
    args = parser.parse_args()
    output = args.output_dir or Path("results") / args.input.stem
    output.mkdir(parents=True, exist_ok=True)
    results = analyze(json.loads(args.input.read_text()), args.permutations, args.seed)
    (output / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(f"Wrote results to {output}")
