"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Sleep API

Author     : Harsh

Description:

Sleep API endpoints.

==============================================================
"""

from typing import List
import traceback

from fastapi import APIRouter, Depends

from src.auth.auth_handler import get_current_user
from src.services.sleep_service import SleepService
from src.api.schemas.sleep_schema import SleepResponse


router = APIRouter(
    prefix="/sleep",
    tags=["Sleep"]
)

service = SleepService()


# ==========================================================
# Get All Sleep Records
# ==========================================================

@router.get(
    "/",
    response_model=List[SleepResponse]
)
def get_all_sleep(
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_user)
):

    data = service.get_all_sleep(
        skip=skip,
        limit=limit
    )

    return data.to_dict(
        orient="records"
    )


# ==========================================================
# Get Sleep By User
# ==========================================================

@router.get(
    "/user/{user_id}",
    response_model=List[SleepResponse]
)
def get_sleep_by_user(
    user_id: int,
    current_user=Depends(get_current_user)
):

    try:

        data = service.get_sleep_by_user(
            user_id
        )

        return data.to_dict(
            orient="records"
        )

    except Exception as e:

        traceback.print_exc()
        raise


# ==========================================================
# Get Latest Sleep
# ==========================================================

@router.get(
    "/latest/{user_id}",
    response_model=List[SleepResponse]
)
def get_latest_sleep(
    user_id: int,
    current_user=Depends(get_current_user)
):

    try:

        data = service.get_latest_sleep(
            user_id
        )

        return data.to_dict(
            orient="records"
        )

    except Exception as e:

        traceback.print_exc()
        raise


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print("Sleep API routes loaded successfully.")