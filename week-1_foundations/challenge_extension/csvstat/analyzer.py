import csv
from collections import Counter


def analyze_csv(file_path, top=5):

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    if not data:
        raise ValueError("CSV file is empty")

    headers = [header.strip() for header in data[0]]
    rows = data[1:]

    result = {
        "rows": len(rows),
        "columns": len(headers),
        "column_details": {}
    }

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

        numeric_values = []

        for value in non_missing:
            try:
                numeric_values.append(float(value))
            except ValueError:
                pass

        if len(numeric_values) == len(non_missing) and non_missing:

            result["column_details"][column] = {
                "type": "numeric",
                "missing": missing,
                "min": min(numeric_values),
                "max": max(numeric_values),
                "mean": sum(numeric_values) / len(numeric_values)
            }

        else:

            result["column_details"][column] = {
                "type": "text",
                "missing": missing,
                "top_values": Counter(non_missing).most_common(top)
            }

    return result