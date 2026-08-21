# CSV Insights

## Overview

CSV Insights is a Python package for CSV profiling and data analysis.

This project is a packaged and unit-tested version of the Week-1 `csvstat` tool.  
It provides a reusable Python API and a command-line interface to analyze CSV files and generate useful statistical summaries.

---

## Features

- CSV file profiling
- Row and column count analysis
- Automatic column data type detection
  - Numeric columns
  - Text columns
- Missing value detection
- Numeric column statistics:
  - Minimum value
  - Maximum value
  - Mean value
- Text column analysis:
  - Top frequent values
  - Frequency count
- Command-line interface support

---

## Project Structure

```text
challenge_extension/
│
├── csvstat/
│   ├── __init__.py
│   ├── analyzer.py
│   └── cli.py
│
├── tests/
│   └── test_analyzer.py
│
├── data/
│   └── sample.csv
│
├── package.md
├── pyproject.toml
└── README.md
```

---

## Installation

### From PyPI

Install the published package using:

```bash
pip install csv-insights
```

### From Source

Clone the repository:

```bash
git clone <repository-url>
cd challenge_extension
```

Install the package locally:

```bash
pip install .
```

---

## Usage

### Python API

```python
from csvstat import analyze_csv

result = analyze_csv("data/sample.csv")

print(result)
```

### Command Line Interface

Analyze CSV files directly from the terminal:

```bash
csvstat data/sample.csv
```

---

## Example Output

```python
{
    'rows': 3,
    'columns': 3,
    'column_details': {
        'Name': {
            'type': 'text',
            'missing': 0,
            'top_values': [
                ('Ron', 1),
                ('John', 1),
                ('Alie', 1)
            ]
        },
        'Age': {
            'type': 'numeric',
            'missing': 0,
            'min': 25.0,
            'max': 30.0,
            'mean': 27.666666666666668
        },
        'Country': {
            'type': 'text',
            'missing': 0,
            'top_values': [
                ('Australia', 1),
                ('USA', 1),
                ('United Kingdom', 1)
            ]
        }
    }
}
```

---

## Testing

This project uses `pytest` for unit testing.

Run tests using:

```bash
pytest
```

The test suite covers:

- Valid CSV files
- Empty CSV files
- Missing files
- Missing values
- Numeric and text column detection
- Edge cases and invalid inputs

---

## Building Package

Install the build dependency:

```bash
pip install build
```

Build the package:

```bash
python -m build
```

The generated package files will be available in the `dist/` directory.

---

## Package Configuration

Package metadata and the PyPI description are maintained in:

```text
package.md
```

The `pyproject.toml` file references `package.md` as the package's long description.

---
