# CSV Insights

A lightweight Python package for **CSV profiling and data analysis**.  
`csvstat` helps users quickly understand the structure and content of CSV files by generating useful statistics, detecting data types, and identifying missing values.

## Features

- 📊 **CSV File Profiling**
  - Analyze CSV files and generate a structured summary
  - Get total number of rows and columns

- 🔍 **Column Analysis**
  - Automatically detect column data types:
    - Numeric columns
    - Text columns
  - Identify missing values in each column

- 📈 **Numeric Statistics**
  - Calculate statistical summaries for numeric columns:
    - Minimum value
    - Maximum value
    - Mean value

- 🔤 **Text Analysis**
  - Find the most frequent values in text columns
  - Generate top occurring values with their frequency

- 💻 **Command Line Interface**
  - Analyze CSV files directly from the terminal using the `csvstat` command


## Installation

Install **CSV Insights** from PyPI:

```bash
pip install csv-insights
```

## Usage

### Python API

```python
from csvstat import analyze_csv

result = analyze_csv("sample.csv")

print(result)
```

### Command Line Interface

Analyze CSV files directly from the terminal:

```bash
csvstat sample.csv
```

## Output

CSV Insights provides:

- Total number of rows and columns
- Column data type detection
- Missing value information
- Numeric statistics:
  - Minimum value
  - Maximum value
  - Mean value
- Most frequent text values


## Testing

Run tests using pytest:

```bash
pytest
```

## Author

Smriti 