"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI Authentication

Module     : JWT Handler

Author     : Harsh

Description:

Generate and verify JWT access tokens.

==============================================================
"""

from datetime import datetime, timedelta, UTC

from jose import jwt
from jose import JWTError

# ==========================================================
# JWT Configuration
# ==========================================================

SECRET_KEY = "YOUR_SUPER_SECRET_KEY_CHANGE_THIS"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


# ==========================================================
# Create Access Token
# ==========================================================

def create_access_token(
    data: dict
) -> str:
    """
    Create JWT access token.
    """

    payload = data.copy()

    expire = datetime.now(
        UTC
    ) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update(

        {
            "exp": expire
        }

    )

    token = jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM

    )

    return token


# ==========================================================
# Verify Access Token
# ==========================================================

def verify_access_token(
    token: str
) -> dict:
    """
    Verify JWT access token.
    """

    try:

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )

        return payload

    except JWTError:

        raise ValueError(
            "Invalid or expired token."
        )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    token = create_access_token(

        {
            "user_id": 1,
            "email": "mayank@gmail.com"
        }

    )

    print("\n========== TOKEN ==========\n")

    print(token)

    print("\n========== VERIFIED ==========\n")

    print(

        verify_access_token(
            token
        )

    )