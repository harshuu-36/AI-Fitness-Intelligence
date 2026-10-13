"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 03 - Exploratory Data Analysis (EDA)

Module     : Visualization

Author     : Harsh

Description:

Generate professional visualizations for numerical
and categorical variables and save them automatically.

====================================================================
"""

import matplotlib.pyplot as plt

from src.common.paths import EDA_REPORTS
from src.utils.logger import logger


def plot_histograms(datasets):
    """
    Generate histogram for all numeric columns.
    """

    logger.info("=" * 70)
    logger.info("GENERATING HISTOGRAMS")
    logger.info("=" * 70)

    for table_name, df in datasets.items():

        numeric_columns = df.select_dtypes(include="number").columns

        for column in numeric_columns:

            try:

                plt.figure(figsize=(8, 5))

                plt.hist(
                    df[column].dropna(),
                    bins=30
                )

                plt.title(f"{table_name} - {column}")

                plt.xlabel(column)

                plt.ylabel("Frequency")

                plt.tight_layout()

                file_path = EDA_REPORTS / f"{table_name}_{column}_histogram.png"

                plt.savefig(file_path)

                plt.close()

                logger.info(f"Saved Histogram : {file_path.name}")

            except Exception as e:

                logger.error(
                    f"Histogram generation failed "
                    f"for {table_name}.{column}: {e}"
                )


def plot_boxplots(datasets):
    """
    Generate boxplots for all numeric columns.
    """

    logger.info("=" * 70)
    logger.info("GENERATING BOXPLOTS")
    logger.info("=" * 70)

    for table_name, df in datasets.items():

        numeric_columns = df.select_dtypes(include="number").columns

        for column in numeric_columns:

            try:

                plt.figure(figsize=(6, 5))

                plt.boxplot(df[column].dropna())

                plt.title(f"{table_name} - {column}")

                plt.ylabel(column)

                plt.tight_layout()

                file_path = EDA_REPORTS / f"{table_name}_{column}_boxplot.png"

                plt.savefig(file_path)

                plt.close()

                logger.info(f"Saved Boxplot : {file_path.name}")

            except Exception as e:

                logger.error(
                    f"Boxplot generation failed "
                    f"for {table_name}.{column}: {e}"
                )


def plot_bar_chart(df, column, table_name):
    """
    Generate bar chart for categorical columns.
    """

    try:

        plt.figure(figsize=(8, 5))

        df[column].value_counts().plot(kind="bar")

        plt.title(f"{table_name} - {column}")

        plt.xlabel(column)

        plt.ylabel("Count")

        plt.tight_layout()

        file_path = EDA_REPORTS / f"{table_name}_{column}_bar_chart.png"

        plt.savefig(file_path)

        plt.close()

        logger.info(f"Saved Bar Chart : {file_path.name}")

    except Exception as e:

        logger.error(
            f"Bar chart generation failed "
            f"for {table_name}.{column}: {e}"
        )


def plot_all_categorical(datasets):
    """
    Generate bar charts for all categorical columns.
    """

    logger.info("=" * 70)
    logger.info("GENERATING BAR CHARTS")
    logger.info("=" * 70)

    for table_name, df in datasets.items():

        categorical_columns = df.select_dtypes(
            include=["object", "category"]
        ).columns

        for column in categorical_columns:

            plot_bar_chart(df, column, table_name)

    logger.info("Categorical charts generated successfully.")