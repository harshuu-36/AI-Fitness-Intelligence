"""
==============================================================
Project    : AI Fitness Intelligence Platform

Phase      : 05 - Machine Learning

Module     : Train Weight Prediction Model

Author     : Harsh

Description:
Train Random Forest model for weight prediction and
save trained model, feature columns and evaluation metrics.
==============================================================
"""

from pathlib import Path
import json

import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import train_test_split

from src.utils.logger import logger


# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATASET_PATH = (
    BASE_DIR
    / "artifacts"
    / "processed_data"
    / "feature_engineered_data.csv"
)

MODEL_DIR = (
    BASE_DIR
    / "artifacts"
    / "models"
)

MODEL_PATH = (
    MODEL_DIR
    / "weight_prediction_model.pkl"
)

FEATURE_PATH = (
    MODEL_DIR
    / "feature_columns.pkl"
)

METRICS_PATH = (
    MODEL_DIR
    / "model_metrics.json"
)


# ==========================================================
# Load Dataset
# ==========================================================

def load_dataset(
    file_path: Path
) -> pd.DataFrame:

    logger.info("=" * 70)
    logger.info("LOADING FEATURE ENGINEERED DATASET")
    logger.info("=" * 70)

    if not file_path.exists():

        raise FileNotFoundError(
            f"Dataset not found:\n{file_path}"
        )

    data = pd.read_csv(file_path)

    logger.info(f"Dataset Shape : {data.shape}")

    return data


# ==========================================================
# Train Model
# ==========================================================

def train_model(
    data: pd.DataFrame
) -> RandomForestRegressor:

    logger.info("=" * 70)
    logger.info("TRAINING RANDOM FOREST MODEL")
    logger.info("=" * 70)

    feature_columns = [

        "Age",
        "HeightCM",
        "CaloriesConsumed",
        "CaloriesBurned",
        "WorkoutMinutes",
        "SleepHours",
        "ProteinG",
        "CarbsG",
        "FatG"

    ]

    available_features = [

        col
        for col in feature_columns
        if col in data.columns

    ]

    if len(available_features) == 0:

        raise ValueError(
            "No training features found."
        )

    if "WeightKG" not in data.columns:

        raise ValueError(
            "Target column WeightKG missing."
        )

    X = data[available_features].copy()

    y = data["WeightKG"].copy()

    X = X.apply(
        pd.to_numeric,
        errors="coerce"
    )

    X = X.fillna(

        X.median(
            numeric_only=True
        )

    )

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42

    )

    model = RandomForestRegressor(

        n_estimators=100,

        random_state=42,

        n_jobs=-1

    )

    model.fit(

        X_train,

        y_train

    )

    predictions = model.predict(

        X_test

    )

    mae = mean_absolute_error(

        y_test,

        predictions

    )

    mse = mean_squared_error(

        y_test,

        predictions

    )

    rmse = np.sqrt(mse)

    r2 = r2_score(

        y_test,

        predictions

    )

    logger.info("=" * 70)
    logger.info("MODEL PERFORMANCE")
    logger.info("=" * 70)

    logger.info(f"MAE  : {mae:.2f}")
    logger.info(f"RMSE : {rmse:.2f}")
    logger.info(f"R2   : {r2:.4f}")

    MODEL_DIR.mkdir(

        parents=True,

        exist_ok=True

    )

    joblib.dump(

        model,

        MODEL_PATH

    )

    joblib.dump(

        available_features,

        FEATURE_PATH

    )

    metrics = {

        "MAE": round(float(mae), 4),

        "RMSE": round(float(rmse), 4),

        "R2": round(float(r2), 4),

        "TrainingRows": len(X_train),

        "TestingRows": len(X_test),

        "Features": available_features

    }

    with open(

        METRICS_PATH,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            metrics,

            file,

            indent=4

        )

    logger.info("Model Saved Successfully.")

    print("\n" + "=" * 60)
    print("MODEL TRAINING COMPLETED")
    print("=" * 60)
    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R²   : {r2:.4f}")
    print("=" * 60)

    return model


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    try:

        dataset = load_dataset(

            DATASET_PATH

        )

        train_model(

            dataset

        )

    except Exception as e:

        logger.exception(

            "Model Training Failed."

        )

        print("\nModel Training Failed\n")

        print(e)