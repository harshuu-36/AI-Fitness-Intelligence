"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Users API

Author     : Harsh

Description:

User API endpoints.

==============================================================
"""

from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from src.auth.auth_handler import get_current_user

from src.services.user_service import UserService

from src.api.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse
)

router = APIRouter(

    prefix="/users",

    tags=["Users"]

)

service = UserService()

# ==========================================================
# Get All Users
# ==========================================================

@router.get(

    "/",

    response_model=List[UserResponse]

)
def get_all_users(



):

    try:

        data = service.get_all_users()

        return data.to_dict(

            orient="records"

        )

    except Exception as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# ==========================================================
# Get User By ID
# ==========================================================

@router.get(

    "/{user_id}",

    response_model=List[UserResponse]

)
def get_user(

    user_id: int,

    current_user=Depends(
        get_current_user
    )

):

    try:

        data = service.get_user_by_id(

            user_id

        )

        if data.empty:

            raise HTTPException(

                status_code=status.HTTP_404_NOT_FOUND,

                detail="User not found."

            )

        return data.to_dict(

            orient="records"

        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# ==========================================================
# Create User
# ==========================================================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate
):
    """
    Create a new user.
    """

    try:

        return service.create_user(
            user.model_dump()
        )

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# ==========================================================
# Update User
# ==========================================================

@router.put(
    "/{user_id}"
)
def update_user(
    user_id: int,
    user: UserUpdate
):
    """
    Update an existing user.
    """

    try:

        return service.update_user(
            user_id,
            user.model_dump()
        )

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# ==========================================================
# Delete User
# ==========================================================

@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    current_user=Depends(get_current_user)
):
    """
    Soft delete a user.
    """

    try:

        return service.delete_user(
            user_id
        )

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print(
        "Users API Loaded Successfully."
    )