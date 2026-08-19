# Claim-to-evidence ledger

Each verdict below is scoped to the paper wording and evidence path named in
the row. The repository preserves the original campaign outputs, source
archives, controls, and branch history; this ledger is the short navigation
surface for reviewing them.

| Claim | Verdict | How the verdict is produced | Primary evidence |
| --- | --- | --- | --- |
| C1. Tangent-space IDD mapping and `T²`/SPE monitoring | `VERIFIED_SCOPED` | Run the paper-scale `d=5`, 600-distribution, 300-point mechanism audit with independent Hungarian OT, radial identity, PCA, `T²`, and SPE checks. The maximum identity error is `6.94e-18`; negative controls pass. | [`src/claim1_paper_scale.py`](src/claim1_paper_scale.py), [`outputs/claim1_attempt2_empirical.json`](outputs/claim1_attempt2_empirical.json), [`outputs/claim1_attempt3_quantile_audit.md`](outputs/claim1_attempt3_quantile_audit.md) |
| C2. Theorem 3.10 empirical-quantile `ARL₀` guarantee | `FALSIFIED_LITERAL` | Compare the live wording with the pinned TeX and run 4,000 seeded null replications at `n₀=200`. The literal proxy is `241.4` against the stated `251`; the source's finite-sample correction gives `234.39`. | [`outputs/claim2_attempt1_audit.md`](outputs/claim2_attempt1_audit.md), [`outputs/claim2_attempt1_empirical_arl.json`](outputs/claim2_attempt1_empirical_arl.json) |
| C3. Up to 95% high-variance delay reduction | `FALSIFIED_SOURCE_TABLE` | Parse all 18 pinned Table-1 rows and regenerate the released `d=5, σ=2` inputs. The largest displayed reduction against the best Log-KDE row is `72.5%` (`1.1` versus `4.0`); the R/`funcharts` runner is unavailable. | [`outputs/claim3_attempt1_audit.md`](outputs/claim3_attempt1_audit.md), [`outputs/claim3_attempt1/result.json`](outputs/claim3_attempt1/result.json) |
| C4. FlowCAP-II F1, `ARL₁`, and Hotelling comparison | `FALSIFIED_LITERAL_SOURCE_SCOPE` | Audit the stated 7-D/2,000-cell/300+300/80%-AML protocol and authoritative availability routes. No public data/labels/runner is released; the paper says Hotelling precision, not F1, is below `0.4`, and the appendix reports IDD `ARL₁` about `2–3`. | [`outputs/claim4_attempt1_audit.md`](outputs/claim4_attempt1_audit.md), [`outputs/claim4_attempt2_audit.md`](outputs/claim4_attempt2_audit.md), [`logbook/claim4.md`](logbook/claim4.md) |
| C5. Reddit event-aligned alarms and baseline behavior | `BLOCKED_INCONCLUSIVE` | Recover the protocol, Figure 4, event chronology, and multiple official-data routes, then check whether the exact daily embeddings, dated alarm arrays, and baseline outputs are available. They are not, so no synthetic substitute is promoted to a full rerun. | [`outputs/claim5_attempt3_audit.md`](outputs/claim5_attempt3_audit.md), [`outputs/claim5_attempt2_audit.md`](outputs/claim5_attempt2_audit.md), [`logbook/claim5.md`](logbook/claim5.md) |
| C6. Finite-dimensional epsilon-isometry component bound | `VERIFIED_SCOPED` | Parse the printed theorem and check nine epsilon-halving cases for `d=1,2,5`. The required ratios are `4`, `16`, and `1024`, matching the printed `ε^(-2d)` scaling; a dimension-free control is rejected. | [`src/claim6_attempt1_theorem_audit.py`](src/claim6_attempt1_theorem_audit.py), [`outputs/claim6_attempt1_audit.md`](outputs/claim6_attempt1_audit.md), [`outputs/claim6_attempt1/result.json`](outputs/claim6_attempt1/result.json) |

## Branch-to-evidence map

`main` is the cumulative publication surface. The 23 supporting branches are
clean, descriptive names for claim audits, release gates, or integration
work. Their historical `orx/*` names and exact purposes are recorded in
[`branch-audit.md`](branch-audit.md).

The most direct paths are [`audit/claim-1-paper-scale-idd`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/audit/claim-1-paper-scale-idd),
[`audit/claim-4-diamond-morphology`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/audit/claim-4-diamond-morphology),
[`audit/claim-5-cnf-sinkhorn`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/audit/claim-5-cnf-sinkhorn), and
[`release/final-publication-candidate`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/release/final-publication-candidate).

## Score and publication boundary

The previous live judged score was `7/12`. It predates later evidence and is
archived for provenance only. This repository makes no current score claim,
does not claim official author endorsement, and does not mark the evidence as
publication-authorized.
