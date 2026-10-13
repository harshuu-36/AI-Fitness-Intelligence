"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : Repository Layer

Module     : Sleep Repository

Author     : Harsh

Description:

Database operations for the Sleep table.

====================================================================
"""

import pandas as pd

from src.database.query_executor import execute_query
from src.utils.logger import logger


class SleepRepository:
    """
    Repository for Sleep table.
    """

    @staticmethod
    def get_all_sleep(
        skip: int = 0,
        limit: int = 100
    ) -> pd.DataFrame:

        query = f"""
        SELECT
            SleepID,
            UserID,
            SleepDate,
            SleepStart,
            SleepEnd,
            DurationMinutes,
            SleepQuality
        FROM Sleep
        ORDER BY SleepDate DESC
        OFFSET {skip} ROWS
        FETCH NEXT {limit} ROWS ONLY;
        """

        logger.info(f"Fetching sleep records (skip={skip}, limit={limit})")

        return execute_query(query)

    @staticmethod
    def get_sleep_by_user(user_id: int) -> pd.DataFrame:
        """
        Fetch sleep records for a specific user.
        """

        query = f"""
        SELECT
            SleepID,
            UserID,
            SleepDate,
            SleepStart,
            SleepEnd,
            DurationMinutes,
            SleepQuality
        FROM Sleep
        WHERE UserID = {user_id}
        ORDER BY SleepDate DESC;
        """

        logger.info(f"Fetching sleep records for UserID={user_id}")

        return execute_query(query)

    @staticmethod
    def get_latest_sleep(user_id: int) -> pd.DataFrame:
        """
        Fetch the latest sleep record of a user.
        """

        query = f"""
        SELECT TOP 1
            SleepID,
            UserID,
            SleepDate,
            SleepStart,
            SleepEnd,
            DurationMinutes,
            SleepQuality
        FROM Sleep
        WHERE UserID = {user_id}
        ORDER BY SleepDate DESC;
        """

        logger.info(f"Fetching latest sleep record for UserID={user_id}")

        return execute_query(query)


if __name__ == "__main__":

    repo = SleepRepository()

    print("\n========== ALL SLEEP RECORDS ==========\n")

    print(repo.get_all_sleep().head())

    print("\n========== USER 1 SLEEP ==========\n")

    print(repo.get_sleep_by_user(1).head())

    print("\n========== LATEST SLEEP ==========\n")

    print(repo.get_latest_sleep(1))