import streamlit as st

st.set_page_config(
    page_title="Diet Planner",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 AI Diet Planner")

goal = st.selectbox(
    "Select Goal",
    [
        "Weight Loss",
        "Weight Gain",
        "Maintain Weight"
    ]
)

diet = st.selectbox(
    "Diet Preference",
    [
        "Vegetarian",
        "Non-Vegetarian"
    ]
)

if st.button("Generate Diet Plan"):

    if goal == "Weight Loss":

        breakfast = "Oats + Milk + Fruits"
        lunch = "Brown Rice + Dal + Salad"
        dinner = "Paneer + Vegetables"

    elif goal == "Weight Gain":

        breakfast = "Oats + Peanut Butter + Banana"
        lunch = "Rice + Paneer + Curd"
        dinner = "Chapati + Soyabean + Milk"

    else:

        breakfast = "Poha + Milk"
        lunch = "Rice + Dal + Vegetables"
        dinner = "Chapati + Paneer"

    st.success("Diet Plan Generated Successfully!")

    st.subheader("🍳 Breakfast")
    st.write(breakfast)

    st.subheader("🍛 Lunch")
    st.write(lunch)

    st.subheader("🍽 Dinner")
    st.write(dinner)