# Status

## Overall verdict

`MIXED_C1_SCOPED_VERIFIED_C2_LITERAL_FALSIFIED_C3_SOURCE_TABLE_FALSIFIED_C4_LITERAL_SOURCE_SCOPE_FALSIFIED_C5_BLOCKED_C6_SCOPED_VERIFIED`

| Gate | Value |
| --- | --- |
| Current score claim | `false` |
| Publication allowed | `false` |
| Official author endorsement | `false` |
| Historical live judge | `7/12`, archived only |

The verdicts are scoped to the exact claim and evidence path. A falsified
literal or source-scope statement does not establish that the broader IDD
method fails; a blocked claim means that source-faithful evidence was not
available and no proxy was promoted to a full reproduction.

- OpenReview ID: aU2sxdnRuL
- Submission number: 30280
- Live claim count / maximum points: 6 / 12
- Selection timestamp: 2026-07-30T06:51:28Z
- Contract manifest: contract/contract_manifest.json
- Paper: https://arxiv.org/abs/2602.07252
- Official code pin: https://github.com/yyzeng43/IDD-icml@c5b1db4060e5081e5c487f91792dc18c17603fd0
- Compute policy: CPU only; no GPU or paid Jobs used.
- GitHub repository: https://github.com/MachineLearning-Nerd/icml26-beyond-euclidean-summaries-distribution-valued-cpd
- Current phase: publication_ready_for_publish
- Claim 1: verified as a scoped paper-scale multivariate mechanism audit; the released R/funcharts performance path remains unavailable.
- Claim 2: falsified as literally written; empirical-quantile correction omitted from the live wording.
- Claim 3: falsified for literal source-table scope; maximum reported high-variance reduction is 72.5%, not 95%.
- Claim 4: falsified for literal source metric scope; Hotelling precision, not F1, is below 0.4.
- Claim 5: inconclusive; source supports post-pause alignment but released artifacts do not permit an independent numeric rerun.
- Claim 6: verified only as a scoped finite-dimensional theorem/algebra audit.
- Historical publication queue event: `publication_queued` — 2026-07-30 Trackio publish to the shortened target hit HF HTTP 429 Space-creation quota after trace/bucket uploads may have succeeded. The failed attempt is retained in `outputs/trackio_publish_short_target.log`; local validation passed in `outputs/official_validator_publish_target.log`.
- Publication status: `published` — 2026-07-31T08:31:43Z. Public logbook: https://huggingface.co/spaces/DineshAI/repro-aU2sxdnRuL-distribution-valued-cpd ; rendered: https://dineshai-repro-au2sxdnrul-distribution-valued-cpd.static.hf.space/ . Anonymous Space API readback: public, tag `paper-aU2sxdnRuL`, Space SHA `881cb4f9cda9250f4bb1394b7cee539825ac6ac7`; all Index, Executive summary, Claim 1–6, Conclusion pages and public GitHub link were fetched/read back. Trace dataset authenticated readback SHA: `25681740ba2c4d353f265bcf9a54de065f9d3e5e`. Points remain unclaimed pending official judge/leaderboard.
