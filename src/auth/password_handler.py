"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI Authentication

Module     : Password Handler

Author     : Harsh

Description:

Password hashing using bcrypt.

==============================================================
"""

import bcrypt


def hash_password(password: str) -> str:
    """
    Hash a password.
    """

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(

        password.encode("utf-8"),

        salt

    )

    return hashed.decode("utf-8")


def verify_password(
    password: str,
    hashed_password: str
) -> bool:
    """
    Verify a password.
    """

    return bcrypt.checkpw(

        password.encode("utf-8"),

        hashed_password.encode("utf-8")

    )


if __name__ == "__main__":

    password = "Mayank@123"

    hashed = hash_password(password)

    print("\n========== HASH ==========\n")

    print(hashed)

    print("\n========== VERIFY ==========\n")

    print(
        verify_password(
            password,
            hashed
        )
    )