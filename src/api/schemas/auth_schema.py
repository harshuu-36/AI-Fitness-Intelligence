"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Authentication Schema

Author     : Harsh

Description:

Pydantic schemas for authentication.

==============================================================
"""

from pydantic import BaseModel
from pydantic import ConfigDict


# ==========================================================
# Login Request
# ==========================================================

class LoginRequest(BaseModel):

    email: str

    password: str


# ==========================================================
# Login Response
# ==========================================================

class LoginResponse(BaseModel):

    access_token: str

    token_type: str

    user_id: int

    email: str

    role: str

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    login = LoginRequest(

        email="jeffreydoyle@example.net",

        password="Mayank@123"

    )

    print(login)

    response = LoginResponse(

        access_token="TOKEN",

        token_type="bearer",

        user_id=1,

        email="jeffreydoyle@example.net",

        role="Admin"

    )

    print(response)