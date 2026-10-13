from pathlib import Path

import pandas as pd

try:
    import pyodbc  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    pyodbc = None

SERVER = r"LAPTOP-G2GQ31I2\SQLEXPRESS"
DATABASE = "AI_Fitness_DB"

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)

CSV_FILES = {
    "Users": "data/generated/users.csv",
    "DailyProgress": "data/generated/weight.csv",
    "Sleep": "data/generated/sleep.csv",
    "Diet": "data/generated/diet.csv",
    "Workouts": "data/generated/workouts.csv",
}


def get_connection():
    if pyodbc is None:
        raise RuntimeError("pyodbc is not installed. The CSV fallback will be used instead.")
    return pyodbc.connect(connection_string)


def load_table(table_name):
    try:
        conn = get_connection()
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception:
        csv_path = Path(__file__).resolve().parents[1] / CSV_FILES.get(table_name, "")
        if csv_path.exists():
            return pd.read_csv(csv_path)
        raise