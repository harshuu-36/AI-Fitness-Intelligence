"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : Data Generation

Module     : Run Generation

Author     : Harsh

Description:

Generate FoodItems, Meals and MealItems
datasets and save them as CSV files.

==============================================================
"""

from pathlib import Path

import pandas as pd

from src.data_generation.food_generator import (
    generate_food_items
)

from src.data_generation.meals_generator import (
    generate_meals
)

from src.data_generation.meal_items_generator import (
    generate_meal_items
)

from src.utils.logger import logger


# ==========================================================
# Paths
# ==========================================================

GENERATED_DATA = Path("data/generated")

GENERATED_DATA.mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================================
# Main
# ==========================================================

def main():

    logger.info("=" * 70)
    logger.info("STARTING DATA GENERATION")
    logger.info("=" * 70)

    # ------------------------------------------------------
    # Load Users
    # ------------------------------------------------------

    users = pd.read_csv(
        GENERATED_DATA / "users.csv"
    )

    logger.info(
        f"Users Loaded : {len(users)}"
    )

    # ------------------------------------------------------
    # Generate FoodItems
    # ------------------------------------------------------

    food_items = generate_food_items()

    # ------------------------------------------------------
    # Generate Meals
    # ------------------------------------------------------

    meals = generate_meals(
        users
    )

    # ------------------------------------------------------
    # Generate MealItems
    # ------------------------------------------------------

    meal_items = generate_meal_items(
        meals,
        food_items
    )

    # ------------------------------------------------------
    # Save CSV Files
    # ------------------------------------------------------

    food_items.to_csv(
        GENERATED_DATA / "fooditems.csv",
        index=False
    )

    meals.to_csv(
        GENERATED_DATA / "meals.csv",
        index=False
    )

    meal_items.to_csv(
        GENERATED_DATA / "mealitems.csv",
        index=False
    )

    logger.info("=" * 70)

    logger.info("DATA GENERATION COMPLETED")

    logger.info(f"FoodItems : {len(food_items)}")

    logger.info(f"Meals : {len(meals)}")

    logger.info(f"MealItems : {len(meal_items)}")

    logger.info("=" * 70)


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()