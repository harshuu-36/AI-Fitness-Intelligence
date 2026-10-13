"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Progress API

==============================================================
"""

from typing import List

from fastapi import APIRouter
from fastapi import Depends

from src.auth.auth_handler import get_current_user
from src.services.progress_service import ProgressService
from src.api.schemas.progress_schema import ProgressResponse

router = APIRouter(
    prefix="/progress",
    tags=["Progress"]
)

service = ProgressService()


# ==========================================================
# Get All Progress
# ==========================================================

@router.get(
    "/",
    response_model=List[ProgressResponse]
)
def get_all_progress(
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_user)
):

    data = service.get_all_progress(
        skip,
        limit
    )

    return data.to_dict(
        orient="records"
    )


# ==========================================================
# Get Progress By User
# ==========================================================

@router.get(
    "/user/{user_id}",
    response_model=List[ProgressResponse]
)
def get_progress_by_user(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_user)
):

    data = service.get_progress_by_user(
        user_id,
        skip,
        limit
    )

    return data.to_dict(
        orient="records"
    )


# ==========================================================
# Get Latest Progress
# ==========================================================

@router.get(
    "/latest/{user_id}",
    response_model=List[ProgressResponse]
)
def get_latest_progress(
    user_id: int,
    current_user=Depends(get_current_user)
):

    data = service.get_latest_progress(
        user_id
    )

    return data.to_dict(
        orient="records"
    )