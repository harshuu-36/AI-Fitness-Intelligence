"""
==============================================================
AI Fitness Intelligence Platform
Dashboard

Author      : Harsh
Description : Main dashboard showing health summary, AI insights,
              fitness metrics, charts and backend status.
==============================================================
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import date, datetime

import pandas as pd
import streamlit as st

from api_client import get_client
from components.cards import info_card, metric_card, section_header
from components.charts import health_gauge, line_chart, macro_chart
from components.sidebar import render_sidebar
from config import (
    AI_MODULES,
    APP_ICON,
    APP_NAME,
    DATABASE,
    DEVELOPER,
    FOOTER,
    ML_MODELS,
    REST_APIS,
)

# ==========================================================
# Page Configuration (must be the first Streamlit call)
# ==========================================================
st.set_page_config(
    page_title="Dashboard",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# Constants
# ==========================================================
# Goal
GOAL_WEIGHT_KG = 70.0

# Default Nutrition Values
DEFAULT_CARBS_G = 280
DEFAULT_FAT_G = 70

# Cache (seconds)
DEMO_CACHE_TTL = 60

WEEK_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
WEEK_WEIGHTS = [72.4, 72.2, 72.1, 71.9, 71.8, 71.7, 71.5]

QUICK_ACTIONS = [
    ("⚖ Predict Weight", "pages/02_Weight_Prediction.py"),
    ("🔥 Calories", "pages/03_Calorie_Recommendation.py"),
    ("🥗 Macros", "pages/04_Macro_Recommendation.py"),
    ("💧 Hydration", "pages/05_Hydration.py"),
    ("🏋 Workout", "pages/06_Workout_Recommendation.py"),
    ("🍽 Meals", "pages/07_Meal_Recommendation.py"),
    ("❤️ Health Score", "pages/08_Health_Score.py"),
]

FITNESS_TIPS = [
    "🥗 Consume sufficient protein every day.",
    "💧 Drink at least 3 liters of water daily.",
    "😴 Sleep for 7–8 hours every night.",
    "🏋 Train consistently and progressively.",
    "🚶 Walk at least 8,000–10,000 steps daily.",
]

RECENT_ACTIVITY = [
    "✅ Weight prediction completed.",
    "🔥 Calories recommendation generated.",
    "🥗 Macro recommendation calculated.",
    "💧 Hydration recommendation generated.",
    "🏋 Workout plan created.",
]


# ==========================================================
# Data
# ==========================================================
@dataclass(frozen=True)
class DashboardData:
    weight_history: pd.DataFrame
    calories_history: list[int]
    protein: int
    water: float
    sleep_history: list[float]
    health_score: int

    @property
    def current_weight(self) -> float:
        return float(self.weight_history["Weight"].iloc[-1])

    @property
    def previous_weight(self) -> float:
        return float(self.weight_history["Weight"].iloc[-2])

    @property
    def start_weight(self) -> float:
        return float(self.weight_history["Weight"].iloc[0])

    @property
    def calories(self) -> int:
        return self.calories_history[-1]

    @property
    def sleep(self) -> float:
        return self.sleep_history[-1]

    @property
    def average_weight(self) -> float:
        return float(self.weight_history["Weight"].mean())


@st.cache_resource(ttl=DEMO_CACHE_TTL)
def load_dashboard_data(day: str) -> DashboardData:
    """
    Temporary demo data (seeded per day so values stay stable).
    Replace with real API / SQL Server data later.
    """
    random_generator = random.Random(day)
    return DashboardData(
        weight_history=pd.DataFrame({"Day": WEEK_DAYS, "Weight": WEEK_WEIGHTS}),
        calories_history=[random_generator.randint(1900, 2700) for _ in WEEK_DAYS],
        protein=random_generator.randint(90, 180),
        water=round(random_generator.uniform(2.2, 4.5), 1),
        sleep_history=[round(random_generator.uniform(6, 9), 1) for _ in WEEK_DAYS],
        health_score=random_generator.randint(75, 98),
    )


def build_insights(data: DashboardData) -> list[str]:
    """Generate rule-based AI insights from today's data."""

    if data.health_score >= 90:
        insights = ["Excellent health score. Keep maintaining your routine."]
    elif data.health_score >= 75:
        insights = ["Good progress. Small improvements can boost your score."]
    else:
        insights = ["Focus on nutrition, sleep and exercise consistency."]

    if data.protein < 120:
        insights.append("Increase protein intake for better muscle recovery.")
    if data.water < 3:
        insights.append("Drink more water throughout the day.")
    if data.sleep < 7:
        insights.append("Try to sleep at least 7–8 hours.")

    return insights

