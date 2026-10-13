"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 02 - Python Analytics

Module     : 03 - ETL

Task       : Load Processed Data

Author     : Harsh

Description:

Save transformed datasets into CSV files.

====================================================================
"""

from src.common.paths import PROCESSED_DATA
from src.utils.logger import logger


def save_csv(datasets):
    """
    Save all transformed datasets as CSV files.

    Parameters
    ----------
    datasets : dict
        Dictionary containing transformed pandas DataFrames.
    """

    logger.info("=" * 70)
    logger.info("STARTING DATA LOADING")
    logger.info("=" * 70)

    try:

        for table_name, df in datasets.items():

            file_path = PROCESSED_DATA / f"{table_name}.csv"

            df.to_csv(file_path, index=False)

            logger.info(
                f"{table_name}.csv saved successfully "
                f"({df.shape[0]} rows × {df.shape[1]} columns)"
            )

        logger.info("=" * 70)
        logger.info("ALL DATASETS SAVED SUCCESSFULLY")
        logger.info("=" * 70)

    except Exception as e:

        logger.error(f"Failed to save datasets: {e}")

        raise