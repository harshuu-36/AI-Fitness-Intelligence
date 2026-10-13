"""
==============================================================
Project    : AI Fitness Intelligence Platform

Module     : Exercise Recommendation Engine

Author     : Harsh

Description:
Provides exercise recommendations based on
muscle group, difficulty level and equipment.
==============================================================
"""

from pathlib import Path

import pandas as pd

from src.utils.logger import logger


class ExerciseEngine:
    """
    Exercise Recommendation Engine
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
            / "exercise_database.csv"
        )

        if not csv_path.exists():

            raise FileNotFoundError(

                f"Exercise database not found:\n{csv_path}"

            )

        self.df = pd.read_csv(csv_path)

        print("=" * 60)
        print("CSV Loaded Successfully")
        print("Rows :", len(self.df))
        print("Columns :", self.df.columns.tolist())
        print("Unique Muscle Groups:")
        print(self.df["muscle_group"].unique())
        print("Unique Difficulty:")
        print(self.df["difficulty"].unique())
        print("=" * 60)

        logger.info(

            f"Exercise database loaded successfully ({len(self.df)} exercises)."

        )

    # ==========================================================
    # Exercise Recommendation
    # ==========================================================

    def recommend(

        self,

        muscle_group: str,

        difficulty: str | None = None,

        equipment: str | None = None,

        limit: int = 6

    ) -> pd.DataFrame:

        """
        Recommend exercises.

        Parameters
        ----------
        muscle_group : str

        difficulty : str | None

        equipment : str | None

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

        # ------------------------------------------
        # Clean Data
        # ------------------------------------------

        data["muscle_group"] = (
            data["muscle_group"]
            .astype(str)
            .str.strip()
        )

        data["difficulty"] = (
            data["difficulty"]
            .astype(str)
            .str.strip()
        )

        # ------------------------------------------
        # Debug
        # ------------------------------------------

        print("\n" + "=" * 60)
        print("Requested Muscle Group :", muscle_group)
        print("Requested Difficulty   :", difficulty)
        print("Available Columns      :", data.columns.tolist())
        print("Available Muscle Groups:", data["muscle_group"].unique())
        print("Available Difficulty   :", data["difficulty"].unique())
        print("=" * 60)

        # ------------------------------------------
        # Muscle Group
        # ------------------------------------------

        data = data[
            data["muscle_group"].str.lower()
            ==
            muscle_group.strip().lower()
        ]

        # ------------------------------------------
        # Difficulty
        # ------------------------------------------

        if difficulty:

            data = data[
                data["difficulty"].str.lower()
                ==
                difficulty.strip().lower()
            ]

        # ------------------------------------------
        # Equipment
        # ------------------------------------------

        if equipment:

            data = data[

                data["equipment"]

                .astype(str)

                .str.lower()

                ==

                equipment.lower()

            ]

        if data.empty:

            logger.warning(

                f"No exercises found for "
                f"Muscle={muscle_group}, "
                f"Difficulty={difficulty}, "
                f"Equipment={equipment}"

            )

            print("\n" + "=" * 60)
            print("NO MATCH FOUND")
            print("=" * 60)
            print("Requested Muscle Group :", muscle_group)
            print("Requested Difficulty   :", difficulty)
            print("Requested Equipment    :", equipment)
            print("Rows after filtering   :", len(data))
            print("=" * 60)

            return pd.DataFrame()

        logger.info(

            f"Exercise recommendation generated "

            f"({len(data.head(limit))} exercises)."

        )
        print("\n" + "=" * 60)
        print("MATCH FOUND")
        print("Muscle Group :", muscle_group)
        print("Difficulty   :", difficulty)
        print("Rows Found   :", len(data))
        print("=" * 60)
        if len(data) > limit:

            data = data.sample(
                n=limit,
                random_state=None
            )

        return data.reset_index(drop=True)


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    engine = ExerciseEngine()

    exercises = engine.recommend(

        muscle_group="Chest",

        difficulty="Intermediate",

        limit=6

    )

    print("\n" + "=" * 60)

    print("EXERCISE RECOMMENDATION")

    print("=" * 60)

    print(exercises)

    print("=" * 60)