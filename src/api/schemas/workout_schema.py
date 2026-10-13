"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Workout Schema

Author     : Harsh

Description:

Pydantic models for Workout APIs.

==============================================================
"""

from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict


class WorkoutResponse(BaseModel):

    WorkoutID: int

    UserID: int

    WorkoutDate: date

    WorkoutType: str

    DurationMinutes: int

    CaloriesBurned: int

    model_config = ConfigDict(
        from_attributes=True
    )


class WorkoutCreate(BaseModel):

    UserID: int

    WorkoutDate: date

    WorkoutType: str

    DurationMinutes: int

    CaloriesBurned: int


class WorkoutUpdate(BaseModel):

    WorkoutDate: date

    WorkoutType: str

    DurationMinutes: int

    CaloriesBurned: int