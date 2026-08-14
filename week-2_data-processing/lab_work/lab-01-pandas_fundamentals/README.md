# Week 2 – Data Processing & Exploratory Data Analysis

This repository documents my Week 2 learning journey focused on data processing, exploratory data analysis (EDA), and numerical computation using Python libraries.

## Labs Completed

## Lab 1: Pandas Fundamentals

### Tasks Completed:
- Loaded CSV data into a Pandas DataFrame and inspected the dataset using:
  - `head()`
  - `info()`
  - `describe()`
  - `shape`

- Selected rows and columns using:
  - `loc`
  - `iloc`

- Applied filtering using conditional statements.

- Created derived columns from existing features:
  - Created `alcohol_level` based on alcohol content.
  - Created `acidity_ratio` using fixed acidity and volatile acidity.

- Performed grouping and aggregation:
  - Grouped data using the `quality` column.
  - Calculated mean and count of alcohol values for each quality group.

- Merged DataFrames using a common key.

---

## Lab 2: NumPy and Vectorization

### Tasks Completed:
- Created and manipulated 2D NumPy arrays.

- Computed numerical statistics:
  - Row means
  - Column maximum values

- Normalized columns using vectorized NumPy operations to scale values between 0 and 1.

- Applied broadcasting operations to perform array transformations without loops.

- Compared vectorized operations with traditional Python loops and analyzed performance differences.

---

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn

## Key Learnings

- Data manipulation using Pandas DataFrames.
- Efficient numerical computation using NumPy arrays.
- Importance of vectorization for faster data processing.
- Grouping, aggregation, and transformation of tabular data.