# Research Data Helper

A simple tool to read a CSV, compute basic stats, and save a summary.
# Research Data Helper

A simple Python tool to:
- Read a CSV file (e.g., lab or research data)
- Compute basic stats for a numeric column (count, mean, min, max)
- Save a short summary to a CSV in `outputs/`

## Project Structure
research-data-helper/
├── src/
│ └── research_data_helper/
│ └── main.py # main entry point
├── data/
│ └── example_measurements.csv
├── outputs/ # generated results (git-ignored)
├── .gitignore
└── README.md

markdown
Copy code

## Requirements
- Python 3 (already available in WSL/Ubuntu)
- No external packages required (uses Python standard library)

## Quick Start

Run with defaults (sample file and `value` column):
```bash
python3 src/research_data_helper/main.py
Specify a CSV, column, and output path:

bash
Copy code
python3 src/research_data_helper/main.py \
  --csv data/example_measurements.csv \
  --column value \
  --out outputs/summary.csv
Example Output (printed)
vbnet
Copy code
✅ CSV loaded: /path/to/data/example_measurements.csv

📊 Summary Statistics:
Count: 5
Mean: 13.6
Min: 10.0
Max: 17.0

💾 Summary saved to: /path/to/outputs/summary.csv
Example Output (saved to outputs/summary.csv)
matlab
Copy code
metric,value
count,5
mean,13.6
min,10.0
max,17.0
## License
Choose one if you plan to share publicly (MIT is a common, permissive choice).
