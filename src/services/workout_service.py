"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Workout Service

Author     : Harsh

Description:

Business logic for Workout APIs.

==============================================================
"""

from src.repository.workout_repository import WorkoutRepository

from src.exceptions.custom_exceptions import (
    DatabaseException,
    UserNotFoundException
)

from src.utils.logger import logger


class WorkoutService:

    def __init__(self):

        self.repository = WorkoutRepository()

    # ==========================================================
    # Get All Workouts
    # ==========================================================

    def get_all_workouts(
        self,
        skip: int = 0,
        limit: int = 100
    ):

        try:

            data = self.repository.get_all_workouts(
                skip,
                limit
            )

            if data.empty:

                raise UserNotFoundException(
                    "No workouts found."
                )

            return data

        except UserNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch workouts."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Get Workout By ID
    # ==========================================================

    def get_workout_by_id(
        self,
        workout_id: int
    ):

        try:

            data = self.repository.get_workout_by_id(
                workout_id
            )

            if data.empty:

                raise UserNotFoundException(
                    f"Workout {workout_id} not found."
                )

            return data

        except UserNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch workout."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Create Workout
    # ==========================================================

    def create_workout(
        self,
        workout_data: dict
    ):

        try:

            self.repository.create_workout(
                workout_data
            )

            return {
                "message": "Workout created successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to create workout."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Update Workout
    # ==========================================================

    def update_workout(
        self,
        workout_id: int,
        workout_data: dict
    ):

        try:

            self.repository.update_workout(
                workout_id,
                workout_data
            )

            return {
                "message": "Workout updated successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to update workout."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Delete Workout
    # ==========================================================

    def delete_workout(
        self,
        workout_id: int
    ):

        try:

            self.repository.delete_workout(
                workout_id
            )

            return {
                "message": "Workout deleted successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to delete workout."
            )

            raise DatabaseException(
                str(e)
            )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    service = WorkoutService()

    print("\n========== ALL WORKOUTS ==========\n")

    print(
        service.get_all_workouts(
            skip=0,
            limit=10
        )
    )

    print("\n========== WORKOUT 1 ==========\n")

    print(
        service.get_workout_by_id(1)
    )