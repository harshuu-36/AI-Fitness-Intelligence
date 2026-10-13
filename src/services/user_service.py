"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : User Service

Author     : Harsh

Description:

Business logic for User APIs.

==============================================================
"""

from src.repository.user_repository import UserRepository

from src.auth.password_handler import (
    hash_password
)

from src.exceptions.custom_exceptions import (
    UserNotFoundException,
    DatabaseException
)

from src.utils.logger import logger


class UserService:

    def __init__(self):

        self.repository = UserRepository()

    # ==========================================================
    # Get All Users
    # ==========================================================

    def get_all_users(self):

        try:

            data = self.repository.get_all_users()

            if data.empty:

                raise UserNotFoundException(
                    "No users found."
                )

            return data

        except UserNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch users."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Get User By ID
    # ==========================================================

    def get_user_by_id(
        self,
        user_id: int
    ):

        try:

            data = self.repository.get_user_by_id(
                user_id
            )

            if data.empty:

                raise UserNotFoundException(
                    f"User {user_id} not found."
                )

            return data

        except UserNotFoundException:

            raise

        except Exception as e:

            logger.exception(
                "Failed to fetch user."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Create User
    # ==========================================================

    def create_user(
        self,
        user_data: dict
    ):

        try:

            user_data["PasswordHash"] = hash_password(
                user_data.pop("Password")
            )

            self.repository.create_user(
                user_data
            )

            return {
                "message": "User created successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to create user."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Update User
    # ==========================================================

    def update_user(
        self,
        user_id: int,
        user_data: dict
    ):

        try:

            self.repository.update_user(
                user_id,
                user_data
            )

            return {
                "message": "User updated successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to update user."
            )

            raise DatabaseException(
                str(e)
            )

    # ==========================================================
    # Delete User
    # ==========================================================

    def delete_user(
        self,
        user_id: int
    ):

        try:

            self.repository.delete_user(
                user_id
            )

            return {
                "message": "User deleted successfully."
            }

        except Exception as e:

            logger.exception(
                "Failed to delete user."
            )

            raise DatabaseException(
                str(e)
            )


if __name__ == "__main__":

    service = UserService()

    print(

        service.get_all_users()

    )