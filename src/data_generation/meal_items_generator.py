"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : Data Generation

Module     : Meal Items Generator

Author     : Harsh

Description:

Generate MealItems dataset by assigning
FoodItems to Meals.

==============================================================
"""

import random

import pandas as pd

from src.utils.logger import logger


# ==========================================================
# Generate Meal Items
# ==========================================================

def generate_meal_items(
    meals_df: pd.DataFrame,
    food_df: pd.DataFrame
) -> pd.DataFrame:

    logger.info(
        "Generating MealItems dataset..."
    )

    rows = []

    meal_item_id = 1

    food_ids = food_df["FoodItemID"].tolist()

    for meal_id in meals_df["MealID"]:


        number_of_foods = random.randint(
            2,
            5
        )

        selected_foods = random.sample(
            food_ids,
            number_of_foods
        )

        for food_id in selected_foods:

            rows.append(

                {

                    "MealItemID": meal_item_id,

                    "MealID": meal_id,

                    "FoodItemID": food_id,

                    "QuantityGrams": random.choice(
                        [
                            50,
                            75,
                            100,
                            125,
                            150,
                            200
                        ]
                    )

                }

            )

            meal_item_id += 1

    df = pd.DataFrame(rows)

    logger.info(

        f"{len(df)} MealItems generated."

    )

    return df


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    meals = pd.DataFrame(

        {

            "MealID": [1, 2, 3]

        }

    )

    foods = pd.DataFrame(

        {

            "FoodItemID": list(
                range(1, 21)
            )

        }

    )

    meal_items = generate_meal_items(
        meals,
        foods
    )

    print(meal_items.head())

    print()

    print(meal_items.shape)