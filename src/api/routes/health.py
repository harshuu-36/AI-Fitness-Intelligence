"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Health Dashboard API

Author     : Harsh

Description:

Health Dashboard API endpoints.

==============================================================
"""

from fastapi import APIRouter

from src.services.health_service import HealthService

from src.api.schemas.health_schema import (
    HealthDashboardResponse
)


router = APIRouter(

    prefix="/health",

    tags=["Health"]

)

service = HealthService()


# ==========================================================
# Health Dashboard
# ==========================================================

@router.get(

    "/{user_id}",

    response_model=HealthDashboardResponse

)
def get_health_dashboard(
    user_id: int
):
    """
    Get complete health dashboard for a user.
    """

    dashboard = service.get_health_dashboard(
        user_id
    )

    return dashboard


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print("Health API routes loaded successfully.")