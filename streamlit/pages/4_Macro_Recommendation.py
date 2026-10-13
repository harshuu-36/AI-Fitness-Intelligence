"""
==============================================================
AI Fitness Intelligence Platform

Macro Recommendation

Author      : Harsh

Description :
AI-powered Macronutrient Recommendation
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
    macro_chart,
    bar_chart,
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Macro Recommendation",

    page_icon="🥗",

    layout="wide",

)

render_sidebar()

client = get_client()

# ==========================================================
# Header
# ==========================================================

section_header(

    "🥗 AI Macro Recommendation",

    "Calculate your daily Protein, Carbs, Fat and Fiber intake."

)

# ==========================================================
# Input Form
# ==========================================================

with st.form(

    "macro_form"

):

    col1, col2 = st.columns(2)

    with col1:

        weight = st.number_input(

            "Weight (kg)",

            min_value=30.0,

            max_value=250.0,

            value=70.0,

            step=0.5,

        )

        total_calories = st.number_input(

            "Daily Calories",

            min_value=1000.0,

            max_value=7000.0,

            value=2500.0,

            step=50.0,

        )

    with col2:

        goal = st.selectbox(

            "Fitness Goal",

            [

                "Weight Loss",

                "Maintenance",

                "Weight Gain",

            ],

        )

    submitted = st.form_submit_button(

        "🥗 Calculate Macros",

        use_container_width=True,

    )

# ==========================================================
# Stop Until User Clicks
# ==========================================================

if not submitted:

    st.info(

        "Fill in your details and click **Calculate Macros**."

    )

    st.stop()

# ==========================================================
# Prepare Payload
# ==========================================================

payload = {

    "weight": weight,

    "goal": goal,

    "total_calories": total_calories,

}

# ==========================================================
# API Call
# ==========================================================

with st.spinner(

    "Generating AI Macro Recommendation..."

):

    response = client.recommend_macros(

        payload

    )

# ==========================================================
# Error Handling
# ==========================================================

if not response:

    st.error(

        "No response received from API."

    )

    st.stop()

if response.get(

    "success"

) is False:

    st.error(

        response.get(

            "message",

            "Unable to generate macro recommendation."

        )

    )

    st.stop()

# ==========================================================
# Extract Response
# ==========================================================

try:

    calories = float(

        response["calories"]

    )

    protein_g = float(

        response["protein_g"]

    )

    carbs_g = float(

        response["carbs_g"]

    )

    fat_g = float(

        response["fat_g"]

    )

    fiber_g = float(

        response["fiber_g"]

    )

    goal = response["goal"]

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
# Success Message
# ==========================================================

st.success(

    "AI Macro Recommendation Generated Successfully."

)

# ==========================================================
# Results Dashboard
# ==========================================================

st.divider()

section_header(
    "📊 Macro Recommendation Results",
    "Your AI-generated daily macronutrient targets."
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="🔥 Calories",
        value=f"{calories:,.0f} kcal",
    )

with col2:

    st.metric(
        label="🍗 Protein",
        value=f"{protein_g:.1f} g",
    )

with col3:

    st.metric(
        label="🍚 Carbohydrates",
        value=f"{carbs_g:.1f} g",
    )

col4, col5 = st.columns(2)

with col4:

    st.metric(
        label="🥑 Fat",
        value=f"{fat_g:.1f} g",
    )

with col5:

    st.metric(
        label="🌾 Fiber",
        value=f"{fiber_g:.1f} g",
    )

# ==========================================================
# Macro Distribution Chart
# ==========================================================

st.divider()

section_header(
    "🥗 Macronutrient Distribution"
)

macro_chart(
    protein=protein_g,
    carbs=carbs_g,
    fat=fat_g,
)

# ==========================================================
# Macro Comparison
# ==========================================================

import pandas as pd

chart_data = pd.DataFrame(
    {
        "Nutrient": [
            "Protein",
            "Carbohydrates",
            "Fat",
            "Fiber",
        ],
        "Grams": [
            protein_g,
            carbs_g,
            fat_g,
            fiber_g,
        ],
    }
)

bar_chart(
    data=chart_data,
    x="Nutrient",
    y="Grams",
    title="Daily Macronutrient Recommendation",
)

# ==========================================================
# Summary
# ==========================================================

st.divider()

section_header(
    "📋 Recommendation Summary"
)

summary = {

    "Goal": goal,

    "Calories": round(calories, 2),

    "Protein (g)": round(protein_g, 2),

    "Carbohydrates (g)": round(carbs_g, 2),

    "Fat (g)": round(fat_g, 2),

    "Fiber (g)": round(fiber_g, 2),

}

st.json(summary)

# ==========================================================
# AI Nutrition Recommendations
# ==========================================================

st.divider()

section_header(
    "💡 AI Nutrition Recommendations",
    "Personalized nutrition advice based on your goal."
)

recommendations = []

# Goal Based Recommendations
if goal == "Weight Loss":

    recommendations.extend([
        "🔥 Maintain a calorie deficit of 300–500 kcal/day.",
        "🍗 Consume high-protein meals to preserve muscle mass.",
        "🥗 Include plenty of vegetables and fiber-rich foods.",
        "🚶 Walk at least 8,000–10,000 steps daily."
    ])

elif goal == "Maintenance":

    recommendations.extend([
        "⚖️ Maintain your current calorie intake.",
        "💪 Continue resistance training 3–5 times per week.",
        "🥦 Eat a balanced diet with all macronutrients.",
        "💧 Stay hydrated throughout the day."
    ])

elif goal == "Weight Gain":

    recommendations.extend([
        "🍚 Eat 300–500 kcal above maintenance calories.",
        "🏋️ Prioritize progressive overload in workouts.",
        "🥛 Include calorie-dense healthy foods.",
        "🍗 Aim for sufficient protein in every meal."
    ])

# Protein Check
recommended_protein = weight * 1.8

if protein_g < recommended_protein:

    recommendations.append(
        f"🍗 Increase protein intake to at least {recommended_protein:.0f} g/day."
    )

# Fiber Check
if fiber_g < 25:

    recommendations.append(
        "🌾 Increase fiber intake through fruits, vegetables, oats and legumes."
    )

# Display Recommendations
for tip in recommendations:

    st.success(tip)

# ==========================================================
# Daily Nutrition Tips
# ==========================================================

st.divider()

section_header(
    "🥗 Daily Nutrition Tips"
)

st.info(f"""
### Suggested Daily Intake

🔥 Calories : **{calories:.0f} kcal**

🍗 Protein : **{protein_g:.1f} g**

🍚 Carbohydrates : **{carbs_g:.1f} g**

🥑 Fat : **{fat_g:.1f} g**

🌾 Fiber : **{fiber_g:.1f} g**

💧 Drink at least **2.5–3.5 liters** of water daily.

🥗 Eat **4–6 balanced meals** throughout the day.
""")

# ==========================================================
# Download Report
# ==========================================================

import json

st.download_button(
    label="📥 Download Macro Report",
    data=json.dumps(summary, indent=4),
    file_name="macro_recommendation_report.json",
    mime="application/json",
    use_container_width=True,
)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "AI Fitness Intelligence Platform • Macro Recommendation Module • Version 1.0"
)