"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 03 - Exploratory Data Analysis (EDA)

Module     : EDA Runner

Author     : Harsh

Description:

Run the complete EDA pipeline:
1. Extract Data
2. Transform Data
3. Dataset Summary
4. Generate Visualizations
5. Correlation Analysis
6. Create Master Dataset

====================================================================
"""

from src.common.constants import TABLES

from src.etl.extract import extract_all_tables
from src.etl.transform import transform_all_tables

from src.eda.eda import dataset_summary
from src.eda.visualization import (
    plot_histograms,
    plot_boxplots,
    plot_all_categorical
)
from src.eda.correlation import analyze_all_correlations

from src.analytics.master_dataset import create_master_dataset

from src.utils.logger import logger


def run_eda():

    logger.info("=" * 70)
    logger.info("STARTING EDA PIPELINE")
    logger.info("=" * 70)

    # --------------------------------------------------
    # Extract Data
    # --------------------------------------------------

    datasets = extract_all_tables(TABLES)

    # --------------------------------------------------
    # Transform Data
    # --------------------------------------------------

    datasets = transform_all_tables(datasets)

    # --------------------------------------------------
    # Dataset Summary
    # --------------------------------------------------

    dataset_summary(datasets)

    # --------------------------------------------------
    # Visualizations
    # --------------------------------------------------

    plot_histograms(datasets)

    plot_boxplots(datasets)

    plot_all_categorical(datasets)

    # --------------------------------------------------
    # Correlation Analysis
    # --------------------------------------------------

    analyze_all_correlations(datasets)

    # --------------------------------------------------
    # Master Dataset
    # --------------------------------------------------

    master_dataset = create_master_dataset(datasets)

    logger.info("=" * 70)
    logger.info("MASTER DATASET PREVIEW")
    logger.info("=" * 70)

    print(master_dataset.head())

    logger.info(f"Master Dataset Shape : {master_dataset.shape}")

    logger.info("=" * 70)
    logger.info("EDA PIPELINE COMPLETED SUCCESSFULLY")
    logger.info("=" * 70)


if __name__ == "__main__":

    run_eda()