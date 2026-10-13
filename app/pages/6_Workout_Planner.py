import streamlit as st

st.set_page_config(
    page_title="Workout Planner",
    page_icon="🏋",
    layout="wide"
)

st.title("🏋 AI Workout Planner")

goal = st.selectbox(
    "Goal",
    [
        "Weight Loss",
        "Muscle Gain",
        "General Fitness"
    ]
)

days = st.slider(
    "Workout Days / Week",
    3,
    6,
    5
)

if st.button("Generate Workout"):

    if goal == "Weight Loss":

        workout = [
            "30 min Cardio",
            "HIIT",
            "Full Body",
            "Core",
            "Cardio"
        ]

    elif goal == "Muscle Gain":

        workout = [
            "Chest",
            "Back",
            "Legs",
            "Shoulders",
            "Arms"
        ]

    else:

        workout = [
            "Full Body",
            "Walking",
            "Yoga",
            "Core",
            "Stretching"
        ]

    st.success("Workout Plan")

    for i in range(days):

        st.write(f"Day {i+1} : {workout[i]}")