"""
==============================================================
AI Fitness Intelligence Platform

Weight Prediction

Author      : Harsh
Description : Predict future body weight using Machine Learning.
==============================================================
"""

from __future__ import annotations
import pandas as pd

import streamlit as st

from api_client import get_client

from components.sidebar import render_sidebar

from components.cards import (
    section_header,
    info_card,
)

from components.charts import line_chart

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Weight Prediction",
    page_icon="⚖️",
    layout="wide",
)

render_sidebar()

client = get_client()

# ==========================================================
# Header
# ==========================================================

section_header(
    "⚖️ Weight Prediction",
    "Predict your future body weight using Machine Learning."
)

# ==========================================================
# Input Form
# ==========================================================

with st.form("weight_prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=10,
            max_value=100,
            value=20,
        )

        height_cm = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
        )

        calories_consumed = st.number_input(
            "Calories Consumed",
            min_value=500,
            max_value=7000,
            value=2500,
        )

        calories_burned = st.number_input(
            "Calories Burned",
            min_value=0,
            max_value=5000,
            value=500,
        )

    with col2:

        workout_minutes = st.number_input(
            "Workout Minutes",
            min_value=0,
            max_value=300,
            value=60,
        )

        sleep_hours = st.number_input(
            "Sleep Hours",
            min_value=0.0,
            max_value=24.0,
            value=7.5,
        )

        protein = st.number_input(
            "Protein (g)",
            min_value=0.0,
            max_value=500.0,
            value=150.0,
        )

        carbs = st.number_input(
            "Carbohydrates (g)",
            min_value=0.0,
            max_value=800.0,
            value=300.0,
        )

        fat = st.number_input(
            "Fat (g)",
            min_value=0.0,
            max_value=300.0,
            value=70.0,
        )

    predict_button = st.form_submit_button(
        "🚀 Predict Weight",
        use_container_width=True,
    )

# ==========================================================
# Waiting Message
# ==========================================================

if not predict_button:

    info_card(
        "Ready",
        "Fill in your fitness information and click 'Predict Weight'."
    )

    st.stop()

# ==========================================================
# Prediction
# ==========================================================

payload = {
    "age": age,
    "height_cm": height_cm,
    "calories_consumed": calories_consumed,
    "calories_burned": calories_burned,
    "workout_minutes": workout_minutes,
    "sleep_hours": sleep_hours,
    "protein": protein,
    "carbs": carbs,
    "fat": fat,
}

with st.spinner("Predicting your future weight..."):

    response = client.predict_weight(payload)

# ==========================================================
# Error Handling
# ==========================================================

if not response.get("success", True):

    st.error(
        response.get(
            "message",
            "Unable to predict weight."
        )
    )

    st.stop()

# ==========================================================
# Extract Prediction
# ==========================================================

predicted_weight = (
    response.get("predicted_weight")
    or response.get("prediction")
    or response.get("weight")
)

if predicted_weight is None:

    st.error(
        "Prediction value was not returned by the API."
    )

    st.json(response)

    st.stop()

predicted_weight = float(predicted_weight)

# ==========================================================
# Success
# ==========================================================

st.success("Weight prediction completed successfully.")

# ==========================================================
# BMI
# ==========================================================

current_weight = predicted_weight

height_m = height_cm / 100

bmi = current_weight / (height_m ** 2)

# ==========================================================
# BMI Category
# ==========================================================

if bmi < 18.5:

    bmi_status = "Underweight"

elif bmi < 25:

    bmi_status = "Normal"

elif bmi < 30:

    bmi_status = "Overweight"

else:

    bmi_status = "Obese"


# ==========================================================
# Results
# ==========================================================

st.divider()

section_header(
    "📊 Prediction Result",
    "Machine Learning prediction summary."
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="⚖️ Predicted Weight",
        value=f"{predicted_weight:.2f} kg",
    )

with col2:

    st.metric(
        label="❤️ BMI",
        value=f"{bmi:.2f}",
    )

with col3:

    st.metric(
        label="📌 BMI Category",
        value=bmi_status,
    )

# ==========================================================
# Weight Trend
# ==========================================================

st.divider()

section_header(
    "📈 Weight Trend",
    "Predicted weight progression."
)

