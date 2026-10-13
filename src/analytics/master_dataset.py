"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 03 - Analytics

Module     : Master Dataset

Author     : Harsh

Description:

Create Master Dataset for ML & Power BI.

====================================================================
"""

import pandas as pd

from src.utils.logger import logger


def create_master_dataset(datasets):

    logger.info("=" * 70)
    logger.info("CREATING MASTER DATASET")
    logger.info("=" * 70)

    # ======================================================
    # Copy DataFrames
    # ======================================================

    users = datasets["Users"].copy()

    progress = datasets["DailyProgress"].copy()

    sleep = datasets["Sleep"].copy()

    diet = datasets["Diet"].copy()

    workouts = datasets["Workouts"].copy()

    goals = datasets["Goals"].copy()

    # ======================================================
    # Aggregate Sleep
    # ======================================================

    sleep = (

        sleep

        .groupby(
            ["UserID", "SleepDate"],
            as_index=False
        )

        .agg(

            SleepMinutes=("DurationMinutes", "mean"),

            SleepQuality=("SleepQuality", "first")

        )

    )

    # ======================================================
    # Aggregate Diet
    # ======================================================

    diet = (

        diet

        .groupby(
            ["UserID", "MealDate"],
            as_index=False
        )

        .agg(

            CaloriesConsumed=("CaloriesConsumed", "sum"),

            ProteinG=("ProteinG", "sum"),

            CarbsG=("CarbsG", "sum"),

            FatG=("FatG", "sum")

        )

    )

    # ======================================================
    # Aggregate Workouts
    # ======================================================

    workouts = (

        workouts

        .groupby(
            ["UserID", "WorkoutDate"],
            as_index=False
        )

        .agg(

            CaloriesBurned=("CaloriesBurned", "sum"),

            WorkoutMinutes=("DurationMinutes", "sum")

        )

    )

    # ======================================================
    # Merge Progress + Users
    # ======================================================

    master = progress.merge(

        users,

        on="UserID",

        how="left"

    )

    # ======================================================
    # Merge Sleep
    # ======================================================

    master = master.merge(

        sleep,

        left_on=["UserID", "ProgressDate"],

        right_on=["UserID", "SleepDate"],

        how="left"

    )

    # ======================================================
    # Merge Diet
    # ======================================================

    master = master.merge(

        diet,

        left_on=["UserID", "ProgressDate"],

        right_on=["UserID", "MealDate"],

        how="left"

    )

    # ======================================================
    # Merge Workout
    # ======================================================

    master = master.merge(

        workouts,

        left_on=["UserID", "ProgressDate"],

        right_on=["UserID", "WorkoutDate"],

        how="left"

    )

    # ======================================================
    # Merge Goals
    # ======================================================

    master = master.merge(

        goals,

        on="UserID",

        how="left"

    )

    # ======================================================
    # Remove duplicate date columns
    # ======================================================

    columns_to_drop = [

        "SleepDate",

        "MealDate",

        "WorkoutDate"

    ]

    master.drop(

        columns=[
            col
            for col in columns_to_drop
            if col in master.columns
        ],

        inplace=True

    )

    logger.info(

        f"Master Dataset Shape : {master.shape}"

    )

    logger.info("=" * 70)

    logger.info("MASTER DATASET CREATED SUCCESSFULLY")

    logger.info("=" * 70)

    return master