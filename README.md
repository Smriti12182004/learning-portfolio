# Learning Portfolio

This repository documents my internship learning journey at **VCreaTek**, including assessments, lab exercises, and projects completed throughout the internship. Each week contains tasks designed to strengthen Python programming, SQL, Linux command-line skills, Bash scripting, software development practices, and version control using Git and GitHub.

---

# Week 1 Foundations

## Assessment Work

### Assessment 0 – Python Version Comparison

**Status:** Completed

#### Objective

- Install and configure Python 3.8 and Python 3.12 on Ubuntu.
- Compare Python language features across versions.
- Demonstrate version compatibility using the `match-case` statement.

#### Completed Tasks

- Installed Python 3.8.
- Installed Python 3.12.
- Verified both Python versions.
- Developed a comparison program.
- Executed the program using Python 3.8.
- Executed the program using Python 3.12.
- Documented outputs with screenshots.

---

# Lab Work

## Lab 1 – Project and Environment Setup

**Status:** Completed

### Objective

- Create a clean and reproducible Python project.
- Configure a virtual environment.
- Organize project files following standard Python practices.

### Completed Tasks

- Created the project structure.
- Created and activated a virtual environment.
- Implemented `hello.py`.
- Generated `requirements.txt`.
- Configured `.gitignore`.
- Added project documentation.
- Captured execution screenshots.

---

## Lab 2 – Python Fluency Drills

**Status:** Completed

### Objective

Improve Python programming fluency by implementing reusable functions and practicing file handling and exception handling.

### Completed Tasks

- Implemented manual word counting.
- Implemented word counting using `collections.Counter`.
- Compared outputs of both methods.
- Flattened nested lists using loops.
- Flattened nested lists using list comprehension.
- Calculated the mean of numbers stored in a text file.
- Implemented exception handling for invalid and missing files.
- Documented outputs with screenshots.

---

## Lab 3 – GitHub and Git Workflow

**Status:** Completed

### Objective

- Learn collaborative development using Git and GitHub workflows.
- Practice working with feature branches, commits, pull requests, and code reviews.

### Completed Tasks

- Created and worked on a feature branch.
- Made multiple meaningful commits following conventional commit messages.
- Created and updated a Pull Request.
- Requested a code review.
- Resolved merge conflicts.
- Performed branch management and synchronization.
- Documented the complete workflow with screenshots.

---

## Lab 4 – Command Line and Bash

**Status:** Completed

### Objective

- Learn Linux command-line tools and Bash scripting.
- Process text files using Unix command pipelines.
- Automate word frequency analysis using a parameterized shell script.

### Completed Tasks

- Downloaded public text files using `curl`.
- Counted lines, words, and characters using `wc`.
- Built command pipelines using `tr`, `sort`, `uniq`, and `head`.
- Developed a reusable Bash script (`top_words.sh`).
- Accepted a filename and optional count as command-line arguments.
- Made the script executable using `chmod +x`.
- Executed the script on two different text files.
- Documented the workflow with screenshots.

---

## Lab 5 – SQL Fundamentals

**Status:** Completed

### Objective

- Practice fundamental SQL concepts using the Chinook SQLite sample database.
- Retrieve, filter, sort, aggregate, group, and join relational data.
- Perform date-based analysis using SQLite.

### Completed Tasks

- Set up and explored the Chinook SQLite database.
- Verified database tables using SQLite commands.
- Retrieved customers from a specific country.
- Identified the 10 most expensive tracks.
- Calculated total revenue by country using table joins.
- Identified the 10 best-selling tracks by quantity sold.
- Calculated monthly revenue for 2021.
- Saved each SQL query in a separate `.sql` file.
- Documented query results with screenshots.

### SQL Concepts Practiced

- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`
- `SUM()`
- `GROUP BY`
- `INNER JOIN`
- `strftime()`
- Date filtering
- Aggregate functions

---

# Weekly Challenge – CSV Profiling Tool & SQL Analysis

**Status:** Completed

## Objective

- Build a command-line CSV profiling tool using Python.
- Analyze CSV datasets to understand structure, data types, and data quality.
- Perform SQL-based analysis using the Chinook database to extract meaningful insights.

---

## Completed Tasks

### Part A – CSV Profiling Tool (`csvstat`)

- Developed a command-line CSV profiling tool using Python.
- Accepted CSV file paths as command-line input.
- Analyzed CSV files to extract:
  - Number of rows and columns.
  - Column names.
  - Data types.
  - Missing value statistics.
  - Numeric column statistics.
  - Top value frequency analysis.
- Generated profiling outputs and documented results with screenshots.

### Part B – SQL Analysis

- Performed SQL analysis using the Chinook SQLite database.
- Wrote SQL queries to answer analytical questions.
- Extracted insights using filtering, aggregation, grouping, and sorting.

### SQL Queries Implemented

- Top customers analysis.
- Revenue analysis by country.
- Best-selling tracks analysis.
- Monthly revenue analysis.

---

# Week 2 – Data Processing & Exploratory Data Analysis

**Status:** Completed

## Overview

Week 2 focused on understanding data processing workflows, exploratory data analysis (EDA), statistical analysis, data cleaning, and visualization techniques using Python.

The work involved analyzing real-world datasets, performing data quality checks, applying statistical methods, cleaning datasets, and creating meaningful visualizations.

## Topics Covered

- Exploratory Data Analysis (EDA)
- NumPy fundamentals
- Pandas data manipulation
- Data cleaning and preprocessing
- Statistical analysis
- Normal Distribution
- Outlier detection using IQR
- Kernel Density Estimation (KDE)
- Contour Plot visualization

## Dataset Used

**Wine Quality Dataset (`WineQT.csv`)**

The dataset was analyzed to understand physicochemical properties of wine samples, identify data quality issues, and explore relationships between features and quality ratings.

## Tools & Libraries Used

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- Git
- GitHub


# Lab Work

## Lab 1 – Pandas Fundamentals

**Status:** Completed

### Objective

- Learn data manipulation and analysis using Pandas DataFrames.
- Perform data inspection, filtering, transformation, and aggregation operations.

### Completed Tasks

- Loaded the Wine Quality dataset into a Pandas DataFrame.

- Inspected dataset structure using:
  - `head()`
  - `info()`
  - `describe()`
  - `shape`

- Selected rows and columns using:
  - `loc`
  - `iloc`

- Applied conditional filtering on dataset features.

- Created derived features:
  - Generated `alcohol_level` based on alcohol content.
  - Created `acidity_ratio` using acidity-related features.

- Performed grouping and aggregation:
  - Grouped data based on wine quality.
  - Calculated mean and count values for alcohol content.

---

## Lab 2 – NumPy and Vectorization

**Status:** Completed

### Objective

- Understand numerical computation using NumPy arrays.
- Apply vectorized operations for efficient data processing.

### Completed Tasks

- Created and manipulated NumPy arrays.

- Performed array operations including:
  - Indexing
  - Slicing
  - Mathematical transformations

- Calculated numerical statistics:
  - Row-wise mean.
  - Column-wise maximum values.

- Applied normalization using vectorized NumPy operations.

- Implemented broadcasting operations for array transformations.

- Compared execution time between:
  - Traditional Python loops.
  - NumPy vectorized operations.

---

## Lab 3 – Data Cleaning

**Status:** Completed

### Objective

- Perform data cleaning and preprocessing to improve dataset quality.
- Identify and handle common data quality issues before analysis.

### Completed Tasks

- Loaded and inspected the Wine Quality dataset.

- Performed missing value analysis:
  - Calculated missing value count.
  - Calculated missing value percentage.
  - Created missingness summary.

- Applied missing value handling strategies:
  - Identified columns requiring treatment.
  - Verified missing-value consistency.

- Performed data type validation:
  - Checked column data types.
  - Confirmed appropriate data representation.

- Detected and handled duplicate records:
  - Identified duplicate rows.
  - Removed duplicate observations.
  - Verified duplicate removal.

- Performed outlier analysis:
  - Detected potential outliers using the IQR method.
  - Visualized distributions using boxplots.
  - Evaluated outlier treatment decisions.

- Validated the cleaned dataset for further analysis.

---

# Practice Work

**Status:** Completed

### Completed Tasks

- Studied statistical concepts used in exploratory data analysis.

- Implemented:
  - Normal distribution analysis.
  - IQR-based outlier detection.
  - Kernel Density Estimation (KDE).

- Created contour plots for visualization.

- Documented learning notes and observations.

---

# Deliverables

Completed:

- Pandas fundamentals notebook.
- NumPy and vectorization notebook.
- Data cleaning notebook.
- Normal distribution analysis.
- IQR outlier analysis.
- KDE visualization.
- Contour plot analysis.
- Learning notes documenting additional insights.

Detailed documentation is available inside Week 2 directories.


---

# Technologies Used

- Ubuntu Linux
- Python 3.8
- Python 3.12
- Python Libraries:
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  - SciPy
- Jupyter Notebook
- SQL
- SQLite 3
- Bash
- Visual Studio Code
- Git
- GitHub
- Markdown

---

# Resources Used

- Python Official Documentation
- NumPy Documentation
- Pandas Documentation
- Matplotlib Documentation
- Seaborn Documentation
- SciPy Documentation
- SQLite Documentation
- SQLBolt
- Ubuntu Documentation
- Git Documentation
- GitHub Documentation
- Visual Studio Code Documentation
- Kaggle Dataset Resources

---

# Learning Outcomes

Through these assessments, labs, and data analysis tasks, I gained practical experience in:

- Setting up Python development environments on Ubuntu.
- Working with Python virtual environments and project structures.
- Writing reusable Python programs and handling exceptions.
- Using Linux command-line tools and Bash scripting.
- Working with relational databases using SQL and SQLite.
- Performing filtering, sorting, grouping, and aggregation operations.
- Working with Git branches, commits, and version control workflows.
- Organizing and documenting projects using GitHub and Markdown.
- Loading and exploring real-world datasets using Pandas.
- Performing exploratory data analysis (EDA).
- Manipulating numerical data using NumPy arrays.
- Applying vectorization techniques for efficient computation.
- Cleaning and validating datasets.
- Handling missing values, duplicate records, and data quality issues.
- Detecting outliers using statistical techniques such as IQR.
- Understanding statistical distributions and data behavior.
- Applying density estimation techniques using KDE.
- Creating visualizations to identify patterns and relationships.
- Combining Python programming, statistical analysis, and visualization for practical data workflows.

---

# Conclusion

The completed assessments, labs, challenges, and data processing activities provided practical experience across Python programming, Linux tools, Bash scripting, SQL fundamentals, Git/GitHub workflows, and exploratory data analysis.

The portfolio demonstrates the ability to build structured projects, analyze real-world datasets, apply data preprocessing techniques, perform statistical analysis, create meaningful visualizations, and maintain professional technical documentation.

Through this learning journey, I developed a strong foundation in programming, data processing, exploratory data analysis, and software development practices.
