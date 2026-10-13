"""
==============================================================
AI Fitness Intelligence Platform

Charts Component

Author      : Harsh

Description :
Reusable Plotly charts for Streamlit pages.
==============================================================
"""

from __future__ import annotations

from typing import Sequence

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ==========================================================
# Theme Colors
# ==========================================================

PRIMARY_COLOR = "#2563EB"
SUCCESS_COLOR = "#22C55E"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#EF4444"

CHART_COLORS = [
    PRIMARY_COLOR,
    SUCCESS_COLOR,
    WARNING_COLOR,
    ERROR_COLOR,
    "#8B5CF6",
    "#EC4899",
]


# ==========================================================
# Common Layout
# ==========================================================

def _apply_layout(
    fig,
    title: str,
):

    fig.update_layout(

        title=dict(
            text=title,
            x=0.5,
            font=dict(
                size=22
            )
        ),

        template="plotly_white",

        height=430,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),

        paper_bgcolor="white",

        plot_bgcolor="white",

        hovermode="x unified",

        legend_title="",

        font=dict(
            family="Arial",
            size=14
        ),

        xaxis=dict(
            showgrid=False,
            zeroline=False
        ),

        yaxis=dict(
            gridcolor="#ECECEC",
            zeroline=False
        )

    )

    return fig


# ==========================================================
# Common Chart Renderer
# ==========================================================

def _show_chart(
    fig,
):
    """
    Render Plotly chart inside Streamlit.
    """

    st.plotly_chart(
        fig,
        use_container_width=True,
        theme="streamlit",
    )


# ==========================================================
# Data Validation
# ==========================================================

