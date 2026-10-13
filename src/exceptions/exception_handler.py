"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Global Exception Handler

Author     : Harsh

Description:

Registers global exception handlers for the API.

==============================================================
"""

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from src.exceptions.custom_exceptions import (
    UserNotFoundException,
    WorkoutNotFoundException,
    MealNotFoundException,
    SleepNotFoundException,
    ProgressNotFoundException,
    HealthDataNotFoundException,
    DatabaseException,
    ValidationException
)


def register_exception_handlers(
    app: FastAPI
):
    """
    Register all application exception handlers.
    """

    # ==========================================================
    # 404 - Not Found Exceptions
    # ==========================================================

    @app.exception_handler(UserNotFoundException)
    @app.exception_handler(WorkoutNotFoundException)
    @app.exception_handler(MealNotFoundException)
    @app.exception_handler(SleepNotFoundException)
    @app.exception_handler(ProgressNotFoundException)
    @app.exception_handler(HealthDataNotFoundException)
    async def not_found_exception_handler(
        request: Request,
        exc: Exception
    ):

        return JSONResponse(

            status_code=404,

            content={

                "success": False,

                "message": str(exc)

            }

        )

    # ==========================================================
    # Validation Exception
    # ==========================================================

    @app.exception_handler(ValidationException)
    async def validation_exception_handler(
        request: Request,
        exc: ValidationException
    ):

        return JSONResponse(

            status_code=400,

            content={

                "success": False,

                "message": str(exc)

            }

        )

    # ==========================================================
    # Database Exception
    # ==========================================================

    @app.exception_handler(DatabaseException)
    async def database_exception_handler(
        request: Request,
        exc: DatabaseException
    ):

        return JSONResponse(

            status_code=500,

            content={

                "success": False,

                "message": str(exc)

            }

        )

    # ==========================================================
    # Generic Exception
    # ==========================================================

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request,
        exc: Exception
    ):

        return JSONResponse(

            status_code=500,

            content={

                "success": False,

                "message": "Internal Server Error"

            }

        )