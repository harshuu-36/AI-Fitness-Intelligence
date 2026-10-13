"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : Data Generation

Module     : Meals Generator

Author     : Harsh

Description:

Generate realistic Meals dataset.

==============================================================
"""

import random
from datetime import timedelta

import pandas as pd

from src.utils.logger import logger


MEAL_TYPES = [

    "Breakfast",

    "Lunch",

    "Dinner",

    "Snack"

]


# ==========================================================
# Generate Meals
# ==========================================================

def generate_meals(users_df):

    logger.info(
        "Generating Meals dataset..."
    )

    rows = []

    meal_id = 1

    start_date = pd.Timestamp(
        "2025-01-01"
    )

    end_date = pd.Timestamp(
        "2025-01-30"
    )

    dates = pd.date_range(
        start_date,
        end_date,
        freq="D"
    )

    for _, user in users_df.iterrows():

        user_id = int(
            user["UserID"]
        )

        for date in dates:

            meal_count = random.randint(
                3,
                4
            )

            meals_today = random.sample(

                MEAL_TYPES,

                meal_count

            )

            for meal in meals_today:

                calories = random.randint(

                    250,

                    900

                )

                rows.append(

                    {

                        "MealID": meal_id,

                        "UserID": user_id,

                        "MealDate": date.date(),

                        "MealType": meal,

                        "TotalCalories": calories

                    }

                )

                meal_id += 1

    df = pd.DataFrame(rows)

    logger.info(

        f"{len(df)} Meals generated."

    )

    return df


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    users = pd.DataFrame(

        {

            "UserID": [

                1,

                2,

                3

            ]

        }

    )

    meals = generate_meals(users)

    print(

        meals.head()

    )

    print()

    print(

        meals.shape

    )