"""
====================================================================

Project    : AI Fitness Intelligence Platform

Module     : OpenAI Provider

Author     : Harsh

Description:

OpenAI provider implementation.

====================================================================
"""

import os

from openai import OpenAI

from dotenv import load_dotenv

from src.ai.ai_coach import BaseAIProvider


# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()


# ==========================================================
# OpenAI Provider
# ==========================================================

class OpenAIProvider(BaseAIProvider):

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:

            raise ValueError(
                "OPENAI_API_KEY not found in environment variables."
            )

        self.client = OpenAI(
            api_key=api_key
        )

    def generate_response(
        self,
        prompt: str
    ) -> str:

        response = self.client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional AI Fitness Coach."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7

        )

        return response.choices[0].message.content