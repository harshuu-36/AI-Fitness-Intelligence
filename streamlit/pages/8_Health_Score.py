"""
==============================================================

AI Fitness Intelligence Platform

Health Score

Author      : Harsh

Description :
AI-powered Health Score Recommendation

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
    health_gauge,
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Health Score",

    page_icon="❤️",

    layout="wide",

)

render_sidebar()

client = get_client()

# ==========================================================
# Header
# ==========================================================

section_header(

    "❤️ AI Health Score",

    "Evaluate your overall health based on BMI, activity, nutrition and hydration."

)

# ==========================================================
# Input Form
# ==========================================================

with st.form(

    "health_score_form"

):

    col1, col2 = st.columns(2)

    with col1:

        bmi = st.number_input(

            "BMI",

            min_value=10.0,

            max_value=50.0,

            value=22.5,

            step=0.1,

        )

        protein = st.number_input(

            "Daily Protein Intake (g)",

            min_value=0.0,

            max_value=300.0,

            value=120.0,

            step=1.0,

        )

        recommended_protein = st.number_input(

            "Recommended Protein (g)",

            min_value=0.0,

            max_value=300.0,

            value=130.0,

            step=1.0,

        )

    with col2:

        activity_level = st.selectbox(

            "Activity Level",

            [

                "Sedentary",

                "Light",

                "Moderate",

                "Active",

                "Very Active",

            ],

            index=2,

        )

        water_liters = st.number_input(

            "Water Intake (Liters)",

            min_value=0.0,

            max_value=10.0,

            value=3.0,

            step=0.1,

        )

        recommended_water = st.number_input(

            "Recommended Water (Liters)",

            min_value=0.0,

            max_value=10.0,

            value=3.5,

            step=0.1,

        )

    submitted = st.form_submit_button(

        "❤️ Calculate Health Score",

        use_container_width=True,

    )

# ==========================================================
# Stop Until User Clicks
# ==========================================================

if not submitted:

    st.info(

        "Fill in your health details and click **Calculate Health Score**."

    )

    st.stop()

# ==========================================================
# Prepare Payload
# ==========================================================

payload = {

    "bmi": bmi,

    "activity_level": activity_level,

    "protein": protein,

    "recommended_protein": recommended_protein,

    "water_liters": water_liters,

    "recommended_water": recommended_water,

}

# ==========================================================
# API Call
# ==========================================================

with st.spinner(

    "Calculating your AI Health Score..."

):

    response = client.health_score(

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

            "Failed to calculate Health Score."

        )

    )

    st.stop()

# ==========================================================
# Extract Response
# ==========================================================

try:

    health_score = int(

        response["health_score"]

    )

    status = response["status"]

    recommendations = response["recommendations"]

    summary = response["summary"]

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
# Extract Summary Values
# ==========================================================

bmi_status = summary.get(

    "bmi_status",

    "N/A"

)

protein_status = summary.get(

    "protein_status",

    "N/A"

)

hydration_status = summary.get(

    "hydration_status",

    "N/A"

)

activity_status = summary.get(

    "activity_status",

    activity_level

)

# ==========================================================
# Success Message
# ==========================================================

st.success(

    "Health Score calculated successfully."

)

# ==========================================================
# Health Score Dashboard
# ==========================================================

st.divider()

section_header(
    "❤️ Health Score Dashboard",
    "Your AI-powered overall health assessment."
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="❤️ Health Score",
        value=f"{health_score}/100",
    )

with col2:

    st.metric(
        label="📊 Health Status",
        value=status,
    )

with col3:

    st.metric(
        label="🏃 Activity Level",
        value=activity_status,
    )

# ==========================================================
# Health Gauge
# ==========================================================

st.divider()

section_header(
    "📊 Overall Health Gauge"
)

health_gauge(
    health_score
)

# ==========================================================
# Health Summary
# ==========================================================

st.divider()

section_header(
    "📋 Health Summary"
)

left, right = st.columns(2)

with left:

    st.success(f"""
### Body Assessment

📏 BMI : **{bmi:.1f}**

