"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : Streamlit

Module     : User Profile

Author     : Harsh

Description:

User Profile Dashboard

==============================================================
"""

from __future__ import annotations

import streamlit as st

from components.sidebar import render_sidebar

from components.cards import (
    section_header,
)

from api_client import get_client

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(

    page_title="Profile",

    page_icon="👤",

    layout="wide",

)

render_sidebar()

client = get_client()

# ==========================================================
# Header
# ==========================================================

section_header(

    "👤 User Profile",

    "Manage your fitness profile and preferences."

)

# ==========================================================
# Personal Information
# ==========================================================

with st.form(

    "profile_form"

):

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input(

            "Full Name",

            value="Harsh"

        )

        email = st.text_input(

            "Email",

            value="mayank@example.com"

        )

        age = st.number_input(

            "Age",

            min_value=10,

            max_value=100,

            value=20

        )

        gender = st.selectbox(

            "Gender",

            [

                "Male",

                "Female",

                "Other"

            ],

            index=0

        )

    with col2:

        height = st.number_input(

            "Height (cm)",

            min_value=100.0,

            max_value=250.0,

            value=173.0,

            step=0.5

        )

        weight = st.number_input(

            "Weight (kg)",

            min_value=20.0,

            max_value=300.0,

            value=50.0,

            step=0.5

        )

        goal = st.selectbox(

            "Fitness Goal",

            [

                "Weight Loss",

                "Weight Gain",

                "Muscle Gain",

                "Maintain Weight"

            ],

            index=1

        )

        activity_level = st.selectbox(

            "Activity Level",

            [

                "Sedentary",

                "Light",

                "Moderate",

                "Active",

                "Very Active"

            ],

            index=3

        )

    save_profile = st.form_submit_button(

        "💾 Save Profile",

        use_container_width=True

    )

# ==========================================================
# Stop Until Save
# ==========================================================

if not save_profile:

    st.info(

        "Update your profile and click **Save Profile**."

    )

    st.stop()

# ==========================================================
# Save Profile
# ==========================================================

st.success(

    "Profile saved successfully."

)

# ==========================================================
# BMI Calculation
# ==========================================================

height_m = height / 100

bmi = weight / (height_m ** 2)

# ==========================================================
# BMI Status
# ==========================================================

if bmi < 18.5:

    bmi_status = "Underweight"

elif bmi < 25:

    bmi_status = "Healthy"

elif bmi < 30:

    bmi_status = "Overweight"

else:

    bmi_status = "Obese"

# ==========================================================
# BMR Calculation
# ==========================================================

if gender == "Male":

    bmr = (

        10 * weight +

        6.25 * height -

        5 * age +

        5

    )

else:

    bmr = (

        10 * weight +

        6.25 * height -

        5 * age -

        161

    )

# ==========================================================
# TDEE
# ==========================================================

activity_factor = {

    "Sedentary": 1.20,

    "Light": 1.375,

    "Moderate": 1.55,

    "Active": 1.725,

    "Very Active": 1.90

}

tdee = bmr * activity_factor.get(

    activity_level,

    1.55

)

# ==========================================================
# Goal Calories
# ==========================================================

if goal == "Weight Loss":

    target_calories = tdee - 500

elif goal == "Weight Gain":

    target_calories = tdee + 500

elif goal == "Muscle Gain":

    target_calories = tdee + 300

else:

    target_calories = tdee

# ==========================================================
# Dashboard
# ==========================================================

st.divider()

section_header(

    "📊 Health Metrics"

)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(

        "BMI",

        f"{bmi:.1f}"

    )

with col2:

    st.metric(

        "BMR",

        f"{bmr:.0f} kcal"

    )

with col3:

    st.metric(

        "TDEE",

        f"{tdee:.0f} kcal"

    )

with col4:

    st.metric(

        "Target Calories",

        f"{target_calories:.0f} kcal"

    )

# ==========================================================
# Profile Summary
# ==========================================================

st.divider()

section_header(

    "👤 Profile Summary"

)

left, right = st.columns(2)

with left:

    st.success(f"""

### Personal Information

👤 Name : **{full_name}**

📧 Email : **{email}**

🎂 Age : **{age}**

⚧ Gender : **{gender}**

""")

with right:

    st.info(f"""

### Fitness Information

📏 Height : **{height:.1f} cm**

⚖ Weight : **{weight:.1f} kg**

🎯 Goal : **{goal}**

🏃 Activity : **{activity_level}**

📊 BMI Status : **{bmi_status}**

