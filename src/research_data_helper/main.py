import csv

import csv
import statistics
import os
from pathlib import Path

def read_csv(file_path):
    """Reads a CSV file and returns a list of rows as dictionaries."""
    with open(file_path, mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def calculate_stats(data, column_name):
    """Calculates count, mean, min, and max for a numeric column."""
    values = [float(row[column_name]) for row in data]
    stats = {
        "count": len(values),
        "mean": statistics.mean(values),
        "min": min(values),
        "max": max(values),
    }
    return stats

def save_summary(summary_dict, output_path):
    """
    Saves a one-row CSV with columns: metric,value.
    Ensures the output folder exists.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "value"])
        for k, v in summary_dict.items():
            writer.writerow([k, v])

if __name__ == "__main__":
    # Resolve project root based on this file's location:
    # main.py -> .../src/research_data_helper/main.py
    # project root is three levels up from this file
    project_root = Path(__file__).resolve().parents[2]

    input_csv = project_root / "data" / "example_measurements.csv"
    rows = read_csv(input_csv)
    print("✅ CSV data loaded successfully!")

    column = "value"
    summary = calculate_stats(rows, column)
    print("\n📊 Summary Statistics:")
    for k, v in summary.items():
        print(f"{k.capitalize()}: {v}")

    output_csv = project_root / "outputs" / "summary.csv"
    save_summary(summary, output_csv)
    print(f"\n💾 Summary saved to: {output_csv}")
