"""
====================================================================

Project    : AI Fitness Intelligence Platform

Phase      : Common Utilities

Module     : Logger

Author     : Harsh

Description:

Centralized logging configuration for the entire project.

====================================================================
"""

import logging

from src.common.paths import LOGS

# ==========================================================
# Ensure Log Directory Exists
# ==========================================================

LOGS.mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================================
# Log File
# ==========================================================

LOG_FILE = LOGS / "project.log"

# ==========================================================
# Configure Logging
# ==========================================================

logging.basicConfig(

    level=logging.INFO,

    format=(
        "%(asctime)s | "
        "%(levelname)-8s | "
        "%(name)s | "
        "%(message)s"
    ),

    datefmt="%Y-%m-%d %H:%M:%S",

    handlers=[

        logging.FileHandler(

            LOG_FILE,

            mode="a",

            encoding="utf-8"

        ),

        logging.StreamHandler()

    ],

    force=True

)

# ==========================================================
# Project Logger
# ==========================================================

logger = logging.getLogger(

    "AI_Fitness_Intelligence_Platform"

)

logger.propagate = False


# ==========================================================
# Example Usage
# ==========================================================

if __name__ == "__main__":

    logger.info("Logger initialized successfully.")

    logger.warning("This is a warning message.")

    logger.error("This is an error message.")