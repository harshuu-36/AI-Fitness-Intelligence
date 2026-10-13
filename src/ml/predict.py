"""
==============================================================
Project    : AI Fitness Intelligence Platform

Phase      : 05 - Machine Learning

Module     : Weight Prediction

Author     : Harsh
==============================================================
"""

import os
import joblib
import pandas as pd


# ---------------------------------------------------
# Model Paths
# ---------------------------------------------------

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "models",
    "weight_prediction_model.pkl"
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "models",
    "feature_columns.pkl"
)


# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)


# ---------------------------------------------------
# Prediction Function
# ---------------------------------------------------

def predict_weight(
    age,
    height_cm,
    calories_consumed,
    calories_burned,
    workout_minutes,
    sleep_hours,
    protein_g,
    carbs_g,
    fat_g,
):

    data = pd.DataFrame([{
        "Age": age,
        "HeightCM": height_cm,
        "CaloriesConsumed": calories_consumed,
        "CaloriesBurned": calories_burned,
        "WorkoutMinutes": workout_minutes,
        "SleepHours": sleep_hours,
        "ProteinG": protein_g,
        "CarbsG": carbs_g,
        "FatG": fat_g,
    }])

    data = data[feature_columns]

    prediction = model.predict(data)

    return round(float(prediction[0]), 2)