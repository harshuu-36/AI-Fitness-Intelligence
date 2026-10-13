import streamlit as st

st.set_page_config(
    page_title="Health Report",
    layout="wide"
)

st.title("🏥 Health Report")

weight = st.number_input(
    "Weight (kg)",
    20.0,
    200.0,
    70.0
)

height = st.number_input(
    "Height (cm)",
    100.0,
    250.0,
    170.0
)

age = st.number_input(
    "Age",
    10,
    100,
    25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

calories = st.number_input(
    "Calories Consumed",
    0,
    10000,
    2200
)

if st.button("Generate Report"):

    height_m = height / 100

    bmi = weight / (height_m ** 2)

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

    tdee = bmr * 1.55

    deficit = tdee - calories

    if bmi < 18.5:
        category = "Underweight"

    elif bmi < 25:
        category = "Normal"

    elif bmi < 30:
        category = "Overweight"

    else:
        category = "Obese"

    c1, c2, c3 = st.columns(3)

    c1.metric("BMI", round(bmi, 2))
    c2.metric("BMR", round(bmr))
    c3.metric("TDEE", round(tdee))

    st.success(f"BMI Category : {category}")

    st.info(f"Calorie Deficit : {deficit:.0f} kcal")
    