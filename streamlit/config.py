"""
==============================================================
AI Fitness Intelligence Platform

Streamlit Configuration

Author      : Harsh

Description :
Central configuration for the Streamlit application.
==============================================================
"""

import os
from datetime import datetime
from pathlib import Path
from typing import Final

# ==========================================================
# Application Information
# ==========================================================

APP_NAME: Final = "AI Fitness Intelligence Platform"

APP_ICON: Final = "💪"

APP_VERSION: Final = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

DEVELOPER: Final = "Harsh"

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR: Final = Path(__file__).resolve().parent

ASSETS_DIR: Final = BASE_DIR / "assets"

LOGO: Final = ASSETS_DIR / "logo.png"

BACKGROUND: Final = ASSETS_DIR / "background.jpg"

# ==========================================================
# FastAPI Configuration
# ==========================================================

API_BASE_URL: Final = os.getenv(
    "API_BASE_URL",
    "http://localhost:8000"
).rstrip("/")

REQUEST_TIMEOUT: Final = int(
    os.getenv(
        "REQUEST_TIMEOUT",
        "10"
    )
)

# ==========================================================
# URL Builder
# ==========================================================

def build_url(path: str) -> str:
    """
    Generate complete API URL.
    """

    return f"{API_BASE_URL}{path}"


# ==========================================================
# Authentication APIs
# ==========================================================

LOGIN_API: Final = build_url(
    "/auth/login"
)

REGISTER_API: Final = build_url(
    "/auth/register"
)

# ==========================================================
# Health APIs
# ==========================================================

HEALTH_API: Final = build_url(
    "/health"
)

HEALTH_DASHBOARD_API: Final = build_url(
    "/health"
)

# ==========================================================
# AI Recommendation APIs
# ==========================================================

AI_ENDPOINTS: Final = {

    "weight_prediction":
        build_url("/ai/predict-weight"),

    "calorie":
        build_url("/ai/recommend-calories"),

    "macro":
        build_url("/ai/recommend-macros"),

    "hydration":
        build_url("/ai/recommend-hydration"),

    "workout":
        build_url("/ai/recommend-workout"),

    "meal":
        build_url("/ai/recommend-meals"),

    "health_score":
        build_url("/ai/health-score")

}

# ==========================================================
# Individual Endpoint Constants
# ==========================================================

WEIGHT_PREDICTION_API: Final = AI_ENDPOINTS[
    "weight_prediction"
]

CALORIE_API: Final = AI_ENDPOINTS[
    "calorie"
]

MACRO_API: Final = AI_ENDPOINTS[
    "macro"
]

HYDRATION_API: Final = AI_ENDPOINTS[
    "hydration"
]

WORKOUT_API: Final = AI_ENDPOINTS[
    "workout"
]

MEAL_API: Final = AI_ENDPOINTS[
    "meal"
]

HEALTH_SCORE_API: Final = AI_ENDPOINTS[
    "health_score"
]

# ==========================================================
# Theme Colors
# ==========================================================

PRIMARY_COLOR: Final = "#4F46E5"

SUCCESS_COLOR: Final = "#22C55E"

WARNING_COLOR: Final = "#F59E0B"

ERROR_COLOR: Final = "#EF4444"

BACKGROUND_COLOR: Final = "#0F172A"

CARD_COLOR: Final = "#1E293B"

TEXT_COLOR: Final = "#FFFFFF"

# ==========================================================
# Dashboard Statistics
# ==========================================================

AI_MODULES: Final = len(
    AI_ENDPOINTS
)

REST_APIS: Final = 25

ML_MODELS: Final = 1

DATABASE: Final = "SQL Server"

# ==========================================================
# Navigation Menu
# ==========================================================

MENU_ITEMS: Final = [

    "Dashboard",

    "Weight Prediction",

    "Calorie Recommendation",

    "Macro Recommendation",

    "Hydration",

    "Workout Recommendation",

    "Meal Recommendation",

    "Health Score",

    "Profile"

]

# ==========================================================
# Footer
# ==========================================================

FOOTER: Final = (
    f"© {datetime.now().year} "
    f"{APP_NAME} | "
    f"Developed by {DEVELOPER}"
)

# ==========================================================
# Streamlit Page Configuration
# ==========================================================

PAGE_CONFIG = {

    "page_title": APP_NAME,

    "page_icon": APP_ICON,

    "layout": "wide",

    "initial_sidebar_state": "expanded"

}