"""
==============================================================
AI Fitness Intelligence Platform

Streamlit API Client

Author      : Harsh

Description :
Central API client for communicating with the
FastAPI backend.
==============================================================
"""

from __future__ import annotations

from typing import Any, Optional

import requests

from config import (
    CALORIE_API,
    HEALTH_API,
    HEALTH_DASHBOARD_API,
    HEALTH_SCORE_API,
    HYDRATION_API,
    LOGIN_API,
    MACRO_API,
    MEAL_API,
    REGISTER_API,
    REQUEST_TIMEOUT,
    WEIGHT_PREDICTION_API,
    WORKOUT_API,
)

HEALTH_CHECK_TIMEOUT = 3

# ==========================================================
# API Response Type
# ==========================================================

APIResponse = dict[str, Any]


# ==========================================================
# API Client
# ==========================================================

class APIClient:
    """
    Central API Client for communicating with
    FastAPI Backend.
    """

    def __init__(

        self,

        token: Optional[str] = None,

        timeout: int = REQUEST_TIMEOUT

    ):

        self.timeout = timeout

        self.session = requests.Session()

        self.session.headers.update(

            {

                "Accept": "application/json"

            }

        )

        if token:

            self.set_token(token)

    # ======================================================
    # Authentication
    # ======================================================

    def set_token(

        self,

        token: str

    ) -> None:

        """
        Store JWT token.
        """

        self.session.headers[

            "Authorization"

        ] = f"Bearer {token}"

    def clear_token(

        self

    ) -> None:

        """
        Remove JWT token.
        """

        self.session.headers.pop(

            "Authorization",

            None

        )

    # ======================================================
    # Error Helpers
    # ======================================================

    @staticmethod
    def _error(

        message: str,

        status_code: Optional[int] = None

    ) -> APIResponse:

        return {

            "success": False,

            "message": message,

            "status_code": status_code

        }

    @staticmethod
    def _extract_error(

        response: requests.Response

    ) -> str:

        """
        Extract FastAPI error.
        """

        try:

            detail = response.json().get(

                "detail"

            )

        except Exception:

            detail = None

        if isinstance(

            detail,

            str

        ):

            return detail

        if isinstance(

            detail,

            list

        ):

            errors = []

            for item in detail:

                field = ".".join(

                    map(

                        str,

                        item.get(

                            "loc",

                            []

                        )[1:]

                    )

                )

                msg = item.get(

                    "msg",

                    ""

                )

                errors.append(

                    f"{field}: {msg}"

                )

            return "; ".join(errors)

        return (

            f"HTTP "

            f"{response.status_code} "

            f"{response.reason}"

        )

    # ======================================================
    # Generic Request
    # ======================================================

    def _request(

        self,

        method: str,

        url: str,

        **kwargs

    ) -> APIResponse:

        """
        Generic request handler.
        """

        try:

            response = self.session.request(

                method,

                url,

                timeout=self.timeout,

                **kwargs

            )

        except requests.ConnectionError:

            return self._error(

                "Unable to connect to server."

            )

        except requests.Timeout:

            return self._error(

                "Server timeout."

            )

        except requests.RequestException as e:

            return self._error(

                str(e)

            )

        if not response.ok:

            return self._error(

                self._extract_error(

                    response

                ),

                response.status_code

            )

        try:

            return response.json()

        except Exception:

            return self._error(

                "Invalid JSON response."

            )


    # ======================================================
    # Generic GET
    # ======================================================

    def get(
        self,
        url: str,
        params: Optional[dict] = None
    ) -> APIResponse:
        """
        Generic GET request.
        """

        return self._request(
            "GET",
            url,
            params=params
        )

    # ======================================================
    # Generic POST
    # ======================================================

    def post(
        self,
        url: str,
        payload: dict
    ) -> APIResponse:
        """
        Generic POST request.
        """

        return self._request(
            "POST",
            url,
            json=payload
        )

    # ======================================================
    # Authentication APIs
    # ======================================================

    def login(
        self,
        payload: dict
    ) -> APIResponse:
        """
        User Login.
        """

        result = self.post(
            LOGIN_API,
            payload
        )

        token = result.get(
            "access_token"
        )

        if token:

            self.set_token(
                token
            )

        return result

    def register(
        self,
        payload: dict
    ) -> APIResponse:
        """
        User Registration.
        """

        return self.post(
            REGISTER_API,
            payload
        )

    def logout(
        self
    ) -> None:
        """
        Logout current user.
        """

        self.clear_token()

    # ======================================================
    # Health APIs
    # ======================================================

    def health_check(
        self
    ) -> APIResponse:
        """
        Server Health Check.
        """

        return self.get(
            HEALTH_API
        )

    def health_dashboard(
        self,
        user_id: int
    ) -> APIResponse:
        """
        Get Health Dashboard.
        """

        return self.get(
            f"{HEALTH_DASHBOARD_API}/{user_id}"
        )

    def is_backend_online(
        self
    ) -> bool:
        """
        Lightweight backend status check.
        """

        try:

            response = self.session.get(

                HEALTH_API,

                timeout=HEALTH_CHECK_TIMEOUT

            )

            return response.ok

        except requests.RequestException:

            return False


    # ======================================================
    # AI - Weight Prediction
    # ======================================================

    def predict_weight(
        self,
        payload: dict
    ) -> APIResponse:
        """
        Predict user weight.
        """

        return self.post(
            WEIGHT_PREDICTION_API,
            payload
        )

    # ======================================================
    # AI - Calorie Recommendation
    # ======================================================

    def recommend_calories(
        self,
        payload: dict
    ) -> APIResponse:
        """
        Get calorie recommendation.
        """

        return self.post(
            CALORIE_API,
            payload
        )

    # ======================================================
    # AI - Macro Recommendation
    # ======================================================

    def recommend_macros(
        self,
        payload: dict
    ) -> APIResponse:
        """
        Get macro recommendation.
        """

        return self.post(
            MACRO_API,
            payload
        )

    # ======================================================
    # AI - Hydration Recommendation
    # ======================================================

    def recommend_hydration(
        self,
        payload: dict
    ) -> APIResponse:
        """
        Get hydration recommendation.
        """

        return self.post(
            HYDRATION_API,
            payload
        )

    # ======================================================
    # AI - Workout Recommendation
    # ======================================================

    def recommend_workout(
        self,
        payload: dict
    ) -> APIResponse:
        """
        Get workout recommendation.
        """

        return self.post(
            WORKOUT_API,
            payload
        )

    # ======================================================
    # AI - Meal Recommendation
    # ======================================================

    def recommend_meals(
        self,
        payload: dict
    ) -> APIResponse:
        """
        Get meal recommendation.
        """

        return self.post(
            MEAL_API,
            payload
        )

    # ======================================================
    # AI - Health Score
    # ======================================================

    def health_score(
        self,
        payload: dict
    ) -> APIResponse:
        """
        Calculate health score.
        """

        return self.post(
            HEALTH_SCORE_API,
            payload
        )

