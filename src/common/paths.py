"""
====================================================================

Project    : AI Fitness Intelligence Platform

Module     : Common Paths

Author     : Harsh

Description:

Centralized project paths.

====================================================================
"""

from pathlib import Path

# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ==========================================================
# Artifacts
# ==========================================================

ARTIFACTS = PROJECT_ROOT / "artifacts"

PROCESSED_DATA = ARTIFACTS / "processed_data"

EDA_REPORTS = ARTIFACTS / "eda_reports"

ML_MODELS = ARTIFACTS / "models"

LOGS = ARTIFACTS / "logs"

PREDICTIONS = ARTIFACTS / "predictions"

REPORTS = ARTIFACTS / "reports"

# ==========================================================
# Data
# ==========================================================

DATA = PROJECT_ROOT / "data"

RAW_DATA = DATA / "raw"

PROCESSED_DATASET = DATA / "processed"

# ==========================================================
# Create folders automatically
# ==========================================================

for folder in [

    ARTIFACTS,

    PROCESSED_DATA,

    EDA_REPORTS,

    ML_MODELS,

    LOGS,

    PREDICTIONS,

    REPORTS,

    RAW_DATA,

    PROCESSED_DATASET

]:
    folder.mkdir(
        parents=True,
        exist_ok=True
    )