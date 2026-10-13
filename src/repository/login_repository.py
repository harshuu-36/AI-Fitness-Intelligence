"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI Authentication

Module     : Login Repository

Author     : Harsh

Description:

Repository for UserLogin table.

==============================================================
"""

from src.database.query_executor import execute_query

from src.utils.logger import logger


class LoginRepository:

    # ==========================================================
    # Get Login By Email
    # ==========================================================

    def get_login_by_email(
        self,
        email: str
    ):

        logger.info(
            f"Fetching login details for email: {email}"
        )

        query = f"""
        SELECT
            LoginID,
            UserID,
            Email,
            PasswordHash,
            Role,
            CreatedAt
        FROM UserLogin
        WHERE Email = '{email}'
        """

        return execute_query(
            query
        )

    # ==========================================================
    # Get Login By User ID
    # ==========================================================

    def get_login_by_user(
        self,
        user_id: int
    ):

        logger.info(
            f"Fetching login details for User ID {user_id}"
        )

        query = f"""
        SELECT
            LoginID,
            UserID,
            Email,
            PasswordHash,
            Role,
            CreatedAt
        FROM UserLogin
        WHERE UserID = {user_id}
        """

        return execute_query(
            query
        )


if __name__ == "__main__":

    repo = LoginRepository()

    print("\n========== LOGIN BY EMAIL ==========\n")

    print(

        repo.get_login_by_email(

            "jeffreydoyle@example.net"

        )

    )

    print("\n========== LOGIN BY USER ==========\n")

    print(

        repo.get_login_by_user(

            1

        )

    )