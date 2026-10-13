"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : Database Layer

Module     : Database Query Executor

Author     : Harsh

Description:

Executes SQL queries and returns results as
Pandas DataFrames.

====================================================================
"""

import pandas as pd

from src.database.connection import get_connection
from src.utils.logger import logger


# ==========================================================
# Execute SELECT Query
# ==========================================================

def execute_query(query: str) -> pd.DataFrame:
    """
    Execute SELECT query and return DataFrame.
    """

    if not query.strip():

        raise ValueError(
            "SQL query cannot be empty."
        )

    connection = None

    try:

        logger.info(
            "Executing SELECT query..."
        )

        connection = get_connection()

        df = pd.read_sql(
            query,
            connection
        )

        logger.info(
            f"SELECT executed successfully "
            f"({len(df)} rows returned)."
        )

        return df

    except Exception:

        logger.exception(
            "Failed to execute SELECT query."
        )

        raise

    finally:

        if connection:

            connection.close()

            logger.info(
                "Database connection closed."
            )


# ==========================================================
# Execute INSERT / UPDATE / DELETE
# ==========================================================

def execute_non_query(query: str):
    """
    Execute INSERT, UPDATE or DELETE query.
    """

    if not query.strip():

        raise ValueError(
            "SQL query cannot be empty."
        )

    connection = None
    cursor = None

    try:

        logger.info(
            "Executing NON-SELECT query..."
        )

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(query)

        connection.commit()

        logger.info(
            "Query executed successfully."
        )

    except Exception:

        if connection:

            connection.rollback()

        logger.exception(
            "Failed to execute NON-SELECT query."
        )

        raise

    finally:

        if cursor:

            cursor.close()

        if connection:

            connection.close()

            logger.info(
                "Database connection closed."
            )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    TEST_QUERY = """

    SELECT TOP 10 *

    FROM Users

    """

    df = execute_query(
        TEST_QUERY
    )

    print(df)