def get_greeting(hour: int) -> str:
    """
    Return greeting according to current time.
    """
    if hour < 12:
        return "Good Morning"
    if hour < 17:
        return "Good Afternoon"
    return "Good Evening"

# ==========================================================
# Hero Header
# ==========================================================

def render_hero() -> None:

    current_time = datetime.now()

    greeting = get_greeting(
        current_time.hour
    )

    today = current_time.strftime(
        "%A, %d %B %Y"
    )

    st.markdown(
        f"""
<div style="
background:linear-gradient(135deg,#2563eb,#1e3a8a);
padding:28px;
border-radius:18px;
color:white;
margin-bottom:20px;
box-shadow:0 6px 18px rgba(0,0,0,.15);
">

<h2 style="margin:0;">
{greeting}, Mayank 👋
</h2>

<p style="
font-size:18px;
margin-top:8px;
margin-bottom:6px;
">

{APP_NAME}

</p>

<p style="
opacity:.9;
font-size:15px;
">

Your AI Powered Fitness Companion

</p>

<hr style="
border:.5px solid rgba(255,255,255,.25);
">

<p style="margin:0;">
📅 {today}
</p>

</div>
""",
        unsafe_allow_html=True,
    )

def goal_progress(start: float, current: float, goal: float) -> float:
    """Fraction of the distance from start weight to goal weight covered (0–1)."""
    total = start - goal
    if total == 0:
        return 1.0
    return max(0.0, min(1.0, (start - current) / total))


# ==========================================================
# Sections
# ==========================================================
def render_welcome(username: str, backend_online: bool) -> None:

    now = datetime.now()

    greeting = get_greeting(now.hour)

    status = "🟢 Online" if backend_online else "🔴 Offline"

    color = "#22c55e" if backend_online else "#ef4444"

    st.markdown(
        f"""
<div style="
background:linear-gradient(135deg,#2563eb,#1e3a8a);
padding:30px;
border-radius:20px;
color:white;
margin-bottom:25px;
box-shadow:0 8px 25px rgba(0,0,0,.15);
">

<h2 style="margin:0;">
{greeting}, {username} 👋
</h2>

<p style="
font-size:18px;
margin-top:10px;
">

Welcome to the AI Fitness Intelligence Platform

</p>

<p style="
opacity:.9;
">

Track workouts • Monitor nutrition • Analyze health • AI Recommendations

</p>

<hr style="
border:.5px solid rgba(255,255,255,.25);
">

<div style="
display:flex;
justify-content:space-between;
">

<span>
📅 {now.strftime("%A, %d %B %Y")}
</span>

<span style="color:{color};font-weight:bold;">
{status}
</span>

</div>

</div>
""",
        unsafe_allow_html=True,
    )


def render_summary(data: DashboardData) -> None:

    section_header(
        "📊 Today's Health Summary",
        "Today's fitness overview"
    )

    weight_delta = data.current_weight - data.previous_weight

    c1, c2, c3 = st.columns(3)

    with c1:

        metric_card(
            "⚖ Weight",
            f"{data.current_weight:.1f} kg",
            f"{weight_delta:+.1f} kg",
            delta_color="inverse"
        )

    with c2:

        metric_card(
            "🔥 Calories",
            f"{data.calories:,} kcal"
        )

    with c3:

        metric_card(
            "❤️ Health Score",
            f"{data.health_score}/100"
        )

    c4, c5, c6 = st.columns(3)

    with c4:

        metric_card(
            "💪 Protein",
            f"{data.protein} g"
        )

    with c5:

        metric_card(
            "💧 Water",
            f"{data.water} L"
        )

    with c6:

        metric_card(
            "😴 Sleep",
            f"{data.sleep:.1f} hrs"
        )


def render_analytics(data: DashboardData) -> None:
    section_header("📈 Health Analytics", "AI generated health insights")
    left, right = st.columns([2, 1])

    with left:
        line_chart(
            data=data.weight_history,
            x="Day",
            y="Weight",
            title="Weight Trend",
        )
    with right:
        health_gauge(data.health_score)


def render_nutrition(data: DashboardData) -> None:
    section_header("🥗 Nutrition Overview")
    left, right = st.columns(2)

    with left:
        macro_chart(
            protein=data.protein,
            carbs=DEFAULT_CARBS_G,
            fat=DEFAULT_FAT_G,
        )
    with right:
        info_card(
            "Daily Nutrition Summary",
            (
                f"- Calories Consumed: **{data.calories:,} kcal**\n"
                f"- Protein Intake: **{data.protein} g**\n"
                f"- Water Intake: **{data.water} L**\n"
                f"- Sleep: **{data.sleep} hrs**\n"
                f"- Current Weight: **{data.current_weight:.1f} kg**"
            ),
        )


