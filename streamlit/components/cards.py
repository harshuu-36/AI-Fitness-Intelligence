"""
==============================================================
AI Fitness Intelligence Platform
Cards Component

Author      : Harsh
Description : Reusable UI cards for Streamlit pages.
==============================================================
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import streamlit as st

# ==========================================================
# Constants
# ==========================================================
MISSING_VALUE = "—"

SCORE_GOOD = 80
SCORE_MODERATE = 60


# ==========================================================
# Helpers
# ==========================================================
def _format_value(value: Any) -> str:
    """Convert backend values into clean, human-readable text."""
    if value is None or value == "":
        return MISSING_VALUE
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if isinstance(value, float):
        return f"{value:,.2f}"
    if isinstance(value, (list, tuple, set)):
        return ", ".join(_format_value(item) for item in value) or MISSING_VALUE
    return str(value)


def _format_label(key: str) -> str:
    """'daily_calories' -> 'Daily Calories'; keeps 'BMI' as is."""
    label = str(key).replace("_", " ").strip()
    return label.title() if label.islower() else label


def _score_color(score: float) -> str:
    """Streamlit color name for :color[text] markdown."""
    if score >= SCORE_GOOD:
        return "green"
    if score >= SCORE_MODERATE:
        return "orange"
    return "red"


def _alert(kind: str, title: str, message: str = "") -> None:
    """Render a coloured alert box with title and message inside it."""
    render, icon = {
        "success": (st.success, "✅"),
        "error": (st.error, "❌"),
        "warning": (st.warning, "⚠️"),
        "info": (st.info, "ℹ️"),
    }[kind]

    body = f"**{title}**"
    if message:
        body += f"\n\n{message}"
    render(body, icon=icon)


# ==========================================================
# Message cards
# ==========================================================
def success_card(title: str, message: str = "") -> None:
    """Success message card."""
    _alert("success", title, message)


def error_card(title: str, message: str = "") -> None:
    """Error message card."""
    _alert("error", title, message)


def warning_card(title: str, message: str = "") -> None:
    """Warning message card."""
    _alert("warning", title, message)


def info_card(title: str, message: str = "") -> None:
    """Information card."""
    _alert("info", title, message)


# ==========================================================
# Data cards
# ==========================================================
def metric_card(
    title: str,
    value: Any,
    delta: str | None = None,
    *,
    help_text: str | None = None,
    delta_color: str = "normal",
) -> None:

    with st.container(border=True):

        st.metric(

            label=title,

            value=_format_value(value),

            delta=delta,

            delta_color=delta_color,

            help=help_text,

        )


def result_card(
    title: str,
    data: Mapping[str, Any],
) -> None:

    with st.container(border=True):

        st.subheader(title)

        st.divider()

        if not data:

            st.info("No data available.")

            return

        for key, value in data.items():

            c1, c2 = st.columns([1,2])

            with c1:

                st.markdown(

                    f"**{_format_label(key)}**"

                )

            with c2:

                st.write(

                    _format_value(value)

                )


def health_score_card(score: float, status: str) -> None:
    """Display health score with progress bar and colour-coded status."""
    safe_score = max(0.0, min(100.0, float(score)))
    color = _score_color(safe_score)

    with st.container(border=True):
        st.subheader("❤️ Health Score")
        st.metric("Score", f"{safe_score:.0f}/100")
        st.progress(safe_score / 100)
        st.markdown(f"**Status:** :{color}[{status}]")


def prediction_card(

    prediction,

    unit="",

    *,

    label="Predicted Value",

    decimals=2,

):

    if isinstance(

        prediction,

        (int,float)

    ):

        value=f"{prediction:.{decimals}f}"

        if unit:

            value+=f" {unit}"

    else:

        value="N/A"

    with st.container(border=True):

        st.subheader(

            "🤖 AI Prediction"

        )

        st.metric(

            label,

            value

        )

        st.progress(

            1.0

        )

        st.success(

            "Prediction generated successfully."

        )

def recommendation_card(

    recommendations,

):

    with st.container(border=True):

        st.subheader(

            "💡 AI Recommendations"

        )

        if not recommendations:

            st.warning(

                "No recommendations available."

            )

            return

        for i,item in enumerate(

            recommendations,

            start=1

        ):

            st.markdown(

                f"✅ **{i}.** {item}"

            )


# ==========================================================
# Layout
# ==========================================================
def section_header(title: str, description: str = "") -> None:
    """Display a section heading with optional description."""
    st.header(title)
    if description:
        st.caption(description)


# ==========================================================
# Manual test
# ==========================================================
if __name__ == "__main__":
    st.set_page_config(page_title="Cards Test", layout="wide")

    section_header("Cards Component", "Testing all reusable cards.")

    left, right = st.columns(2)

    with left:
        metric_card("Calories", 2400, "+150", delta_color="inverse")
        success_card("Success", "Prediction completed successfully.")
        warning_card("Warning", "Protein intake is low.")
        error_card("Error", "Unable to connect to API.")
        info_card("Information", "Workout recommendation generated.")

    with right:
        prediction_card(72.4567, "kg")
        result_card(
            "Macro Recommendation",
            {"protein": "150 g", "carbs": 320.456, "BMI": 22.1, "notes": None},
        )
        health_score_card(88, "Good")
        recommendation_card(
            [
                "Increase water intake",
                "Sleep at least 8 hours",
                "Consume more protein",
            ]
        )