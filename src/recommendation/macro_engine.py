"""
==============================================================
Project    : AI Fitness Intelligence Platform

Module     : Macronutrient Recommendation Engine

Author     : Harsh

Description:
Calculates daily protein, carbohydrates, fats and fiber
requirements based on body weight, calorie target and goal.
==============================================================
"""

from src.constants.nutrition_constants import (
    PROTEIN_WEIGHT_LOSS,
    PROTEIN_WEIGHT_GAIN,
    PROTEIN_MAINTAIN,
    FAT_PERCENTAGE,
    PROTEIN_CALORIES,
    CARB_CALORIES,
    FAT_CALORIES,
    FIBER_PER_1000_KCAL,
    WEIGHT_LOSS,
    WEIGHT_GAIN,
    MAINTAIN
)

from src.utils.validators import (
    validate_weight,
    validate_goal
)

from src.utils.logger import logger


# ==========================================================
# Protein
# ==========================================================

def calculate_protein(
    weight: float,
    goal: str
) -> float:

    validate_weight(weight)
    validate_goal(goal)

    if goal == WEIGHT_LOSS:

        factor = PROTEIN_WEIGHT_LOSS

    elif goal == WEIGHT_GAIN:

        factor = PROTEIN_WEIGHT_GAIN

    else:

        factor = PROTEIN_MAINTAIN

    return round(weight * factor)


# ==========================================================
# Fat
# ==========================================================

def calculate_fat(
    total_calories: float
) -> float:

    if total_calories <= 0:

        raise ValueError(
            "Calories must be greater than zero."
        )

    fat_calories = total_calories * FAT_PERCENTAGE

    return round(
        fat_calories / FAT_CALORIES
    )


# ==========================================================
# Carbohydrates
# ==========================================================

def calculate_carbs(
    total_calories: float,
    protein: float,
    fat: float
) -> float:

    protein_calories = protein * PROTEIN_CALORIES

    fat_calories = fat * FAT_CALORIES

    remaining_calories = (

        total_calories

        - protein_calories

        - fat_calories

    )

    if remaining_calories < 0:

        remaining_calories = 0

    return round(

        remaining_calories

        / CARB_CALORIES

    )


# ==========================================================
# Fiber
# ==========================================================

def calculate_fiber(
    total_calories: float
) -> float:

    return round(

        (total_calories / 1000)

        * FIBER_PER_1000_KCAL

    )


# ==========================================================
# Complete Recommendation
# ==========================================================

def recommend_macros(
    weight: float,
    goal: str,
    total_calories: float
) -> dict:

    """
    Generate complete macro recommendation.
    """

    try:

        protein = calculate_protein(

            weight,
            goal

        )

        fat = calculate_fat(

            total_calories

        )

        carbs = calculate_carbs(

            total_calories,

            protein,

            fat

        )

        fiber = calculate_fiber(

            total_calories

        )

        logger.info(

            "Macronutrient recommendation generated."

        )

        return {

            "goal": goal,

            "calories": round(total_calories),

            "protein_g": protein,

            "carbs_g": carbs,

            "fat_g": fat,

            "fiber_g": fiber

        }

    except Exception:

        logger.exception(

            "Failed to generate macro recommendation."

        )

        raise


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    result = recommend_macros(

        weight=80,

        goal=WEIGHT_LOSS,

        total_calories=2200

    )

    print("\n" + "=" * 60)

    print("MACRONUTRIENT RECOMMENDATION")

    print("=" * 60)

    for key, value in result.items():

        print(f"{key:20}: {value}")

    print("=" * 60)