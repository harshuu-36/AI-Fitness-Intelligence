"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : Repository Layer

Module     : User Repository

Author     : Harsh

Description:

Database operations for the Users table.

====================================================================
"""

import pandas as pd

from src.database.query_executor import (
    execute_query,
    execute_non_query
)

from src.utils.logger import logger


class UserRepository:
    """
    Repository for Users table.
    """

    # ==========================================================
    # Get All Users
    # ==========================================================

    @staticmethod
    def get_all_users() -> pd.DataFrame:

        query = """
        SELECT
            UserID,
            FirstName,
            LastName,
            Email,
            DateOfBirth,
            Gender,
            HeightCM,
            CreatedAt
        FROM Users
        WHERE IsActive = 1;
        """

        logger.info("Fetching all active users.")

        return execute_query(query)

    # ==========================================================
    # Get User By ID
    # ==========================================================

    @staticmethod
    def get_user_by_id(
        user_id: int
    ) -> pd.DataFrame:

        query = f"""
        SELECT
            UserID,
            FirstName,
            LastName,
            Email,
            DateOfBirth,
            Gender,
            HeightCM,
            CreatedAt
        FROM Users
        WHERE UserID = {user_id}
          AND IsActive = 1;
        """

        logger.info(
            f"Fetching user {user_id}"
        )

        return execute_query(query)

    # ==========================================================
    # Create User
    # ==========================================================

    @staticmethod
    def create_user(
        user_data: dict
    ):

        query = f"""
        INSERT INTO Users
        (
            FirstName,
            LastName,
            Email,
            PasswordHash,
            DateOfBirth,
            Gender,
            HeightCM,
            IsActive
        )
        VALUES
        (
            '{user_data["FirstName"]}',
            '{user_data["LastName"]}',
            '{user_data["Email"]}',
            '{user_data["PasswordHash"]}',
            '{user_data["DateOfBirth"]}',
            '{user_data["Gender"]}',
            {user_data["HeightCM"]},
            1
        );
        """

        logger.info(
            f"Creating user {user_data['Email']}"
        )

        execute_non_query(query)

    # ==========================================================
    # Update User
    # ==========================================================

    @staticmethod
    def update_user(
        user_id: int,
        user_data: dict
    ):

        query = f"""
        UPDATE Users
        SET
            FirstName = '{user_data["FirstName"]}',
            LastName = '{user_data["LastName"]}',
            DateOfBirth = '{user_data["DateOfBirth"]}',
            Gender = '{user_data["Gender"]}',
            HeightCM = {user_data["HeightCM"]}
        WHERE UserID = {user_id}
        AND IsActive = 1;
        """

        logger.info(
            f"Updating user {user_id}"
        )

        execute_non_query(query)

    # ==========================================================
    # Delete User (Soft Delete)
    # ==========================================================

    @staticmethod
    def delete_user(
        user_id: int
    ):

        query = f"""
        UPDATE Users
        SET IsActive = 0
        WHERE UserID = {user_id};
        """

        logger.info(
            f"Deleting user {user_id}"
        )

        execute_non_query(query)


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    repo = UserRepository()

    print("\n========== ALL USERS ==========\n")

    print(
        repo.get_all_users()
    )

    print("\n========== USER 1 ==========\n")

    print(
        repo.get_user_by_id(1)
    )