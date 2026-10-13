import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Progress Tracker",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Fitness Progress Tracker")

df = pd.read_csv(
    "artifacts/processed_data/feature_engineered_data.csv"
)

df["ProgressDate"] = pd.to_datetime(df["ProgressDate"])

users = sorted(df["UserID"].unique())

user = st.selectbox(
    "Select User",
    users
)

user_df = df[df["UserID"] == user]

st.subheader("Weight Progress")

fig = px.line(
    user_df,
    x="ProgressDate",
    y="WeightKG",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Calories Burned")

fig2 = px.bar(
    user_df,
    x="ProgressDate",
    y="CaloriesBurned"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Sleep Hours")

fig3 = px.line(
    user_df,
    x="ProgressDate",
    y="SleepHours",
    markers=True
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Progress Data")

st.dataframe(
    user_df,
    use_container_width=True
)