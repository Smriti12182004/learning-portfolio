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

# Lab 4 – Statistics Intuition

**Status:** Completed

### Objective

- Understand descriptive statistics and data behavior.
- Analyze relationships between variables.
- Apply hypothesis testing and interpret statistical results.

### Completed Tasks

- Calculated mean, median, standard deviation, and percentiles.
- Compared mean and median to understand central tendency.
- Analyzed distribution and skewness.
- Identified potential outliers.
- Created and interpreted a correlation matrix.
- Identified the strongest correlation pair.
- Explained why correlation does not imply causation.
- Formulated hypotheses for two quality groups.
- Performed an independent samples t-test.
- Interpreted the p-value and statistical significance.
- Explained what a p-value does and does not tell us.
- Stated the final conclusion from the hypothesis test.

### Commands & Functions Used

```python
df.mean()
df.median()
df.std()
df.quantile()
df.skew()
df.corr()
```
---
---

# Lab 5 – Visualization and Mini-EDA

**Status:** Completed

### Objective

- Apply visualization techniques to understand data distributions and relationships.
- Perform a basic end-to-end exploratory data analysis workflow.

### Completed Tasks

- Created a labeled histogram.
- Created a boxplot to analyze spread and potential outliers.
- Created a scatter plot to analyze relationships between variables.
- Added a caption explaining the scatter plot.
- Created a correlation matrix.
- Created a Seaborn correlation heatmap.
- Performed a quick end-to-end mini-EDA.
- Reviewed dataset structure and summary statistics.
- Checked missing values and duplicate records.
- Documented key observations from the analysis.

### Commands & Functions Used

```python
sns.histplot()
sns.boxplot()
sns.scatterplot()

df.corr()

sns.heatmap()

df.head()
df.info()
df.describe()

df.isnull().sum()
df.duplicated().sum()
```

---

# Practice Work

**Status:** Completed

### Objective

- Strengthen understanding of statistical concepts through additional practice.
- Apply statistical techniques to analyze distributions, outliers, and data density.
- Explore different visualization methods for better interpretation of data.

### Completed Tasks

- Generated and analyzed normal distributions.
- Calculated and interpreted mean and standard deviation.
- Applied z-score standardization.
- Detected outliers using the Interquartile Range (IQR) method.
- Visualized outliers using boxplots.
- Applied Kernel Density Estimation (KDE) to understand data distributions.
- Studied the effect of bandwidth on KDE curves.
- Created contour plots to visualize two-dimensional data density.
- Compared different visualization techniques to identify patterns.
- Documented observations and learning notes.

### Concepts Practiced

- Normal distribution
- Mean and standard deviation
- Z-score
- Quartiles and IQR
- Outlier detection
- Kernel Density Estimation (KDE)
- Bandwidth
- Contour plots
- Data distribution
- Statistical visualization

---
## Repository Structure 

```
week-2_data-processing/
│
├── README.md
├── learning_notes.md
├── requirement.txt
├── .gitignore
│
├── data/
│   └── WineQT.csv
│
├── lab_work/
│   ├── README.md
│   │
│   ├── lab-1-pandas/
│   │   └── pandas_fundamentals.ipynb
│   │
│   ├── lab-2-numpy/
│   │   └── numpy_vectorization.ipynb
│   │
│   ├── lab-3-data-cleaning/
│   │   ├── data/
│   │   │   └── WineQT.csv
│   │   └── data-cleaning.ipynb
│   │
│   ├── lab-4-statistics-intuition/
│   │   ├── data/
│   │   │   └── WineQT.csv
│   │   └── statistics-intuition.ipynb
│   │
│   └── lab-05-visualizaton-and-mini-eda/
│       ├── data/
│       │   └── WineQT.csv
│       └── visualization-and-mini-eda.ipynb
│
└── practice/
    ├── data/
    │
    ├── notebooks/
    │   ├── 01_eda.ipynb
    │   ├── 02_pandas_numpy.ipynb
    │   ├── 03_normal_distribution.ipynb
    │   ├── 04_IQR.ipynb
    │   ├── 05_KDE.ipynb
    │   └── 06_Contour_Plot.ipynb
    │
    ├── learning_notes.md
    └── README.md

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
```
---
---

# Week 1 – Foundations

### Labs

- [Lab 1 – Project and Environment Setup](./week-1_foundations/lab_work/lab-01-project-and-environment-setup/)
- [Lab 2 – Python Fluency Drills](./week-1_foundations/lab_work/lab-02-python-fluency-drills/)
- [Lab 4 – Command Line and Bash](./week-1_foundations/lab_work/lab-04-command-line-and-bash/)
- [Lab 5 – SQL Fundamentals](./week-1_foundations/lab_work/lab-05-sql-fundamentals/)

