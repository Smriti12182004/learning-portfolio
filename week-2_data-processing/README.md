# Week 2 – Data Processing & Exploratory Data Analysis

This repository documents my **Week 2 internship learning journey at VCreateK**.

The focus of this week was **data processing, exploratory data analysis (EDA), statistical analysis, and visualization techniques using Python**.

The objective was to understand how raw datasets are loaded, cleaned, explored, analyzed, and visualized using Python libraries.

## Libraries Used

- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy

---

# Dataset Used

## Wine Quality Dataset

**File:** `WineQT.csv`

The dataset contains physicochemical properties of wine samples along with their quality ratings.

## Features Analyzed

- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality

---

# Notebook Work

# Notebook 1 – Exploratory Data Analysis (EDA)

**File:** `01_eda.ipynb`

## Theory

Exploratory Data Analysis (EDA) is used to understand dataset structure, identify patterns, detect missing values, find outliers, and analyze relationships between variables before applying machine learning models.

## Objective

- Understand dataset structure.
- Perform data quality checks.
- Analyze feature distributions.
- Visualize relationships between variables.

## Completed Tasks

- Loaded Wine Quality dataset.
- Checked dataset dimensions.
- Inspected columns and data types.
- Generated statistical summaries.
- Checked missing values.
- Checked duplicate records.
- Created visualizations.

## Commands Used

```python
pd.read_csv()

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()
```

### Visualization

```python
sns.histplot()

sns.boxplot()

sns.scatterplot()

sns.heatmap()
```

## Concepts Practiced

- Data exploration
- Data quality analysis
- Statistical summary
- Data visualization

---

# Notebook 2 – NumPy and Pandas Fundamentals

**File:** `02_pandas_numpy.ipynb`

## Theory

NumPy provides efficient numerical computation using arrays, while Pandas provides powerful tools for data manipulation using Series and DataFrames.

## Objective

- Understand NumPy arrays.
- Perform numerical operations.
- Learn Pandas data structures.
- Perform data manipulation.

## Completed Tasks

### NumPy

- Created arrays.
- Checked array properties.
- Performed mathematical operations.
- Applied filtering.
- Reshaped arrays.

### Pandas

- Created Series and DataFrames.
- Selected rows and columns.
- Filtered data.
- Grouped data.
- Performed cleaning operations.

## Commands Used

```python
np.array()

array.shape

array.ndim

array.size

array.dtype

np.mean()

np.median()

np.std()

pd.DataFrame()

df.loc[]

df.iloc[]

df.groupby()

drop_duplicates()

rename()
```

## Concepts Practiced

- ndarray
- Array indexing
- Array slicing
- DataFrames
- Filtering
- GroupBy operations

---

# Notebook 3 – Normal Distribution

**File:** `03_normal_distribution.ipynb`

## Theory

Normal distribution is a probability distribution where data is symmetrically distributed around the mean and follows a bell-shaped curve.

## Properties

- Mean = Median = Mode
- Data is concentrated around the mean
- Spread depends on standard deviation

## Objective

- Understand normal distribution properties.
- Analyze statistical behavior.
- Visualize probability distributions.

## Completed Tasks

- Generated normal distributions.
- Calculated mean and standard deviation.
- Visualized bell curves.
- Applied z-score standardization.

## Commands Used

```python
np.random.normal()

np.mean()

np.std()

sns.histplot(kde=True)
```

### Z-score

```python
z = (x - mean) / standard_deviation
```

## Concepts Practiced

- Gaussian distribution
- Mean
- Standard deviation
- Bell curve
- Z-score

---

# Notebook 4 – Interquartile Range (IQR)

**File:** `04_IQR.ipynb`

## Theory

IQR is a statistical method used to measure data spread and identify outliers.

## Formula

```python
IQR = Q3 - Q1
```

## Outlier Boundaries

```python
Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

## Completed Tasks

- Calculated quartiles.
- Calculated IQR.
- Detected outliers.
- Visualized box plots.

## Commands Used

```python
quantile()

sns.boxplot()
```

## Concepts Practiced

- Quartiles
- IQR
- Outlier detection
- Box plot analysis

---

# Notebook 5 – Kernel Density Estimation (KDE)

**File:** `05_KDE.ipynb`

## Theory

KDE is a statistical technique used to estimate probability density and understand the distribution pattern of data.

## Completed Tasks

- Created KDE plots.
- Compared histogram and KDE.
- Studied bandwidth effect.
- Applied KDE on Wine Quality features.

## Commands Used

```python
sns.kdeplot()

sns.histplot(kde=True)

bw_adjust
```

## Concepts Practiced

- Density estimation
- Density curves
- Bandwidth
- Distribution analysis

---

# Notebook 6 – Contour Plot

**File:** `06_contour_plot.ipynb`

## Theory

Contour plots represent relationships between continuous variables using contour lines and help visualize density regions.

## Completed Tasks

- Created contour plots.
- Generated density visualizations.
- Studied feature relationships.

## Commands Used

```python
plt.contour()
```

```python
sns.kdeplot(
    x=,
    y=,
    fill=True
)
```

## Concepts Practiced

- Contour lines
- Density visualization
- Two-dimensional visualization
- Feature relationship analysis

---

# Repository Structure

```
week-2_data-processing/

│
├── README.md
├── requirements.txt
│
├── data/
│   └── WineQT.csv
│
└── notebooks/
    ├── 01_eda.ipynb
    ├── 02_pandas_numpy.ipynb
    ├── 03_normal_distribution.ipynb
    ├── 04_IQR.ipynb
    ├── 05_KDE.ipynb
    └── 06_contour_plot.ipynb
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming |
| Jupyter Notebook | Analysis |
| NumPy | Numerical Computing |
| Pandas | Data Processing |
| Matplotlib | Visualization |
| Seaborn | Statistical Visualization |
| SciPy | Scientific Computing |
| Git/GitHub | Version Control |

---

# Learning Outcomes

Through Week 2 activities, I gained practical experience in:

- Loading and inspecting datasets.
- Data cleaning and preprocessing.
- Exploratory data analysis.
- Statistical analysis.
- Data visualization.
- Normal distribution analysis.
- Outlier detection using IQR.
- Density estimation using KDE.
- Contour visualization.
- Documenting technical work using Markdown.

---

# Conclusion

Week 2 provided practical experience with **data processing and exploratory data analysis workflows**.

The completed notebooks demonstrate the ability to analyze real-world datasets, apply statistical techniques, visualize patterns, and use Python libraries for data-driven analysis.

These concepts provide a strong foundation for further learning in:

- Data Science
- Machine Learning
- Analytics