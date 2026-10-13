"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : AI Recommendation Schemas

Author     : Harsh

Description:

Pydantic request and response models for
AI Recommendation APIs.

==============================================================
"""

from typing import List, Dict, Any

from pydantic import BaseModel, ConfigDict


# ==========================================================
# Weight Prediction
# ==========================================================

class WeightPredictionRequest(BaseModel):

    age: int

    height_cm: float

    calories_consumed: float

    calories_burned: float

    workout_minutes: int

    sleep_hours: float

    protein: float

    carbs: float

    fat: float


class WeightPredictionResponse(BaseModel):

    predicted_weight: float

    bmi: float | None = None

    status: str | None = None

    recommendations: list[str] = []

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Calorie Recommendation
# ==========================================================

class CalorieRecommendationRequest(BaseModel):

    weight: float

    height: float

    age: int

    gender: str

    activity_level: str

    goal: str


class CalorieRecommendationResponse(BaseModel):

    bmr: float

    tdee: float

    recommended_calories: float

    goal: str

    activity_level: str

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Macro Recommendation
# ==========================================================

class MacroRecommendationRequest(BaseModel):

    weight: float

    goal: str

    total_calories: float

class MacroRecommendationResponse(BaseModel):

    goal: str

    calories: float

    protein_g: float

    carbs_g: float

    fat_g: float

    fiber_g: float

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Hydration Recommendation
# ==========================================================

class HydrationRecommendationRequest(BaseModel):

    weight: float

    workout_minutes: int


class HydrationRecommendationResponse(BaseModel):

    weight_kg: float

    workout_minutes: int

    base_water_ml: float

    extra_water_ml: float

    total_water_ml: float

    total_water_liters: float

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Workout Recommendation
# ==========================================================

class WorkoutRecommendationRequest(BaseModel):

    split: str

    difficulty: str = "Intermediate"


class WorkoutRecommendationResponse(BaseModel):

    workout: Dict[str, Any]

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Meal Recommendation
# ==========================================================

class MealRecommendationRequest(BaseModel):

    meal_type: str

    vegetarian: bool = True

    limit: int = 5


class MealRecommendationResponse(BaseModel):

    meals: List[Dict[str, Any]]

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Health Score
# ==========================================================

class HealthScoreRequest(BaseModel):

    bmi: float

    activity_level: str

    protein: float

    recommended_protein: float

    water_liters: float

    recommended_water: float


class HealthScoreResponse(BaseModel):

    health_score: int

    status: str

    recommendations: List[str]

    summary: Dict[str, Any]

    model_config = ConfigDict(
        from_attributes=True
    )