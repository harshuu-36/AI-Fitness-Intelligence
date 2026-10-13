"""
Synthetic Data Generator - AI Fitness Intelligence Platform
Generates 500 users + 1 year of workout, diet, sleep, and weight records.
Outputs: users.csv, workouts.csv, diet.csv, sleep.csv, weight.csv
"""

from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import date, timedelta
from pathlib import Path

# ---------------------------------------------------------------
# 1. Setup & reproducibility
# ---------------------------------------------------------------
SEED = 42
Faker.seed(SEED)
random.seed(SEED)
np.random.seed(SEED)
fake = Faker()

NUM_USERS = 500
START_DATE = date(2025, 8, 31)
END_DATE = date(2026, 8, 30)
WORKOUT_TYPES = ['Strength', 'Cardio', 'Mixed', 'Flexibility']
MEAL_TYPES = ['Breakfast', 'Lunch', 'Dinner', 'Snack']

# ---------------------------------------------------------------
# 2. Users - each gets a hidden "consistency" trait that drives
#    behavior across every other table, so a single user's data
#    is internally coherent (not independently random per table).
# ---------------------------------------------------------------
def generate_users(n):
    users = []
    for uid in range(1, n + 1):
        gender = random.choice(['M', 'F'])
        dob = fake.date_of_birth(minimum_age=18, maximum_age=65)
        height = np.random.normal(175 if gender == 'M' else 162, 7)
        starting_weight = np.random.normal(82 if gender == 'M' else 68, 12)
        goal_type = random.choices(
            ['WeightLoss', 'MuscleGain', 'Maintain'], weights=[0.45, 0.30, 0.25]
        )[0]
        consistency = float(np.clip(np.random.normal(0.55, 0.2), 0.05, 0.95))

        users.append({
            'UserID': uid,
            'FirstName': fake.first_name_male() if gender == 'M' else fake.first_name_female(),
            'LastName': fake.last_name(),
            'Email': fake.unique.email(),
            'DateOfBirth': dob,
            'Gender': gender,
            'HeightCM': round(height, 1),
            'StartingWeightKG': round(max(starting_weight, 45), 1),
            'GoalType': goal_type,
            '_consistency': consistency,   # internal use only, dropped before export
        })
    return pd.DataFrame(users)


# ---------------------------------------------------------------
# 3. Workouts - daily probability scales with consistency trait
# ---------------------------------------------------------------
def generate_workouts(users_df):
    rows = []
    workout_id = 1
    for _, u in users_df.iterrows():
        current = START_DATE
        while current <= END_DATE:
            if random.random() < (0.15 + 0.5 * u['_consistency']):
                rows.append({
                    'WorkoutID': workout_id,
                    'UserID': u['UserID'],
                    'WorkoutDate': current,
                    'WorkoutType': random.choice(WORKOUT_TYPES),
                    'DurationMinutes': int(np.clip(np.random.normal(45, 15), 10, 120)),
                })
                workout_id += 1
            current += timedelta(days=1)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------
# 4. Sleep - weekend effect + quality correlated with duration
# ---------------------------------------------------------------
def generate_sleep(users_df):
    rows = []
    sleep_id = 1
    for _, u in users_df.iterrows():
        current = START_DATE
        while current <= END_DATE:
            if random.random() < (0.3 + 0.6 * u['_consistency']):
                is_weekend = current.weekday() >= 5
                base_hours = 8.2 if is_weekend else 7.5
                hours = float(np.clip(np.random.normal(base_hours, 1.0), 3.5, 11))
                quality = int(np.clip(np.random.normal(5 + hours / 2, 1.5), 1, 10))
                start_hour = 22 + np.random.normal(0, 1)
                sleep_start = pd.Timestamp(current) + pd.Timedelta(hours=start_hour)
                sleep_end = sleep_start + pd.Timedelta(hours=hours)
                rows.append({
                    'SleepID': sleep_id,
                    'UserID': u['UserID'],
                    'SleepDate': current,
                    'SleepStart': sleep_start,
                    'SleepEnd': sleep_end,
                    'DurationMinutes': round(hours * 60),
                    'SleepQuality': quality,
                })
                sleep_id += 1
            current += timedelta(days=1)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------
# 5. Diet - 1-4 meals/day, calories vary by meal type and goal
# ---------------------------------------------------------------
MEAL_CALORIE_RANGES = {
    'Breakfast': (250, 550),
    'Lunch': (450, 800),
    'Dinner': (500, 900),
    'Snack': (80, 300),
}

