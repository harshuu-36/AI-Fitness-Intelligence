"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : Repository Layer

Module     : Progress Repository

Author     : Harsh

Description:

Database operations for the DailyProgress table.

====================================================================
"""

import pandas as pd

from src.database.query_executor import execute_query
from src.utils.logger import logger


class ProgressRepository:
    """
    Repository for DailyProgress table.
    """

    # ==========================================================
    # Get All Progress
    # ==========================================================

    @staticmethod
    def get_all_progress(
        skip: int = 0,
        limit: int = 100
    ) -> pd.DataFrame:

        query = f"""
        SELECT
            ProgressID,
            UserID,
            ProgressDate,
            WeightKG
        FROM DailyProgress
        ORDER BY ProgressDate DESC
        OFFSET {skip} ROWS
        FETCH NEXT {limit} ROWS ONLY;
        """

        logger.info(
            f"Fetching all progress (skip={skip}, limit={limit})"
        )

        return execute_query(query)

    # ==========================================================
    # Get Progress By User
    # ==========================================================

    @staticmethod
    def get_progress_by_user(
        user_id: int,
        skip: int = 0,
        limit: int = 100
    ) -> pd.DataFrame:

        query = f"""
        SELECT
            ProgressID,
            UserID,
            ProgressDate,
            WeightKG
        FROM DailyProgress
        WHERE UserID = {user_id}
        ORDER BY ProgressDate DESC
        OFFSET {skip} ROWS
        FETCH NEXT {limit} ROWS ONLY;
        """

        logger.info(
            f"Fetching progress for UserID={user_id}"
        )

        return execute_query(query)

    # ==========================================================
    # Get Latest Progress
    # ==========================================================

    @staticmethod
    def get_latest_progress(
        user_id: int
    ) -> pd.DataFrame:

        query = f"""
        SELECT TOP 1
            ProgressID,
            UserID,
            ProgressDate,
            WeightKG
        FROM DailyProgress
        WHERE UserID = {user_id}
        ORDER BY ProgressDate DESC;
        """

        logger.info(
            f"Fetching latest progress for UserID={user_id}"
        )

        return execute_query(query)


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    repo = ProgressRepository()

    print("\n========== ALL PROGRESS ==========\n")

    print(
        repo.get_all_progress(
            skip=0,
            limit=10
        ).head()
    )

    print("\n========== USER 1 PROGRESS ==========\n")

    print(
        repo.get_progress_by_user(
            1,
            skip=0,
            limit=10
        ).head()
    )

    print("\n========== LATEST PROGRESS ==========\n")

    print(
        repo.get_latest_progress(1)
    )