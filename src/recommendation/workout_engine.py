"""
==============================================================
Project    : AI Fitness Intelligence Platform

Module     : Workout Recommendation Engine

Author     : Harsh

Description:
Generates workout plans using Exercise Recommendation Engine.
==============================================================
"""

from typing import Dict

from src.recommendation.exercise_engine import ExerciseEngine
from src.utils.logger import logger


class WorkoutEngine:

    """
    Workout Recommendation Engine
    """

    SUPPORTED_SPLITS = {

        "full body": {
            "Chest": 2,
            "Back": 2,
            "Shoulders": 2,
            "Legs": 2,
            "Core": 1,
            "Abs": 1
        },

        "push pull legs": {
            "Chest": 2,
            "Shoulders": 2,
            "Triceps": 2,
            "Back": 2,
            "Biceps": 2,
            "Legs": 3
        },

        "upper lower": {
            "Chest": 2,
            "Back": 2,
            "Shoulders": 2,
            "Biceps": 1,
            "Triceps": 1,
            "Legs": 3
        },

        "bro split": {
            "Chest": 2,
            "Back": 2,
            "Shoulders": 2,
            "Biceps": 2,
            "Triceps": 2,
            "Legs": 2
        },

        "strength": {
            "Chest": 2,
            "Back": 2,
            "Legs": 3,
            "Shoulders": 2,
            "Core": 2
        },

        "cardio": {
            "Cardio": 8
        },

        "hiit": {
            "HIIT": 8
        },

        "home workout": {
            "Home Workout": 8
        }

    }

    # ======================================================

    def __init__(self):

        self.exercise_engine = ExerciseEngine()

    # ======================================================

    def generate_workout(

        self,

        split: str,

        difficulty: str = "Intermediate"

    ) -> Dict:

        split = split.lower().strip()

        if split not in self.SUPPORTED_SPLITS:

            raise ValueError(

                f"Unsupported workout split '{split}'. "

                f"Supported splits: "

                f"{', '.join(self.SUPPORTED_SPLITS.keys())}"

            )

        logger.info(

            f"Generating {split.upper()} workout ({difficulty})"

        )

        workout = {}

        used_exercises = set()

        for muscle_group, limit in self.SUPPORTED_SPLITS[split].items():

            df = self.exercise_engine.recommend(

                muscle_group=muscle_group,

                difficulty=difficulty,

                limit=limit

            )

            if df.empty:

                logger.warning(

                    f"No exercises found for {muscle_group}"

                )

                workout[muscle_group] = df

                continue

            # Remove duplicate exercises
            df = df[
                ~df["exercise_name"].isin(used_exercises)
            ]

            used_exercises.update(
                df["exercise_name"].tolist()
            )

            workout[muscle_group] = df.reset_index(drop=True)

            logger.info(

                f"{muscle_group}: {len(df)} exercises selected."

            )

        logger.info("Workout generated successfully.")

        return workout


# ======================================================

if __name__ == "__main__":

    engine = WorkoutEngine()

    workout = engine.generate_workout(

        split="Full Body",

        difficulty="Intermediate"

    )

    print("\n" + "=" * 60)
    print("WORKOUT")
    print("=" * 60)

    for muscle, df in workout.items():

        print(f"\n{muscle}")
        print(df)