def generate_diet(users_df):
    rows = []
    meal_id = 1
    for _, u in users_df.iterrows():
        # goal shifts overall calorie intake up or down slightly
        goal_multiplier = {'WeightLoss': 0.85, 'MuscleGain': 1.15, 'Maintain': 1.0}[u['GoalType']]
        current = START_DATE
        while current <= END_DATE:
            if random.random() < (0.4 + 0.5 * u['_consistency']):
                meals_today = random.choices([2, 3, 4], weights=[0.2, 0.55, 0.25])[0]
                todays_meal_types = random.sample(MEAL_TYPES, k=min(meals_today, len(MEAL_TYPES)))
                for meal_type in todays_meal_types:
                    low, high = MEAL_CALORIE_RANGES[meal_type]
                    calories = int(np.clip(
                        np.random.normal((low + high) / 2, (high - low) / 6) * goal_multiplier,
                        low * 0.7, high * 1.3
                    ))
                    protein = round(calories * random.uniform(0.15, 0.30) / 4, 1)  # 4 kcal/g protein
                    carbs = round(calories * random.uniform(0.35, 0.55) / 4, 1)    # 4 kcal/g carbs
                    fat = round(calories * random.uniform(0.20, 0.35) / 9, 1)      # 9 kcal/g fat
                    rows.append({
                        'MealID': meal_id,
                        'UserID': u['UserID'],
                        'MealDate': current,
                        'MealType': meal_type,
                        'CaloriesConsumed': calories,
                        'ProteinG': protein,
                        'CarbsG': carbs,
                        'FatG': fat,
                    })
                    meal_id += 1
            current += timedelta(days=1)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------
# 6. Weight / Daily Progress - a slow trend toward the user's
#    goal, plus daily noise (real body weight fluctuates day to
#    day even when the underlying trend is steady).
# ---------------------------------------------------------------
def generate_weight(users_df):
    rows = []
    progress_id = 1
    num_days = (END_DATE - START_DATE).days + 1

    for _, u in users_df.iterrows():
        start_w = u['StartingWeightKG']
        if u['GoalType'] == 'WeightLoss':
            total_change = -np.random.uniform(3, 10)   # kg lost over the year
        elif u['GoalType'] == 'MuscleGain':
            total_change = np.random.uniform(1, 6)      # kg gained over the year
        else:
            total_change = np.random.uniform(-1.5, 1.5) # roughly flat

        # not every user logs weight every day - depends on consistency
        current = START_DATE
        day_index = 0
        while current <= END_DATE:
            if random.random() < (0.2 + 0.6 * u['_consistency']):
                trend_progress = day_index / num_days
                trend_weight = start_w + total_change * trend_progress
                noise = np.random.normal(0, 0.4)  # daily water/food fluctuation
                weight_today = round(max(trend_weight + noise, 40), 1)
                rows.append({
                    'ProgressID': progress_id,
                    'UserID': u['UserID'],
                    'ProgressDate': current,
                    'WeightKG': weight_today,
                })
                progress_id += 1
            current += timedelta(days=1)
            day_index += 1
    return pd.DataFrame(rows)


# ---------------------------------------------------------------
# 7. Run generation and save CSVs
# ---------------------------------------------------------------
if __name__ == '__main__':
    print("Generating users...")
    users_df = generate_users(NUM_USERS)

    print("Generating workouts...")
    workouts_df = generate_workouts(users_df)

    print("Generating sleep...")
    sleep_df = generate_sleep(users_df)

    print("Generating diet...")
    diet_df = generate_diet(users_df)

    print("Generating weight/progress...")
    weight_df = generate_weight(users_df)

    # drop the internal-only trait column before export
    users_export = users_df.drop(columns=['_consistency'])

    output_dir = Path(__file__).parent.parent / "data" / "generated"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Saving CSVs to: {output_dir}")

    users_export.to_csv(output_dir / "users.csv", index=False)
    workouts_df.to_csv(output_dir / "workouts.csv", index=False)
    diet_df.to_csv(output_dir / "diet.csv", index=False)
    sleep_df.to_csv(output_dir / "sleep.csv", index=False)
    weight_df.to_csv(output_dir / "weight.csv", index=False)

    print("\nDone. Row counts:")
    print(f"  users.csv:     {len(users_export):,}")
    print(f"  workouts.csv:  {len(workouts_df):,}")
    print(f"  diet.csv:      {len(diet_df):,}")
    print(f"  sleep.csv:     {len(sleep_df):,}")
    print(f"  weight.csv:    {len(weight_df):,}")