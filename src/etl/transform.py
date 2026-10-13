"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : 02 - ETL

Module     : Transform

Author     : Harsh

Description:

Clean datasets and standardize column names.

====================================================================
"""

from src.utils.logger import logger


def transform_table(df, table_name):
    """
    Clean and standardize a single dataframe.
    """

    logger.info(f"Transforming {table_name}...")

    # -----------------------------------------
    # Remove duplicate rows
    # -----------------------------------------

    df = df.drop_duplicates()

    # -----------------------------------------
    # Trim spaces from string columns
    # -----------------------------------------

    object_columns = df.select_dtypes(include="object").columns

    for column in object_columns:

        df[column] = df[column].astype(str).str.strip()

    # -----------------------------------------
    # Standardize column names
    # -----------------------------------------

    column_mapping = {

        # IDs
        "userid": "UserID",
        "mealid": "MealID",
        "mealitemid": "MealItemID",
        "fooditemid": "FoodItemID",
        "exerciseid": "ExerciseID",
        "workoutid": "WorkoutID",
        "sleepid": "SleepID",
        "progressid": "ProgressID",
        "goalid": "GoalID",

        # User
        "firstname": "FirstName",
        "lastname": "LastName",
        "email": "Email",
        "passwordhash": "PasswordHash",
        "dateofbirth": "DateOfBirth",
        "gender": "Gender",
        "heightcm": "HeightCm",
        "createdat": "CreatedAt",
        "isactive": "IsActive",

        # Meals
        "mealdate": "MealDate",
        "mealtype": "MealType",
        "totalcalories": "TotalCalories",

        # Food
        "foodname": "FoodName",
        "servingsizegrams": "ServingSizeGrams",
        "calories": "Calories",
        "proteing": "ProteinG",
        "carbsg": "CarbsG",
        "fatg": "FatG",

        # Exercise
        "exercisename": "ExerciseName",
        "musclegroup": "MuscleGroup",
        "caloriesperhour": "CaloriesPerHour",
        "difficultylevel": "DifficultyLevel",

        # Workout
        "workoutdate": "WorkoutDate",
        "workouttype": "WorkoutType",
        "durationminutes": "DurationMinutes",
        "caloriesburned": "CaloriesBurned",

        # Sleep
        "sleepdate": "SleepDate",
        "sleepstart": "SleepStart",
        "sleepend": "SleepEnd",
        "sleepquality": "SleepQuality",

        # Progress
        "progressdate": "ProgressDate",
        "weightkg": "WeightKg",

        # Goals
        "goaltype": "GoalType",
        "targetweightkg": "TargetWeightKg",
        "startdate": "StartDate",
        "targetdate": "TargetDate",
        "status": "Status",

        # Diet
        "caloriesconsumed": "CaloriesConsumed"

    }

    df.rename(columns=column_mapping, inplace=True)

    logger.info(f"{table_name} transformed successfully.")

    return df


def transform_all_tables(datasets):
    """
    Transform all datasets.
    """

    transformed = {}

    for table_name, df in datasets.items():

        transformed[table_name] = transform_table(
            df,
            table_name
        )

    logger.info("All datasets transformed successfully.")

    return transformed