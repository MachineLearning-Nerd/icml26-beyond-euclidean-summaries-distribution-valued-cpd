# Environment and reproduction contract

## Fixed command

```bash
uv sync --frozen
uv run --frozen python scripts/run_campaign.py
```

The lockfile and the existing campaign logs are authoritative for the
scientific evidence. This documentation pass records those outputs and does
not silently replace them with a new untracked run.

## Runtime boundary

- Runs were designed for CPU-only execution.
- No Hugging Face Job, model, dataset, or Bucket was used for the campaign.
- The complete released R/`funcharts` monitoring path was unavailable.
- FlowCAP-II and paper-era Reddit artifacts required for source-faithful
  numeric reruns were unavailable.

## Evidence layout

- `src/` contains executable claim audits.
- `tests/` contains focused contract and claim checks.
- `outputs/` contains raw results, logs, hashes, and availability audits.
- `evidence/` contains retained official-source downloads and provenance.
- `logbook/` contains the evaluator-facing claim pages and conclusion.
- `branch-audit.md` maps every clean branch to its historical role.

The claims are therefore reproducible as scoped audits under the recorded
inputs, but Claims 3–5 are not presented as a complete end-to-end rerun of
every paper experiment.
