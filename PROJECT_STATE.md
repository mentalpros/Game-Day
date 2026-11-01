# CFB Quant Engine — Project State

## Current milestone
Environment foundation.

## Repository
/workspaces/Game-Day

## Runtime
Python 3.12 managed by uv.
Dependency versions are resolved in uv.lock.

## Target architecture
- CFBD data ingestion and schema validation.
- Point-in-time historical feature generation.
- Dynamic state-space team ratings.
- XGBoost margin and total models.
- Chronological ensemble calibration.
- Expanding-window walk-forward backtesting.
- Predictive uncertainty and score projections.
- Timestamp-aware market-line evaluation.

## Historical scope
2018–2025, initially regular season.
2026 is the current-season update and prediction period.

## Data safety
Raw data, processed data, model artifacts, and secrets must not be committed.
CFBD_API_KEY must be stored as an environment secret or entered securely.

## Critical integrity requirement
Predictions must be generated before game outcomes update team states.
Games sharing a kickoff timestamp must be predicted as a batch.

## Reconstruction notice
The original server source is unavailable.
This project is a controlled reconstruction of the documented design,
not a byte-for-byte restoration of the previous source.

## Current limitations
The model modules and data-ingestion modules have not yet been implemented.
No predictive performance or profitability has been established.
