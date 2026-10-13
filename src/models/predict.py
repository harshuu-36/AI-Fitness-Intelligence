"""
==============================================================
Project    : AI Fitness Intelligence Platform

Module     : Weight Prediction

Author     : Harsh

Description:
Loads the trained Random Forest model and predicts
user weight based on fitness and nutrition features.
==============================================================
"""

from pathlib import Path

import joblib
import pandas as pd

from src.utils.logger import logger


# ======================================================
# Model Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    BASE_DIR
    / "artifacts"
    / "models"
    / "weight_prediction_model.pkl"
)

FEATURE_PATH = (
    BASE_DIR
    / "artifacts"
    / "models"
    / "feature_columns.pkl"
)

DATA_PATH = (
    BASE_DIR
    / "artifacts"
    / "processed_data"
    / "feature_engineered_data.csv"
)


def _build_training_data():
    if DATA_PATH.exists():
        data = pd.read_csv(DATA_PATH)
        if all(col in data.columns for col in [
            "Age", "HeightCM", "CaloriesConsumed", "CaloriesBurned",
            "WorkoutMinutes", "SleepHours", "ProteinG", "CarbsG", "FatG", "WeightKG"
        ]):
            return data

    generated_dir = BASE_DIR / "data" / "generated"
    users = pd.read_csv(generated_dir / "users.csv")
    progress = pd.read_csv(generated_dir / "weight.csv")
    diet = pd.read_csv(generated_dir / "diet.csv")
    sleep = pd.read_csv(generated_dir / "sleep.csv")
    workouts = pd.read_csv(generated_dir / "workouts.csv")

    users = users[["UserID", "DateOfBirth", "HeightCM"]].copy()
    users["Age"] = (
        (pd.Timestamp.today() - pd.to_datetime(users["DateOfBirth"]))
        .dt.days / 365.25
    ).round().astype(int)

    latest_weight = progress.sort_values("ProgressDate").groupby("UserID", as_index=False).tail(1)
    latest_weight = latest_weight[["UserID", "ProgressDate", "WeightKG"]]

    diet_daily = diet.groupby(["UserID", "MealDate"], as_index=False).agg(
        CaloriesConsumed=("CaloriesConsumed", "sum"),
        ProteinG=("ProteinG", "sum"),
        CarbsG=("CarbsG", "sum"),
        FatG=("FatG", "sum"),
    )
    diet_daily = diet_daily.rename(columns={"MealDate": "ProgressDate"})

    sleep_daily = sleep.groupby(["UserID", "SleepDate"], as_index=False).agg(
        SleepMinutes=("DurationMinutes", "sum")
    )
    sleep_daily["SleepHours"] = sleep_daily["SleepMinutes"] / 60
    sleep_daily = sleep_daily.rename(columns={"SleepDate": "ProgressDate"})

    workouts_daily = workouts.groupby(["UserID", "WorkoutDate"], as_index=False).agg(
        WorkoutMinutes=("DurationMinutes", "sum")
    )
    workouts_daily["CaloriesBurned"] = workouts_daily["WorkoutMinutes"] * 7.5
    workouts_daily = workouts_daily.rename(columns={"WorkoutDate": "ProgressDate"})

    data = latest_weight.merge(users, on="UserID", how="left")
    data = data.merge(diet_daily, on=["UserID", "ProgressDate"], how="left")
    data = data.merge(sleep_daily, on=["UserID", "ProgressDate"], how="left")
    data = data.merge(workouts_daily, on=["UserID", "ProgressDate"], how="left")

    data["CaloriesConsumed"] = data["CaloriesConsumed"].fillna(0)
    data["ProteinG"] = data["ProteinG"].fillna(0)
    data["CarbsG"] = data["CarbsG"].fillna(0)
    data["FatG"] = data["FatG"].fillna(0)
    data["SleepHours"] = data["SleepHours"].fillna(0)
    data["WorkoutMinutes"] = data["WorkoutMinutes"].fillna(0)
    data["CaloriesBurned"] = data["CaloriesBurned"].fillna(0)

    return data


def _train_default_model():
    from sklearn.ensemble import RandomForestRegressor

    data = _build_training_data()
    feature_columns = [
        "Age",
        "HeightCM",
        "CaloriesConsumed",
        "CaloriesBurned",
        "WorkoutMinutes",
        "SleepHours",
        "ProteinG",
        "CarbsG",
        "FatG",
    ]

    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(data[feature_columns], data["WeightKG"])

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(feature_columns, FEATURE_PATH)
    return model, feature_columns


# ======================================================
# Load Model
# ======================================================

try:
    if MODEL_PATH.exists() and FEATURE_PATH.exists():
        model = joblib.load(MODEL_PATH)
        feature_columns = joblib.load(FEATURE_PATH)
        logger.info("Weight prediction model loaded successfully.")
    else:
        model, feature_columns = _train_default_model()
        logger.info("Weight prediction model trained and saved automatically.")

except Exception as e:
    logger.exception("Failed to load ML model.")
    raise RuntimeError(
        f"Unable to load model artifacts.\n{e}"
    )


# ======================================================
# Prediction Function
# ======================================================

def predict_weight(
    age: int,
    height_cm: float,
    calories_consumed: float,
    calories_burned: float,
    workout_minutes: float,
    sleep_hours: float,
    protein: float,
    carbs: float,
    fat: float
) -> float:

    """
    Predict user's weight.

    Returns
    -------
    float
        Predicted weight in KG.
    """

    # --------------------------------------------
    # Basic Validation
    # --------------------------------------------

    if age <= 0:
        raise ValueError("Age must be greater than 0.")

    if height_cm <= 0:
        raise ValueError("Height must be greater than 0.")

    if calories_consumed < 0:
        raise ValueError("Calories consumed cannot be negative.")

    if calories_burned < 0:
        raise ValueError("Calories burned cannot be negative.")

    if workout_minutes < 0:
        raise ValueError("Workout minutes cannot be negative.")

    if sleep_hours <= 0:
        raise ValueError("Sleep hours must be greater than 0.")

    if protein < 0 or carbs < 0 or fat < 0:
        raise ValueError("Macronutrients cannot be negative.")

    # --------------------------------------------
    # Create DataFrame
    # --------------------------------------------

    input_data = pd.DataFrame(
        [
            {
                "Age": age,
                "HeightCM": height_cm,
                "CaloriesConsumed": calories_consumed,
                "CaloriesBurned": calories_burned,
                "WorkoutMinutes": workout_minutes,
                "SleepHours": sleep_hours,
                "ProteinG": protein,
                "CarbsG": carbs,
                "FatG": fat
            }
        ]
    )

    # --------------------------------------------
    # Match Training Features
    # --------------------------------------------

    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # --------------------------------------------
    # Prediction
    # --------------------------------------------

    prediction = model.predict(input_data)[0]

    prediction = round(float(prediction), 2)

    logger.info(
        f"Weight Prediction Successful : {prediction} KG"
    )

    return prediction


# ======================================================
# Testing
# ======================================================

if __name__ == "__main__":

    try:

        predicted_weight = predict_weight(

            age=25,
            height_cm=175,

            calories_consumed=2300,
            calories_burned=500,

            workout_minutes=60,

            sleep_hours=8,

            protein=140,
            carbs=250,
            fat=60
        )

        print("=" * 60)
        print(f"Predicted Weight : {predicted_weight} KG")
        print("=" * 60)

    except Exception as e:

        print("=" * 60)
        print("Prediction Failed")
        print(e)
        print("=" * 60)