📊 BMI Status : **{bmi_status}**

🏃 Activity : **{activity_status}**
""")

with right:

    st.info(f"""
### Nutrition Assessment

🍗 Protein : **{protein_status}**

💧 Hydration : **{hydration_status}**

❤️ Overall : **{status}**
""")

# ==========================================================
# Summary JSON
# ==========================================================

st.divider()

section_header(
    "📑 Detailed Summary"
)

st.json(summary)

# ==========================================================
# Health Indicators
# ==========================================================

st.divider()

section_header(
    "📈 Health Indicators"
)

indicator1, indicator2, indicator3 = st.columns(3)

with indicator1:

    if bmi_status.lower() == "healthy":

        st.success("✅ Healthy BMI")

    else:

        st.warning(f"⚠️ {bmi_status}")

with indicator2:

    if protein_status.lower() in ["good", "adequate"]:

        st.success("✅ Protein Intake")

    else:

        st.warning(f"⚠️ {protein_status}")

with indicator3:

    if hydration_status.lower() in ["good", "adequate"]:

        st.success("✅ Hydration")

    else:

        st.warning(f"⚠️ {hydration_status}")

# ==========================================================
# AI Health Recommendations
# ==========================================================

st.divider()

section_header(
    "💡 AI Health Recommendations",
    "Personalized recommendations to improve your health."
)

# API Recommendations
if recommendations:

    for recommendation in recommendations:

        st.success(recommendation)

else:

    st.info(
        "No additional recommendations available."
    )

# ==========================================================
# Health Improvement Tips
# ==========================================================

st.divider()

section_header(
    "🏥 Health Improvement Tips"
)

tips = []

# BMI Tips
if bmi < 18.5:

    tips.extend([
        "🍚 Increase your calorie intake with nutritious foods.",
        "🏋️ Focus on strength training to build muscle mass."
    ])

elif bmi < 25:

    tips.extend([
        "✅ Maintain your current weight with balanced nutrition.",
        "🏃 Continue regular exercise and active lifestyle."
    ])

elif bmi < 30:

    tips.extend([
        "🥗 Reduce processed foods and sugary drinks.",
        "🚶 Increase daily physical activity."
    ])

else:

    tips.extend([
        "👨‍⚕️ Consult a healthcare professional.",
        "📋 Follow a structured weight management plan."
    ])

# Protein Tips
if protein < recommended_protein:

    tips.append(
        f"🍗 Increase protein intake to at least {recommended_protein:.0f} g/day."
    )

# Water Tips
if water_liters < recommended_water:

    tips.append(
        f"💧 Drink approximately {recommended_water:.1f} liters of water daily."
    )

# Activity Tips
if activity_level == "Sedentary":

    tips.append(
        "🚶 Aim for at least 30 minutes of walking every day."
    )

elif activity_level == "Light":

    tips.append(
        "🏃 Increase activity to 150 minutes of exercise per week."
    )

elif activity_level == "Moderate":

    tips.append(
        "💪 Continue resistance training 3–5 times per week."
    )

elif activity_level == "Active":

    tips.append(
        "🏋️ Maintain your workout routine and prioritize recovery."
    )

elif activity_level == "Very Active":

    tips.append(
        "😴 Ensure adequate sleep and recovery between intense sessions."
    )

for tip in tips:

    st.info(tip)

# ==========================================================
# Download Health Report
# ==========================================================

st.divider()

section_header(
    "📥 Download Health Report"
)

import json

report = {

    "Health Score": health_score,

    "Status": status,

    "BMI": bmi,

    "Activity Level": activity_level,

    "Protein Intake": protein,

    "Recommended Protein": recommended_protein,

    "Water Intake": water_liters,

    "Recommended Water": recommended_water,

    "Summary": summary,

    "Recommendations": recommendations,

}

st.download_button(

    label="📄 Download Health Report",

    data=json.dumps(report, indent=4),

    file_name="health_score_report.json",

    mime="application/json",

    use_container_width=True,

)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "AI Fitness Intelligence Platform • Health Score Module • Version 1.0"
)