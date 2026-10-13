"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Meal Schema

Author     : Harsh

Description:

Pydantic models for Meal API.

==============================================================
"""

from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict


# ==========================================================
# Meal Response
# ==========================================================

class MealResponse(BaseModel):

    MealID: int

    UserID: int

    MealDate: date

    MealType: str

    TotalCalories: float

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Create Meal
# ==========================================================

class MealCreate(BaseModel):

    UserID: int

    MealDate: date

    MealType: str

    TotalCalories: float


# ==========================================================
# Update Meal
# ==========================================================

class MealUpdate(BaseModel):

    MealDate: date

    MealType: str

    TotalCalories: float