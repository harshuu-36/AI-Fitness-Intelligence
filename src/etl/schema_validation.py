"""
====================================================================

Schema Validation

====================================================================
"""

from configs.schema import EXPECTED_SCHEMAS
from src.utils.logger import logger


def validate_schema(table_name, df):
    """
    Validate dataframe schema.
    """

    expected = EXPECTED_SCHEMAS.get(table_name)

    if expected is None:

        logger.warning(f"No schema defined for {table_name}")

        return

    actual = list(df.columns)

    missing = list(set(expected) - set(actual))

    extra = list(set(actual) - set(expected))

    if not missing and not extra:

        logger.info(f"{table_name} schema validation passed.")

    else:

        if missing:

            logger.error(
                f"{table_name} Missing Columns : {missing}"
            )

        if extra:

            logger.warning(
                f"{table_name} Extra Columns : {extra}"
            )