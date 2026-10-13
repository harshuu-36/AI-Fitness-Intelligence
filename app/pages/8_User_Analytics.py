import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="User Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 User Analytics")

# =====================================
# Load Dataset
# =====================================

@st.cache_data
def load_data():
    return pd.read_csv(
        "artifacts/processed_data/feature_engineered_data.csv"
    )

df = load_data()

# =====================================
# Data Types
# =====================================

df["ProgressDate"] = pd.to_datetime(df["ProgressDate"])

numeric_cols = [
    "WeightKG",
    "CaloriesConsumed",
    "CaloriesBurned",
    "SleepHours",
    "WorkoutMinutes"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# =====================================
# Sidebar Filters
# =====================================

st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].dropna().unique(),
    default=df["Gender"].dropna().unique()
)

filtered_df = df[df["Gender"].isin(gender)]

# =====================================
# KPIs
# =====================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Users",
    filtered_df["UserID"].nunique()
)

col2.metric(
    "Avg Weight",
    round(filtered_df["WeightKG"].mean(), 1)
)

col3.metric(
    "Avg Sleep",
    round(filtered_df["SleepHours"].mean(), 1)
)

col4.metric(
    "Avg Calories",
    round(filtered_df["CaloriesConsumed"].mean(), 0)
)

st.divider()

# =====================================
# Gender Chart
# =====================================

fig = px.pie(
    filtered_df,
    names="Gender",
    title="Gender Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================
# BMI Category
# =====================================

fig2 = px.histogram(
    filtered_df,
    x="BMICategory",
    color="BMICategory",
    title="BMI Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# =====================================
# Sleep Trend
# =====================================

sleep = (
    filtered_df
    .groupby("ProgressDate")["SleepHours"]
    .mean()
    .reset_index()
)

fig3 = px.line(
    sleep,
    x="ProgressDate",
    y="SleepHours",
    markers=True,
    title="Average Sleep Hours"
)

st.plotly_chart(fig3, use_container_width=True)

# =====================================
# Weight Trend
# =====================================

weight = (
    filtered_df
    .groupby("ProgressDate")["WeightKG"]
    .mean()
    .reset_index()
)

fig4 = px.line(
    weight,
    x="ProgressDate",
    y="WeightKG",
    markers=True,
    title="Weight Trend"
)

st.plotly_chart(fig4, use_container_width=True)

# =====================================
# Preview
# =====================================

st.subheader("Dataset Preview")

st.dataframe(
    filtered_df,
    use_container_width=True
)