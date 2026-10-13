"""
====================================================================

Project    : AI Fitness Intelligence Platform

Module     : AI Coach

Author     : Harsh

Description:

Central AI Coach Interface.

Supports future integration with:

- OpenAI
- Gemini
- Claude
- Ollama
- Azure OpenAI

====================================================================
"""

from abc import ABC, abstractmethod


# ==========================================================
# Base AI Provider
# ==========================================================

class BaseAIProvider(ABC):

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate AI response.
        """
        pass


# ==========================================================
# Dummy Provider
# ==========================================================

class DummyAIProvider(BaseAIProvider):

    def generate_response(self, prompt: str) -> str:

        return (
            "AI Coach is configured successfully.\n\n"
            "No external AI provider is connected yet.\n\n"
            "Supported providers:\n"
            "- OpenAI\n"
            "- Gemini\n"
            "- Claude\n"
            "- Ollama\n"
        )


# ==========================================================
# AI Coach
# ==========================================================

class AICoach:

    def __init__(self, provider: BaseAIProvider):

        self.provider = provider

    def ask(self, prompt: str) -> str:

        return self.provider.generate_response(prompt)


# ==========================================================
# Example
# ==========================================================

if __name__ == "__main__":

    provider = DummyAIProvider()

    coach = AICoach(provider)

    answer = coach.ask(
        "Create a Push Pull Legs workout."
    )

    print(answer)