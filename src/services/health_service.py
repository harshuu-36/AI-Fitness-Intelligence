"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Health Service

Author     : Harsh

Description:

Business logic for Health Dashboard APIs.

==============================================================
"""

from src.repository.user_repository import UserRepository
from src.repository.progress_repository import ProgressRepository
from src.repository.workout_repository import WorkoutRepository
from src.repository.sleep_repository import SleepRepository
from src.repository.meal_repository import MealRepository

from src.exceptions.custom_exceptions import (
    HealthDataNotFoundException,
    DatabaseException
)

from src.utils.logger import logger


class HealthService:

    def __init__(self):

        self.user_repository = UserRepository()

        self.progress_repository = ProgressRepository()

        self.workout_repository = WorkoutRepository()

        self.sleep_repository = SleepRepository()

        self.meal_repository = MealRepository()

    # ==========================================================
    # Health Dashboard
    # ==========================================================

    def get_health_dashboard(
        self,
        user_id: int
    ):

        try:

            logger.info(
                f"Generating Health Dashboard for UserID={user_id}"
            )

            # --------------------------------------------------
            # User
            # --------------------------------------------------

            user = self.user_repository.get_user_by_id(
                user_id
            )

            if user.empty:

                raise HealthDataNotFoundException(
                    f"User ID {user_id} not found."
                )

            # --------------------------------------------------
            # Latest Progress
            # --------------------------------------------------

            latest_progress = (
                self.progress_repository.get_latest_progress(
                    user_id
                )
            )

            # --------------------------------------------------
            # Latest Workout
            # --------------------------------------------------

            latest_workout = (
                self.workout_repository.get_latest_workout(
                    user_id
                )
            )

            # --------------------------------------------------
            # Latest Sleep
            # --------------------------------------------------

            latest_sleep = (
                self.sleep_repository.get_latest_sleep(
                    user_id
                )
            )

            # --------------------------------------------------
            # Meal History
            # --------------------------------------------------

            meal_history = (
                self.meal_repository.get_meals_by_user(
                    user_id=user_id,
                    skip=0,
                    limit=100
                )
            )

            dashboard = {

                "user": user.to_dict(
                    orient="records"
                ),

                "latest_progress": latest_progress.to_dict(
                    orient="records"
                ),

                "latest_workout": latest_workout.to_dict(
                    orient="records"
                ),

                "latest_sleep": latest_sleep.to_dict(
                    orient="records"
                ),

                "meal_history": meal_history.to_dict(
                    orient="records"
                )

            }

            logger.info(
                f"Health Dashboard generated successfully for UserID={user_id}"
            )

            return dashboard

        except HealthDataNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to generate Health Dashboard."
            )

            raise DatabaseException(
                str(e)
            )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    service = HealthService()

    result = service.get_health_dashboard(
        1
    )

    print("\n========== HEALTH DASHBOARD ==========\n")

    for key, value in result.items():

        print(f"{key}:\n{value}\n")