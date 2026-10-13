"""
==============================================================
AI Fitness Intelligence Platform

Calorie Recommendation

Author      : Harsh
Description : AI-powered Daily Calorie Recommendation.
==============================================================
"""

from __future__ import annotations

import streamlit as st

from api_client import get_client

from components.sidebar import render_sidebar

from components.cards import (
    section_header,
    info_card,
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Calorie Recommendation",
    page_icon="🔥",
    layout="wide",
)

render_sidebar()

client = get_client()

# ==========================================================
# Header
# ==========================================================

section_header(
    "🔥 Calorie Recommendation",
    "Get your personalized daily calorie requirement."
)

# ==========================================================
# Input Form
# ==========================================================

with st.form("calorie_form"):

    col1, col2 = st.columns(2)

    with col1:

        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=250.0,
            value=70.0,
            step=0.5,
        )

        height = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.5,
        )

        age = st.number_input(
            "Age",
            min_value=10,
            max_value=100,
            value=22,
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
            ],
        )

        activity_level = st.selectbox(
            "Activity Level",
            [
                "Sedentary",
                "Light",
                "Moderate",
                "Active",
                "Very Active",
            ],
        )

        goal = st.selectbox(
            "Fitness Goal",
            [
                "Weight Loss",
                "Maintenance",
                "Weight Gain",
            ],
        )

    calculate_button = st.form_submit_button(
        "🔥 Calculate Calories",
        use_container_width=True,
    )

# ==========================================================
# Wait Until User Clicks Button
# ==========================================================

if not calculate_button:

    info_card(
        "Ready",
        "Enter your details and click 'Calculate Calories'."
    )

    st.stop()

# ==========================================================
# Prepare Payload
# ==========================================================

payload = {
    "weight": weight,
    "height": height,
    "age": age,
    "gender": gender,
    "activity_level": activity_level,
    "goal": goal,
}

# ==========================================================
# API Call
# ==========================================================

with st.spinner("Calculating your daily calorie requirement..."):

    response = client.recommend_calories(payload)

# ==========================================================
# Error Handling
# ==========================================================

if not response.get("success", True):

    st.error(
        response.get(
            "message",
            "Unable to calculate calorie recommendation."
        )
    )

    st.stop()

# ==========================================================
# Extract API Response
# ==========================================================

recommended_calories = response.get("recommended_calories")

if recommended_calories is None:

    st.error("Invalid response received from API.")

    st.json(response)

    st.stop()

recommended_calories = float(recommended_calories)



# ==========================================================
# Optional Values
# ==========================================================

bmr = float(response.get("bmr",0))

tdee = float(response.get("tdee",0))

goal_adjustment = response.get("goal_adjustment")

message = response.get("message", "")

# ==========================================================
# Success Message
# ==========================================================

st.success("Calorie recommendation generated successfully.")

# ==========================================================
# Results
# ==========================================================

st.divider()

section_header(
    "📊 Calorie Recommendation Result",
    "AI-generated daily calorie requirement."
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="🔥 Recommended Calories",
        value=f"{recommended_calories:,.0f} kcal/day",
    )

with col2:

    st.metric(
        label="⚡ BMR",
        value=f"{bmr:,.0f} kcal",
        help="Calories your body burns at complete rest.",
    )

with col3:

    st.metric(
        label="🏃 TDEE",
        value=f"{tdee:,.0f} kcal",
        help="Estimated calories burned in a day.",
    )

# ==========================================================
# BMI
# ==========================================================

height_m = height / 100

bmi = weight / (height_m ** 2)

if bmi < 18.5:

    bmi_status = "Underweight"

elif bmi < 25:

    bmi_status = "Normal"

elif bmi < 30:

    bmi_status = "Overweight"

else:

    bmi_status = "Obese"

st.divider()

section_header(
    "❤️ Body Mass Index"
)

left, right = st.columns(2)

with left:

    st.metric(
        "BMI",
        f"{bmi:.2f}",
    )

