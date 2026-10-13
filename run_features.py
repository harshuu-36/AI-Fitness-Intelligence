"""
==============================================================
Project    : AI Fitness Intelligence Platform

Phase      : 04 - Feature Engineering

Module     : Run Feature Engineering Pipeline

Author     : Harsh

Description:
Load data from SQL Server, create master dataset,
perform feature engineering and save final dataset.
==============================================================
"""

import os
from pathlib import Path

import pandas as pd

from src.database.query_executor import execute_query
from src.analytics.master_dataset import create_master_dataset
from src.features.feature_engineering import create_features


def _load_csv_datasets():
    """Load the generated CSV files when SQL Server is unavailable."""
    root = Path(__file__).resolve().parent
    generated_dir = root / "data" / "generated"

    users = pd.read_csv(generated_dir / "users.csv")
    progress = pd.read_csv(generated_dir / "weight.csv")
    sleep = pd.read_csv(generated_dir / "sleep.csv")
    diet = pd.read_csv(generated_dir / "diet.csv")
    workouts = pd.read_csv(generated_dir / "workouts.csv")

    goals = users[["UserID", "GoalType"]].copy()
    goals["TargetWeightKG"] = goals["GoalType"].map({
        "WeightLoss": 0,
        "MuscleGain": 0,
        "Maintain": 0,
    })

    return {
        "Users": users,
        "DailyProgress": progress,
        "Sleep": sleep,
        "Diet": diet,
        "Workouts": workouts,
        "Goals": goals,
    }


def load_all_tables():

    datasets = {}

    try:
        tables = [
            "Users",
            "Meals",
            "MealItems",
            "FoodItems",
            "Diet",
            "Exercises",
            "Workouts",
            "Sleep",
            "DailyProgress",
            "Goals"
        ]

        for table in tables:
            datasets[table] = execute_query(f"SELECT * FROM {table}")

        return datasets

    except Exception as exc:
        print(f"SQL database not available; using CSV fallback instead. Reason: {exc}")
        return _load_csv_datasets()


def run_feature_engineering():

    print("\n" + "=" * 80)
    print("LOADING DATA")
    print("=" * 80)

    datasets = load_all_tables()

    print("\n" + "=" * 80)
    print("CREATING MASTER DATASET")
    print("=" * 80)

    master = create_master_dataset(datasets)

    print("\n" + "=" * 80)
    print("MASTER DATASET")
    print("=" * 80)

    print(master.head())

    print("\nShape :", master.shape)

    print("\nColumns :")

    print(master.columns.tolist())

    print("\n" + "=" * 80)
    print("FEATURE ENGINEERING")
    print("=" * 80)

    feature_data = create_features(master)

    print("\n" + "=" * 80)
    print("FINAL FEATURE DATASET")
    print("=" * 80)

    print(feature_data.head())

    print("\nShape :", feature_data.shape)

    print("\nColumns :")

    print(feature_data.columns.tolist())

    # =====================================================
    # SAVE DATASET
    # =====================================================

    os.makedirs(
        "artifacts/processed_data",
        exist_ok=True
    )

    output_path = (
        "artifacts/processed_data/"
        "feature_engineered_data.csv"
    )

    feature_data.to_csv(

        output_path,

        index=False

    )

    print("\n" + "=" * 80)
    print("DATASET SAVED")
    print("=" * 80)

    print(f"Saved Successfully : {output_path}")


if __name__ == "__main__":

    run_feature_engineering()