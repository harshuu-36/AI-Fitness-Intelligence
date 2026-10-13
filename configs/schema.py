"""
====================================================================

Project    : AI Fitness Intelligence Platform

Configuration : Expected Database Schemas

Author     : Harsh

====================================================================
"""

EXPECTED_SCHEMAS = {

    "Users": [
        "UserID",
        "FirstName",
        "LastName",
        "Gender",
        "Age",
        "HeightCm",
        "WeightKg",
        "ActivityLevel",
        "GoalType",
        "RegistrationDate"
    ],

    "Meals": [
        "MealID",
        "UserID",
        "MealDate",
        "MealType"
    ],

    "MealItems": [
        "MealItemID",
        "MealID",
        "FoodID",
        "Quantity"
    ],

    "FoodItems": [
        "FoodID",
        "FoodName",
        "Calories",
        "Protein",
        "Carbs",
        "Fat"
    ],

    "Diet": [
        "DietID",
        "UserID",
        "DietDate",
        "CaloriesConsumed"
    ],

    "Exercises": [
        "ExerciseID",
        "ExerciseName",
        "Category",
        "METValue"
    ],

    "Workouts": [
        "WorkoutID",
        "UserID",
        "ExerciseID",
        "WorkoutDate",
        "DurationMinutes",
        "CaloriesBurned"
    ],

    "Sleep": [
        "SleepID",
        "UserID",
        "SleepDate",
        "SleepHours"
    ],

    "DailyProgress": [
        "ProgressID",
        "UserID",
        "ProgressDate",
        "WeightKg",
        "Steps"
    ],

    "Goals": [
        "GoalID",
        "UserID",
        "TargetWeight",
        "TargetCalories",
        "TargetSteps"
    ]

}