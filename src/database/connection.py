"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : Database Layer

Module     : SQL Server Connection

Author     : Harsh

Description:

Creates a reusable SQL Server database connection using
environment variables stored in the .env file.

====================================================================
"""

import pyodbc

from configs.config import (
    DB_SERVER,
    DB_DATABASE,
    DB_AUTH
)

from src.utils.logger import logger


def get_connection() -> pyodbc.Connection:
    """
    Create and return SQL Server connection.
    """

    try:

        if DB_AUTH.strip().lower() == "windows":

            connection_string = (
                "DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={DB_SERVER};"
                f"DATABASE={DB_DATABASE};"
                "Trusted_Connection=yes;"
            )

        else:

            raise ValueError(
                f"Unsupported authentication type: {DB_AUTH}"
            )

        connection = pyodbc.connect(
            connection_string,
            timeout=10
        )

        logger.info(
            "Connected to SQL Server successfully."
        )

        return connection

    except pyodbc.Error as e:

        logger.exception(
            f"Database connection failed: {e}"
        )

        raise

    except Exception:

        logger.exception(
            "Unexpected error while connecting to SQL Server."
        )

        raise


if __name__ == "__main__":

    try:

        conn = get_connection()

        print("\n✅ Database Connection Successful")

        conn.close()

        print("✅ Connection Closed")

    except Exception as e:

        print(f"\n❌ {e}")