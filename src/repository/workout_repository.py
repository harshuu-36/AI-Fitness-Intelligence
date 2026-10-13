"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : Repository Layer

Module     : Workout Repository

Author     : Harsh

Description:

Database operations for the Workouts table.

====================================================================
"""

import pandas as pd

from src.database.query_executor import (
    execute_query,
    execute_non_query
)

from src.utils.logger import logger


class WorkoutRepository:

    # ==========================================================
    # Get All Workouts (Pagination)
    # ==========================================================

    @staticmethod
    def get_all_workouts(
        skip: int = 0,
        limit: int = 100
    ) -> pd.DataFrame:

        query = f"""
        SELECT
            WorkoutID,
            UserID,
            WorkoutDate,
            WorkoutType,
            DurationMinutes,
            CaloriesBurned
        FROM Workouts
        ORDER BY WorkoutID
        OFFSET {skip} ROWS
        FETCH NEXT {limit} ROWS ONLY;
        """

        logger.info(
            f"Fetching workouts (Skip={skip}, Limit={limit})"
        )

        return execute_query(query)

    # ==========================================================
    # Get Workout By ID
    # ==========================================================

    @staticmethod
    def get_workout_by_id(
        workout_id: int
    ) -> pd.DataFrame:

        query = f"""
        SELECT
            WorkoutID,
            UserID,
            WorkoutDate,
            WorkoutType,
            DurationMinutes,
            CaloriesBurned
        FROM Workouts
        WHERE WorkoutID = {workout_id};
        """

        logger.info(
            f"Fetching workout {workout_id}"
        )

        return execute_query(query)


    # ==========================================================
    # Get Latest Workout
    # ==========================================================

    @staticmethod
    def get_latest_workout(
        user_id: int
    ) -> pd.DataFrame:

        query = f"""
        SELECT TOP 1
            WorkoutID,
            UserID,
            WorkoutDate,
            WorkoutType,
            DurationMinutes,
            CaloriesBurned
        FROM Workouts
        WHERE UserID = {user_id}
        ORDER BY WorkoutDate DESC;
        """

        logger.info(
            f"Fetching latest workout for UserID={user_id}"
        )

        return execute_query(query)

    # ==========================================================
    # Create Workout
    # ==========================================================

    @staticmethod
    def create_workout(
        workout_data: dict
    ):

        query = f"""
        INSERT INTO Workouts
        (
            UserID,
            WorkoutDate,
            WorkoutType,
            DurationMinutes,
            CaloriesBurned
        )
        VALUES
        (
            {workout_data["UserID"]},
            '{workout_data["WorkoutDate"]}',
            '{workout_data["WorkoutType"]}',
            {workout_data["DurationMinutes"]},
            {workout_data["CaloriesBurned"]}
        );
        """

        logger.info(
            "Creating workout."
        )

        execute_non_query(query)

    # ==========================================================
    # Update Workout
    # ==========================================================

    @staticmethod
    def update_workout(
        workout_id: int,
        workout_data: dict
    ):

        query = f"""
        UPDATE Workouts
        SET
            WorkoutDate = '{workout_data["WorkoutDate"]}',
            WorkoutType = '{workout_data["WorkoutType"]}',
            DurationMinutes = {workout_data["DurationMinutes"]},
            CaloriesBurned = {workout_data["CaloriesBurned"]}
        WHERE WorkoutID = {workout_id};
        """

        logger.info(
            f"Updating workout {workout_id}"
        )

        execute_non_query(query)

    # ==========================================================
    # Delete Workout
    # ==========================================================

    @staticmethod
    def delete_workout(
        workout_id: int
    ):

        query = f"""
        DELETE FROM Workouts
        WHERE WorkoutID = {workout_id};
        """

        logger.info(
            f"Deleting workout {workout_id}"
        )

        execute_non_query(query)


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    repo = WorkoutRepository()

    print("\n========== ALL WORKOUTS ==========\n")

    print(
        repo.get_all_workouts(
            skip=0,
            limit=10
        ).head()
    )

    print("\n========== WORKOUT ID 1 ==========\n")

    print(
        repo.get_workout_by_id(1)
    )

    print("\n========== LATEST WORKOUT ==========\n")

    print(
        repo.get_latest_workout(1)
    )