"""
==============================================================

AI Fitness Intelligence Platform

Workout Recommendation

Author      : Harsh

Description :
AI-powered Workout Recommendation

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

    page_title="Workout Recommendation",

    page_icon="🏋️",

    layout="wide",

)

render_sidebar()

client = get_client()

# ==========================================================
# Header
# ==========================================================

section_header(

    "🏋️ AI Workout Recommendation",

    "Generate a personalized workout plan based on your preferred workout split and difficulty."

)

# ==========================================================
# Input Form
# ==========================================================

with st.form(

    "workout_form"

):

    col1, col2 = st.columns(2)

    with col1:

        split = st.selectbox(

            "Workout Split",

            [

                "Full Body",

                "Push Pull Legs",

                "Upper Lower",

                "Bro Split",

                "Strength",

                "Cardio",

                "HIIT",

                "Home Workout",

            ],

        )

    with col2:

        difficulty = st.selectbox(

            "Difficulty Level",

            [

                "Beginner",

                "Intermediate",

                "Advanced",

            ],

            index=1,

        )

    submitted = st.form_submit_button(

        "🏋️ Generate Workout Plan",

        use_container_width=True,

    )

# ==========================================================
# Stop Until User Clicks
# ==========================================================

if not submitted:

    st.info(

        "Select your workout preferences and click **Generate Workout Plan**."

    )

    st.stop()

# ==========================================================
# Prepare Payload
# ==========================================================

payload = {

    "split": split,

    "difficulty": difficulty,

}

# ==========================================================
# API Call
# ==========================================================

with st.spinner(

    "Generating your AI workout plan..."

):

    response = client.recommend_workout(

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

            "Failed to generate workout recommendation."

        )

    )

    st.stop()

# ==========================================================
# Extract Workout
# ==========================================================

try:

    workout = response["workout"]

except KeyError:

    st.error(

        "Workout data not found in API response."

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
# Extract Workout Fields
# ==========================================================

workout_name = split

duration = "60 Minutes"

target = split

calories = 400

exercises = []

for muscle, items in workout.items():

    if isinstance(items, list):

        for item in items:

            item["muscle_group"] = muscle

            exercises.append(item)

# ==========================================================
# Success
# ==========================================================

st.success(

    "Workout plan generated successfully."

)

# ==========================================================
# Workout Summary
# ==========================================================

st.divider()

section_header(
    "🏋️ Workout Plan Summary",
    "Your personalized AI-generated workout plan."
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "💪 Workout",
        workout_name
    )

with col2:

    st.metric(
        "🎯 Target",
        target
    )

with col3:

    st.metric(
        "⏱ Duration",
        duration
    )

with col4:

    st.metric(
        "🔥 Calories",
        f"{calories} kcal"
    )

# ==========================================================
# Exercise List
# ==========================================================

st.divider()

section_header(
    "📋 Exercise List"
)

if exercises:

    import pandas as pd

    exercise_rows = []

    for i, exercise in enumerate(exercises, start=1):

        if isinstance(exercise, dict):

            exercise_rows.append({

                "No.": i,

                "Exercise": exercise.get(
                    "exercise_name",
                    "Unknown Exercise"
                ),

                "Sets": exercise.get(
                    "sets",
                    "-"
                ),

                "Reps": exercise.get(
                    "reps",
                    "-"
                ),

                "Rest": exercise.get(
                    "rest_seconds",
                    "-"
                ),

                "Muscle": exercise.get(
                    "muscle_group",
                    "-"
                )

            })

        else:

            exercise_rows.append({

                "No.": i,

                "Exercise": str(exercise),

                "Sets": "-",

                "Reps": "-",

                "Rest": "-"

            })

    exercise_df = pd.DataFrame(exercise_rows)

    st.dataframe(
        exercise_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "No exercises available."
    )

# ==========================================================
# Workout Statistics
# ==========================================================

st.divider()

section_header(
    "📊 Workout Statistics"
)

left, right = st.columns(2)

with left:

    st.info(f"""
### Workout Information

🏋️ Split : **{split}**

📈 Difficulty : **{difficulty}**

🎯 Target Muscle : **{target}**
""")

with right:

    st.info(f"""
### Session Details

⏱ Duration : **{duration}**

🔥 Estimated Calories : **{calories} kcal**

💪 Exercises : **{len(exercises)}**
""")

# ==========================================================
# Weekly Plan
# ==========================================================

st.divider()

section_header(
    "📅 Weekly Workout Schedule"
)

days = [

    "Monday",

    "Tuesday",

    "Wednesday",

    "Thursday",

    "Friday",

    "Saturday",

    "Sunday"

]

schedule = []

for day in days:

    if day == "Sunday":

        schedule.append({

            "Day": day,

            "Workout": "Rest & Recovery"

        })

    else:

        schedule.append({

            "Day": day,

            "Workout": workout_name

        })

st.table(schedule)

# ==========================================================
# AI Workout Recommendations
# ==========================================================

st.divider()

section_header(
    "💡 AI Workout Recommendations",
    "Personalized tips based on your workout plan."
)

recommendations = []

# Difficulty Based
if difficulty == "Beginner":

    recommendations.extend([

        "🏋️ Focus on learning proper exercise form.",

        "😴 Take 60–90 seconds rest between sets.",

        "📈 Increase weights gradually each week.",

    ])

elif difficulty == "Intermediate":

    recommendations.extend([

        "💪 Apply progressive overload every week.",

        "🔥 Train each muscle group twice weekly if possible.",

        "🥗 Maintain sufficient protein intake for recovery.",

    ])

else:

    recommendations.extend([

        "🏆 Prioritize recovery and mobility sessions.",

        "⚡ Include advanced compound movements.",

        "📊 Track volume, intensity, and progression.",

    ])

# Workout Split Tips
if split == "Push Pull Legs":

    recommendations.append(
        "📅 Follow a 6-day Push-Pull-Legs schedule for best results."
    )

elif split == "Full Body":

    recommendations.append(
        "🏋️ Perform full-body workouts 3–4 times per week."
    )

elif split == "Upper Lower":

    recommendations.append(
        "💪 Alternate Upper and Lower body sessions throughout the week."
    )

elif split == "Cardio":

    recommendations.append(
        "❤️ Mix moderate and high-intensity cardio sessions."
    )

elif split == "HIIT":

    recommendations.append(
        "⚡ Keep HIIT sessions between 20–30 minutes."
    )

# Display Recommendations
for tip in recommendations:

    st.success(tip)

# ==========================================================
# Workout Notes
# ==========================================================

st.divider()

section_header(
    "📋 Workout Notes"
)

st.info(f"""
### Training Summary

🏋️ Workout Split: **{split}**

📈 Difficulty: **{difficulty}**

🎯 Target: **{target}**

⏱ Estimated Duration: **{duration}**

🔥 Estimated Calories Burned: **{calories} kcal**

💧 Stay hydrated before, during and after every workout.

🍗 Consume sufficient protein to support muscle recovery.

😴 Sleep 7–9 hours every night for optimal recovery.
""")

# ==========================================================
# Download Workout Plan
# ==========================================================

import json

report = {

    "Workout": workout_name,

    "Split": split,

    "Difficulty": difficulty,

    "Target": target,

    "Duration": duration,

    "Calories": calories,

    "Exercises": exercises,

}

st.download_button(

    label="📥 Download Workout Plan",

    data=json.dumps(report, indent=4),

    file_name="workout_plan.json",

    mime="application/json",

    use_container_width=True,

)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "AI Fitness Intelligence Platform • Workout Recommendation Module • Version 1.0"
)