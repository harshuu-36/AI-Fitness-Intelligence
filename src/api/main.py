"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Main API

Author     : Harsh

Description:

Main FastAPI application.

==============================================================
"""

from fastapi import FastAPI

from src.api.routes.users import router as users_router
from src.api.routes.workouts import router as workouts_router
from src.api.routes.meals import router as meals_router
from src.api.routes.sleep import router as sleep_router
from src.api.routes.progress import router as progress_router
from src.api.routes.health import router as health_router
from src.api.routes.auth import router as auth_router
from src.api.routes.ai import router as ai_router

from src.exceptions.exception_handler import (
    register_exception_handlers
)

from src.utils.logger import logger


# ==========================================================
# Create FastAPI App
# ==========================================================

app = FastAPI(

    title="AI Fitness Intelligence Platform API",

    description="Backend APIs for AI Fitness Intelligence Platform",

    version="1.0.0"

)

# ==========================================================
# Register Global Exception Handlers
# ==========================================================

register_exception_handlers(
    app
)

# ==========================================================
# Register API Routes
# ==========================================================

app.include_router(users_router)

app.include_router(workouts_router)

app.include_router(meals_router)

app.include_router(sleep_router)

app.include_router(progress_router)

app.include_router(health_router)

app.include_router(auth_router)

app.include_router(ai_router)

# ==========================================================
# Home Endpoint
# ==========================================================

@app.get("/")
def home():
    """
    Home endpoint.
    """

    logger.info("Home endpoint called.")

    return {

        "message": "AI Fitness Intelligence Platform API",

        "status": "Running"

    }


# ==========================================================
# Health Check Endpoint
# ==========================================================

@app.get("/health")
def health_check():
    """
    Health Check API.
    """

    logger.info("Health check endpoint called.")

    return {

        "status": "Healthy",

        "message": "API is running successfully."

    }


# ==========================================================
# Run Server
# ==========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(

        "src.api.main:app",

        host="127.0.0.1",

        port=8000,

        reload=True

    )