"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Sleep Service

Author     : Harsh

Description:

Business logic for Sleep APIs.

==============================================================
"""

from src.repository.sleep_repository import SleepRepository

from src.exceptions.custom_exceptions import (
    SleepNotFoundException,
    DatabaseException
)

from src.utils.logger import logger


class SleepService:

    def __init__(self):

        self.repository = SleepRepository()

    # ==========================================================
    # Get All Sleep Records
    # ==========================================================

    def get_all_sleep(
        self,
        skip: int = 0,
        limit: int = 100
    ):

        try:

            data = self.repository.get_all_sleep(
                skip,
                limit
            )

            if data.empty:

                raise SleepNotFoundException(
                    "No sleep records found."
                )

            return data

        except SleepNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch sleep records."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Get Sleep By User
    # ==========================================================

    def get_sleep_by_user(
        self,
        user_id: int
    ):

        try:

            data = self.repository.get_sleep_by_user(
                user_id
            )

            if data.empty:

                raise SleepNotFoundException(
                    f"No sleep records found for User ID {user_id}."
                )

            return data

        except SleepNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch sleep records by user."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Get Latest Sleep
    # ==========================================================

    def get_latest_sleep(
        self,
        user_id: int
    ):

        try:

            data = self.repository.get_latest_sleep(
                user_id
            )

            if data.empty:

                raise SleepNotFoundException(
                    f"No latest sleep record found for User ID {user_id}."
                )

            return data

        except SleepNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch latest sleep record."
            )

            raise DatabaseException(
                str(e)
            )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    service = SleepService()

    print("\n========== ALL SLEEP RECORDS ==========\n")

    print(
        service.get_all_sleep(
            skip=0,
            limit=100
        ).head()
    )

    print("\n========== USER 1 SLEEP ==========\n")

    print(
        service.get_sleep_by_user(
            1
        ).head()
    )

    print("\n========== LATEST SLEEP ==========\n")

    print(
        service.get_latest_sleep(
            1
        )
    )