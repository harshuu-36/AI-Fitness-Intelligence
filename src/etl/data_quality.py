"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 02 - Python Analytics

Module     : 06 - Data Quality Report

Author     : Harsh

Description:

Generate a Data Quality Report for all extracted datasets.

====================================================================
"""

import pandas as pd

from src.utils.logger import logger


def generate_data_quality_report(datasets):
    """
    Generate Data Quality Report.
    """

    report = []

    for table_name, df in datasets.items():

        rows = df.shape[0]

        columns = df.shape[1]

        missing = df.isnull().sum().sum()

        duplicate = df.duplicated().sum()

        memory = round(
            df.memory_usage(deep=True).sum() / 1024 / 1024,
            2
        )

        report.append({

            "Table": table_name,

            "Rows": rows,

            "Columns": columns,

            "Missing Values": missing,

            "Duplicate Rows": duplicate,

            "Memory (MB)": memory

        })

    quality_report = pd.DataFrame(report)

    return quality_report


def save_quality_report(report):

    output = "artifacts/data_quality_report.csv"

    report.to_csv(output, index=False)

    logger.info("Data Quality Report Saved Successfully.")