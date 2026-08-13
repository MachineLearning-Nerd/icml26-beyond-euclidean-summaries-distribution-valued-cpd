# Branch audit

This repository began with OpenResearch-style `orx/` names. The clean names
below preserve each branch's history while making its claim, evidence route,
or release role readable. `main` is the public documentation surface.

| Historical branch | Clean branch | Purpose and evidence scope |
| --- | --- | --- |
| `main` | `main` | Publication surface and cumulative six-claim evidence |
| `orx/frozen-judged-baseline` | `audit/frozen-baseline` | Freeze the previously judged baseline and retain its regression |
| `orx/claim-1-nonzero-mean-centering-control` | `audit/claim-1-centering-control` | Check centering and nonzero-mean controls for the tangent mechanism |
| `orx/claim-1-paper-scale-multivariate-idd` | `audit/claim-1-paper-scale-idd` | Run the `d=5`, 600-distribution mechanism audit |
| `orx/claim-1-durable-evidence-output` | `audit/claim-1-durable-evidence` | Make Claim 1 evidence durable and evaluator-visible |
| `orx/claim-4-primary-flowrepository-acquisition` | `audit/claim-4-primary-flowrepository` | Probe the primary FlowRepository acquisition route |
| `orx/claim-4-stateful-public-api-session` | `audit/claim-4-stateful-api` | Preserve the stateful public API/session availability audit |
| `orx/claim-4-official-full-file-get` | `audit/claim-4-official-file-get` | Test complete official FlowCAP file retrieval |
| `orx/claim-4-official-legacy-download-hosts` | `audit/claim-4-legacy-hosts` | Test official legacy FlowCAP download hosts |
| `orx/claim-4-original-figure-falsification-audit` | `audit/claim-4-figure-falsification` | Audit the original FlowCAP figure and literal metrics |
| `orx/claim-4-dense-marker-checker-and-current-gate` | `audit/claim-4-marker-checker` | Strengthen figure-marker checking and current release gates |
| `orx/claim-4-filled-diamond-morphology-verifier` | `audit/claim-4-diamond-morphology` | Independently verify filled-diamond morphology and falsification scope |
| `orx/claim-5-official-artifact-schema-reconstruction` | `audit/claim-5-official-schema` | Audit official TSV/CSV artifact representations |
| `orx/claim-5-official-comments-only-dataset` | `audit/claim-5-comments-dataset` | Audit the public comments-only dataset route |
| `orx/claim-5-exact-author-text-cleaning` | `audit/claim-5-author-cleaning` | Match the authors' documented Reddit text cleaning |
| `orx/claim-5-all-records-minimum-30-interpretation` | `audit/claim-5-minimum-30` | Test the all-records/minimum-30 interpretation |
| `orx/claim-5-released-minimum-20-protocol` | `audit/claim-5-minimum-20` | Test the released minimum-20 protocol |
| `orx/claim-5-released-split-semantics-falsification` | `audit/claim-5-split-semantics` | Test released split semantics and falsification controls |
| `orx/claim-5-faithful-sbert-pca20-reconstruction` | `audit/claim-5-sbert-pca20` | Reconstruct the faithful SBERT/PCA-20 route |
| `orx/claim-5-cnf-sinkhorn-50-49-reconstruction` | `audit/claim-5-cnf-sinkhorn` | Run the closest 50+49-day CNF/Sinkhorn/MFPCA route |
| `orx/cumulative-release-candidate` | `release/cumulative-candidate` | Assemble cumulative science and publication gates |
| `orx/evaluator-blind-release-red-team` | `release/evaluator-blind-red-team` | Repeat evaluator-blind traversal after red-team review |
| `orx/final-publication-candidate` | `release/final-publication-candidate` | Embed final facts and execute publication gates |
| `orx/hub-metadata-publication-repair` | `integration/hub-metadata-publication-repair` | Repair final Hub metadata and mirror the publication surface |

Branch hygiene after publication:

- 24 public branches remain: `main` plus 23 descriptive audit, release, and
  integration branches;
- every historical `orx/*` ref is removed from GitHub;
- README, report, status, and live logbook links use the clean repository URL;
  historical source/provenance files retain their original identifiers where
  they are evidence of what was audited; and
- all published commits are attributed to `MachineLearning-Nerd` with the
  account's noreply address.
