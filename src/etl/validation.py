"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 02 - Python Analytics

Module     : 03 - ETL

Task       : Data Validation

Author     : Harsh

Description:

Validate extracted datasets before transformation.

====================================================================
"""

import pandas as pd
from src.etl.schema_validation import validate_schema

def validate_dataframe(df, table_name):
    """
    Validate a DataFrame and print quality report.
    """

    print("\n" + "=" * 70)
    print(f"VALIDATION REPORT : {table_name}")
    print("=" * 70)

    # Shape
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    # Missing Values
    missing = df.isnull().sum()

    print("\nMissing Values")

    if missing.sum() == 0:
        print("✅ No Missing Values")
    else:
        print(missing[missing > 0])

    # Duplicate Records
    duplicates = df.duplicated().sum()

    print("\nDuplicate Records")

    if duplicates == 0:
        print("✅ No Duplicate Records")
    else:
        print(f"Duplicate Rows : {duplicates}")

    # Data Types
    print("\nData Types")

    print(df.dtypes)

    # Memory Usage
    memory = df.memory_usage(deep=True).sum() / (1024 * 1024)

    print(f"\nMemory Usage : {memory:.2f} MB")

    print("=" * 70)


def validate_all_tables(datasets):
    """
    Validate all extracted tables.
    """

    for table_name, df in datasets.items():

        validate_dataframe(df, table_name)
        validate_schema(table_name, df)