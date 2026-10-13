"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 02 - Python Analytics

Module     : 03 - ETL
Task       : Multi-Table Data Extraction

Author     : Harsh

Description:

Extract one or more SQL Server tables and return them
as Pandas DataFrames.

====================================================================
"""

from src.database.query_executor import execute_query
from src.etl.validation import validate_all_tables
from src.etl.transform import transform_all_tables
from src.etl.load import save_csv
from src.utils.logger import logger
from src.etl.data_quality import (
    generate_data_quality_report,
    save_quality_report
)

def extract_table(table_name):
    """
    Extract a single table from SQL Server.

    Parameters
    ----------
    table_name : str
        SQL Server table name.

    Returns
    -------
    pandas.DataFrame
    """

    query = f"SELECT * FROM {table_name}"

    return execute_query(query)


def extract_all_tables(table_list):
    """
    Extract multiple SQL Server tables.

    Parameters
    ----------
    table_list : list

    Returns
    -------
    dict
        Dictionary containing DataFrames.
    """

    datasets = {}

    for table in table_list:

        logger.info(f"Extracting table : {table}")

        try:

            df = extract_table(table)

            datasets[table] = df

            logger.info(
                f"{table} extracted successfully "
                f"({df.shape[0]} rows × {df.shape[1]} columns)"
            )

        except Exception as e:

            logger.error(f"Failed to extract table : {table}")

            logger.error(str(e))

    return datasets


if __name__ == "__main__":

    from src.common.constants import TABLES

    logger.info("=" * 70)
    logger.info("STARTING ETL PIPELINE")
    logger.info("=" * 70)

    # -------------------------------
    # Extract
    # -------------------------------

    datasets = extract_all_tables(TABLES)

    logger.info("Data Extraction Completed Successfully.")

    # -------------------------------
    # Validation
    # -------------------------------

    validate_all_tables(datasets)

    logger.info("Data Validation Completed Successfully.")

    # -------------------------------
    # Transformation
    # -------------------------------

    transformed_data = transform_all_tables(datasets)

    logger.info("Data Transformation Completed Successfully.")

    # -------------------------------
    # Load
    # -------------------------------

    save_csv(transformed_data)

    logger.info("Processed CSV files saved successfully.")

    logger.info("=" * 70)
    logger.info("ETL PIPELINE COMPLETED SUCCESSFULLY")
    logger.info("=" * 70)

    quality = generate_data_quality_report(transformed_data)

    save_quality_report(quality)

    logger.info("Data Quality Report Generated.")