"""
==============================================================
Project : AI Fitness Intelligence Platform
Module  : Feature Engineering
==============================================================
"""

import numpy as np
import pandas as pd

from src.utils.logger import logger


def create_features(master):

    logger.info("=" * 70)
    logger.info("STARTING FEATURE ENGINEERING")
    logger.info("=" * 70)

    data = master.copy()

    # ======================================================
    # DATE CONVERSION
    # ======================================================

    date_columns = [
        "DateOfBirth",
        "ProgressDate",
        "CreatedAt",
        "StartDate",
        "TargetDate"
    ]

    for col in date_columns:
        if col in data.columns:
            data[col] = pd.to_datetime(data[col], errors="coerce")

    # ======================================================
    # NUMERIC CONVERSION
    # ======================================================

    numeric_columns = [
        "WeightKG",
        "HeightCM",
        "SleepMinutes",
        "SleepQuality",
        "CaloriesConsumed",
        "ProteinG",
        "CarbsG",
        "FatG",
        "CaloriesBurned",
        "WorkoutMinutes",
        "TargetWeightKG"
    ]

    for col in numeric_columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    # ======================================================
    # FILL MISSING VALUES
    # ======================================================

    for col in numeric_columns:
        if col in data.columns:
            data[col] = data[col].fillna(0)

    # ======================================================
    # AGE
    # ======================================================

    if "DateOfBirth" in data.columns:

        today = pd.Timestamp.today()

        age = (
            (today - data["DateOfBirth"]).dt.days
            / 365.25
        )

        data["Age"] = (
            age
            .fillna(0)
            .round()
            .astype(int)
        )

    # ======================================================
    # HEIGHT
    # ======================================================

    if "HeightCM" in data.columns:
        data["HeightM"] = data["HeightCM"] / 100

    # ======================================================
    # BMI
    # ======================================================

    if (
        "WeightKG" in data.columns
        and
        "HeightM" in data.columns
    ):

        data["BMI"] = np.where(
            data["HeightM"] > 0,
            data["WeightKG"] / (data["HeightM"] ** 2),
            np.nan
        )

        data["BMI"] = data["BMI"].round(2)

    # ======================================================
    # SLEEP HOURS
    # ======================================================

    if "SleepMinutes" in data.columns:
        data["SleepHours"] = (
            data["SleepMinutes"] / 60
        ).round(2)

    # ======================================================
    # CALORIES PER MINUTE
    # ======================================================

    if (
        "CaloriesBurned" in data.columns
        and
        "WorkoutMinutes" in data.columns
    ):

        data["CaloriesPerMinute"] = np.where(
            data["WorkoutMinutes"] > 0,
            data["CaloriesBurned"] / data["WorkoutMinutes"],
            0
        )

        data["CaloriesPerMinute"] = (
            data["CaloriesPerMinute"]
            .round(2)
        )

    # ======================================================
    # BMR
    # ======================================================

    if (
        "Gender" in data.columns
        and
        "WeightKG" in data.columns
        and
        "HeightCM" in data.columns
        and
        "Age" in data.columns
    ):

        gender = (
            data["Gender"]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.strip()
        )

        data["BMR"] = np.where(

            gender == "male",

            (
                10 * data["WeightKG"]
                +
                6.25 * data["HeightCM"]
                -
                5 * data["Age"]
                +
                5
            ),

            (
                10 * data["WeightKG"]
                +
                6.25 * data["HeightCM"]
                -
                5 * data["Age"]
                -
                161
            )

        )

        data["BMR"] = data["BMR"].round(2)

    # ======================================================
    # TDEE
    # ======================================================

    if "BMR" in data.columns:

        data["TDEE"] = (
            data["BMR"] * 1.55
        ).round(2)

    # ======================================================
    # CALORIE DEFICIT
    # ======================================================

    if (
        "CaloriesConsumed" in data.columns
        and
        "TDEE" in data.columns
    ):

        data["CalorieDeficit"] = (
            data["TDEE"]
            -
            data["CaloriesConsumed"]
        ).round(2)

    # ======================================================
    # WEIGHT DIFFERENCE
    # ======================================================

    if (
        "WeightKG" in data.columns
        and
        "TargetWeightKG" in data.columns
    ):

        data["WeightDifference"] = (
            data["WeightKG"]
            -
            data["TargetWeightKG"]
        ).round(2)

    # ======================================================
    # BMI CATEGORY
    # ======================================================

    if "BMI" in data.columns:

        data["BMICategory"] = pd.cut(

            data["BMI"],

            bins=[0, 18.5, 25, 30, 100],

            labels=[
                "Underweight",
                "Normal",
                "Overweight",
                "Obese"
            ]

        )

    # ======================================================
    # SLEEP CATEGORY
    # ======================================================

    if "SleepHours" in data.columns:

        data["SleepCategory"] = pd.cut(

            data["SleepHours"],

            bins=[0, 6, 7, 9, 24],

            labels=[
                "Poor",
                "Average",
                "Good",
                "Excellent"
            ]

        )

    logger.info("=" * 70)
    logger.info("FEATURE ENGINEERING COMPLETED")
    logger.info("=" * 70)

    logger.info(f"Final Dataset Shape : {data.shape}")

    return data