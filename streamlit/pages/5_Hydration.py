"""
==============================================================
AI Fitness Intelligence Platform

Hydration Recommendation

Author      : Harsh

Description :
AI-powered Daily Hydration Recommendation
==============================================================
"""

from __future__ import annotations

import streamlit as st

from api_client import get_client

from components.sidebar import render_sidebar

from components.cards import (
    section_header,
)

from components.charts import (
    progress_chart,
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Hydration Recommendation",

    page_icon="💧",

    layout="wide",

)

render_sidebar()

client = get_client()

# ==========================================================
# Header
# ==========================================================

section_header(

    "💧 AI Hydration Recommendation",

    "Calculate your daily water intake based on your body weight and workout duration."

)

# ==========================================================
# Input Form
# ==========================================================

with st.form(

    "hydration_form"

):

    col1, col2 = st.columns(2)

    with col1:

        weight = st.number_input(

            "Weight (kg)",

            min_value=20.0,

            max_value=250.0,

            value=70.0,

            step=0.5,

        )

    with col2:

        workout_minutes = st.number_input(

            "Workout Duration (minutes)",

            min_value=0,

            max_value=300,

            value=60,

            step=5,

        )

    submitted = st.form_submit_button(

        "💧 Calculate Water Intake",

        use_container_width=True,

    )

# ==========================================================
# Stop Until User Clicks
# ==========================================================

if not submitted:

    st.info(

        "Enter your details and click **Calculate Water Intake**."

    )

    st.stop()

# ==========================================================
# Prepare Payload
# ==========================================================

payload = {

    "weight": weight,

    "workout_minutes": workout_minutes,

}

# ==========================================================
# API Call
# ==========================================================

with st.spinner(

    "Calculating hydration recommendation..."

):

    response = client.recommend_hydration(

        payload

    )

# ==========================================================
# Validate Response
# ==========================================================

if response is None:

    st.error(

        "Unable to connect to the API."

    )

    st.stop()

if isinstance(response, dict) and response.get("success") is False:

    st.error(

        response.get(

            "message",

            "Failed to generate hydration recommendation."

        )

    )

    st.stop()

# ==========================================================
# Extract Response
# ==========================================================

try:

    weight_kg = float(

        response["weight_kg"]

    )

    workout_minutes = int(

        response["workout_minutes"]

    )

    base_water_ml = float(

        response["base_water_ml"]

    )

    extra_water_ml = float(

        response["extra_water_ml"]

    )

    total_water_ml = float(

        response["total_water_ml"]

    )

    total_water_liters = float(

        response["total_water_liters"]

    )

except KeyError as e:

    st.error(

        f"Missing API field: {e}"

    )

    st.json(response)

    st.stop()

except Exception as e:

    st.error(

        f"Unexpected Error: {e}"

    )

    st.json(response)

    st.stop()

# ==========================================================
# Success
# ==========================================================

st.success(

    "Hydration recommendation generated successfully."

)

# ==========================================================
# Hydration Results
# ==========================================================

st.divider()

section_header(

    "💧 Hydration Recommendation Results",

    "Your personalized daily water intake."

)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        label="💧 Base Water",

        value=f"{base_water_ml:,.0f} ml",

    )

with col2:

    st.metric(

        label="🏋️ Extra Water",

        value=f"{extra_water_ml:,.0f} ml",

    )

with col3:

    st.metric(

        label="💦 Total Water",

        value=f"{total_water_liters:.2f} L",

        delta=f"{total_water_ml:,.0f} ml",

    )

# ==========================================================
# Progress Chart
# ==========================================================

st.divider()

section_header(

    "📊 Daily Hydration Progress"

)

progress_chart(

    current=total_water_ml,

    target=4000,

    title="Recommended Water Intake",

)

# ==========================================================
# Water Breakdown
# ==========================================================

st.divider()

section_header(

    "📋 Water Intake Summary"

)

summary = {

    "Weight (kg)": round(weight_kg, 1),

    "Workout (minutes)": workout_minutes,

    "Base Water (ml)": round(base_water_ml),

    "Extra Water (ml)": round(extra_water_ml),

    "Total Water (ml)": round(total_water_ml),

    "Total Water (liters)": round(total_water_liters, 2),

}

st.json(

    summary

)

# ==========================================================
# Quick Statistics
# ==========================================================

st.divider()

section_header(

    "📈 Hydration Statistics"

)

left, right = st.columns(2)

with left:

    st.info(

        f"""
### Daily Water Goal

💧 **{total_water_liters:.2f} Liters**

This includes your normal daily requirement plus
extra water needed for your workout.
"""
    )

with right:

    workout_bonus = (
        (extra_water_ml / total_water_ml) * 100
        if total_water_ml > 0
        else 0
    )

    st.info(

        f"""
### Workout Contribution

🏋️ Extra Water: **{extra_water_ml:.0f} ml**

📊 Workout Contribution:
**{workout_bonus:.1f}%**
"""
    )

# ==========================================================
# AI Hydration Recommendations
# ==========================================================

st.divider()

section_header(
    "💡 AI Hydration Recommendations",
    "Personalized tips to help you stay hydrated."
)

recommendations = []

# Water Intake
if total_water_liters < 2.5:

    recommendations.append(
        "💧 Increase your daily water intake."
    )

elif total_water_liters < 3.5:

    recommendations.append(
        "✅ Your daily hydration is within a healthy range."
    )

else:

    recommendations.append(
        "🏋️ High hydration requirement due to activity level."
    )

# Workout Advice
if workout_minutes >= 90:

    recommendations.append(
        "🏃 Drink water before, during and after long workouts."
    )

elif workout_minutes >= 45:

    recommendations.append(
        "🥤 Carry a water bottle during exercise."
    )

# General Tips
recommendations.extend([
    "🍉 Eat water-rich fruits like watermelon and oranges.",
    "🥒 Include cucumber and leafy vegetables in meals.",
    "☕ Limit sugary drinks and excessive caffeine.",
    "💧 Sip water regularly instead of drinking large amounts at once."
])

for tip in recommendations:

    st.success(tip)

# ==========================================================
# Hydration Tips
# ==========================================================

st.divider()

section_header(
    "📋 Daily Hydration Guide"
)

st.info(f"""
### Your Daily Water Target

💧 **{total_water_liters:.2f} Liters**

Base Water : **{base_water_ml:.0f} ml**

Workout Water : **{extra_water_ml:.0f} ml**

Total Water : **{total_water_ml:.0f} ml**

Try to drink water throughout the day instead of all at once.
""")

# ==========================================================
# Download Report
# ==========================================================

import json

st.download_button(
    label="📥 Download Hydration Report",
    data=json.dumps(summary, indent=4),
    file_name="hydration_report.json",
    mime="application/json",
    use_container_width=True,
)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "AI Fitness Intelligence Platform • Hydration Recommendation Module • Version 1.0"
)