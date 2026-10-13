"""
==============================================================
AI Fitness Intelligence Platform

Sidebar Component

Author      : Harsh

Description :
Reusable sidebar component for the Streamlit application.
==============================================================
"""

from __future__ import annotations

import streamlit as st

from api_client import APIClient, get_client

from datetime import datetime

from config import (
    AI_MODULES,
    APP_ICON,
    APP_NAME,
    APP_VERSION,
    DATABASE,
    FOOTER,
    ML_MODELS,
    REST_APIS
)

GUEST_NAME = "Guest User"

STATUS_CACHE_TTL = 30


# ==========================================================
# Backend Status
# ==========================================================

@st.cache_data(
    ttl=STATUS_CACHE_TTL,
    show_spinner=False
)
def _get_backend_status(
    _client: APIClient
) -> bool:
    """
    Cached backend health check.
    """

    return _client.is_backend_online()


# ==========================================================
# Session Helpers
# ==========================================================

def _is_logged_in() -> bool:

    return bool(
        st.session_state.get("access_token")
    )


def _logout() -> None:
    """
    Logout current user.
    """

    client = st.session_state.get(
        "api_client"
    )

    if client:

        client.clear_token()

    for key in list(st.session_state.keys()):

        del st.session_state[key]

    st.rerun()


# ==========================================================
# Sidebar Sections
# ==========================================================

def _render_header() -> None:

    st.markdown(
        f"""
# {APP_ICON} {APP_NAME}

### AI Fitness Intelligence Platform

**Version : {APP_VERSION}**
"""
    )

    st.success("🚀 AI Powered Health Analytics")


def _render_user() -> None:

    st.subheader("👤 User")

    username = st.session_state.get(
        "username",
        GUEST_NAME
    )

    st.write(f"**{username}**")

    st.caption(
        datetime.now().strftime(
            "%d %b %Y | %I:%M %p"
        )
    )


def _render_status(
    backend_online: bool
) -> None:

    st.subheader("🖥 System Status")

    if backend_online:

        st.success(
            "Backend : Online"
        )

        st.success(
            "Authentication : Ready"
        )

    else:

        st.error(
            "Backend : Offline"
        )

    st.info(
        f"Database : {DATABASE}"
    )


def _render_project_info() -> None:

    with st.expander(
        "📊 Project Statistics",
        expanded=False
    ):

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "AI Modules",
                AI_MODULES
            )

            st.metric(
                "ML Models",
                ML_MODELS
            )

        with col2:

            st.metric(
                "REST APIs",
                REST_APIS
            )

            st.metric(
                "Database",
                "SQL"
            )

            st.divider()

            st.caption("Tech Stack")

            st.write(
                "FastAPI\n\n"
                "SQL Server\n\n"
                "Machine Learning\n\n"
                "Streamlit"
            )


def _render_navigation() -> None:

    st.subheader("🚀 AI Modules")

    modules = [

        "🏠 Dashboard",

        "⚖ Weight Prediction",

        "🔥 Calorie Recommendation",

        "🥗 Macro Recommendation",

        "💧 Hydration",

        "🏋 Workout",

        "🍽 Meal Recommendation",

        "❤️ Health Score",

    ]

    for module in modules:

        st.markdown(f"• {module}")


def _render_actions() -> None:

    if st.button(
        "🔄 Refresh Status",
        use_container_width=True
    ):

        _get_backend_status.clear()

        st.rerun()

    if _is_logged_in():

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            _logout()

    else:

        st.caption(
            "Login to unlock all features."
        )


# ==========================================================
# Public Function
# ==========================================================

def render_sidebar() -> None:
    """
    Render complete sidebar.
    """

    try:

        backend_online = _get_backend_status(
            get_client()
        )

    except Exception:

        backend_online = False

    with st.sidebar:

        _render_header()

        st.divider()

        _render_user()

        st.divider()

        _render_status(
            backend_online
        )

        st.divider()

        _render_project_info()

        st.divider()

        _render_navigation()

        st.divider()

        _render_actions()

        st.divider()

        st.caption(
            FOOTER
        )


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    st.set_page_config(

        page_title="Sidebar Test",

        page_icon="💪",

        layout="wide"

    )

    render_sidebar()

    st.title(
        "Sidebar Component Test"
    )

    st.write(
        "Sidebar loaded successfully."
    )