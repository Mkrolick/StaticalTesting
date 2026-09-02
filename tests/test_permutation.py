import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

from statistical_tests.permutation import analyze, hedges_g, holm, unpaired_permutation_test


class StatisticalTests(unittest.TestCase):
    def test_holm_adjustment(self) -> None:
        np.testing.assert_allclose(holm([0.01, 0.04, 0.03]), [0.03, 0.06, 0.06])

    def test_hedges_g_for_constant_groups(self) -> None:
        self.assertEqual(hedges_g(np.array([1.0, 1.0]), np.array([1.0, 1.0])), 0.0)
        self.assertIsNone(hedges_g(np.array([1.0, 1.0]), np.array([2.0, 2.0])))

    def test_two_group_test_is_exact_and_two_sided(self) -> None:
        result = unpaired_permutation_test(
            np.array([10.0, 11.0, 12.0]),
            np.array([1.0, 2.0, 3.0]),
            100,
            np.random.default_rng(1),
        )
        self.assertEqual(result["method"], "exact")
        self.assertAlmostEqual(result["p_value"], 0.1)
        self.assertEqual(result["mean_difference"], 9.0)

    def test_analysis_is_reproducible(self) -> None:
        data = {"runs": {"q": {"runs": {"score": {
            "a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]
        }}}}}
        self.assertEqual(analyze(data, 100, 7), analyze(data, 100, 7))

    def test_cli_writes_only_json(self) -> None:
        data = {"runs": {"q": {"runs": {"score": {
            "a": [1, 2, 3], "b": [4, 5, 6]
        }}}}}
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, output = root / "input.json", root / "output"
            source.write_text(json.dumps(data))
            subprocess.run(
                [sys.executable, "-m", "statistical_tests", str(source),
                 "--output-dir", str(output), "--permutations", "100"],
                check=True,
            )
            self.assertEqual([path.name for path in output.iterdir()], ["results.json"])
            json.loads((output / "results.json").read_text())


if __name__ == "__main__":
    unittest.main()
