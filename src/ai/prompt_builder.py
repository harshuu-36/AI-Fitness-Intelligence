"""
====================================================================

Project    : AI Fitness Intelligence Platform

Module     : Prompt Builder

Author     : Harsh

Description:

Builds personalized prompts for the AI Fitness Coach.

====================================================================
"""

from src.ai.system_prompt import SYSTEM_PROMPT


def build_prompt(

    age: int,

    gender: str,

    height: float,

    weight: float,

    goal: str,

    activity_level: str,

    calories: float,

    protein: float,

    carbs: float,

    fats: float,

    water: float,

    bmi: float,

    bmi_category: str,

    health_score: int,

    user_question: str

) -> str:

    """
    Build a personalized AI prompt.
    """

    prompt = f"""

{SYSTEM_PROMPT}

==================================================

USER PROFILE

==================================================

Age : {age}

Gender : {gender}

Height : {height} cm

Weight : {weight} kg

Goal : {goal}

Activity Level : {activity_level}

BMI : {bmi}

BMI Category : {bmi_category}

Health Score : {health_score}/100

==================================================

DAILY NUTRITION

==================================================

Calories : {calories} kcal

Protein : {protein} g

Carbohydrates : {carbs} g

Fat : {fats} g

Water : {water} L

==================================================

USER QUESTION

==================================================

{user_question}

==================================================

Provide a professional answer.

"""

    return prompt


# ==========================================================
# Example
# ==========================================================

if __name__ == "__main__":

    prompt = build_prompt(

        age=24,

        gender="Male",

        height=175,

        weight=78,

        goal="Muscle Gain",

        activity_level="Active",

        calories=2800,

        protein=170,

        carbs=320,

        fats=70,

        water=3.5,

        bmi=24.2,

        bmi_category="Normal",

        health_score=91,

        user_question="Can you create a Push Pull Legs workout plan?"

    )

    print(prompt)