import os
from dotenv import load_dotenv

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to .env file
ENV_PATH = os.path.join(BASE_DIR, ".env")

# Load .env
load_dotenv(dotenv_path=ENV_PATH)

# Database Configuration
DB_SERVER = os.getenv("DB_SERVER")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_AUTH = os.getenv("DB_AUTH")

# Debug (temporary)
print("DB_SERVER :", DB_SERVER)
print("DB_DATABASE :", DB_DATABASE)
print("DB_AUTH :", DB_AUTH)