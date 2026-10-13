import streamlit as st

st.set_page_config(
    page_title="AI Recommendations",
    layout="wide"
)

st.title("🤖 AI Fitness Recommendations")

bmi = st.number_input(
    "BMI",
    10.0,
    50.0,
    24.0
)

sleep = st.number_input(
    "Sleep Hours",
    0.0,
    12.0,
    7.0
)

calories = st.number_input(
    "Calories",
    0,
    6000,
    2200
)

if st.button("Get Recommendations"):

    recommendations = []

    if bmi > 25:
        recommendations.append("🏃 Lose weight with 30–45 min cardio daily.")

    elif bmi < 18.5:
        recommendations.append("🍚 Increase healthy calorie intake.")

    else:
        recommendations.append("✅ Maintain your current weight.")

    if sleep < 7:
        recommendations.append("😴 Sleep at least 7–8 hours daily.")

    if calories > 2800:
        recommendations.append("🥗 Reduce processed foods and sugary drinks.")

    if not recommendations:
        recommendations.append("🎉 You're doing great! Keep it up.")

    st.subheader("Your Recommendations")

    for item in recommendations:
        st.write(item)