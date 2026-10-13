"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : User Schema

Author     : Harsh

Description:

Pydantic models for User API.

==============================================================
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, EmailStr


# ==========================================================
# Create User
# ==========================================================

class UserCreate(BaseModel):

    FirstName: str

    LastName: str

    Email: EmailStr

    Password: str

    DateOfBirth: date

    Gender: str

    HeightCM: float


# ==========================================================
# Update User
# ==========================================================

class UserUpdate(BaseModel):

    FirstName: str

    LastName: str

    DateOfBirth: date

    Gender: str

    HeightCM: float


# ==========================================================
# User Response
# ==========================================================

class UserResponse(BaseModel):

    UserID: int

    FirstName: str

    LastName: str

    Email: EmailStr

    DateOfBirth: date

    Gender: str

    HeightCM: float

    CreatedAt: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


if __name__ == "__main__":

    print("User Schema Loaded Successfully.")