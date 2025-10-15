import csv

import csv
import statistics

def read_csv(file_path):
    """Reads a CSV file and returns a list of rows as dictionaries."""
    with open(file_path, mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def calculate_stats(data, column_name):
    """Calculates count, mean, min, and max for a numeric column."""
    # Convert text values into numbers
    values = [float(row[column_name]) for row in data]
    
    stats = {
        "count": len(values),
        "mean": statistics.mean(values),
        "min": min(values),
        "max": max(values)
    }
    return stats

if __name__ == "__main__":
    file_path = "data/example_measurements.csv"
    rows = read_csv(file_path)
    
    # Print confirmation
    print("✅ CSV data loaded successfully!\n")
    
    # Calculate and print stats
    summary = calculate_stats(rows, "value")
    print("📊 Summary Statistics:")
    for key, val in summary.items():
        print(f"{key.capitalize()}: {val}")

