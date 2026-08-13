# Beyond Euclidean Summaries — independent reproduction

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/blob/main/notebooks/reproduction.py)

Independent reproduction and claim audit for **Beyond Euclidean Summaries:
Online Change Point Detection for Distribution-Valued Data** by Yingyan Zeng,
Yujing (Zipan) Huang, and Xiaoyu Chen.

- Paper: [arXiv:2602.07252](https://arxiv.org/abs/2602.07252) · ICML 2026 / PMLR 306
- Clean repository: [MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd)
- Official implementation pin: [`yyzeng43/IDD-icml@c5b1db4`](https://github.com/yyzeng43/IDD-icml/tree/c5b1db4060e5081e5c487f91792dc18c17603fd0)
- Reproduction command: `uv sync --frozen && uv run --frozen python scripts/run_campaign.py`
- Published logbook: [DineshAI/repro-aU2sxdnRuL-distribution-valued-cpd](https://huggingface.co/spaces/DineshAI/repro-aU2sxdnRuL-distribution-valued-cpd)

## What the paper does

The paper proposes an intrinsic online change-point detector for streams of
empirical distributions. Each batch is treated as an observation in the
2-Wasserstein space and transported to a tangent space at a pre-change Fréchet
barycenter. Multivariate functional PCA then produces a low-dimensional score
space and a residual space, monitored with Hotelling's `T²` and squared
prediction error (SPE) charts.

The paper studies sequential false-alarm control, detection delay, synthetic
Gaussian-translation shifts, FlowCAP-II AML cytometry, and Reddit vaccine
sentiment. It also gives an epsilon-isometry result controlling the number of
principal components needed for finite-dimensional tangent-space approximation.

## Reproduction status

The campaign has six live claim contracts. A verdict is always scoped to the
exact statement and evidence path below. `FALSIFIED` means the literal claim
or source scope is contradicted; it does not by itself prove that the broader
IDD method fails. `BLOCKED`/`INCONCLUSIVE` means the required source-faithful
data or dependency was unavailable and no proxy was promoted to a full
reproduction.

| Claim | Paper result | Evidence and how the verdict is produced | Verdict |
| --- | --- | --- | --- |
| 1 | IDD maps distributions to the barycenter tangent space using the radial OT isometry and applies `T²`/SPE | [`src/claim1_paper_scale.py`](src/claim1_paper_scale.py) audits `d=5`, 600 distributions, 300 points each, with exact Hungarian OT checks; maximum identity error is `6.94e-18`; independent PCA/`T²`/SPE and negative controls also pass | **VERIFIED · scoped mechanism** |
| 2 | Theorem 3.10 gives `ARL₀ ≥ n₀ + 1 + 1/(αT² + αSPE)` under empirical-quantile calibration | Source audit separates the fixed-threshold theorem from its finite-sample empirical-quantile corollary; 4,000 seeded null replications at `n₀=200` give literal proxy `241.4` versus bound `251`, while the corrected source bound is `234.39` | **FALSIFIED · literal wording** |
| 3 | High-variance Gaussian translation yields up to 95% delay reduction over best-tuned Log-KDE at matched `ARL₀` | [`src/claim3_attempt1_source_audit.py`](src/claim3_attempt1_source_audit.py) parses all 18 pinned Table-1 rows and regenerates the released `d=5, σ=2` inputs; the largest displayed high-variance reduction is `72.5%` (`1.1` vs `4.0`), and the R/`funcharts` runner is unavailable | **FALSIFIED · source-table scope** |
| 4 | FlowCAP-II IDD result: F1 about `0.75`, `ARL₁` about `1`, and Hotelling `T²` F1 below `0.4` | The source/release audit checks the stated 7-D/2,000-cell/300+300/80%-AML protocol, finds no public FlowCAP data/labels/loader/runner, and finds that the paper says Hotelling **precision**, not F1; the appendix reports IDD `ARL₁` about `2–3` | **FALSIFIED · literal source scope** |
| 5 | Reddit d=20 alarms align with vaccine-news events while Euclidean baselines show unrelated drift/noise | Three independent availability/provenance routes recover the protocol and Figure 4, but not the exact daily embeddings, dated alarm arrays, or baseline outputs; the source places the post-gap reorganization on Apr 30 after an Apr 3–28 data gap | **BLOCKED · inconclusive** |
| 6 | Theorem 3.14 gives polynomial principal-component growth for epsilon-isometry under regularity assumptions | [`src/claim6_attempt1_theorem_audit.py`](src/claim6_attempt1_theorem_audit.py) parses the theorem and checks nine epsilon-halving cases for `d=1,2,5`; ratios are `4`, `16`, and `1024`, and the dimension-free control is rejected | **VERIFIED · scoped theorem audit** |

The campaign's previous live judged score was `7/12`. That score predates
some of the later evidence and is not a claim of final acceptance. The exact
run artifacts, source hashes, controls, and limitations are retained under
`outputs/`, `evidence/`, `contract/`, and `logbook/`.

## How the claims are produced

The fixed runner executes the campaign's historical regression, claim audits,
negative controls, release validation, and evaluator-visible traversal:

```text
scripts/run_campaign.py
├── src/claim1_paper_scale.py                 # Claim 1 mechanism audit
├── src/claim2_attempt1_empirical_arl.py      # Claim 2 calibration audit
├── src/claim3_attempt1_source_audit.py      # Claim 3 table/source audit
├── src/claim4_attempt*_*.py                  # Claim 4 source/data availability
├── src/claim5_attempt*_*.py                  # Claim 5 data/provenance routes
├── src/claim6_attempt1_theorem_audit.py      # Claim 6 theorem/algebra audit
└── scripts/validate_release_candidate.py    # publication and navigation gates
```

Claim 1 uses a controlled Gaussian affine-pushforward family, solves the
empirical OT assignment independently, and checks that the tangent norm equals
the solved Wasserstein cost. This verifies the mechanism at paper-scale
dimensions but does not recreate the unavailable R/`funcharts` performance
pipeline or FlowCAP/Reddit results.

Claim 2 compares the literal live formula with the paper's own finite-sample
quantile correction. Claim 3 compares the paper's printed Table-1 numbers
against the exact “high variance / best Log-KDE” wording and separately records
the missing R dependency. Claim 4 searches only authoritative sources for the
exact FlowCAP files and labels. Claim 5 refuses to substitute synthetic Reddit
streams for the missing paper-era arrays. Claim 6 audits the printed theorem's
assumptions and epsilon algebra, including a control that incorrectly drops the
dimension exponent.

## Evidence map

- `contract/` — six claim contracts, metadata, and pinned source URLs.
- `src/` — executable claim audits and source-faithful probes.
- `tests/` — focused regression tests for contracts, claims, and publication.
- `outputs/` — raw results, logs, hashes, generated-input manifests, and
  availability audits.
- `evidence/` — retained official-source downloads and provenance records.
- `logbook/` — current claim pages, conclusion, poster, and evaluator surface.
- `reports/campaign/` — illustrated technical report.
- `notebooks/reproduction.py` — self-contained marimo walkthrough.
- `branch-audit.md` — complete old-to-clean branch mapping.

## Branches and experiments

`main` is the publication surface. The original OpenResearch-style `orx/*`
branches have been renamed to descriptive `audit/`, `release/`, and
`integration/` branches. The full 23-branch mapping is in
[`branch-audit.md`](branch-audit.md); the most important evidence paths are:

| Clean branch | Purpose | Recorded outcome |
| --- | --- | --- |
| [`audit/claim-1-paper-scale-idd`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/audit/claim-1-paper-scale-idd) | Paper-scale multivariate tangent/OT mechanism | Claim 1 scoped verification; 19 checks passed |
| [`audit/claim-4-diamond-morphology`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/audit/claim-4-diamond-morphology) | Independent FlowCAP figure-marker audit | Literal Claim 4 source scope falsified |
| [`audit/claim-5-official-schema`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/audit/claim-5-official-schema) | Audit official Reddit artifact representations | Exact minimum-30 stream unavailable |
| [`audit/claim-5-cnf-sinkhorn`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/audit/claim-5-cnf-sinkhorn) | Closest 50+49-day CNF/Sinkhorn/MFPCA route | Blocked; 49/49 SPE alarms under the closest route |
| [`release/cumulative-candidate`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/release/cumulative-candidate) | Cumulative science and publication gates | 24 checks and protected traversal passed |
| [`release/evaluator-blind-red-team`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/release/evaluator-blind-red-team) | Repeat evaluator-blind review after red-team fixes | 24 checks and 143 upload paths passed |
| [`release/final-publication-candidate`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/release/final-publication-candidate) | Final publication candidate and review facts | Publication-ready artifact |
| [`integration/hub-metadata-publication-repair`](https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd/tree/integration/hub-metadata-publication-repair) | Repair and publish final Hub metadata | Current historical tip mirrored into `main` |

Every branch's role and historical name is recorded in
[`branch-audit.md`](branch-audit.md), including the three Claim 1 branches,
seven Claim 4 branches, eight Claim 5 branches, and five release/integration
branches.

## Reproduce

Use Python 3.12 and `uv`; the lockfile is authoritative. All campaign runs
were CPU-only and used no Hugging Face Job, model, dataset, or Bucket.

```bash
uv sync --frozen
uv run --frozen python scripts/run_campaign.py
```

The repository deliberately does not claim to recreate unavailable FlowCAP
FCS files, the exact Reddit 50+50 stream, or private author modules. Those
limitations are part of the verdicts, not hidden setup requirements.

## Citation

```bibtex
@article{zeng2026beyond,
  title   = {Beyond Euclidean Summaries: Online Change Point Detection for Distribution-Valued Data},
  author  = {Zeng, Yingyan and Huang, Yujing and Chen, Xiaoyu},
  journal = {arXiv preprint arXiv:2602.07252},
  year    = {2026},
  doi     = {10.48550/arXiv.2602.07252}
}
```

## Thank you

Thank you to Yingyan Zeng, Yujing (Zipan) Huang, and Xiaoyu Chen for making
the IDD formulation, theoretical claims, source archive, and implementation
available for careful study. This independent reproduction is maintained by
[MachineLearning-Nerd](https://github.com/MachineLearning-Nerd) as a
transparent audit and learning resource; its scoped verdicts are intended to
make the evidence and missing prerequisites easy to inspect, not to diminish
the authors' contribution.
