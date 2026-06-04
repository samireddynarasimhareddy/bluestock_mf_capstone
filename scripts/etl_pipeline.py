import pandas as pd
import sqlite3
from pathlib import Path

# Paths
RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")
DB_PATH = "data/db/bluestock.db"

# Create processed folder if not exists
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

# SQLite connection
conn = sqlite3.connect(DB_PATH)

# Read all CSV files
csv_files = list(RAW_PATH.glob("*.csv"))

for file in csv_files:
    print(f"Processing {file.name}")

    df = pd.read_csv(file)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("Unknown")

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Save cleaned CSV
    output_file = PROCESSED_PATH / file.name
    df.to_csv(output_file, index=False)

    # Save into SQLite
    table_name = file.stem
    df.to_sql(table_name, conn, if_exists="replace", index=False)

print("ETL Completed Successfully!")

conn.close()