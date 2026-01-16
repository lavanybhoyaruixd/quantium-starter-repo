import pandas as pd
from pathlib import Path

# Path to data folder
DATA_DIR = Path("data")

# Read all CSV files in data folder
csv_files = DATA_DIR.glob("*.csv")

processed_data = []

for file in csv_files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns to match output requirement
    df.columns = ["Sales", "Date", "Region"]

    processed_data.append(df)

# Combine all files into one DataFrame
final_df = pd.concat(processed_data, ignore_index=True)

# Save output file
final_df.to_csv("processed_sales.csv", index=False)

print("✅ Data processing complete. Output saved as processed_sales.csv")