def render_insights(data: DashboardData) -> None:
    section_header("🤖 AI Insights")
    for insight in build_insights(data):
        st.success(insight)


def render_quick_actions() -> None:
    section_header("⚡ Quick Actions", "Access AI modules instantly")

    per_row = 4
    for start in range(0, len(QUICK_ACTIONS), per_row):
        row = QUICK_ACTIONS[start:start + per_row]
        cols = st.columns(per_row)
        for col, (label, page) in zip(cols, row):
            with col:
                if st.button(label, key=f"qa_{page}", use_container_width=True):
                    st.switch_page(page)


def render_weekly_summary(data: DashboardData) -> None:
    section_header("📅 Weekly Summary")
    col1, col2, col3 = st.columns(3)

    col1.metric("Average Weight", f"{data.weight_history['Weight'].mean():.2f} kg")
    col2.metric("Average Calories", f"{sum(data.calories_history) / len(data.calories_history):,.0f} kcal")
    col3.metric("Average Sleep", f"{sum(data.sleep_history) / len(data.sleep_history):.1f} hrs")


def render_goal_progress(data: DashboardData) -> None:
    section_header("🎯 Goal Progress")
    progress = goal_progress(data.start_weight, data.current_weight, GOAL_WEIGHT_KG)

    col1, col2, col3 = st.columns(3)
    col1.metric("Starting Weight", f"{data.start_weight:.1f} kg")
    col2.metric("Current Weight", f"{data.current_weight:.1f} kg")
    col3.metric("Target Weight", f"{GOAL_WEIGHT_KG:.1f} kg")

    st.progress(progress)
    st.caption(f"{progress * 100:.1f}% of goal achieved")


def render_recent_activity() -> None:
    section_header("📝 Recent Activity")
    st.markdown("\n".join(f"- {item}" for item in RECENT_ACTIVITY))


def render_system_status(backend_online: bool, username: str) -> None:
    section_header("🖥 System Information")
    now = datetime.now()
    left, right = st.columns(2)

    with left:
        st.subheader("System Health")
        if backend_online:
            st.success("✅ FastAPI Backend Connected")
        else:
            st.error("❌ Backend Offline")
        st.info(f"Database: {DATABASE}")

    with right:
        st.subheader("Session")
        st.write(f"**User:** {username}")
        st.write(f"**Date:** {now.strftime('%d %B %Y')}")
        st.write(f"**Time:** {now.strftime('%I:%M %p')}")


def render_platform_stats() -> None:
    section_header("📊 Platform Statistics", "Overall AI Fitness Platform Overview")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("AI Modules", AI_MODULES)
    col2.metric("ML Models", ML_MODELS)
    col3.metric("REST APIs", REST_APIS)
    col4.metric("Database", DATABASE)


def render_controls() -> None:
    section_header("🔄 Dashboard Controls")

    if st.button("🔄 Refresh Dashboard", use_container_width=True):
        st.cache_data.clear()
        st.rerun()


def render_tips() -> None:
    with st.expander("💡 AI Fitness Tips"):
        st.markdown("\n".join(f"- {tip}" for tip in FITNESS_TIPS))


def render_footer() -> None:

    st.divider()

    st.markdown(
        f"""
<div style="
text-align:center;
padding:20px;
color:#9ca3af;
">

<h3>
{APP_ICON} {APP_NAME}
</h3>

<p>
Developed by <b>{DEVELOPER}</b>
</p>

<p>
FastAPI • SQL Server • Machine Learning • Streamlit
</p>

<p>
{FOOTER}
</p>

</div>
""",
        unsafe_allow_html=True,
    )

# ==========================================================
# Main
# ==========================================================
def main() -> None:
    st.session_state.setdefault("username", "Guest")
    username = st.session_state["username"]

    client = get_client()
    backend_online = client.is_backend_online()
    data = load_dashboard_data(date.today().isoformat())

    render_sidebar()

    section_header("🏠 Dashboard", "AI Powered Fitness Analytics")
    render_welcome(username, backend_online)

    render_summary(data)
    st.divider()

    render_analytics(data)
    st.divider()

    render_nutrition(data)
    st.divider()

    render_insights(data)
    st.divider()

    render_quick_actions()
    st.divider()

    render_weekly_summary(data)
    st.divider()

    render_goal_progress(data)
    st.divider()

    render_recent_activity()
    st.divider()

    render_system_status(backend_online, username)
    st.divider()

    render_platform_stats()
    st.divider()

    render_controls()
    render_tips()
    st.divider()

    render_footer()


main()