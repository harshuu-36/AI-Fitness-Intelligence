"""
==============================================================
AI Fitness Intelligence Platform

Calculation Utilities

Author : Harsh
==============================================================
"""

from src.constants.nutrition_constants import (
    ACTIVITY_MULTIPLIERS,
    CALORIE_DEFICIT,
    CALORIE_SURPLUS,
    WATER_PER_KG,
    WATER_PER_WORKOUT_MINUTE,
    UNDERWEIGHT_LIMIT,
    NORMAL_LIMIT,
    OVERWEIGHT_LIMIT,
    WEIGHT_GAIN,
    WEIGHT_LOSS,
    MAINTAIN
)


def calculate_bmr(
    weight: float,
    height: float,
    age: int,
    gender: str
) -> float:
    """
    Calculate Basal Metabolic Rate using
    Mifflin-St Jeor Equation.
    """

    gender = gender.lower()

    if gender == "male":

        return (
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            + 5
        )

    return (
        (10 * weight)
        + (6.25 * height)
        - (5 * age)
        - 161
    )


def calculate_tdee(
    bmr: float,
    activity_level: str
) -> float:
    """
    Calculate Total Daily Energy Expenditure.
    """

    multiplier = ACTIVITY_MULTIPLIERS.get(
        activity_level.lower(),
        1.55
    )

    return bmr * multiplier


def calculate_goal_calories(
    tdee: float,
    goal: str
) -> float:
    """
    Calculate calories according to goal.
    """

    if goal == WEIGHT_LOSS:
        return tdee - CALORIE_DEFICIT

    if goal == WEIGHT_GAIN:
        return tdee + CALORIE_SURPLUS

    return tdee


def calculate_bmi(
    weight: float,
    height: float
) -> float:
    """
    Calculate BMI.
    """

    height_m = height / 100

    return round(
        weight / (height_m ** 2),
        2
    )


def get_bmi_category(
    bmi: float
) -> str:
    """
    Return BMI category.
    """

    if bmi < UNDERWEIGHT_LIMIT:
        return "Underweight"

    if bmi < NORMAL_LIMIT:
        return "Normal"

    if bmi < OVERWEIGHT_LIMIT:
        return "Overweight"

    return "Obese"


def calculate_water(
    weight: float,
    workout_minutes: int
) -> float:
    """
    Calculate recommended water intake.
    """

    return (
        (weight * WATER_PER_KG)
        +
        (workout_minutes * WATER_PER_WORKOUT_MINUTE)
    )