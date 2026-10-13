"""
==============================================================
AI Fitness Intelligence Platform

Input Validators

Author : Harsh
==============================================================
"""

from typing import Literal


def validate_weight(weight: float) -> None:
    """
    Validate body weight.
    """

    if weight <= 0:
        raise ValueError("Weight must be greater than 0 kg.")

    if weight > 350:
        raise ValueError("Weight seems unrealistic.")


def validate_height(height: float) -> None:
    """
    Validate height in centimeters.
    """

    if height <= 0:
        raise ValueError("Height must be greater than 0 cm.")

    if height > 300:
        raise ValueError("Height seems unrealistic.")


def validate_age(age: int) -> None:
    """
    Validate age.
    """

    if age <= 0:
        raise ValueError("Age must be greater than 0.")

    if age > 120:
        raise ValueError("Age seems unrealistic.")


def validate_gender(gender: str) -> None:
    """
    Validate gender.
    """

    valid = {"male", "female"}

    if gender.lower() not in valid:
        raise ValueError(
            f"Gender must be one of {valid}."
        )


def validate_activity(activity_level: str) -> None:
    """
    Validate activity level.
    """

    valid = {
        "sedentary",
        "light",
        "moderate",
        "active",
        "very_active"
    }

    if activity_level.lower() not in valid:
        raise ValueError(
            f"Activity level must be one of {valid}."
        )


def validate_goal(goal: str) -> None:
    """
    Validate fitness goal.
    """

    valid = {
        "Weight Loss",
        "Weight Gain",
        "Maintain"
    }

    if goal not in valid:
        raise ValueError(
            f"Goal must be one of {valid}."
        )


def validate_workout_minutes(minutes: int) -> None:
    """
    Validate workout duration.
    """

    if minutes < 0:
        raise ValueError(
            "Workout minutes cannot be negative."
        )

    if minutes > 600:
        raise ValueError(
            "Workout duration seems unrealistic."
        )


def validate_user_inputs(
    weight: float,
    height: float,
    age: int,
    gender: str,
    activity_level: str,
    goal: str,
    workout_minutes: int
) -> None:
    """
    Validate all user inputs.
    """

    validate_weight(weight)
    validate_height(height)
    validate_age(age)
    validate_gender(gender)
    validate_activity(activity_level)
    validate_goal(goal)
    validate_workout_minutes(workout_minutes)