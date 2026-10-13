"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Progress Schema

Author     : Harsh

Description:

Pydantic models for Progress API.

==============================================================
"""

from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict


# ==========================================================
# Progress Response
# ==========================================================

class ProgressResponse(BaseModel):

    ProgressID: int

    UserID: int

    ProgressDate: date

    WeightKG: float

    model_config = ConfigDict(
        from_attributes=True
    )