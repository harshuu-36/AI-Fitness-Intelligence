"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : AI Recommendation API

Author     : Harsh

Description:

API endpoints for AI Recommendation Engine.

==============================================================
"""

from fastapi import APIRouter

from src.services.ai_service import AIService

from src.api.schemas.ai_schema import (
    WeightPredictionRequest,
    WeightPredictionResponse,
    CalorieRecommendationRequest,
    CalorieRecommendationResponse,
    MacroRecommendationRequest,
    MacroRecommendationResponse,
    HydrationRecommendationRequest,
    HydrationRecommendationResponse,
    WorkoutRecommendationRequest,
    WorkoutRecommendationResponse,
    MealRecommendationRequest,
    MealRecommendationResponse,
    HealthScoreRequest,
    HealthScoreResponse
)

router = APIRouter(

    prefix="/ai",

    tags=["AI Recommendation"]

)

service = AIService()

# ==========================================================
# Weight Prediction
# ==========================================================

@router.post(

    "/predict-weight",

    response_model=WeightPredictionResponse

)
def predict_weight(
    request: WeightPredictionRequest
):

    return service.predict_weight(

        age=request.age,

        height_cm=request.height_cm,

        calories_consumed=request.calories_consumed,

        calories_burned=request.calories_burned,

        workout_minutes=request.workout_minutes,

        sleep_hours=request.sleep_hours,

        protein=request.protein,

        carbs=request.carbs,

        fat=request.fat

    )


# ==========================================================
# Calorie Recommendation
# ==========================================================

@router.post(

    "/recommend-calories",

    response_model=CalorieRecommendationResponse

)
def recommend_calories(
    request: CalorieRecommendationRequest
):

    return service.recommend_calories(

        weight=request.weight,

        height=request.height,

        age=request.age,

        gender=request.gender,

        activity_level=request.activity_level,

        goal=request.goal

    )


# ==========================================================
# Macro Recommendation
# ==========================================================

@router.post(

    "/recommend-macros",

    response_model=MacroRecommendationResponse

)
def recommend_macros(
    request: MacroRecommendationRequest
):

    return service.recommend_macros(

        weight=request.weight,

        goal=request.goal,

        total_calories=request.total_calories

    )


# ==========================================================
# Hydration Recommendation
# ==========================================================

@router.post(

    "/recommend-hydration",

    response_model=HydrationRecommendationResponse

)
def recommend_hydration(
    request: HydrationRecommendationRequest
):

    return service.recommend_hydration(

        weight=request.weight,

        workout_minutes=request.workout_minutes

    )


# ==========================================================
# Workout Recommendation
# ==========================================================

@router.post(

    "/recommend-workout",

    response_model=WorkoutRecommendationResponse

)
def recommend_workout(
    request: WorkoutRecommendationRequest
):

    return service.recommend_workout(

        split=request.split,

        difficulty=request.difficulty

    )


# ==========================================================
# Meal Recommendation
# ==========================================================

@router.post(

    "/recommend-meals",

    response_model=MealRecommendationResponse

)
def recommend_meals(
    request: MealRecommendationRequest
):

    return service.recommend_meals(

        meal_type=request.meal_type,

        vegetarian=request.vegetarian,

        limit=request.limit

    )


# ==========================================================
# Health Score
# ==========================================================

@router.post(

    "/health-score",

    response_model=HealthScoreResponse

)
def health_score(
    request: HealthScoreRequest
):

    return service.health_score(

        bmi=request.bmi,

        activity_level=request.activity_level,

        protein=request.protein,

        recommended_protein=request.recommended_protein,

        water_liters=request.water_liters,

        recommended_water=request.recommended_water

    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print("AI Recommendation API loaded successfully.")