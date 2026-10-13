"""
==============================================================
AI Fitness Intelligence Platform

Streamlit Home Page

Author : Harsh
==============================================================
"""

import os
from dataclasses import dataclass

import requests
import streamlit as st

# ==========================================================
# Configuration
# ==========================================================

APP_TITLE = "AI Fitness Intelligence Platform"
APP_ICON = "💪"
APP_VERSION = "1.0.0"

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://localhost:8000"
)

HEALTH_ENDPOINT = f"{API_BASE_URL}/health"

REQUEST_TIMEOUT = 3


# ==========================================================
# Feature Model
# ==========================================================

@dataclass(frozen=True)
class Feature:

    icon: str

    title: str

    description: str


FEATURES = [

    Feature(
        "🤖",
        "Weight Prediction",
        "Predict future body weight using Machine Learning."
    ),

    Feature(
        "🔥",
        "Calorie Recommendation",
        "Personalized calorie recommendations."
    ),

    Feature(
        "🥗",
        "Macro Recommendation",
        "Protein, carbs and fat recommendations."
    ),

    Feature(
        "💧",
        "Hydration Recommendation",
        "Daily water intake recommendation."
    ),

    Feature(
        "💪",
        "Workout Recommendation",
        "AI based workout planner."
    ),

    Feature(
        "🍽",
        "Meal Recommendation",
        "Healthy meal suggestions."
    ),

    Feature(
        "❤️",
        "Health Score",
        "Overall fitness score."
    ),

    Feature(
        "📊",
        "Health Dashboard",
        "Complete health analytics dashboard."
    )

]


# ==========================================================
# Backend Status
# ==========================================================

@st.cache_data(
    ttl=30,
    show_spinner=False
)
def check_backend():

    try:

        response = requests.get(
            HEALTH_ENDPOINT,
            timeout=REQUEST_TIMEOUT
        )

        return response.ok

    except Exception:

        return False


# ==========================================================
# Sidebar
# ==========================================================

def sidebar(backend_online):

    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/dumbbell.png",
            width=90
        )

        st.title(APP_TITLE)

        st.caption(
            f"Version {APP_VERSION}"
        )

        st.divider()

        st.subheader("Backend Status")

        if backend_online:

            st.success("🟢 Online")

        else:

            st.error("🔴 Offline")

        st.divider()

        st.markdown(
            """
### Navigation

Use the pages from the sidebar.

- Dashboard
- Weight Prediction
- Calories
- Macros
- Hydration
- Workout
- Meals
- Health Score
- Profile
"""
        )


# ==========================================================
# Feature Cards
# ==========================================================

def feature_cards():

    cols = st.columns(4)

    for index, feature in enumerate(FEATURES):

        with cols[index % 4]:

            with st.container(border=True):

                st.markdown(
                    f"# {feature.icon}"
                )

                st.markdown(
                    f"### {feature.title}"
                )

                st.caption(
                    feature.description
                )


# ==========================================================
# Main
# ==========================================================

def main():

    st.set_page_config(

        page_title=APP_TITLE,

        page_icon=APP_ICON,

        layout="wide",

        initial_sidebar_state="expanded"

    )

    backend_online = check_backend()

    sidebar(backend_online)

    st.title(
        f"{APP_ICON} {APP_TITLE}"
    )

    st.markdown(
        """
### AI Powered Fitness Analytics Platform

A complete AI-powered fitness management system built using:

- FastAPI
- SQL Server
- Machine Learning
- Streamlit
- Power BI
"""
    )

    if backend_online:

        st.success(
            "Backend connected successfully."
        )

    else:

        st.warning(
            "Backend server is currently offline."
        )

    st.divider()

    # ======================================================
    # KPI Cards
    # ======================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "AI Modules",
            "7"
        )

    with col2:

        st.metric(
            "REST APIs",
            "20+"
        )

    with col3:

        st.metric(
            "ML Models",
            "1"
        )

    with col4:

        st.metric(
            "Database",
            "SQL Server"
        )

    st.divider()

    st.subheader("Platform Features")

    feature_cards()

    st.divider()

    st.subheader("System Architecture")

    st.code(
        """
        Streamlit
            │
            ▼
        FastAPI
            │
            ▼
        Service Layer
            │
            ▼
        Repository Layer
            │
            ▼
        SQL Server

             +

      Machine Learning

             +

   Recommendation Engine
"""
    )

    st.divider()

    st.info(
        "👈 Use the sidebar to navigate through all modules."
    )

    st.markdown("---")

    st.caption(
        "© 2026 AI Fitness Intelligence Platform | Developed by Harsh"
    )


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()