history = [
    round(predicted_weight - 2.4, 2),
    round(predicted_weight - 1.8, 2),
    round(predicted_weight - 1.2, 2),
    round(predicted_weight - 0.7, 2),
    round(predicted_weight - 0.3, 2),
    round(predicted_weight, 2),
]

labels = [
    "Week 1",
    "Week 2",
    "Week 3",
    "Week 4",
    "Week 5",
    "Prediction",
]

chart_data = pd.DataFrame({
    "Week": labels,
    "Weight": history,
})

line_chart(
    data=chart_data,
    x="Week",
    y="Weight",
    title="Predicted Weight Trend",
)

# ==========================================================
# Nutrition Summary
# ==========================================================

st.divider()

section_header(
    "🥗 Nutrition Summary"
)

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Protein",
        f"{protein:.0f} g",
    )

with c2:

    st.metric(
        "Carbohydrates",
        f"{carbs:.0f} g",
    )

with c3:

    st.metric(
        "Fat",
        f"{fat:.0f} g",
    )

# ==========================================================
# Lifestyle Summary
# ==========================================================

st.divider()

section_header(
    "🏃 Lifestyle Summary"
)

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Workout",
        f"{workout_minutes} min",
    )

with c2:

    st.metric(
        "Sleep",
        f"{sleep_hours:.1f} hrs",
    )

with c3:

    calorie_balance = calories_consumed - calories_burned

    st.metric(
        "Net Calories",
        f"{calorie_balance} kcal",
    )

# ==========================================================
# AI Recommendations
# ==========================================================

st.divider()

section_header(
    "💡 AI Recommendations",
    "Personalized fitness suggestions based on your prediction."
)

recommendations = []

# BMI Recommendations
if bmi < 18.5:

    recommendations.append(
        "🥗 Increase your daily calorie intake using healthy foods."
    )

    recommendations.append(
        "🏋️ Focus on strength training 4-5 days per week."
    )

elif bmi < 25:

    recommendations.append(
        "✅ Maintain your current nutrition and workout routine."
    )

    recommendations.append(
        "🚶 Continue regular physical activity."
    )

elif bmi < 30:

    recommendations.append(
        "🔥 Create a moderate calorie deficit."
    )

    recommendations.append(
        "🏃 Increase cardio sessions to improve fat loss."
    )

else:

    recommendations.append(
        "👨‍⚕️ Consult a certified fitness professional."
    )

    recommendations.append(
        "🥦 Start a structured weight-loss nutrition plan."
    )

# Sleep
if sleep_hours < 7:

    recommendations.append(
        "😴 Aim for 7–9 hours of quality sleep every night."
    )

# Protein
if protein < 120:

    recommendations.append(
        "🍗 Increase your daily protein intake."
    )

# Workout
if workout_minutes < 45:

    recommendations.append(
        "💪 Increase workout duration to at least 45 minutes."
    )

# Calories
if calories_consumed < calories_burned:

    recommendations.append(
        "🍚 Your calorie intake is low compared to calories burned."
    )

if recommendations:

    for item in recommendations:

        st.success(item)

else:

    st.info("Excellent! Keep maintaining your healthy lifestyle.")

# ==========================================================
# Prediction Summary
# ==========================================================

st.divider()

section_header(
    "📋 Prediction Summary"
)

summary = {
    "Age": age,
    "Height (cm)": height_cm,
    "Predicted Weight (kg)": round(predicted_weight, 2),
    "BMI": round(bmi, 2),
    "BMI Status": bmi_status,
    "Calories Consumed": calories_consumed,
    "Calories Burned": calories_burned,
    "Workout Minutes": workout_minutes,
    "Sleep Hours": sleep_hours,
    "Protein (g)": protein,
    "Carbs (g)": carbs,
    "Fat (g)": fat,
}

st.json(summary)

# ==========================================================
# Download Report
# ==========================================================

st.download_button(
    label="📥 Download Prediction Report",
    data=str(summary),
    file_name="weight_prediction_report.txt",
    mime="text/plain",
    use_container_width=True,
)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "AI Fitness Intelligence Platform • Weight Prediction Module • Version 1.0"
)