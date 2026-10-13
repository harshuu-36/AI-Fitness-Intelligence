"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 03 - Exploratory Data Analysis

Module     : Correlation Analysis

Author     : Harsh

Description:

Generate correlation matrices and identify
top positive and negative correlations.

====================================================================
"""

import matplotlib.pyplot as plt
import pandas as pd

from src.common.paths import EDA_REPORTS
from src.utils.logger import logger


def correlation_matrix(df, table_name):
    """
    Generate correlation matrix and save as CSV.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:

        logger.warning(
            f"{table_name}: Not enough numeric columns."
        )

        return

    corr = numeric_df.corr()

    csv_path = EDA_REPORTS / f"{table_name}_correlation.csv"

    corr.to_csv(csv_path)

    logger.info(f"Saved Correlation CSV : {csv_path.name}")

    plt.figure(figsize=(10,8))

    plt.imshow(corr)

    plt.xticks(
        range(len(corr.columns)),
        corr.columns,
        rotation=90
    )

    plt.yticks(
        range(len(corr.columns)),
        corr.columns
    )

    plt.colorbar()

    plt.title(f"{table_name} Correlation Matrix")

    plt.tight_layout()

    image_path = (
        EDA_REPORTS /
        f"{table_name}_correlation_heatmap.png"
    )

    plt.savefig(image_path)

    plt.close()

    logger.info(
        f"Saved Correlation Heatmap : {image_path.name}"
    )

    return corr


def top_correlations(corr, table_name):

    """
    Display strongest positive and negative correlations.
    """

    corr_pairs = (
        corr.unstack()
        .sort_values(kind="quicksort")
    )

    corr_pairs = corr_pairs[
        corr_pairs != 1
    ]

    positive = corr_pairs.tail(10)

    negative = corr_pairs.head(10)

    positive.to_csv(
        EDA_REPORTS /
        f"{table_name}_top_positive.csv"
    )

    negative.to_csv(
        EDA_REPORTS /
        f"{table_name}_top_negative.csv"
    )

    logger.info(
        f"{table_name}: Top correlations saved."
    )


def analyze_all_correlations(datasets):

    logger.info("=" * 70)
    logger.info("STARTING CORRELATION ANALYSIS")
    logger.info("=" * 70)

    for table_name, df in datasets.items():

        corr = correlation_matrix(df, table_name)

        if corr is not None:

            top_correlations(
                corr,
                table_name
            )

    logger.info("=" * 70)
    logger.info("CORRELATION ANALYSIS COMPLETED")
    logger.info("=" * 70)