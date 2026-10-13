"""
==============================================================

AI Fitness Intelligence Platform

Meal Recommendation

Author      : Harsh

Description :
AI-powered Meal Recommendation

==============================================================
"""

from __future__ import annotations

import streamlit as st

from api_client import get_client

from components.sidebar import render_sidebar

from components.cards import (
    section_header,
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Meal Recommendation",

    page_icon="🍽️",

    layout="wide",

)

render_sidebar()

client = get_client()

# ==========================================================
# Header
# ==========================================================

section_header(

    "🍽️ AI Meal Recommendation",

    "Generate a personalized meal plan based on your preferences."

)

# ==========================================================
# Input Form
# ==========================================================

with st.form(

    "meal_form"

):

    col1, col2 = st.columns(2)

    with col1:

        meal_type = st.selectbox(

            "Meal Type",

            [

                "Breakfast",

                "Lunch",

                "Dinner",

                "Snack",

                "Pre Workout",

                "Post Workout",

            ],

        )

    with col2:

        vegetarian = st.checkbox(

            "Vegetarian",

            value=True,

        )

    limit = st.slider(

        "Number of Meal Suggestions",

        min_value=1,

        max_value=10,

        value=5,

    )

    submitted = st.form_submit_button(

        "🍽️ Generate Meal Plan",

        use_container_width=True,

    )

# ==========================================================
# Stop Until User Clicks
# ==========================================================

if not submitted:

    st.info(

        "Select your meal preferences and click **Generate Meal Plan**."

    )

    st.stop()

# ==========================================================
# Prepare Payload
# ==========================================================

payload = {

    "meal_type": meal_type,

    "vegetarian": vegetarian,

    "limit": limit,

}

# ==========================================================
# API Call
# ==========================================================

with st.spinner(

    "Generating AI Meal Recommendation..."

):

    response = client.recommend_meals(

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

            "Failed to generate meal recommendation."

        )

    )

    st.stop()

# ==========================================================
# Extract Meals
# ==========================================================

try:

    meals = response["meals"]

except KeyError:

    st.error(

        "Meals not found in API response."

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
# Validate Meals
# ==========================================================

if not meals:

    st.warning(

        "No meals available for the selected criteria."

    )

    st.stop()

# ==========================================================
# Success
# ==========================================================

st.success(

    f"{len(meals)} meal recommendation(s) generated successfully."

)

# ==========================================================
# Meal Recommendations
# ==========================================================

st.divider()

section_header(
    "🍽️ Recommended Meals",
    "AI-generated meals based on your preferences."
)

total_calories = 0.0
total_protein = 0.0
total_carbs = 0.0
total_fat = 0.0

for index, meal in enumerate(meals, start=1):

    if not isinstance(meal, dict):

        meal = {
            "food_name": str(meal)
        }

    meal_name = meal.get(
        "food_name",
        f"Meal {index}"
    )

    calories = float(
        meal.get("calories", 0) or 0
    )

    protein = float(
        meal.get("protein", 0) or 0
    )

    carbs = float(
        meal.get("carbs", 0) or 0
    )

    fat = float(
        meal.get("fats", 0) or 0
    )

    description = meal.get(
        "description",
        "No description available."
    )

    total_calories += calories
    total_protein += protein
    total_carbs += carbs
    total_fat += fat

    with st.container(border=True):

        st.subheader(
            f"🍴 {meal_name}"
        )

        st.write(description)

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🔥 Calories",
                f"{calories:.0f} kcal"
            )

        with c2:
            st.metric(
                "🍗 Protein",
                f"{protein:.0f} g"
            )

        with c3:
            st.metric(
                "🍚 Carbs",
                f"{carbs:.0f} g"
            )

        with c4:
            st.metric(
                "🥑 Fat",
                f"{fat:.0f} g"
            )

        if meal.get("serving_size"):
            st.caption(
                f"🍽 Serving Size : {meal['serving_size']}"
            )

        if meal.get("goal"):
            st.caption(
                f"🎯 Goal : {meal['goal']}"
            )

        if meal.get("cuisine"):
            st.caption(
                f"🌍 Cuisine : {meal['cuisine']}"
            )

# ==========================================================
# Nutrition Summary
# ==========================================================

st.divider()

