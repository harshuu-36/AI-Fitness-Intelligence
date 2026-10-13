"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Meal Service

Author     : Harsh

Description:

Business logic for Meal APIs.

==============================================================
"""

from src.repository.meal_repository import MealRepository

from src.exceptions.custom_exceptions import (
    MealNotFoundException,
    DatabaseException
)

from src.utils.logger import logger


class MealService:

    def __init__(self):

        self.repository = MealRepository()

    # ==========================================================
    # Get All Meals
    # ==========================================================

    def get_all_meals(
        self,
        skip: int = 0,
        limit: int = 100
    ):

        try:

            data = self.repository.get_all_meals(
                skip,
                limit
            )

            if data.empty:

                raise MealNotFoundException(
                    "No meal records found."
                )

            return data

        except MealNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch meal records."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Get Meals By User
    # ==========================================================

    def get_meals_by_user(
        self,
        user_id: int,
        skip: int = 0,
        limit: int = 100
    ):

        try:

            data = self.repository.get_meals_by_user(
                user_id,
                skip,
                limit
            )

            if data.empty:

                raise MealNotFoundException(
                    f"No meals found for User ID {user_id}."
                )

            return data

        except MealNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch meals by user."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Get Daily Calories
    # ==========================================================

    def get_daily_calories(
        self,
        user_id: int,
        meal_date: str
    ):

        try:

            data = self.repository.get_daily_calories(
                user_id,
                meal_date
            )

            if data.empty:

                raise MealNotFoundException(
                    f"No meal records found for User ID {user_id} on {meal_date}."
                )

            return data

        except MealNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch daily calories."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Create Meal
    # ==========================================================

    def create_meal(
        self,
        meal_data: dict
    ):

        try:

            self.repository.create_meal(
                meal_data
            )

            return {
                "message": "Meal created successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to create meal."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Update Meal
    # ==========================================================

    def update_meal(
        self,
        meal_id: int,
        meal_data: dict
    ):

        try:

            self.repository.update_meal(
                meal_id,
                meal_data
            )

            return {
                "message": "Meal updated successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to update meal."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Delete Meal
    # ==========================================================

    def delete_meal(
        self,
        meal_id: int
    ):

        try:

            self.repository.delete_meal(
                meal_id
            )

            return {
                "message": "Meal deleted successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to delete meal."
            )

            raise DatabaseException(
                str(e)
            )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    service = MealService()

    print("\n========== ALL MEALS ==========\n")

    print(
        service.get_all_meals().head()
    )