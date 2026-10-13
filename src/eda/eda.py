"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 03 - Exploratory Data Analysis

Module     : Basic EDA

Author     : Harsh

Description:

Perform basic exploratory data analysis on datasets.

====================================================================
"""

from src.utils.logger import logger


def dataset_summary(datasets):
    """
    Display summary statistics for all datasets.
    """

    logger.info("=" * 70)
    logger.info("DATASET SUMMARY")
    logger.info("=" * 70)

    for table_name, df in datasets.items():

        logger.info(f"\nTable : {table_name}")

        logger.info(f"Shape : {df.shape}")

        logger.info(f"\nColumns:\n{list(df.columns)}")

        logger.info(f"\nData Types:\n{df.dtypes}")

        logger.info(f"\nSummary Statistics:\n{df.describe(include='all')}")