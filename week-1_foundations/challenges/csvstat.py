import argparse
import csv
from collections import Counter


# Create command line parser
parser = argparse.ArgumentParser(
    description="CSV profiling tool"
)

# CSV file path argument
parser.add_argument(
    "file",
    help="Path to CSV file"
)

# Top N values argument
parser.add_argument(
    "--top",
    type=int,
    default=5,
    help="Show top N values"
)

args = parser.parse_args()


# Read CSV file
try:
    with open(args.file, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

except FileNotFoundError:
    print("Error: File not found")
    exit()


# Separate header and rows
# Separate header and rows
if not data:
    print("Error: CSV file is empty")
    exit()

if len(data) < 2:
    print("Error: CSV file must contain a header and at least one row")
    exit()

headers = [header.strip() for header in data[0]]
rows = data[1:]

# Row and column count
print("Rows:", len(rows))
print("Columns:", len(headers))


# Column names
print("\nColumns:")
for column in headers:
    print(column)


# Column profiling
print("\nColumn Details:")

for i, column in enumerate(headers):

    values = [
        row[i].strip()
        for row in rows
    ]

    missing = sum(
        1 for value in values
        if value == ""
    )


    non_missing = [
        value for value in values
        if value != ""
    ]


    # Detect numeric
    is_numeric = True

    for value in non_missing:
        try:
            float(value)
        except ValueError:
            is_numeric = False
            break


    if is_numeric and non_missing:

        data_type = "numeric"

    else:

        data_type = "text"


    print("\nColumn:", column)
    print("Type:", data_type)
    print("Missing:", missing)


    # Numeric statistics
    if data_type == "numeric":

        numeric_values = [
            float(value)
            for value in non_missing
        ]

        print("Min:", min(numeric_values))
        print("Mean:", sum(numeric_values)/len(numeric_values))
        print("Max:", max(numeric_values))


    # Text statistics
    elif data_type == "text":

        counts = Counter(non_missing)

        print(f"Top {args.top} values:")

        for value, count in counts.most_common(args.top):
            print(value, ":", count)