# Week 2 Weekly Challenge Summary

## Overview

This weekly challenge applied the concepts learned during Week 2 to perform a complete Exploratory Data Analysis (EDA) on the **Wine Quality dataset**.

The analysis covered data inspection, cleaning, statistical analysis, visualization, automated profiling, and advanced EDA techniques.

## Dataset

**Dataset:** Wine Quality Dataset

The dataset contains physicochemical properties of wine along with a `quality` score.

## Work Completed

### 1. Data Exploration
- Loaded the dataset using Pandas.
- Examined dataset shape, columns, data types, and basic statistics.
- Checked for missing values and duplicate records.
- Examined unique values and distributions.

### 2. Data Cleaning & EDA
- Checked data quality and duplicate records.
- Identified potential outliers using the IQR method.
- Analyzed distributions of numerical variables.
- Studied relationships between wine quality and important features.
- Used correlation analysis to identify relationships between variables.

### 3. Visualization
Created visualizations using Matplotlib and Seaborn, including:
- Quality distribution
- Boxplots
- Strip plots
- Correlation heatmap
- Feature-quality relationships

### 4. Automated Profiling
Used `ydata-profiling` to generate an automated EDA report and compared its findings with the manual EDA.

Automated profiling provided a broad overview of distributions, correlations, duplicates, and data-quality checks, while manual EDA allowed more focused analysis and interpretation.

### 5. Statistical Analysis
Performed a Welch's independent-samples t-test to compare alcohol content between lower-quality and higher-quality wine groups.

The resulting p-value was extremely small, providing statistically significant evidence of a difference in mean alcohol content between the two groups.

### 6. Leakage Hunt
Identified a hypothetical target-leakage feature, `quality_after_review`, which would directly reveal the target `quality` if created after evaluation.

This demonstrated why model features must only contain information available at prediction time.

### 7. Interactive Visualization
Created an interactive Plotly visualization of alcohol content versus wine quality.

The chart supports:
- Hover information
- Filtering by wine-quality category

### 8. Reusable EDA Function
Created a reusable:

```python
eda_report(df)

Tools & Libraries
Python
Pandas
NumPy
Matplotlib
Seaborn
SciPy
Plotly
ydata-profiling