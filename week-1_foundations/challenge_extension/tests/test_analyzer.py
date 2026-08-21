import pytest
from csvstat import analyze_csv


@pytest.fixture
def csv_result():
    result = analyze_csv("data/sample.csv")
    return result


def test_row_count(csv_result):
    assert csv_result["rows"] == 3


def test_column_count(csv_result):
    assert csv_result["columns"] == 3


def test_numeric_column_detection(csv_result):
    assert csv_result["column_details"]["Age"]["type"] == "numeric"


def test_text_column_detection(csv_result):
    assert csv_result["column_details"]["Name"]["type"] == "text"


def test_missing_values(csv_result):
    assert csv_result["column_details"]["Age"]["missing"] == 0


def test_numeric_statistics(csv_result):
    age_details = csv_result["column_details"]["Age"]

    assert age_details["min"] == 25
    assert age_details["max"] == 30


def test_numeric_mean(csv_result):
    age_details = csv_result["column_details"]["Age"]

    assert age_details["mean"] == 27.666666666666668


def test_text_top_values(csv_result):
    name_details = csv_result["column_details"]["Name"]

    assert "top_values" in name_details
    assert len(name_details["top_values"]) > 0


def test_column_details_exist(csv_result):
    assert "Name" in csv_result["column_details"]
    assert "Age" in csv_result["column_details"]
    assert "Country" in csv_result["column_details"]


def test_result_structure(csv_result):
    assert "rows" in csv_result
    assert "columns" in csv_result
    assert "column_details" in csv_result


def test_numeric_min_less_than_max(csv_result):
    age_details = csv_result["column_details"]["Age"]

    assert age_details["min"] < age_details["max"]


def test_numeric_values_are_correct_type(csv_result):
    age_details = csv_result["column_details"]["Age"]

    assert isinstance(age_details["min"], float)
    assert isinstance(age_details["max"], float)


def test_default_top_values_limit(csv_result):
    name_details = csv_result["column_details"]["Name"]

    assert len(name_details["top_values"]) <= 5


def test_rows_value_is_integer(csv_result):
    assert isinstance(csv_result["rows"], int)


def test_columns_value_is_integer(csv_result):
    assert isinstance(csv_result["columns"], int)


def test_column_details_is_dictionary(csv_result):
    assert isinstance(csv_result["column_details"], dict)


def test_age_details_contains_required_fields(csv_result):
    age_details = csv_result["column_details"]["Age"]

    assert "type" in age_details
    assert "missing" in age_details
    assert "min" in age_details
    assert "max" in age_details
    assert "mean" in age_details


def test_name_details_contains_required_fields(csv_result):
    name_details = csv_result["column_details"]["Name"]

    assert "type" in name_details
    assert "missing" in name_details
    assert "top_values" in name_details


def test_no_missing_values_in_name(csv_result):
    assert csv_result["column_details"]["Name"]["missing"] == 0


def test_numeric_mean_between_min_max(csv_result):
    age_details = csv_result["column_details"]["Age"]

    assert age_details["min"] <= age_details["mean"] <= age_details["max"]


def test_age_type_not_text(csv_result):
    assert csv_result["column_details"]["Age"]["type"] != "text"


def test_name_type_not_numeric(csv_result):
    assert csv_result["column_details"]["Name"]["type"] != "numeric"

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        analyze_csv("data/not_found.csv")


def test_empty_csv():
    with pytest.raises(ValueError):
        analyze_csv("data/empty.csv")


def test_csv_with_only_header():
    with pytest.raises(ValueError):
        analyze_csv("data/header_only.csv")


def test_csv_with_missing_values():
    result = analyze_csv("data/missing_values.csv")

    assert result["column_details"]["Age"]["missing"] > 0


def test_single_row_csv():
    result = analyze_csv("data/single_row.csv")

    assert result["rows"] == 1


def test_duplicate_values_counting():
    result = analyze_csv("data/duplicate_values.csv")

    assert "top_values" in result["column_details"]["Name"]


def test_numeric_column_with_invalid_values():
    result = analyze_csv("data/mixed_numeric.csv")

    assert result["column_details"]["Age"]["type"] in [
        "numeric",
        "text"
    ]


def test_empty_column_values():
    result = analyze_csv("data/empty_column.csv")

    assert result is not None


def test_result_is_not_none():
    result = analyze_csv("data/sample.csv")

    assert result is not None


def test_invalid_file_extension():
    with pytest.raises(Exception):
        analyze_csv("data/sample.txt")