# ==========================================================
# Streamlit Client Factory
# ==========================================================

def get_client() -> APIClient:
    """
    Return a per-user API client stored in Streamlit
    session_state.

    Each logged-in user gets their own APIClient instance.
    """

    import streamlit as st

    if "api_client" not in st.session_state:

        token = st.session_state.get(
            "access_token"
        )

        st.session_state.api_client = APIClient(
            token=token
        )

    return st.session_state.api_client


# ==========================================================
# Default Client
# ==========================================================

client = APIClient()


# ==========================================================
# Convenience Functions
# ==========================================================

def login(payload: dict) -> APIResponse:

    return get_client().login(payload)


def register(payload: dict) -> APIResponse:

    return get_client().register(payload)


def predict_weight(payload: dict) -> APIResponse:

    return get_client().predict_weight(payload)


def recommend_calories(payload: dict) -> APIResponse:

    return get_client().recommend_calories(payload)


def recommend_macros(payload: dict) -> APIResponse:

    return get_client().recommend_macros(payload)


def recommend_hydration(payload: dict) -> APIResponse:

    return get_client().recommend_hydration(payload)


def recommend_workout(payload: dict) -> APIResponse:

    return get_client().recommend_workout(payload)


def recommend_meals(payload: dict) -> APIResponse:

    return get_client().recommend_meals(payload)


def health_score(payload: dict) -> APIResponse:

    return get_client().health_score(payload)


def health_dashboard(user_id: int) -> APIResponse:

    return get_client().health_dashboard(user_id)


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("AI Fitness Intelligence Platform")

    print("Streamlit API Client Test")

    print("=" * 70)

    if client.is_backend_online():

        print("✅ Backend Status : ONLINE")

    else:

        print("❌ Backend Status : OFFLINE")

    print("=" * 70)