with right:

    st.metric(
        "Category",
        bmi_status,
    )

# ==========================================================
# Daily Calorie Breakdown
# ==========================================================

import pandas as pd

st.divider()

section_header(
    "📈 Daily Calorie Breakdown"
)

chart_data = pd.DataFrame(
    {
        "Metric": [
            "BMR",
            "TDEE",
            "Recommended"
        ],
        "Calories": [
            bmr,
            tdee,
            recommended_calories
        ]
    }
)

st.subheader("📈 Calories Comparison")

st.line_chart(
    data=chart_data,
    x="Metric",
    y="Calories",
)

# ==========================================================
# User Information
# ==========================================================

st.divider()

section_header(
    "👤 User Information"
)

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Weight",
        f"{weight:.1f} kg",
    )

with c2:

    st.metric(
        "Height",
        f"{height:.1f} cm",
    )

with c3:

    st.metric(
        "Age",
        age,
    )

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "Activity",
        activity_level,
    )

with c2:

    st.metric(
        "Goal",
        goal,
    )

# ==========================================================
# AI Recommendations
# ==========================================================

st.divider()

section_header(
    "💡 AI Recommendations",
    "Personalized calorie and nutrition advice."
)

recommendations = []

# Goal Based Recommendations
if goal == "Weight Loss":

    recommendations.append(
        "🔥 Maintain a calorie deficit of 300–500 kcal per day."
    )

    recommendations.append(
        "🚶 Aim for at least 8,000–10,000 steps daily."
    )

elif goal == "Maintenance":

    recommendations.append(
        "⚖️ Keep your calorie intake close to your TDEE."
    )

    recommendations.append(
        "💪 Continue regular strength training."
    )

elif goal == "Weight Gain":

    recommendations.append(
        "🍚 Eat 300–500 kcal above your maintenance calories."
    )

    recommendations.append(
        "🏋️ Focus on progressive overload in workouts."
    )

# BMI Based Recommendations
if bmi < 18.5:

    recommendations.append(
        "🥗 Increase calorie intake using nutrient-rich foods."
    )

elif bmi >= 25:

    recommendations.append(
        "🥦 Include more vegetables and lean protein."
    )

# Activity Recommendations
if activity_level == "Sedentary":

    recommendations.append(
        "🚶 Increase your daily physical activity."
    )

elif activity_level == "Very Active":

    recommendations.append(
        "💧 Stay hydrated throughout the day."
    )

# Display Recommendations
for item in recommendations:

    st.success(item)

# ==========================================================
# Daily Nutrition Tips
# ==========================================================

st.divider()

section_header(
    "🥗 Daily Nutrition Tips"
)

st.info(
    f"""
**Recommended Calories:** {recommended_calories:.0f} kcal/day

• Protein: 25–30% of calories

• Carbohydrates: 45–55% of calories

• Healthy Fats: 20–30% of calories

• Drink 2.5–3.5 liters of water daily

• Eat 4–6 balanced meals throughout the day
"""
)

# ==========================================================
# Summary
# ==========================================================

st.divider()

section_header(
    "📋 Recommendation Summary"
)

summary = {
    "Weight (kg)": weight,
    "Height (cm)": height,
    "Age": age,
    "Gender": gender,
    "Activity Level": activity_level,
    "Goal": goal,
    "BMI": round(bmi, 2),
    "BMI Category": bmi_status,
    "BMR": round(bmr, 2),
    "TDEE": round(tdee, 2),
    "Recommended Calories": round(recommended_calories, 2),
}

st.json(summary)

# ==========================================================
# Download Report
# ==========================================================

import json

st.download_button(
    label="📥 Download Report",
    data=json.dumps(summary, indent=4),
    file_name="calorie_recommendation_report.json",
    mime="application/json",
    use_container_width=True,
)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "AI Fitness Intelligence Platform • Calorie Recommendation Module • Version 1.0"
)
