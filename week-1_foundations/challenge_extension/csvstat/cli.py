import argparse
from .analyzer import analyze_csv


def main():
    parser = argparse.ArgumentParser(
        description="CSV profiling tool"
    )

    parser.add_argument(
        "file",
        help="Path to CSV file"
    )

    args = parser.parse_args()

    result = analyze_csv(args.file)

    print(result)


if __name__ == "__main__":
    main()