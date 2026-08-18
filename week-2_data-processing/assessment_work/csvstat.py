import csv
from collections import Counter
import boto3
from datetime import datetime
import os


# AWS S3 Configuration
BUCKET_NAME = "csvstat-week2-smriti-2026"

INPUT_KEY = "input/example.csv"

LOCAL_FILE = "example.csv"


# Create S3 client
s3 = boto3.client("s3")


# Download CSV from S3 input folder
try:
    print("Downloading CSV from S3...")

    s3.download_file(
        BUCKET_NAME,
        INPUT_KEY,
        LOCAL_FILE
    )

    print("Download completed")

except Exception as e:
    print("Error downloading file:", e)
    exit()


# Read CSV file
try:

    with open(LOCAL_FILE, "r") as file:

        reader = csv.reader(file)
        data = list(reader)

except FileNotFoundError:

    print("Error: File not found")
    exit()



# Separate header and rows
headers = [
    header.strip()
    for header in data[0]
]

rows = data[1:]


# Store report output
report = []


# Row and column count
report.append(f"Rows: {len(rows)}")
report.append(f"Columns: {len(headers)}")


# Column names
report.append("\nColumns:")

for column in headers:
    report.append(column)



# Column profiling
report.append("\nColumn Details:")


for i, column in enumerate(headers):

    values = [
        row[i].strip()
        for row in rows
    ]


    missing = sum(
        1
        for value in values
        if value == ""
    )


    non_missing = [
        value
        for value in values
        if value != ""
    ]


    # Detect numeric data
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



    report.append("")
    report.append(f"Column: {column}")
    report.append(f"Type: {data_type}")
    report.append(f"Missing: {missing}")



    # Numeric statistics
    if data_type == "numeric":

        numeric_values = [
            float(value)
            for value in non_missing
        ]


        report.append(
            f"Min: {min(numeric_values)}"
        )

        report.append(
            f"Mean: {sum(numeric_values)/len(numeric_values)}"
        )

        report.append(
            f"Max: {max(numeric_values)}"
        )



    # Text statistics
    else:

        counts = Counter(non_missing)

        report.append("Top 5 values:")


        for value, count in counts.most_common(5):

            report.append(
                f"{value}: {count}"
            )



# Create output report file
timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)


output_file = f"csvstat_report_{timestamp}.txt"



with open(output_file, "w") as file:

    file.write(
        "\n".join(report)
    )



print("Report generated:", output_file)



# Upload report to S3 output folder
try:

    s3.upload_file(
        output_file,
        BUCKET_NAME,
        f"output/{output_file}"
    )


    print("Report uploaded to S3 successfully")


except Exception as e:

    print("Upload error:", e)



# Remove temporary CSV file
if os.path.exists(LOCAL_FILE):

    os.remove(LOCAL_FILE)



print("CSVStat execution completed")