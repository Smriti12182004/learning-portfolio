import csv
from collections import Counter


def analyze_csv(file_path, top=5):

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    columns = reader.fieldnames

    result = {
        "rows": len(rows),
        "columns": len(columns),
        "column_details": {}
    }

    for column in columns:
        values = [row[column] for row in rows]

        numeric_values = []

        for value in values:
            try:
                numeric_values.append(float(value))
            except ValueError:
                pass

        if len(numeric_values) == len(values):

            result["column_details"][column] = {
                "type": "numeric",
                "missing": values.count(""),
                "min": min(numeric_values),
                "max": max(numeric_values),
                "mean": sum(numeric_values) / len(numeric_values)
            }

        else:

            result["column_details"][column] = {
                "type": "text",
                "missing": values.count(""),
                "top_values": Counter(values).most_common(top)
            }

    return result