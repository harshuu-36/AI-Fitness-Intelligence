"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : Data Generation

Module     : Food Generator

Author     : Harsh

Description:

Generate realistic FoodItems dataset.

==============================================================
"""

import random

import pandas as pd

from src.utils.logger import logger


# ==========================================================
# Food Database
# ==========================================================

FOODS = [

    ("Rice", 130, 2.7, 28.0, 0.3),
    ("Chapati", 120, 3.5, 22.0, 2.0),
    ("Brown Rice", 112, 2.6, 23.0, 0.8),
    ("Oats", 389, 16.9, 66.3, 6.9),
    ("Paneer", 265, 18.3, 1.2, 20.8),
    ("Tofu", 144, 15.7, 3.9, 8.7),
    ("Milk", 61, 3.2, 4.8, 3.3),
    ("Curd", 98, 11.0, 3.4, 4.3),
    ("Banana", 89, 1.1, 23.0, 0.3),
    ("Apple", 52, 0.3, 14.0, 0.2),
    ("Orange", 47, 0.9, 12.0, 0.1),
    ("Mango", 60, 0.8, 15.0, 0.4),
    ("Peanut Butter", 588, 25.0, 20.0, 50.0),
    ("Almonds", 579, 21.0, 22.0, 50.0),
    ("Cashews", 553, 18.0, 30.0, 44.0),
    ("Walnuts", 654, 15.0, 14.0, 65.0),
    ("Boiled Potato", 87, 2.0, 20.0, 0.1),
    ("Sweet Potato", 86, 1.6, 20.0, 0.1),
    ("Broccoli", 35, 2.8, 7.0, 0.4),
    ("Spinach", 23, 2.9, 3.6, 0.4),
    ("Carrot", 41, 0.9, 10.0, 0.2),
    ("Tomato", 18, 0.9, 3.9, 0.2),
    ("Cucumber", 15, 0.7, 3.6, 0.1),
    ("Chickpeas", 364, 19.0, 61.0, 6.0),
    ("Rajma", 333, 24.0, 60.0, 0.8),
    ("Moong Dal", 347, 24.0, 63.0, 1.2),
    ("Masoor Dal", 352, 25.0, 60.0, 1.0),
    ("Soy Chunks", 345, 52.0, 33.0, 0.5),
    ("Protein Shake", 420, 35.0, 40.0, 8.0),
    ("Whole Wheat Bread", 247, 13.0, 41.0, 4.2)

]


# ==========================================================
# Generate FoodItems
# ==========================================================

def generate_food_items():

    logger.info("Generating FoodItems dataset...")

    rows = []

    food_id = 1

    for _ in range(10):

        random.shuffle(FOODS)

        for food in FOODS:

            serving = random.choice(

                [50, 75, 100, 125, 150, 200]

            )

            rows.append({

                "FoodItemID": food_id,

                "FoodName": food[0],

                "ServingSizeGrams": serving,

                "Calories": round(food[1] * serving / 100, 2),

                "ProteinG": round(food[2] * serving / 100, 2),

                "CarbsG": round(food[3] * serving / 100, 2),

                "FatG": round(food[4] * serving / 100, 2)

            })

            food_id += 1

    df = pd.DataFrame(rows)

    logger.info(

        f"{len(df)} FoodItems generated successfully."

    )

    return df


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    foods = generate_food_items()

    print(foods.head())

    print()

    print(foods.shape)