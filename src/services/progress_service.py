"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Progress Service

Author     : Harsh

Description:

Business logic for Progress APIs.

==============================================================
"""

from src.repository.progress_repository import ProgressRepository

from src.exceptions.custom_exceptions import (
    ProgressNotFoundException,
    DatabaseException
)

from src.utils.logger import logger


class ProgressService:

    def __init__(self):

        self.repository = ProgressRepository()

    # ==========================================================
    # Get All Progress Records
    # ==========================================================

    def get_all_progress(
        self,
        skip: int = 0,
        limit: int = 100
    ):

        try:

            data = self.repository.get_all_progress(
                skip,
                limit
            )

            if data.empty:

                raise ProgressNotFoundException(
                    "No progress records found."
                )

            return data

        except ProgressNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch progress records."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Get Progress By User
    # ==========================================================

    def get_progress_by_user(
        self,
        user_id: int,
        skip: int = 0,
        limit: int = 100
    ):

        try:

            data = self.repository.get_progress_by_user(
                user_id,
                skip,
                limit
            )

            if data.empty:

                raise ProgressNotFoundException(
                    f"No progress records found for User ID {user_id}."
                )

            return data

        except ProgressNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch progress records by user."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Get Latest Progress
    # ==========================================================

    def get_latest_progress(
        self,
        user_id: int
    ):

        try:

            data = self.repository.get_latest_progress(
                user_id
            )

            if data.empty:

                raise ProgressNotFoundException(
                    f"No latest progress record found for User ID {user_id}."
                )

            return data

        except ProgressNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch latest progress record."
            )

            raise DatabaseException(
                str(e)
            )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    service = ProgressService()

    print("\n========== ALL PROGRESS RECORDS ==========\n")

    print(
        service.get_all_progress(
            skip=0,
            limit=10
        ).head()
    )