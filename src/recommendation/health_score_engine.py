"""
==============================================================
Project    : AI Fitness Intelligence Platform

Module     : Health Score Engine

Author     : Harsh

Description:
Calculates an overall health score based on BMI,
activity level, protein intake and hydration.
==============================================================
"""

from typing import Dict, List

from src.constants.nutrition_constants import (
    UNDERWEIGHT_LIMIT,
    NORMAL_LIMIT,
    OVERWEIGHT_LIMIT
)

from src.utils.logger import logger


# ==========================================================
# Health Score
# ==========================================================

def calculate_health_score(
    bmi: float,
    activity_level: str,
    protein: float,
    recommended_protein: float,
    water_liters: float,
    recommended_water: float
) -> Dict:

    """
    Calculate overall health score.
    """

    if bmi <= 0:
        raise ValueError("BMI must be greater than zero.")

    if protein < 0 or recommended_protein < 0:
        raise ValueError("Protein values cannot be negative.")

    if water_liters < 0 or recommended_water < 0:
        raise ValueError("Water values cannot be negative.")

    score = 100

    recommendations: List[str] = []

    activity_level = activity_level.strip().lower()

    # ------------------------------------------------------
    # BMI
    # ------------------------------------------------------

    if bmi < UNDERWEIGHT_LIMIT:

        score -= 15

        recommendations.append(
            "BMI indicates underweight. Increase healthy calorie intake."
        )

    elif bmi >= OVERWEIGHT_LIMIT:

        score -= 15

        recommendations.append(
            "BMI indicates overweight. Aim for a calorie deficit and regular exercise."
        )

    elif bmi >= NORMAL_LIMIT:

        score -= 5

        recommendations.append(
            "Slightly reduce body fat to reach the healthy BMI range."
        )

    # ------------------------------------------------------
    # Activity
    # ------------------------------------------------------

    if activity_level == "sedentary":

        score -= 15

        recommendations.append(
            "Increase physical activity to at least 30 minutes daily."
        )

    elif activity_level == "light":

        score -= 8

        recommendations.append(
            "Aim for moderate activity at least 5 days per week."
        )

    # ------------------------------------------------------
    # Protein
    # ------------------------------------------------------

    if protein < recommended_protein:

        diff = round(

            recommended_protein - protein,

            1

        )

        score -= 10

        recommendations.append(

            f"Increase protein intake by approximately {diff} g/day."

        )

    # ------------------------------------------------------
    # Hydration
    # ------------------------------------------------------

    if water_liters < recommended_water:

        diff = round(

            recommended_water - water_liters,

            1

        )

        score -= 10

        recommendations.append(

            f"Drink approximately {diff} more liters of water daily."

        )

    # ------------------------------------------------------
    # Final Score
    # ------------------------------------------------------

    score = max(

        0,

        min(score, 100)

    )

    if score >= 90:

        status = "Excellent"

    elif score >= 75:

        status = "Good"

    elif score >= 60:

        status = "Average"

    else:

        status = "Needs Improvement"

    if not recommendations:

        recommendations.append(

            "Excellent! Maintain your current healthy lifestyle."

        )

    logger.info(

        f"Health Score Generated : {score} ({status})"

    )

    return {

        "health_score": score,

        "status": status,

        "recommendations": recommendations,

        "summary": {

            "bmi": round(bmi, 2),

            "activity_level": activity_level,

            "protein_intake": protein,

            "recommended_protein": recommended_protein,

            "water_intake": water_liters,

            "recommended_water": recommended_water

        }

    }


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    result = calculate_health_score(

        bmi=23.4,

        activity_level="moderate",

        protein=140,

        recommended_protein=140,

        water_liters=3.2,

        recommended_water=3.0

    )

    print("\n" + "=" * 60)

    print("HEALTH SCORE")

    print("=" * 60)

    print(f"Score  : {result['health_score']}")

    print(f"Status : {result['status']}")

    print("\nRecommendations")

    for rec in result["recommendations"]:

        print(f"- {rec}")

    print("=" * 60)