def _validate_dataframe(
    data: pd.DataFrame,
    required_columns: Sequence[str],
):
    """
    Ensure required columns exist before plotting.
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")

    missing = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing:

        raise ValueError(
            f"Missing columns: {', '.join(missing)}"
        )

# ==========================================================
# Line Chart
# ==========================================================

def line_chart(

    data: pd.DataFrame,

    x: str,

    y: str,

    title: str,

    color: str | None = None,

):

    _validate_dataframe(
        data,
        [x, y]
    )

    fig = px.line(

        data,

        x=x,

        y=y,

        color=color,

        markers=True,

        color_discrete_sequence=[PRIMARY_COLOR]

    )

    fig.update_traces(

        line=dict(
            width=4,
            shape="spline"
        ),

        marker=dict(
            size=9
        ),

        hovertemplate="<b>%{x}</b><br>%{y}<extra></extra>"

    )

    _apply_layout(
        fig,
        title
    )

    _show_chart(
        fig
    )


# ==========================================================
# Bar Chart
# ==========================================================

def bar_chart(
    data: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    color: str | None = None,
):
    """
    Display a Plotly bar chart.
    """

    _validate_dataframe(
        data,
        [x, y],
    )

    fig = px.bar(
        data_frame=data,
        x=x,
        y=y,
        color=color,
        color_discrete_sequence=CHART_COLORS,
        text_auto=".2s",
    )

    fig.update_traces(
        textposition="outside",
    )

    _apply_layout(
        fig,
        title,
    )

    _show_chart(
        fig,
    )

# ==========================================================
# Pie Chart
# ==========================================================

def pie_chart(

    labels,

    values,

    title,

):

    fig = go.Figure(

        data=[

            go.Pie(

                labels=labels,

                values=values,

                hole=.60,

                textinfo="label+percent",

                marker=dict(

                    colors=CHART_COLORS,

                    line=dict(
                        color="white",
                        width=3
                    )

                )

            )

        ]

    )

    _apply_layout(

        fig,

        title

    )

    _show_chart(

        fig

    )


# ==========================================================
# Macronutrient Donut Chart
# ==========================================================

def macro_chart(

    protein: float,

    carbs: float,

    fat: float,

):

    fig = go.Figure(

        data=[

            go.Pie(

                labels=[

                    "Protein",

                    "Carbs",

                    "Fat",

                ],

                values=[

                    protein,

                    carbs,

                    fat,

                ],

                hole=0.65,

                sort=False,

                textinfo="label+percent",

                textfont=dict(
                    size=14
                ),

                marker=dict(

                    colors=[

                        PRIMARY_COLOR,

                        SUCCESS_COLOR,

                        WARNING_COLOR,

                    ],

                    line=dict(

                        color="white",

                        width=3

                    )

                ),

                hovertemplate=

                "<b>%{label}</b><br>"

                "%{value} g"

                "<br>%{percent}"

                "<extra></extra>",

            )

        ]

    )

    fig.add_annotation(

        text="Macros",

        x=0.5,

        y=0.5,

        showarrow=False,

        font=dict(

            size=18

        )

    )

    _apply_layout(

        fig,

        "Macronutrient Distribution"

    )

    _show_chart(

        fig

    )

# ==========================================================
# Health Score Gauge
# ==========================================================

def health_gauge(

    score: float,

):

    score = max(

        0,

        min(

            float(score),

            100

        )

    )

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            number={

                "suffix": "/100",

                "font": {

                    "size": 42

                }

            },

            title={

                "text": "<b>Health Score</b>",

                "font": {

                    "size": 22

                }

            },

            gauge={

                "shape": "angular",

                "axis": {

                    "range": [

                        0,

                        100

                    ],

                    "tickwidth": 1

                },

                "bar": {

                    "color": PRIMARY_COLOR,

                    "thickness": 0.35

                },

                "steps": [

                    {

                        "range": [

                            0,

                            40

                        ],

                        "color": "#FEE2E2"

                    },

                    {

                        "range": [

                            40,

                            70

                        ],

                        "color": "#FEF3C7"

                    },

                    {

                        "range": [

                            70,

                            100

                        ],

                        "color": "#DCFCE7"

                    }

                ],

                "threshold": {

                    "line": {

                        "color": "#111827",

                        "width": 5

                    },

                    "thickness": 0.8,

                    "value": score

                }

            }

        )

    )

    fig.update_layout(

        height=360,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        )

    )

    _show_chart(

        fig

    )


# ==========================================================
# BMI Gauge Chart
# ==========================================================

def bmi_chart(

    bmi: float,

):

    bmi = max(

        10.0,

        min(

            float(bmi),

            40.0

        )

    )

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=bmi,

            number={

                "font": {

                    "size": 40

                }

            },

            title={

                "text": "<b>Body Mass Index</b>",

                "font": {

                    "size": 22

                }

            },

            gauge={

                "axis": {

                    "range": [

                        10,

                        40

                    ]

                },

                "bar": {

                    "color": PRIMARY_COLOR,

                    "thickness": 0.35

                },

                "steps": [

                    {

                        "range":[10,18.5],

                        "color":"#DBEAFE"

                    },

                    {

                        "range":[18.5,25],

                        "color":"#DCFCE7"

                    },

                    {

                        "range":[25,30],

                        "color":"#FEF3C7"

                    },

                    {

                        "range":[30,40],

                        "color":"#FEE2E2"

                    }

                ],

                "threshold": {

                    "line": {

                        "color":"black",

                        "width":5

                    },

                    "value": bmi

                }

            }

        )

    )

    fig.update_layout(

        height=360,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        )

    )

    _show_chart(

        fig

    )

# ==========================================================
# Progress Chart
# ==========================================================

def progress_chart(

    current: float,

    target: float,

    title: str,

):

    percentage = 0

    if target > 0:

        percentage = min(

            current / target,

            1

        )

    st.subheader(title)

    st.progress(percentage)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Current",

            f"{current:,.0f}"

        )

    with c2:

        st.metric(

            "Target",

            f"{target:,.0f}"

        )

    with c3:

        st.metric(

            "Progress",

            f"{percentage*100:.1f}%"

        )

    if percentage >= 1:

        st.success(

            "🎉 Goal Achieved!"

        )

    elif percentage >= 0.75:

        st.info(

            "🔥 Almost There!"

        )

    else:

        st.warning(

            "💪 Keep Going!"
        )


# ==========================================================
# Manual Test
# ==========================================================

if __name__ == "__main__":

    st.set_page_config(
        page_title="Charts Test",
        page_icon="📊",
        layout="wide",
    )

    st.title("📊 Charts Component Test")

    df = pd.DataFrame(
        {
            "Day": [
                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
            ],
            "Weight": [
                70.0,
                69.8,
                69.5,
                69.2,
                69.0,
            ],
            "Calories": [
                2200,
                2350,
                2100,
                2400,
                2300,
            ],
        }
    )

    st.header("Line Chart")

    line_chart(
        data=df,
        x="Day",
        y="Weight",
        title="Weight Trend",
    )

    st.header("Bar Chart")

    bar_chart(
        data=df,
        x="Day",
        y="Calories",
        title="Daily Calories",
    )

    st.header("Pie Chart")

    pie_chart(
        labels=[
            "Protein",
            "Carbs",
            "Fat",
        ],
        values=[
            150,
            320,
            70,
        ],
        title="Macronutrient Split",
    )

    st.header("Macro Chart")

    macro_chart(
        protein=150,
        carbs=320,
        fat=70,
    )

    st.header("Health Gauge")

    health_gauge(86)

    st.header("BMI Gauge")

    bmi_chart(22.4)

    st.header("Progress")

    progress_chart(
        current=7200,
        target=10000,
        title="Daily Steps",
    )