# Permutation test results

Independent, two-sided tests; pairwise p-values use Holm correction.

## question_1: Bimamba vs. SISO

### test_auprc (omnibus p = 0.00793651)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| bimamba − siso | 0.0201 | 2.49 | 0.00793651 | yes |

### val_auprc (omnibus p = 0.00793651)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| bimamba − siso | 0.01762 | 3.255 | 0.00793651 | yes |

### test_loss (omnibus p = 0.00793651)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| bimamba − siso | -0.0122724 | -2.097 | 0.00793651 | yes |

## question_2: descriminate between less layers 2, 3, or 4

### test_auprc (omnibus p = 9.9999e-06)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| 2 − 3 | -0.05004 | -11.79 | 0.0238095 | yes |
| 2 − 4 | -0.06578 | -8.969 | 0.0238095 | yes |
| 3 − 4 | -0.01574 | -2.369 | 0.0238095 | yes |

### val_auprc (omnibus p = 1.99998e-05)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| 2 − 3 | -0.04592 | -8.972 | 0.0238095 | yes |
| 2 − 4 | -0.05872 | -9.222 | 0.0238095 | yes |
| 3 − 4 | -0.0128 | -2.442 | 0.0238095 | yes |

### test_loss (omnibus p = 1.99998e-05)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| 2 − 3 | 0.028816 | 7.865 | 0.0238095 | yes |
| 2 − 4 | 0.040361 | 9.171 | 0.0238095 | yes |
| 3 − 4 | 0.011545 | 2.732 | 0.0238095 | yes |

## question_3: sweeping effect kernel sizes across bimamba

### test_auprc (omnibus p = 0.170348)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| 15 − 19 | -0.00402 | -0.6665 | 1 | no |
| 15 − 23 | -0.0016 | -0.2136 | 1 | no |
| 15 − 27 | -0.00838 | -1.668 | 0.238095 | no |
| 15 − 31 | -0.00822 | -1.067 | 0.928571 | no |
| 19 − 23 | 0.00242 | 0.3229 | 1 | no |
| 19 − 27 | -0.00436 | -0.8668 | 1 | no |
| 19 − 31 | -0.0042 | -0.5449 | 1 | no |
| 23 − 27 | -0.00678 | -1.01 | 1 | no |
| 23 − 31 | -0.00662 | -0.7441 | 1 | no |
| 27 − 31 | 0.00016 | 0.02303 | 1 | no |

### val_auprc (omnibus p = 0.281897)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| 15 − 19 | -0.00404 | -0.5271 | 1 | no |
| 15 − 23 | -0.00352 | -0.4861 | 1 | no |
| 15 − 27 | -0.00668 | -0.9068 | 1 | no |
| 15 − 31 | -0.0094 | -0.8987 | 1 | no |
| 19 − 23 | 0.00052 | 0.1133 | 1 | no |
| 19 − 27 | -0.00264 | -0.5516 | 1 | no |
| 19 − 31 | -0.00536 | -0.6067 | 1 | no |
| 23 − 27 | -0.00316 | -0.7759 | 1 | no |
| 23 − 31 | -0.00588 | -0.6943 | 1 | no |
| 27 − 31 | -0.00272 | -0.3171 | 1 | no |

### test_loss (omnibus p = 0.156868)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| 15 − 19 | 0.0023794 | 0.5166 | 1 | no |
| 15 − 23 | 0.001154 | 0.2192 | 1 | no |
| 15 − 27 | 0.0055312 | 1.217 | 0.31746 | no |
| 15 − 31 | 0.0057406 | 0.905 | 1 | no |
| 19 − 23 | -0.0012254 | -0.3472 | 1 | no |
| 19 − 27 | 0.0031518 | 1.358 | 0.428571 | no |
| 19 − 31 | 0.0033612 | 0.6725 | 1 | no |
| 23 − 27 | 0.0043772 | 1.27 | 0.444444 | no |
| 23 − 31 | 0.0045866 | 0.8175 | 1 | no |
| 27 − 31 | 0.0002094 | 0.04238 | 1 | no |

## question_4: on the removal of the CNN (for bimamba)

### test_auprc (omnibus p = 0.015873)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| embedding − embedding_cnn | 0.01478 | 2.338 | 0.015873 | yes |

### val_auprc (omnibus p = 0.00793651)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| embedding − embedding_cnn | 0.01408 | 2.045 | 0.00793651 | yes |

### test_loss (omnibus p = 0.0238095)

| Comparison | Mean difference | Hedges' g | Holm p | Significant |
|---|---:|---:|---:|:---:|
| embedding − embedding_cnn | -0.010729 | -1.719 | 0.0238095 | yes |
