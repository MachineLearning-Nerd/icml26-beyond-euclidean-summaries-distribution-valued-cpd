# Source audit

## Canonical paper

**Beyond Euclidean Summaries: Online Change Point Detection for
Distribution-Valued Data** by Yingyan Zeng, Yujing (Zipan) Huang, and Xiaoyu
Chen. The pinned paper record is [arXiv:2602.07252](https://arxiv.org/abs/2602.07252),
also listed as ICML 2026 / PMLR 306 in the repository's source metadata.

## Pinned inputs

| Input | SHA-256 | Role |
| --- | --- | --- |
| `paper_source/source.tar` | `6d4af865d403a1c4f72ed3ef8057069212ac1633aa79410b4607b04a8b9edb87` | Retained arXiv source archive |
| `paper_source/main0.tex` | `7c88af0f1ccb66458f0b396331bdee3b5aed26c1b041730e891900f38a5591f6` | Exact TeX used for theorem and claim wording audits |
| Official implementation | `c5b1db4060e5081e5c487f91792dc18c17603fd0` | [`yyzeng43/IDD-icml`](https://github.com/yyzeng43/IDD-icml/tree/c5b1db4060e5081e5c487f91792dc18c17603fd0) |

The audit does not silently replace the pinned source with a later paper or
an unpinned upstream checkout. Source tables, theorem text, appendix metrics,
and availability statements are retained in `outputs/`, `evidence/`, and
`paper_source/`.

## Important source boundaries

- The R/`funcharts` performance path is not available in the public release.
- FlowCAP-II files, labels, preprocessing, and an executable source-faithful
  runner are not present in the pinned public artifacts.
- The exact paper-era Reddit embeddings, daily alarms, and baseline outputs are
  not recoverable from the public artifacts.
- Claim 2's empirical-quantile wording must be separated from the fixed-
  threshold theorem and its finite-sample correction.
- Claim 4's printed precision comparison must not be rewritten as an F1
  comparison.
