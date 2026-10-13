"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : AI Service

Author     : Harsh

Description:

Business logic for AI Recommendation APIs.

==============================================================
"""
from src.models.predict import predict_weight

from src.recommendation.calorie_engine import (
    recommend_calories
)

from src.recommendation.macro_engine import (
    recommend_macros
)

from src.recommendation.hydration_engine import (
    calculate_water
)

from src.recommendation.workout_engine import (
    WorkoutEngine
)

from src.recommendation.meal_engine import (
    MealEngine
)

from src.recommendation.health_score_engine import (
    calculate_health_score
)

from src.utils.logger import logger

from src.exceptions.custom_exceptions import (
    DatabaseException
)


class AIService:

    """
    AI Recommendation Service
    """

    def __init__(self):

        self.workout_engine = WorkoutEngine()

        self.meal_engine = MealEngine()

    # ==========================================================
    # Weight Prediction
    # ==========================================================

    def predict_weight(

        self,

        age: int,

        height_cm: float,

        calories_consumed: float,

        calories_burned: float,

        workout_minutes: int,

        sleep_hours: float,

        protein: float,

        carbs: float,

        fat: float

    ):

        try:

            result = predict_weight(

                age=age,

                height_cm=height_cm,

                calories_consumed=calories_consumed,

                calories_burned=calories_burned,

                workout_minutes=workout_minutes,

                sleep_hours=sleep_hours,

                protein=protein,

                carbs=carbs,

                fat=fat

            )

            return {

                "predicted_weight": result

            }

        except Exception as e:

            logger.exception(

                "Weight prediction failed."

            )

            raise DatabaseException(str(e))

    # ==========================================================
    # Calorie Recommendation
    # ==========================================================

    def recommend_calories(

        self,

        weight,

        height,

        age,

        gender,

        activity_level,

        goal

    ):

        try:

            return recommend_calories(

                weight,

                height,

                age,

                gender,

                activity_level,

                goal

            )

        except Exception as e:

            logger.exception(

                "Calorie recommendation failed."

            )

            raise DatabaseException(str(e))

    # ==========================================================
    # Macro Recommendation
    # ==========================================================

    def recommend_macros(

        self,

        weight,

        goal,

        total_calories

    ):

        try:

            return recommend_macros(

                weight,

                goal,

                total_calories

            )

        except Exception as e:

            logger.exception(

                "Macro recommendation failed."

            )

            raise DatabaseException(str(e))

    # ==========================================================
    # Hydration Recommendation
    # ==========================================================

    def recommend_hydration(

        self,

        weight,

        workout_minutes

    ):

        try:

            return calculate_water(

                weight,

                workout_minutes

            )

        except Exception as e:

            logger.exception(

                "Hydration recommendation failed."

            )

            raise DatabaseException(str(e))

    # ==========================================================
    # Workout Recommendation
    # ==========================================================

    def recommend_workout(
        self,
        split,
        difficulty
    ):

        try:

            workout = self.workout_engine.generate_workout(
                split=split,
                difficulty=difficulty
            )

            output = {}
            total_exercises = 0

            for muscle, df in workout.items():

                if df is None or df.empty:

                    output[muscle] = []

                else:

                    records = df.to_dict(
                        orient="records"
                    )

                    output[muscle] = records
                    total_exercises += len(records)

            print("\n" + "=" * 70)
            print("WORKOUT API RESPONSE")
            print("=" * 70)

            print(f"Split      : {split}")
            print(f"Difficulty : {difficulty}")
            print(f"Total      : {total_exercises}")

            for muscle, exercises in output.items():
                print(f"{muscle} : {len(exercises)} exercises")

            print("=" * 70 + "\n")

            return {

                "success": True,

                "split": split,

                "difficulty": difficulty,

                "total_exercises": total_exercises,

                "workout": output

            }

        except Exception as e:

            logger.exception(
                "Workout recommendation failed."
            )

            raise DatabaseException(str(e))

    # ==========================================================
    # Meal Recommendation
    # ==========================================================

    def recommend_meals(
        self,
        meal_type,
        vegetarian,
        limit
    ):

        try:

            meals = self.meal_engine.recommend(
                meal_type=meal_type,
                vegetarian=vegetarian,
                limit=limit
            )

            print("\n" + "="*60)
            print(meals.columns.tolist())
            print("="*60)
            print(meals.head())
            print("="*60)

            return {
                "meals": meals.to_dict(
                    orient="records"
                )
            }

        except Exception as e:

            logger.exception(
                "Meal recommendation failed."
            )

            raise DatabaseException(str(e))

    # ==========================================================
    # Health Score
    # ==========================================================

    def health_score(
        self,
        bmi,
        activity_level,
        protein,
        recommended_protein,
        water_liters,
        recommended_water
    ):

        try:

            return calculate_health_score(
                bmi,
                activity_level,
                protein,
                recommended_protein,
                water_liters,
                recommended_water
            )

        except Exception as e:

            logger.exception(
                "Health score calculation failed."
            )

            raise DatabaseException(str(e))