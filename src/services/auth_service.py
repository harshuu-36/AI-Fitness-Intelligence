"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI Authentication

Module     : Authentication Service

Author     : Harsh

Description:

Handles user authentication and JWT token generation.

==============================================================
"""

from src.repository.login_repository import LoginRepository

from src.auth.password_handler import (
    verify_password
)

from src.auth.jwt_handler import (
    create_access_token
)

from src.exceptions.custom_exceptions import (
    UserNotFoundException
)

from src.utils.logger import logger


class AuthService:

    def __init__(self):

        self.repository = LoginRepository()

    # ==========================================================
    # Login User
    # ==========================================================

    def login(
        self,
        email: str,
        password: str
    ) -> dict:

        try:

            logger.info("========== LOGIN START ==========")

            logger.info(f"Email : {email}")

            # --------------------------------------------------

            logger.info("Step 1 : Fetching user from database...")

            user = self.repository.get_login_by_email(
                email
            )

            logger.info("Step 2 : Database query completed.")

            if user.empty:

                logger.error("User not found.")

                raise UserNotFoundException(
                    "Invalid email or password."
                )

            user = user.iloc[0]

            logger.info(
                f"User Found : {user['Email']}"
            )

            # --------------------------------------------------

            logger.info("Step 3 : Verifying password...")

            password_ok = verify_password(

                password,

                user["PasswordHash"]

            )

            logger.info(
                f"Password Verified : {password_ok}"
            )

            if not password_ok:

                raise UserNotFoundException(
                    "Invalid email or password."
                )

            # --------------------------------------------------

            logger.info("Step 4 : Creating JWT Token...")

            token = create_access_token(

                {

                    "user_id": int(
                        user["UserID"]
                    ),

                    "email": user["Email"],

                    "role": user["Role"]

                }

            )

            logger.info("Step 5 : JWT Token Created Successfully.")

            logger.info("========== LOGIN SUCCESS ==========")

            return {

                "access_token": token,

                "token_type": "bearer",

                "user_id": int(
                    user["UserID"]
                ),

                "email": user["Email"],

                "role": user["Role"]

            }

        except Exception as e:

            logger.exception(
                f"LOGIN FAILED : {str(e)}"
            )

            raise


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    service = AuthService()

    result = service.login(

        email="jeffreydoyle@example.net",

        password="Mayank@123"

    )

    print(result)