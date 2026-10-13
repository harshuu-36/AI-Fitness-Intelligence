"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Meals API

Author     : Harsh

Description:

Meal API endpoints.

==============================================================
"""

from typing import List
import traceback

from fastapi import APIRouter, Depends

from src.auth.auth_handler import get_current_user
from src.services.meal_service import MealService

from src.api.schemas.meal_schema import (
    MealResponse,
    MealCreate,
    MealUpdate
)

router = APIRouter(
    prefix="/meals",
    tags=["Meals"]
)

service = MealService()


# ==========================================================
# Get All Meals
# ==========================================================

@router.get(
    "/",
    response_model=List[MealResponse]
)
def get_all_meals(
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_user)
):
    try:

        print("\n" + "=" * 80)
        print("GET /meals")
        print(f"skip={skip}, limit={limit}")

        data = service.get_all_meals(
            skip=skip,
            limit=limit
        )

        print("Service executed successfully.")

        print("Type :", type(data))
        print("Rows :", len(data))

        print("Columns :")
        print(list(data.columns))

        if not data.empty:
            print("First Row :")
            print(data.iloc[0].to_dict())

        response = data.to_dict(
            orient="records"
        )

        print("Response converted successfully.")
        print("=" * 80)

        return response

    except Exception as e:

        print("\n" + "=" * 80)
        print("ERROR IN GET /meals")
        traceback.print_exc()
        print("Exception Type :", type(e))
        print("Exception :", e)
        print("=" * 80)

        raise


# ==========================================================
# Get Meals By User
# ==========================================================

@router.get(
    "/user/{user_id}",
    response_model=List[MealResponse]
)
def get_meals_by_user(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_user)
):
    return service.get_meals_by_user(
        user_id,
        skip,
        limit
    ).to_dict(
        orient="records"
    )


# ==========================================================
# Get Daily Calories
# ==========================================================

@router.get(
    "/calories/{user_id}/{meal_date}"
)
def get_daily_calories(
    user_id: int,
    meal_date: str,
    current_user=Depends(get_current_user)
):
    return service.get_daily_calories(
        user_id,
        meal_date
    ).to_dict(
        orient="records"
    )


# ==========================================================
# Create Meal
# ==========================================================

@router.post("/")
def create_meal(
    meal: MealCreate,
    current_user=Depends(get_current_user)
):
    return service.create_meal(
        meal.model_dump()
    )


# ==========================================================
# Update Meal
# ==========================================================

@router.put("/{meal_id}")
def update_meal(
    meal_id: int,
    meal: MealUpdate,
    current_user=Depends(get_current_user)
):
    return service.update_meal(
        meal_id,
        meal.model_dump()
    )


# ==========================================================
# Delete Meal
# ==========================================================

@router.delete("/{meal_id}")
def delete_meal(
    meal_id: int,
    current_user=Depends(get_current_user)
):
    return service.delete_meal(
        meal_id
    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print("Meals API routes loaded successfully.")