"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : Authentication

Module     : Auth Handler

Author     : Harsh

Description:

JWT Authentication Handler

==============================================================
"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from jose import jwt
from jose import JWTError


# ==========================================================
# JWT Configuration
# ==========================================================

SECRET_KEY = "YOUR_SUPER_SECRET_KEY_CHANGE_THIS"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


# ==========================================================
# OAuth2
# ==========================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# ==========================================================
# Create Access Token
# ==========================================================

def create_access_token(
    data: dict
):

    to_encode = data.copy()

    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ==========================================================
# Verify Token
# ==========================================================

def verify_token(
    token: str
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )


# ==========================================================
# Current User
# ==========================================================

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
        print("\n==============================")
        print("TOKEN RECEIVED:")
        print(token)
        print("==============================")

        payload = verify_token(token)

        print("\n==============================")
        print("PAYLOAD:")
        print(payload)
        print("==============================")

        return payload


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    token = create_access_token(
        {
            "user_id": 1,
            "email": "admin@example.com",
            "role": "Admin"
        }
    )

    print(token)

    print(
        verify_token(token)
    )