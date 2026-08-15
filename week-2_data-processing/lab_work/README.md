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

---

## Lab 3: Data Cleaning

### Tasks Completed:
- Performed missing value analysis:
  - Calculated missing value count for each column.
  - Calculated missing value percentage.
  - Created a missingness summary table.

- Applied missing value handling strategy:
  - Identified columns requiring treatment.
  - Verified that no missing-value imputation was required.

- Performed data type validation:
  - Checked existing data types of all columns.
  - Verified that features were stored in appropriate formats.
  - Confirmed no datatype conversion was required.

- Detected and handled duplicate records:
  - Identified duplicate rows.
  - Removed duplicate observations.
  - Verified that no duplicate records remained.

- Performed outlier analysis:
  - Detected potential outliers using the IQR method.
  - Visualized feature distributions using boxplots.
  - Evaluated outlier treatment strategy and retained valid observations.

- Validated the cleaned dataset:
  - Checked missing values after cleaning.
  - Verified duplicate removal.
  - Confirmed dataset consistency.

  ---

  ---

## Lab 4: Statistics Intuition

### Tasks Completed:
- Performed descriptive statistical analysis:
  - Calculated mean, median, and standard deviation.
  - Calculated the 25th, 50th, and 75th percentiles.
  - Compared mean and median to understand central tendency.

- Analyzed distribution characteristics:
  - Visualized the alcohol distribution using a histogram.
  - Calculated skewness to measure distribution asymmetry.
  - Identified potential outliers using the IQR method.
  - Visualized potential outliers using a boxplot.

- Performed correlation analysis:
  - Created a correlation matrix for numerical variables.
  - Identified the strongest correlation pair.
  - Interpreted the direction and strength of the relationship.
  - Understood why correlation does not imply causation.

- Performed hypothesis testing:
  - Divided wines into low-quality and high-quality groups.
  - Formulated null and alternative hypotheses.
  - Compared mean alcohol content between the two groups.
  - Performed an independent samples t-test.
  - Interpreted the p-value and statistical significance.
  - Understood the limitations of p-value interpretation.

---

## Lab 5: Visualization and Mini-EDA

### Tasks Completed:
- Created distribution visualizations:
  - Created a labeled histogram for alcohol content.
  - Created a boxplot to visualize spread and potential outliers.

- Created relationship visualizations:
  - Created a scatter plot between alcohol content and wine quality.
  - Added a caption explaining the relationship shown.

- Performed correlation visualization:
  - Created a correlation matrix for numerical variables.
  - Visualized correlations using a Seaborn heatmap.

- Performed mini-EDA:
  - Reviewed dataset shape and structure.
  - Generated summary statistics for numerical variables.
  - Checked for missing values and duplicate records.
  - Summarized key patterns and characteristics of the dataset.

---