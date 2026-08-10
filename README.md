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


# Repository Structure

```text
learning-portfolio/
│
├── README.md
├── .gitignore
│
└── week-1_foundations/
│
├── assessment_work/
│ └── assessment-0-python-version-comparison/
│
├── lab_work/
│ │
│ ├── lab-01-project-and-environment-setup/
│ │
│ ├── lab-02-python-fluency-drills/
│ │
│ ├── lab-03-github-and-github-workflow/
│ │
│ ├── lab-04-command-line-and-bash/
│ │
│ └── lab-05-sql-fundamentals/
│ ├── README.md
│ ├── Chinook_Sqlite.sqlite
│ ├── screenshots/
│ └── sql/
│
└── challenges/
│
├── README.md
├── challenges_faced.md
├── csvstat.py
├── learnings.md
├── questions.md
├── samples/
│ └── example.csv
│
├── screenshots/
│ ├── part-a/
│ │ ├── 1.1_row_column_count.png
│ │ ├── 1.2_columns.png
│ │ ├── 1.3_datatype_check.png
│ │ ├── 1.4_datatype_check.png
│ │ ├── 1.5_numeric_stats.png
│ │ └── 1.6_top_value_frequency.png
│ │
│ └── part-b/
│ ├── 2.1_sql_top_customers.png
│ ├── 2.2_revenue_by_country.png
│ ├── 2.3_best_selling_tracks.png
│ └── 2.4_monthly_revenue.png
│
└── sql/
├── top_customers.sql
├── revenue_by_country.sql
├── best_selling_tracks.sql
└── monthly_revenue.sql
            
```

---

# Technologies Used

- Ubuntu Linux
- Python 3.8
- Python 3.12
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
- SQLite Documentation
- SQLite Tutorial
- SQLBolt
- Ubuntu Documentation
- Git Documentation
- GitHub Documentation
- Visual Studio Code Documentation
- Bash Manual
- GNU Coreutils Documentation
- Project Gutenberg

---

# Learning Outcomes

Through these assessments and labs, I gained practical experience in:

- Setting up Python development environments on Ubuntu.
- Working with multiple Python versions.
- Understanding version-specific language features.
- Managing isolated virtual environments.
- Writing reusable Python functions.
- Using list comprehensions and Python collections.
- Reading data from files and handling exceptions.
- Using Linux command-line tools effectively.
- Writing reusable Bash scripts.
- Processing text using Unix command pipelines.
- Automating command-line tasks with shell scripting.
- Working with relational databases using SQL.
- Filtering, sorting, grouping, and aggregating database records.
- Joining related database tables.
- Performing date-based analysis using SQLite.
- Working with Git branches and pull requests.
- Resolving merge conflicts and synchronizing branches.
- Organizing projects using Git and GitHub.
- Documenting technical work using Markdown.
- Building command-line data profiling tools using Python.
- Performing exploratory data analysis on CSV datasets.
- Understanding data quality checks and profiling techniques.
- Writing analytical SQL queries for extracting business insights.
- Combining Python scripting and SQL analysis for practical data workflows.

---

# Conclusion

The completed assessments, labs, and weekly challenge provided practical experience across Python programming, Linux command-line operations, Bash scripting, SQL fundamentals, data profiling, and Git/GitHub workflows.

The portfolio demonstrates the ability to apply programming and data analysis concepts through structured exercises, build command-line tools, perform SQL-based analysis, document technical work, and maintain projects using professional development practices.
