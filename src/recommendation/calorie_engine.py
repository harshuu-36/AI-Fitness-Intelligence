"""
==============================================================
Project    : AI Fitness Intelligence Platform

Module     : Calorie Recommendation Engine

Author     : Harsh

Description:
Calculates BMR, TDEE and goal-based calorie recommendation.
==============================================================
"""

from src.utils.calculations import (
    calculate_bmr,
    calculate_tdee,
    calculate_goal_calories
)

from src.utils.validators import (
    validate_weight,
    validate_height,
    validate_age,
    validate_gender,
    validate_activity,
    validate_goal
)

from src.utils.logger import logger


# ==========================================================
# Calorie Recommendation
# ==========================================================

def recommend_calories(
    weight: float,
    height: float,
    age: int,
    gender: str,
    activity_level: str,
    goal: str
) -> dict:

    """
    Calculate daily calorie recommendation.

    Returns
    -------
    dict
    """

    try:

        # -----------------------------------------
        # Validation
        # -----------------------------------------

        validate_weight(weight)
        validate_height(height)
        validate_age(age)
        validate_gender(gender)
        validate_activity(activity_level)
        validate_goal(goal)

        # -----------------------------------------
        # Calculations
        # -----------------------------------------

        bmr = calculate_bmr(

            weight,
            height,
            age,
            gender

        )

        tdee = calculate_tdee(

            bmr,
            activity_level

        )

        recommended = calculate_goal_calories(

            tdee,
            goal

        )

        calorie_difference = round(

            recommended - tdee

        )

        logger.info(

            "Calorie recommendation generated successfully."

        )

        # -----------------------------------------
        # Response
        # -----------------------------------------

        return {

            "goal": goal,

            "activity_level": activity_level,

            "bmr": round(bmr),

            "tdee": round(tdee),

            "recommended_calories": round(recommended),

            "calorie_difference": calorie_difference

        }

    except Exception as e:

        logger.exception(

            "Failed to generate calorie recommendation."

        )

        raise


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    result = recommend_calories(

        weight=80,

        height=178,

        age=24,

        gender="Male",

        activity_level="moderate",

        goal="Weight Loss"

    )

    print("\n" + "=" * 60)
    print("CALORIE RECOMMENDATION")
    print("=" * 60)

    for key, value in result.items():

        print(f"{key:25}: {value}")

    print("=" * 60)