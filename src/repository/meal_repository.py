"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : Repository Layer

Module     : Meal Repository

Author     : Harsh

Description:

Database operations for the Meals table.

====================================================================
"""

import pandas as pd

from src.database.query_executor import (
    execute_query,
    execute_non_query
)

from src.utils.logger import logger


class MealRepository:
    """
    Repository for Meals table.
    """

    # ==========================================================
    # Get All Meals
    # ==========================================================

    @staticmethod
    def get_all_meals(
        skip: int = 0,
        limit: int = 100
    ) -> pd.DataFrame:
        """
        Fetch all meals with pagination.
        """

        query = f"""
        SELECT
            MealID,
            UserID,
            MealDate,
            MealType,
            TotalCalories
        FROM Meals
        ORDER BY MealDate DESC
        OFFSET {skip} ROWS
        FETCH NEXT {limit} ROWS ONLY;
        """

        logger.info(
            f"Fetching all meals (skip={skip}, limit={limit})."
        )

        return execute_query(query)

    # ==========================================================
    # Get Meals By User
    # ==========================================================

    @staticmethod
    def get_meals_by_user(
        user_id: int,
        skip: int = 0,
        limit: int = 100
    ) -> pd.DataFrame:
        """
        Fetch meals for a specific user.
        """

        query = f"""
        SELECT
            MealID,
            UserID,
            MealDate,
            MealType,
            TotalCalories
        FROM Meals
        WHERE UserID = {user_id}
        ORDER BY MealDate DESC
        OFFSET {skip} ROWS
        FETCH NEXT {limit} ROWS ONLY;
        """

        logger.info(
            f"Fetching meals for UserID={user_id}"
        )

        return execute_query(query)

    # ==========================================================
    # Get Daily Calories
    # ==========================================================

    @staticmethod
    def get_daily_calories(
        user_id: int,
        meal_date: str
    ) -> pd.DataFrame:
        """
        Fetch total calories consumed on a given date.
        """

        query = f"""
        SELECT
            SUM(TotalCalories) AS TotalCalories
        FROM Meals
        WHERE UserID = {user_id}
          AND MealDate = '{meal_date}';
        """

        logger.info(
            f"Fetching calories for UserID={user_id} on {meal_date}"
        )

        return execute_query(query)

    # ==========================================================
    # Create Meal
    # ==========================================================

    @staticmethod
    def create_meal(
        meal_data: dict
    ):

        query = f"""
        INSERT INTO Meals
        (
            UserID,
            MealDate,
            MealType,
            TotalCalories
        )
        VALUES
        (
            {meal_data["UserID"]},
            '{meal_data["MealDate"]}',
            '{meal_data["MealType"]}',
            {meal_data["TotalCalories"]}
        );
        """

        logger.info(
            "Creating meal."
        )

        execute_non_query(query)

    # ==========================================================
    # Update Meal
    # ==========================================================

    @staticmethod
    def update_meal(
        meal_id: int,
        meal_data: dict
    ):

        query = f"""
        UPDATE Meals
        SET
            MealDate = '{meal_data["MealDate"]}',
            MealType = '{meal_data["MealType"]}',
            TotalCalories = {meal_data["TotalCalories"]}
        WHERE MealID = {meal_id};
        """

        logger.info(
            f"Updating meal {meal_id}"
        )

        execute_non_query(query)

    # ==========================================================
    # Delete Meal
    # ==========================================================

    @staticmethod
    def delete_meal(
        meal_id: int
    ):

        query = f"""
        DELETE FROM Meals
        WHERE MealID = {meal_id};
        """

        logger.info(
            f"Deleting meal {meal_id}"
        )

        execute_non_query(query)


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    repo = MealRepository()

    print("\n========== ALL MEALS ==========\n")

    print(
        repo.get_all_meals().head()
    )

    print("\n========== USER 1 MEALS ==========\n")

    print(
        repo.get_meals_by_user(1).head()
    )

    print("\n========== DAILY CALORIES ==========\n")

    print(
        repo.get_daily_calories(
            1,
            "2025-08-31"
        )
    )