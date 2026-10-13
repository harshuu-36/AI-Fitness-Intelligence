"""
==============================================================
Project    : AI Fitness Intelligence Platform

Module     : Hydration Recommendation Engine

Author     : Harsh

Description:
Calculates recommended daily water intake based on
body weight and workout duration.
==============================================================
"""

from src.constants.nutrition_constants import (
    WATER_PER_KG,
    WATER_PER_WORKOUT_MINUTE
)

from src.utils.validators import (
    validate_weight,
    validate_workout_minutes
)

from src.utils.logger import logger


# ==========================================================
# Hydration Recommendation
# ==========================================================

def calculate_water(
    weight: float,
    workout_minutes: int
) -> dict:
    """
    Calculate recommended daily water intake.

    Parameters
    ----------
    weight : float
        Body weight in kilograms.

    workout_minutes : int
        Total workout duration.

    Returns
    -------
    dict
        Recommended daily water intake.
    """

    try:

        # --------------------------------------------------
        # Validation
        # --------------------------------------------------

        validate_weight(weight)

        validate_workout_minutes(
            workout_minutes
        )

        # --------------------------------------------------
        # Calculation
        # --------------------------------------------------

        base_water = (

            weight

            * WATER_PER_KG

        )

        workout_water = (

            workout_minutes

            * WATER_PER_WORKOUT_MINUTE

        )

        total_water = (

            base_water

            + workout_water

        )

        logger.info(

            "Hydration recommendation generated."

        )

        return {

            "weight_kg": round(weight, 2),

            "workout_minutes": workout_minutes,

            "base_water_ml": round(base_water),

            "extra_water_ml": round(workout_water),

            "total_water_ml": round(total_water),

            "total_water_liters": round(
                total_water / 1000,
                2
            )

        }

    except Exception:

        logger.exception(

            "Failed to generate hydration recommendation."

        )

        raise


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    result = calculate_water(

        weight=80,

        workout_minutes=60

    )

    print("\n" + "=" * 60)

    print("HYDRATION RECOMMENDATION")

    print("=" * 60)

    for key, value in result.items():

        print(f"{key:22}: {value}")

    print("=" * 60)