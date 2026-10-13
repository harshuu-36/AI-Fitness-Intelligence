"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Workout API

Author     : Harsh

Description:

Workout API endpoints.

==============================================================
"""

from typing import List

from fastapi import APIRouter
from fastapi import Depends

from src.auth.auth_handler import get_current_user

from src.services.workout_service import WorkoutService

from src.api.schemas.workout_schema import (
    WorkoutResponse,
    WorkoutCreate,
    WorkoutUpdate
)

router = APIRouter(
    prefix="/workouts",
    tags=["Workouts"]
)

service = WorkoutService()


# ==========================================================
# Get All Workouts
# ==========================================================

@router.get(
    "/",
    response_model=List[WorkoutResponse]
)
def get_all_workouts(
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_user)
):

    data = service.get_all_workouts(
        skip=skip,
        limit=limit
    )

    return data.to_dict(
        orient="records"
    )


# ==========================================================
# Get Workout By ID
# ==========================================================

@router.get(
    "/{workout_id}",
    response_model=List[WorkoutResponse]
)
def get_workout(
    workout_id: int,
    current_user=Depends(get_current_user)
):

    data = service.get_workout_by_id(
        workout_id
    )

    return data.to_dict(
        orient="records"
    )


# ==========================================================
# Create Workout
# ==========================================================

@router.post("/")
def create_workout(
    workout: WorkoutCreate,
    current_user=Depends(get_current_user)
):

    return service.create_workout(
        workout.model_dump()
    )


# ==========================================================
# Update Workout
# ==========================================================

@router.put("/{workout_id}")
def update_workout(
    workout_id: int,
    workout: WorkoutUpdate,
    current_user=Depends(get_current_user)
):

    return service.update_workout(
        workout_id,
        workout.model_dump()
    )


# ==========================================================
# Delete Workout
# ==========================================================

@router.delete("/{workout_id}")
def delete_workout(
    workout_id: int,
    current_user=Depends(get_current_user)
):

    return service.delete_workout(
        workout_id
    )