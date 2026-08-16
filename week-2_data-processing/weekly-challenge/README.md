# Week 2 Weekly Challenge — Exploratory Data Analysis

## Overview

This project applies the concepts learned during Week 2 to perform a complete **Exploratory Data Analysis (EDA)** on the **Wine Quality dataset**.

The analysis focuses on understanding the dataset, identifying data-quality issues, discovering relationships between variables, and communicating meaningful insights through statistical and visual analysis.

## Objectives

- Perform systematic data exploration and cleaning.
- Analyze distributions, outliers, and correlations.
- Create meaningful visualizations.
- Apply statistical hypothesis testing.
- Compare automated profiling with manual EDA.
- Identify potential target leakage.
- Build an interactive Plotly visualization.
- Create a reusable EDA profiling function.

## Dataset

**Wine Quality Dataset**

The dataset contains physicochemical properties of wine and a `quality` score.

## Analysis Performed

### Data Exploration & Cleaning
- Dataset shape and structure
- Data types
- Missing-value checks
- Duplicate detection
- Descriptive statistics
- Unique-value analysis
- IQR-based outlier analysis

### Exploratory Data Analysis
- Quality distribution
- Feature distributions
- Feature vs. quality relationships
- Correlation analysis
- Target-focused visual analysis

### Statistical Analysis
A Welch's independent-samples t-test was performed to compare alcohol content between lower-quality and higher-quality wine groups.

### Automated Profiling
`ydata-profiling` was used to generate an automated overview of the dataset and compare it with the manual EDA.

### Leakage Hunt
A hypothetical `quality_after_review` feature was used to demonstrate how target leakage can occur when a feature contains information unavailable at prediction time.

### Interactive Visualization
A Plotly scatter plot was created to explore **alcohol content vs. wine quality**, with hover information and filtering by quality category.

### Reusable EDA

A reusable `eda_report(df)` function was developed to profile any DataFrame.

## Key Learning Outcomes

- Understanding the complete EDA workflow
- Data cleaning and quality assessment
- Statistical reasoning and hypothesis testing
- Interpretation of p-values
- Identifying target leakage
- Automated vs. manual EDA
- Interactive data visualization
- Reusable Python workflows

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Plotly
- ydata-profiling
