"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Health Dashboard Schema

Author     : Harsh

Description:

Pydantic models for Health Dashboard API.

==============================================================
"""

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict


class HealthDashboardResponse(BaseModel):

    user: list[Any]

    latest_progress: list[Any]

    latest_workout: list[Any]

    latest_sleep: list[Any]

    meal_history: list[Any]

    model_config = ConfigDict(
        from_attributes=True
    )