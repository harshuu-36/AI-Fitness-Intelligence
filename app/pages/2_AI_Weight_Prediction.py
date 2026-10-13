import streamlit as st
from utils import predict_weight

st.set_page_config(
    page_title="AI Weight Prediction",
    layout="wide"
)

st.title("🤖 AI Weight Prediction")

st.write("Enter your fitness details below.")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        10,
        100,
        25
    )

    height = st.number_input(
        "Height (cm)",
        100,
        250,
        170
    )

    calories = st.number_input(
        "Calories Consumed",
        0,
        10000,
        2200
    )

    calories_burned = st.number_input(
        "Calories Burned",
        0,
        5000,
        450
    )

    workout_minutes = st.number_input(
        "Workout Minutes",
        0,
        500,
        60
    )

with col2:

    sleep = st.number_input(
        "Sleep Hours",
        0.0,
        15.0,
        7.5
    )

    protein = st.number_input(
        "Protein (g)",
        0,
        500,
        120
    )

    carbs = st.number_input(
        "Carbs (g)",
        0,
        1000,
        250
    )

    fat = st.number_input(
        "Fat (g)",
        0,
        300,
        70
    )

if st.button("Predict Weight"):

    prediction = predict_weight(

        age,

        height,

        calories,

        calories_burned,

        workout_minutes,

        sleep,

        protein,

        carbs,

        fat

    )

    st.success(
        f"🏋️ Predicted Weight : {prediction:.2f} kg"
    )