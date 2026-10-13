"""
==============================================================

Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Custom Exceptions

Author     : Harsh

Description:

Contains all custom exceptions used throughout the project.

==============================================================
"""


class UserNotFoundException(Exception):
    """
    Raised when a user is not found.
    """

    def __init__(
        self,
        message: str = "User not found."
    ):
        self.message = message
        super().__init__(self.message)


class WorkoutNotFoundException(Exception):
    """
    Raised when workout data is not found.
    """

    def __init__(
        self,
        message: str = "Workout data not found."
    ):
        self.message = message
        super().__init__(self.message)


class MealNotFoundException(Exception):
    """
    Raised when meal data is not found.
    """

    def __init__(
        self,
        message: str = "Meal data not found."
    ):
        self.message = message
        super().__init__(self.message)


class SleepNotFoundException(Exception):
    """
    Raised when sleep data is not found.
    """

    def __init__(
        self,
        message: str = "Sleep data not found."
    ):
        self.message = message
        super().__init__(self.message)


class ProgressNotFoundException(Exception):
    """
    Raised when progress data is not found.
    """

    def __init__(
        self,
        message: str = "Progress data not found."
    ):
        self.message = message
        super().__init__(self.message)


class HealthDataNotFoundException(Exception):
    """
    Raised when health dashboard data is not found.
    """

    def __init__(
        self,
        message: str = "Health data not found."
    ):
        self.message = message
        super().__init__(self.message)


class DatabaseException(Exception):
    """
    Raised for database related errors.
    """

    def __init__(
        self,
        message: str = "Database operation failed."
    ):
        self.message = message
        super().__init__(self.message)


class ValidationException(Exception):
    """
    Raised when validation fails.
    """

    def __init__(
        self,
        message: str = "Validation failed."
    ):
        self.message = message
        super().__init__(self.message)