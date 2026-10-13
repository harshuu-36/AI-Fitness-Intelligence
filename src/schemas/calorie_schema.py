"""
==============================================================
AI Fitness Intelligence Platform

Calorie Recommendation Schema

Author : Harsh
==============================================================
"""

from typing import Dict, List

from pydantic import BaseModel, Field


class CalorieRecommendation(BaseModel):
    """
    Complete nutrition recommendation result.
    """

    # ======================================================
    # Energy
    # ======================================================

    bmr: float = Field(
        ...,
        gt=0,
        description="Basal Metabolic Rate"
    )

    tdee: float = Field(
        ...,
        gt=0,
        description="Total Daily Energy Expenditure"
    )

    goal_calories: float = Field(
        ...,
        gt=0,
        description="Recommended daily calories"
    )

    # ======================================================
    # Macronutrients
    # ======================================================

    protein: float = Field(
        ...,
        ge=0,
        description="Protein (grams)"
    )

    carbs: float = Field(
        ...,
        ge=0,
        description="Carbohydrates (grams)"
    )

    fats: float = Field(
        ...,
        ge=0,
        description="Fats (grams)"
    )

    fiber: float = Field(
        ...,
        ge=0,
        description="Fiber (grams)"
    )

    # ======================================================
    # Hydration
    # ======================================================

    water_ml: float = Field(
        ...,
        ge=0,
        description="Water intake (ml)"
    )

    water_liters: float = Field(
        ...,
        ge=0,
        description="Water intake (liters)"
    )

    # ======================================================
    # BMI
    # ======================================================

    bmi: float = Field(
        ...,
        gt=0,
        description="Body Mass Index"
    )

    bmi_category: str = Field(
        ...,
        description="BMI Category"
    )

    # ======================================================
    # Goal
    # ======================================================

    goal: str = Field(
        ...,
        description="Fitness Goal"
    )

    # ======================================================
    # Health Score
    # ======================================================

    health_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Overall Health Score"
    )

    # ======================================================
    # Meal Distribution
    # ======================================================

    meal_distribution: Dict[str, float] = Field(
        default_factory=dict,
        description="Calories per meal"
    )

    # ======================================================
    # AI Explanation
    # ======================================================

    explanation: List[str] = Field(
        default_factory=list,
        description="AI-generated explanations"
    )

    # ======================================================
    # Nutrition Notes
    # ======================================================

    nutrition_tips: List[str] = Field(
        default_factory=list,
        description="Nutrition recommendations"
    )

    warnings: List[str] = Field(
        default_factory=list,
        description="Health warnings if applicable"
    )