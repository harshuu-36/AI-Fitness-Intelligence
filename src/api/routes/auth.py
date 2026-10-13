"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Authentication API

Author     : Harsh

Description:

Authentication endpoints.

==============================================================
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from src.services.auth_service import AuthService

from src.api.schemas.auth_schema import (
    LoginResponse
)

router = APIRouter(

    prefix="/auth",

    tags=["Authentication"]

)

service = AuthService()


# ==========================================================
# Login
# ==========================================================

@router.post(

    "/login",

    response_model=LoginResponse

)
def login(

    form_data: OAuth2PasswordRequestForm = Depends()

):

    try:

        return service.login(

            email=form_data.username,

            password=form_data.password

        )

    except Exception as e:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail=str(e)

        )