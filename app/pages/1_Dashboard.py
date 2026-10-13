import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Fitness Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Fitness Dashboard")
st.markdown("---")


# ==========================================
# Load Dataset
# ==========================================

@st.cache_data
def load_data():
    return pd.read_csv(
        "artifacts/processed_data/feature_engineered_data.csv"
    )


df = load_data()


# ==========================================
# Convert Data Types
# ==========================================

numeric_columns = [
    "WeightKG",
    "CaloriesConsumed",
    "CaloriesBurned",
    "SleepHours",
    "WorkoutMinutes"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

if "ProgressDate" in df.columns:
    df["ProgressDate"] = pd.to_datetime(df["ProgressDate"])


# ==========================================
# KPI Cards
# ==========================================

st.subheader("📌 Overall Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Users",
        df["UserID"].nunique()
    )

with col2:
    st.metric(
        "⚖ Average Weight",
        f"{df['WeightKG'].mean():.1f} kg"
    )

with col3:
    st.metric(
        "🔥 Avg Calories Burned",
        f"{df['CaloriesBurned'].mean():.0f}"
    )

with col4:
    st.metric(
        "😴 Avg Sleep",
        f"{df['SleepHours'].mean():.1f} hrs"
    )


st.markdown("---")


# ==========================================
# Weight Trend
# ==========================================

st.subheader("📈 Weight Trend")

weight = (
    df.groupby("ProgressDate")["WeightKG"]
      .mean()
      .reset_index()
)

fig = px.line(
    weight,
    x="ProgressDate",
    y="WeightKG",
    markers=True,
    title="Average Weight Over Time"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ==========================================
# Calories Burned
# ==========================================

st.subheader("🔥 Calories Burned Trend")

calories = (
    df.groupby("ProgressDate")["CaloriesBurned"]
      .mean()
      .reset_index()
)

fig2 = px.bar(
    calories,
    x="ProgressDate",
    y="CaloriesBurned",
    title="Average Calories Burned"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# ==========================================
# BMI Distribution
# ==========================================

st.subheader("🏋 BMI Distribution")

fig3 = px.pie(
    df,
    names="BMICategory",
    hole=0.45,
    title="BMI Categories"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


# ==========================================
# Sleep Category
# ==========================================

st.subheader("😴 Sleep Quality Distribution")

fig4 = px.histogram(
    df,
    x="SleepCategory",
    color="SleepCategory",
    title="Sleep Categories"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)


# ==========================================
# Gender Distribution
# ==========================================

st.subheader("🚻 Gender Distribution")

gender = (
    df["Gender"]
      .value_counts()
      .reset_index()
)

gender.columns = ["Gender", "Count"]

fig5 = px.bar(
    gender,
    x="Gender",
    y="Count",
    text="Count",
    title="Users by Gender"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)


# ==========================================
# Dataset Preview
# ==========================================

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)