"""
==============================================================
AI Fitness Intelligence Platform

Nutrition Engine

Author : Harsh

Description:
Integrates calorie, macro, hydration,
BMI and health score engines.

==============================================================
"""

from src.recommendation.calorie_engine import (
    recommend_calories
)

from src.recommendation.macro_engine import (
    recommend_macros
)

from src.recommendation.hydration_engine import (
    calculate_water
)

from src.recommendation.health_score_engine import (
    calculate_health_score
)

from src.utils.calculations import (
    calculate_bmi,
    get_bmi_category
)

from src.utils.logger import logger


def generate_nutrition_plan(
    weight: float,
    height: float,
    age: int,
    gender: str,
    activity_level: str,
    goal: str,
    workout_minutes: int
) -> dict:
    """
    Generate complete nutrition recommendation.
    """

    try:

        # ======================================================
        # Calorie Recommendation
        # ======================================================

        calorie_data = recommend_calories(

            weight=weight,

            height=height,

            age=age,

            gender=gender,

            activity_level=activity_level,

            goal=goal

        )

        # ======================================================
        # Macronutrients
        # ======================================================

        macro_data = recommend_macros(

            weight=weight,

            goal=goal,

            total_calories=calorie_data["recommended_calories"]

        )

        # ======================================================
        # Hydration
        # ======================================================

        water_data = calculate_water(

            weight=weight,

            workout_minutes=workout_minutes

        )

        # ======================================================
        # BMI
        # ======================================================

        bmi = calculate_bmi(

            weight,

            height

        )

        bmi_category = get_bmi_category(

            bmi

        )

        # ======================================================
        # Health Score
        # ======================================================

        health_data = calculate_health_score(

            bmi=bmi,

            activity_level=activity_level,

            protein=macro_data["protein"],

            recommended_protein=macro_data["protein"],

            water_liters=water_data["water_liters"],

            recommended_water=water_data["water_liters"]

        )

        logger.info(
            "Nutrition plan generated successfully."
        )

        # ======================================================
        # Final Result
        # ======================================================

        return {

            "bmr": calorie_data["bmr"],

            "tdee": calorie_data["tdee"],

            "recommended_calories":
                calorie_data["recommended_calories"],

            "protein":
                macro_data["protein"],

            "carbs":
                macro_data["carbs"],

            "fat":
                macro_data["fat"],

            "fiber":
                macro_data["fiber"],

            "water_ml":
                water_data["water_ml"],

            "water_liters":
                water_data["water_liters"],

            "bmi":
                round(bmi, 2),

            "bmi_category":
                bmi_category,

            "health_score":
                health_data["health_score"],

            "health_status":
                health_data["status"],

            "recommendations":
                health_data["recommendations"]

        }

    except Exception:

        logger.exception(
            "Nutrition engine failed."
        )

        raise


if __name__ == "__main__":

    report = generate_nutrition_plan(

        weight=80,

        height=178,

        age=24,

        gender="Male",

        activity_level="moderate",

        goal="Weight Loss",

        workout_minutes=60

    )

    print("\n========== NUTRITION REPORT ==========\n")

    for key, value in report.items():

        print(f"{key:25}: {value}")

    print("\n======================================")