### Assessment Work

- [Assessment 0 – Python Version Comparison](./week-1_foundations/assessment_work/assessment-0-python-version-comparison/)

### Challenges

- [Week 1 Challenges](./week-1_foundations/challenges/)

---

# Week 2 – Data Processing & Exploratory Data Analysis

### Labs

- [Lab 1 – Pandas Fundamentals](./week-2_data-processing/lab_work/lab-01-pandas_fundamentals/pandas-fundamentals.ipynb)
- [Lab 2 – NumPy and Vectorization](./week-2_data-processing/lab_work/lab-02-numpy-and-vectorization/numpy-vectorization.ipynb)
- [Lab 3 – Data Cleaning](./week-2_data-processing/lab_work/lab-3-data-cleaning/data-cleaning.ipynb)
- [Lab 4 – Statistics Intuition](./week-2_data-processing/lab_work/lab-4-statistics-intuition/statistics-intuition.ipynb)
- [Lab 5 – Visualization and Mini-EDA](./week-2_data-processing/lab_work/lab-05-visualizaton-and-mini-eda/visualization-and-mini-eda.ipynb)

### Practice Notebooks

- [Practice 1 – EDA](./week-2_data-processing/practice/notebooks/01_eda.ipynb)
- [Practice 2 – Pandas & NumPy](./week-2_data-processing/practice/notebooks/02_pandas_numpy.ipynb)
- [Practice 3 – Normal Distribution](./week-2_data-processing/practice/notebooks/03_normal_distribution.ipynb)
- [Practice 4 – IQR](./week-2_data-processing/practice/notebooks/04_IQR.ipynb)
- [Practice 5 – KDE](./week-2_data-processing/practice/notebooks/05_KDE.ipynb)
- [Practice 6 – Contour Plot](./week-2_data-processing/practice/notebooks/06_Contour_Plot.ipynb)

### Documentation

- [Week 2 README](./week-2_data-processing/README.md)
- [Week 2 Learning Notes](./week-2_data-processing/learning_notes.md)

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

Through the Week 2 labs, practice work, and data analysis tasks, I gained practical experience in:

- Setting up and working with Python environments on Ubuntu.
- Using Jupyter Notebook for interactive data analysis.
- Loading and inspecting real-world datasets using Pandas.
- Selecting, filtering, grouping, and aggregating data.
- Creating derived features from existing data.
- Performing numerical computation using NumPy arrays.
- Applying vectorization and broadcasting for efficient computation.
- Comparing vectorized operations with traditional Python loops.
- Cleaning and validating datasets.
- Analyzing missing values and duplicate records.
- Detecting and evaluating potential outliers using the IQR method.
- Understanding mean, median, standard deviation, percentiles, and skewness.
- Analyzing relationships between variables using correlation.
- Performing hypothesis testing using an independent samples t-test.
- Interpreting p-values and statistical significance.
- Understanding normal distributions and z-scores.
- Applying Kernel Density Estimation (KDE).
- Creating histograms, boxplots, scatter plots, heatmaps, and contour plots.
- Performing a basic end-to-end exploratory data analysis workflow.
- Understanding the importance of selecting appropriate statistical methods and visualizations.
- Interpreting analytical results rather than relying only on numerical outputs.
- Documenting technical work using Markdown and GitHub.
- Organizing practical work using Git and version control.

---

# Conclusion

The completed Week 2 labs and practice exercises provided practical experience in **data processing, data cleaning, exploratory data analysis, statistical analysis, and visualization using Python**.

The work demonstrated the complete data analysis workflow, from loading and validating a dataset to performing statistical analysis, identifying patterns, detecting outliers, and communicating findings through visualizations.

Through this learning journey, I developed a stronger understanding of how Python libraries such as **Pandas, NumPy, Matplotlib, Seaborn, and SciPy** can be combined to perform practical data analysis.

The practical exercises also helped me understand that effective data analysis requires both **technical implementation and careful interpretation of results**. I learned that data analysis is an iterative process, where observations from one stage can guide the next stage of investigation.

Week 2 provided a strong foundation for further learning in:

- Data Science
- Machine Learning
- Data Analytics
- Statistical Analysis
- Data Visualization
# Conclusion

The completed assessments, labs, challenges, and data processing activities provided practical experience across Python programming, Linux tools, Bash scripting, SQL fundamentals, Git/GitHub workflows, and exploratory data analysis.

The portfolio demonstrates the ability to build structured projects, analyze real-world datasets, apply data preprocessing techniques, perform statistical analysis, create meaningful visualizations, and maintain professional technical documentation.

Through this learning journey, I developed a strong foundation in programming, data processing, exploratory data analysis, and software development practices.