""")

# ==========================================================
# Health & Fitness Dashboard
# ==========================================================

st.divider()

section_header(

    "📈 Health & Fitness Dashboard"

)

recommended_protein = weight * 2

recommended_water = weight * 35 / 1000

# Estimated Values
current_protein = recommended_protein * 0.90
current_water = recommended_water * 0.85
current_calories = target_calories * 0.95

# ==========================================================
# BMI Gauge
# ==========================================================

st.divider()

section_header(

    "❤️ BMI Overview"

)

try:

    from components.charts import bmi_chart

    bmi_chart(

        bmi

    )

except Exception:

    st.info(

        f"Current BMI : {bmi:.1f}"

    )

# ==========================================================
# Nutrition Progress
# ==========================================================

st.divider()

section_header(

    "🍽️ Daily Nutrition Progress"

)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        "🍗 Protein",

        f"{current_protein:.0f} g",

        f"Goal: {recommended_protein:.0f} g"

    )

    st.progress(

        min(current_protein / recommended_protein, 1.0)

    )

with col2:

    st.metric(

        "💧 Water",

        f"{current_water:.1f} L",

        f"Goal: {recommended_water:.1f} L"

    )

    st.progress(

        min(current_water / recommended_water, 1.0)

    )

with col3:

    st.metric(

        "🔥 Calories",

        f"{current_calories:.0f}",

        f"Goal: {target_calories:.0f}"

    )

    st.progress(

        min(current_calories / target_calories, 1.0)

    )

# ==========================================================
# Fitness Statistics
# ==========================================================

st.divider()

section_header(

    "📊 Fitness Statistics"

)

stats1, stats2, stats3, stats4 = st.columns(4)

with stats1:

    st.metric(

        "BMI Status",

        bmi_status

    )

with stats2:

    st.metric(

        "Goal",

        goal

    )

with stats3:

    st.metric(

        "Activity",

        activity_level

    )

with stats4:

    st.metric(

        "Health",

        "Excellent" if bmi_status == "Healthy" else "Needs Improvement"

    )

# ==========================================================
# Goal Progress
# ==========================================================

st.divider()

section_header(

    "🎯 Goal Progress"

)

goal_progress = {

    "Weight Loss": 40,

    "Weight Gain": 65,

    "Muscle Gain": 55,

    "Maintain Weight": 80

}

progress = goal_progress.get(

    goal,

    50

)

st.progress(

    progress / 100

)

st.caption(

    f"Goal Completion : {progress}%"

)

# ==========================================================
# Daily Targets
# ==========================================================

st.divider()

section_header(

    "🎯 Daily Targets"

)

target_df = {

    "Metric": [

        "Calories",

        "Protein",

        "Water"

    ],

    "Target": [

        round(target_calories),

        round(recommended_protein),

        round(recommended_water, 1)

    ]

}

import pandas as pd

st.dataframe(

    pd.DataFrame(target_df),

    use_container_width=True,

    hide_index=True

)

# ==========================================================
# AI Suggestions
# ==========================================================

st.divider()

section_header(

    "💡 AI Fitness Suggestions"

)

suggestions = []

if bmi < 18.5:

    suggestions.extend([

        "Increase your daily calorie intake with nutritious foods.",

        "Focus on progressive strength training.",

        "Consume protein every 3–4 hours."

    ])

elif bmi < 25:

    suggestions.extend([

        "Maintain your current diet and exercise routine.",

        "Continue resistance training 4–5 days per week.",

        "Prioritize recovery and sleep."

    ])

elif bmi < 30:

    suggestions.extend([

        "Create a moderate calorie deficit.",

        "Increase daily walking and cardio.",

        "Reduce processed food consumption."

    ])

else:

    suggestions.extend([

        "Consult a healthcare professional.",

        "Follow a medically supervised weight-loss plan.",

        "Track nutrition consistently."

    ])

if current_water < recommended_water:

    suggestions.append(

        f"Increase water intake to at least {recommended_water:.1f} L/day."

    )

if current_protein < recommended_protein:

    suggestions.append(

        f"Increase protein intake to approximately {recommended_protein:.0f} g/day."

    )

for suggestion in suggestions:

    st.success(suggestion)

# ==========================================================
# Account Information
# ==========================================================

st.divider()

section_header(

    "👤 Account Information"

)

account = {

    "Name": full_name,

    "Email": email,

    "Age": age,

    "Gender": gender,

    "Height (cm)": height,

    "Weight (kg)": weight,

    "Goal": goal,

    "Activity Level": activity_level,

}

st.json(account)

# ==========================================================
# Download Profile
# ==========================================================

st.divider()

section_header(

    "📥 Export Profile"

)

import json

profile_data = {

    "personal_information": account,

    "health_metrics": {

        "BMI": round(bmi, 2),

        "BMI Status": bmi_status,

        "BMR": round(bmr),

        "TDEE": round(tdee),

        "Target Calories": round(target_calories),

    },

    "nutrition": {

        "Protein Goal": round(recommended_protein),

        "Current Protein": round(current_protein),

        "Water Goal": round(recommended_water, 1),

        "Current Water": round(current_water, 1),

    },

    "suggestions": suggestions,

}

st.download_button(

    label="📄 Download Profile Report",

    data=json.dumps(profile_data, indent=4),

    file_name="profile_report.json",

    mime="application/json",

    use_container_width=True,

)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(

    "AI Fitness Intelligence Platform • User Profile • Version 1.0"

)