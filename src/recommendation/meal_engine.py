"""
==============================================================
Project    : AI Fitness Intelligence Platform

Module     : Meal Recommendation Engine

Author     : Harsh

Description:
Provides meal recommendations from the food database
based on meal type and dietary preference.
==============================================================
"""

from pathlib import Path

import pandas as pd

from src.utils.logger import logger


class MealEngine:
    """
    Meal Recommendation Engine
    """

    # ==========================================================
    # Constructor
    # ==========================================================

    def __init__(self):

        project_root = Path(__file__).resolve().parents[2]

        csv_path = (
            project_root
            / "data"
            / "master"
            / "food_database.csv"
        )

        if not csv_path.exists():

            raise FileNotFoundError(
                f"Food database not found:\n{csv_path}"
            )

        self.df = pd.read_csv(csv_path)

        logger.info(
            f"Food database loaded successfully ({len(self.df)} foods)."
        )

    # ==========================================================
    # Meal Recommendation
    # ==========================================================

    def recommend(

        self,

        meal_type: str,

        vegetarian: bool = True,

        limit: int = 5

    ) -> pd.DataFrame:

        """
        Recommend meals based on meal type.

        Parameters
        ----------
        meal_type : str
        vegetarian : bool
        limit : int

        Returns
        -------
        pd.DataFrame
        """

        if limit <= 0:

            raise ValueError(
                "Limit must be greater than zero."
            )

        data = self.df.copy()

        data = data[

            data["meal_type"]

            .astype(str)

            .str.lower()

            ==

            meal_type.lower()

        ]

        if vegetarian:

            data = data[

                data["vegetarian"]

                .astype(str)

                .str.lower()

                ==

                "yes"

            ]

        if data.empty:

            logger.warning(

                f"No meals found for "

                f"{meal_type}"

            )

            return pd.DataFrame()

        logger.info(

            f"Meal recommendation generated "

            f"({len(data.head(limit))} meals)."

        )

        return data.head(limit).reset_index(drop=True)


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    engine = MealEngine()

    breakfast = engine.recommend(

        meal_type="Breakfast",

        vegetarian=True,

        limit=5

    )

    print("\n" + "=" * 60)

    print("BREAKFAST RECOMMENDATIONS")

    print("=" * 60)

    print(breakfast)

    print("=" * 60)