section_header(

    "📊 Nutrition Summary"

)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(

        "🔥 Calories",

        f"{total_calories:.0f} kcal"

    )

with col2:

    st.metric(

        "🍗 Protein",

        f"{total_protein:.1f} g"

    )

with col3:

    st.metric(

        "🍚 Carbs",

        f"{total_carbs:.1f} g"

    )

with col4:

    st.metric(

        "🥑 Fat",

        f"{total_fat:.1f} g"

    )

# ==========================================================
# Meals Table
# ==========================================================

st.divider()

section_header(

    "📋 Meal Summary"

)

import pandas as pd

meal_table = []

for meal in meals:

    if isinstance(meal, dict):

        meal_table.append({

            "Meal": meal.get("name", "-"),

            "Calories": meal.get("calories", 0),

            "Protein": meal.get("protein", 0),

            "Carbs": meal.get("carbs", 0),

            "Fat": meal.get("fat", 0),

        })

if meal_table:

    st.dataframe(

        pd.DataFrame(meal_table),

        use_container_width=True,

        hide_index=True

    )

# ==========================================================
# AI Nutrition Recommendations
# ==========================================================

st.divider()

section_header(
    "💡 AI Nutrition Recommendations",
    "Personalized suggestions based on your selected meal plan."
)

recommendations = []

# Meal Type Recommendations
if meal_type == "Breakfast":

    recommendations.extend([
        "🥣 Start your day with a protein-rich breakfast.",
        "🍌 Include fruits for vitamins and minerals.",
        "🥛 Add milk or yogurt for calcium."
    ])

elif meal_type == "Lunch":

    recommendations.extend([
        "🍚 Include complex carbohydrates for sustained energy.",
        "🥗 Fill half of your plate with vegetables.",
        "🍗 Ensure sufficient protein for muscle recovery."
    ])

elif meal_type == "Dinner":

    recommendations.extend([
        "🥦 Prefer a lighter dinner with lean protein.",
        "🍽️ Avoid overeating before bedtime.",
        "💧 Drink water throughout the evening."
    ])

elif meal_type == "Snack":

    recommendations.extend([
        "🥜 Choose healthy snacks like nuts and fruits.",
        "🍎 Avoid processed sugary snacks."
    ])

elif meal_type == "Pre Workout":

    recommendations.extend([
        "🍌 Eat 60–90 minutes before your workout.",
        "🍞 Choose easily digestible carbohydrates."
    ])

elif meal_type == "Post Workout":

    recommendations.extend([
        "🍗 Consume protein within 30–60 minutes after exercise.",
        "🍚 Replenish glycogen with quality carbohydrates."
    ])

# Vegetarian Advice
if vegetarian:

    recommendations.append(
        "🌱 Include paneer, tofu, soy chunks, lentils and beans for protein."
    )

else:

    recommendations.append(
        "🥩 Include lean meat, eggs and fish as quality protein sources."
    )

# Display Tips
for tip in recommendations:

    st.success(tip)

# ==========================================================
# Healthy Eating Tips
# ==========================================================

st.divider()

section_header(
    "🥗 Healthy Eating Tips"
)

st.info(f"""
### Daily Nutrition Guidelines

🍽️ Meal Type : **{meal_type}**

🥬 Vegetarian : **{"Yes" if vegetarian else "No"}**

🍴 Suggested Meals : **{len(meals)}**

💧 Drink at least **2.5–3.5 liters** of water daily.

🥦 Eat plenty of vegetables and fruits.

🍗 Include protein in every meal.

🍚 Prefer whole grains over refined carbohydrates.

🥜 Include healthy fats such as nuts and seeds.
""")

# ==========================================================
# Download Meal Plan
# ==========================================================

import json

report = {

    "Meal Type": meal_type,

    "Vegetarian": vegetarian,

    "Number of Meals": len(meals),

    "Meals": meals,

    "Total Calories": total_calories,

    "Total Protein": total_protein,

    "Total Carbohydrates": total_carbs,

    "Total Fat": total_fat,

}

st.download_button(

    label="📥 Download Meal Plan",

    data=json.dumps(report, indent=4),

    file_name="meal_recommendation.json",

    mime="application/json",

    use_container_width=True,

)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "AI Fitness Intelligence Platform • Meal Recommendation Module • Version 1.0"
)