# Customer Churn Prediction — Week 4

## 1. Project Overview

This project builds an end-to-end machine learning solution to predict customer churn for a subscription-based company.

The goal is to identify customers who are likely to leave the service so that the business can prioritize customer-retention efforts.

The project covers the complete machine learning workflow:

- Dataset understanding and exploratory data analysis
- Data quality checks
- Target and class-imbalance analysis
- Train-validation-test splitting
- Baseline modelling
- Feature engineering
- Data preprocessing
- Random Forest and XGBoost modelling
- Hyperparameter tuning using cross-validation
- Fair model comparison
- Final test evaluation
- Error analysis
- Post-training visualization
- Complete ML Pipeline creation
- Model serialization using Joblib
- Model loading and inference
- PySpark feature engineering

---

## 2. Problem Statement

Customer churn occurs when an existing customer stops using a company's service.

For subscription-based businesses, identifying customers who are likely to churn can help the company take preventive actions such as targeted retention campaigns, customer-support interventions, or customized offers.

The objective of this project is to build a binary classification model that predicts whether a customer is likely to churn based on available demographic, subscription, service usage, and billing information.

### Target Variable

The target variable used for prediction is:

`Churn Value`

where:

- `0` = customer does not churn
- `1` = customer churns

---

## 3. Dataset

### Dataset Used

**IBM Telco Customer Churn**

### Source

Kaggle — IBM Telco Customer Churn dataset.

### Dataset Size

- Rows: 7,043
- Columns: 33

The dataset contains customer information related to:

- Demographics
- Customer tenure
- Phone services
- Internet services
- Online services
- Contract information
- Payment methods
- Monthly charges
- Total charges
- Customer churn

### Dataset Files

```text
dataset/
├── Telco_customer_churn.xlsx
└── Telco_customer_churn.csv
```

The Excel file is used in the main training workflow, while the CSV version is used for the Spark feature-engineering workflow.

---

## 4. Project Objectives

The main objectives of this project are:

1. Understand the structure and quality of the customer churn dataset.
2. Identify the target variable and analyze class imbalance.
3. Create a reproducible train-validation-test evaluation strategy.
4. Build a simple baseline model before feature engineering.
5. Engineer meaningful customer-level features.
6. Apply appropriate preprocessing techniques.
7. Train and compare Random Forest and XGBoost models.
8. Tune both tree-based models using cross-validation.
9. Select a final model using validation performance.
10. Evaluate the final model on the untouched test set.
11. Perform error analysis to identify difficult customer segments.
12. Create the required post-training visualizations.
13. Build one reusable preprocessing + model Pipeline.
14. Save the final Pipeline using Joblib.
15. Demonstrate inference using the saved Pipeline.
16. Translate selected feature-engineering operations into PySpark.

---

## 5. Evaluation Strategy

The dataset is divided into three parts:

- Training set: 70%
- Validation set: 15%
- Test set: 15%

Stratified splitting is used because this is a binary classification problem with class imbalance.

A fixed random seed is used to ensure reproducibility.

### Primary Evaluation Metric

**ROC-AUC** is selected as the primary metric.

ROC-AUC measures how well the model distinguishes between churned and non-churned customers across different classification thresholds.

### Supporting Metric

**F1-score** is used as a supporting metric because it balances precision and recall and is useful when dealing with imbalanced classes.

The test set is kept untouched during model training, hyperparameter tuning, and model selection and is used only for the final evaluation.

---

## 6. Baseline Model

A **Logistic Regression** model is used as the baseline before feature engineering.

The purpose of the baseline is to establish a simple reference point against which the more advanced tree-based models can be compared.

The baseline is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

---

## 7. Feature Engineering

Feature engineering is used to transform raw customer information into more meaningful variables that can help the machine learning models identify churn patterns.

The following engineered features were created.

### 7.1 Average Monthly Spend

```text
Avg_Monthly_Spend = Total Charges / Tenure Months
```

This feature represents the customer's approximate average spending per month over their observed tenure.

### 7.2 Total Services

`Total_Services` represents the number of services subscribed to by the customer.

This provides an estimate of the customer's overall level of service engagement.

### 7.3 Tenure Category

Customer tenure is divided into three categories:

- New
- Medium
- Long

This allows the model to capture differences in churn behaviour across customer lifecycle stages.

### 7.4 Contract Risk

`Contract_Risk` is derived from contract type and represents the different levels of churn exposure associated with customer contract commitments.

### 7.5 Log Total Charges

```text
Log_Total_Charges = log-transformed Total Charges
```

The logarithmic transformation reduces the effect of highly skewed charge values and provides a more stable representation of the numerical feature.

---

## 8. Data Preprocessing

The project uses scikit-learn preprocessing pipelines.

### Numerical Features

Numerical features are processed using:

- Median imputation
- StandardScaler

### Categorical Features

Categorical features are processed using:

- Most-frequent imputation
- One-Hot Encoding

The categorical encoder uses:

```text
handle_unknown = "ignore"
```

so that unseen categories during inference do not cause transformation errors.

All required preprocessing steps are incorporated into the final machine learning Pipeline.

---

## 9. Leakage Prevention

Target leakage is checked during data preparation and feature engineering.

The following columns are removed from the modelling features:

```text
Churn Label
Churn Score
Churn Reason
```

These columns contain churn-related information that would not be appropriate to use when making a real prediction at prediction time.

The test set is also protected from model tuning and model selection.

---

## 10. Machine Learning Models

Two tree-based models are trained and evaluated.

### Random Forest

Random Forest is a bagging-based ensemble algorithm that combines multiple decision trees.

It is useful for capturing non-linear relationships and interactions between customer features.

### XGBoost

XGBoost is a gradient-boosting algorithm that builds trees sequentially, with later trees focusing on correcting previous errors.

It is used to model complex non-linear relationships and interactions in the customer churn data.

---

## 11. Hyperparameter Tuning

Both Random Forest and XGBoost are tuned using:

```text
GridSearchCV
```

Three-fold cross-validation is used.

The tuning objective is:

```text
ROC-AUC
```

The held-out test set is not used during hyperparameter tuning or model selection.

The selected XGBoost configuration is:

```text
n_estimators = 100
learning_rate = 0.05
max_depth = 3
```

---

## 12. Model Comparison

The baseline and tuned tree-based models are compared using the same validation dataset and evaluation methodology.

| Model | Validation ROC-AUC | Validation F1 |
|---|---:|---:|
| Logistic Regression | 0.8349 | 0.5836 |
| Tuned Random Forest | 0.8415 | — |
| Tuned XGBoost | 0.8535 | 0.5792 |

ROC-AUC is treated as the primary metric while F1-score is used as a supporting metric.

XGBoost achieved the strongest validation ROC-AUC and was selected as the final model.

Although Logistic Regression achieved a slightly higher F1-score, XGBoost provided better overall discrimination according to the project's primary metric.

Detailed comparison and model-selection reasoning are documented in:

```text
comparison.md
```

---

## 13. Final Test Evaluation

After selecting the final model using the validation results, the selected XGBoost model is evaluated on the untouched test set.

### Final Test Results

| Metric | Score |
|---|---:|
| Accuracy | 0.8051 |
| Precision | 0.6812 |
| Recall | 0.5018 |
| F1-score | 0.5779 |
| ROC-AUC | 0.8576 |

The validation and test results are compared to assess the model's generalization performance.

---

## 14. Error Analysis

Error analysis is performed using the predictions made by the final model on the held-out test dataset.

Incorrect predictions are identified and analyzed across customer contract types.

The highest error rate is observed among:

**Month-to-month contract customers**

This indicates that the model has greater difficulty distinguishing churn behaviour within this segment.

### Potential Future Improvement

A possible next step would be to investigate validation-based probability threshold tuning.

This could help improve the balance between precision and recall depending on the business cost associated with false positives and false negatives.

---

## 15. Post-Training Visual Analysis

The training notebook contains the following visualizations:

1. Model Performance Comparison
2. Confusion Matrix
3. ROC Curve
4. Precision-Recall Curve
5. Top 10 Feature Importance
6. Error Analysis

Each visualization is based on the actual experiment results and includes an explanation of the key observation.

---

## 16. Final Machine Learning Pipeline

The final model is packaged as a single scikit-learn Pipeline.

The overall workflow is:

```text
Raw Customer Data
        |
        v
Feature Engineering
        |
        v
Numerical / Categorical Preprocessing
        |
        v
XGBoost Classifier
        |
        v
Churn Prediction
```

The Pipeline accepts raw customer input columns and automatically performs the required feature engineering and preprocessing before making predictions.

This avoids manually recreating preprocessing steps during inference and improves reproducibility.

---

## 17. Model Serialization

The complete fitted Pipeline is saved using **Joblib**.

Saved artifact:

```text
model/final_pipeline.joblib
```

The saved artifact contains the complete preprocessing and model workflow rather than only the trained estimator.

Notebook 2 loads this single Pipeline artifact and performs inference without retraining the model.

The project uses Joblib for serialization and does not explicitly use Pickle for saving or loading the model.

---

## 18. Inference Workflow

Notebook 2 represents the inference stage of the project.

The workflow is:

```text
Saved Pipeline
      |
      v
joblib.load()
      |
      v
Raw Customer Records
      |
      v
Feature Engineering
      |
      v
Preprocessing
      |
      v
XGBoost
      |
      +-------------------+
      |                   |
      v                   v
Predicted Class     Churn Probability
```

Notebook 2 demonstrates:

```python
predict()
```

for the predicted churn class and:

```python
predict_proba()
```

for churn probability.

The input customer information and corresponding predictions are displayed together in a clear table.

No retraining or manual reproduction of the preprocessing steps is performed during inference.

---

## 19. Spark Feature Engineering

Notebook 3 demonstrates how selected feature-engineering transformations from Notebook 1 can be translated into PySpark.

Two transformations are implemented.

### Average Monthly Spend

```text
Avg_Monthly_Spend = Total Charges / Tenure Months
```

This ratio feature is implemented using PySpark DataFrame operations.

### Tenure Category

Customer tenure is converted into:

- New
- Medium
- Long

using Spark conditional expressions.

The Spark implementation uses DataFrame APIs such as:

- `withColumn`
- `col`
- `when`
- `otherwise`

The notebook also compares the Pandas/scikit-learn and PySpark implementations.

Spark becomes useful when datasets become too large for efficient single-machine processing because it distributes data processing across multiple machines.

---

## 20. Repository Structure

```text
week-4-churn/
│
├── README.md
├── comparison.md
├── requirements.txt
│
├── dataset/
│   ├── Telco_customer_churn.xlsx
│   └── Telco_customer_churn.csv
│
├── model/
│   └── final_pipeline.joblib
│
├── src/
│   └── feature_engineering.py
│
├── train_model.ipynb
├── predict_model.ipynb
└── spark_feature_engineering.ipynb
```

### File Responsibilities

| File | Purpose |
|---|---|
| `README.md` | Project documentation, feature-engineering concepts, results, and instructions |
| `comparison.md` | Final model comparison and model-selection reasoning |
| `requirements.txt` | Project dependencies |
| `train_model.ipynb` | Complete training, evaluation, tuning, error analysis, visual analysis, and Pipeline creation |
| `predict_model.ipynb` | Load the saved Pipeline and perform inference |
| `spark_feature_engineering.ipynb` | Translate selected feature-engineering transformations into PySpark |
| `model/final_pipeline.joblib` | Saved fitted preprocessing + final model Pipeline |
| `src/feature_engineering.py` | Feature-engineering implementation |
| `dataset/` | Project datasets |

---

## 21. Installation

Install the project dependencies using:

```bash
pip install -r requirements.txt
```

### Main Dependencies

```text
pandas==2.3.3
numpy==2.3.5
matplotlib==3.10.0
seaborn==0.13.2
scikit-learn==1.9.0
xgboost==3.4.1
joblib==1.5.3
openpyxl==3.1.5
pyspark==4.2.0
```

---

## 22. How to Run

### Notebook 1 — Train and Save

Open:

```text
train_model.ipynb
```

Run the notebook from top to bottom.

This notebook performs the complete machine learning workflow and saves the final Pipeline to:

```text
model/final_pipeline.joblib
```

### Notebook 2 — Load and Predict

Open:

```text
predict_model.ipynb
```

This notebook loads the saved Pipeline and performs predictions on raw customer data without retraining.

### Notebook 3 — Spark Feature Engineering

Open:

```text
spark_feature_engineering.ipynb
```

This notebook demonstrates selected feature-engineering transformations using PySpark.

---

## 23. Feature Engineering Concepts

### One-Hot Encoding

**What it does:**

One-Hot Encoding converts categorical variables into numerical binary columns so machine learning models can process them.

**When useful:**

Useful for nominal categorical variables where categories do not have any natural order, such as Contract Type, Payment Method, or Internet Service.

**Limitation/Risk:**

It can create a large number of features when a column contains many unique categories.

### Ordinal / Label Encoding

**What it does:**

Ordinal encoding assigns numerical values to categories based on their order.

**When useful:**

Useful when categories have a meaningful ranking, such as Low, Medium, and High.

**Limitation/Risk:**

Using it on unordered categories may create false relationships because the model may interpret numbers as having a mathematical meaning.

### Target / Mean Encoding

**What it does:**

Target encoding replaces categories with the average target value associated with each category.

**When useful:**

Useful for high-cardinality categorical features where One-Hot Encoding creates too many columns.

**Limitation/Risk:**

It can cause target leakage if calculated using information from validation or test data.

### Scaling / Standardization

**What it does:**

Scaling transforms numerical features into a similar range, commonly using StandardScaler.

**When useful:**

Useful for models affected by feature magnitude, such as Logistic Regression, SVM, and KNN.

**Limitation/Risk:**

Scaling is usually unnecessary for tree-based models because they split data using thresholds.

### Missing-value Imputation

**What it does:**

Imputation replaces missing values with estimated values.

**When useful:**

Used when datasets contain incomplete information.

**Common approaches:**

- Median imputation for numerical variables
- Most-frequent imputation for categorical variables

**Limitation/Risk:**

Poor imputation choices can introduce bias into the dataset.

### Binning

**What it does:**

Binning converts continuous numerical values into groups or ranges.

**When useful:**

Useful when ranges are more meaningful than exact values.

Example:

```text
Age → Young, Adult, Senior
```

**Limitation/Risk:**

Too many bins can increase complexity, while too few bins may remove useful information.

### Interaction Features

**What it does:**

Interaction features combine two or more variables to capture relationships between them.

**When useful:**

Useful when the effect of one feature depends on another feature.

Example:

```text
Income × Spending
```

**Limitation/Risk:**

Creating too many interactions can increase model complexity and overfitting.

### Ratio Features

**What it does:**

Ratio features create relationships between numerical variables.

**When useful:**

Useful when relative values are more meaningful than absolute values.

Example:

```text
Total Charges / Tenure Months
→ Average Monthly Spend
```

**Limitation/Risk:**

Division by zero and unstable ratios need to be handled carefully.

### Date / Time Features

**What it does:**

Date information can be converted into useful features such as year, month, day, or duration.

**When useful:**

Useful when time patterns influence the target.

Examples:

```text
Customer signup month
Days since registration
```

**Limitation/Risk:**

Future information must not be used during prediction.

### Target Leakage

**What it does:**

Target leakage occurs when information unavailable at prediction time is included in training data.

**When useful:**

Target leakage checks are useful during data preparation and feature engineering to make sure that no feature contains information that would be unavailable when the model makes a real-world prediction.

**Risk:**

It produces unrealistically high performance and poor real-world results.

Example:

```text
Using Churn Reason to predict Churn
```

---

## 24. Learning and Reference Resources

The following resources were used to understand the concepts, APIs, and implementation used in the project.

### Dataset

- IBM Telco Customer Churn dataset from Kaggle

### Machine Learning and Preprocessing

- Scikit-learn User Guide
  - preprocessing
  - pipelines
  - model evaluation
  - cross-validation
  - hyperparameter tuning
  - ensemble methods

### Feature Engineering

- Coursera learning material covering feature engineering and preprocessing

### XGBoost

- XGBoost documentation and API references

### PySpark

- Apache Spark / PySpark documentation
  - Spark DataFrame APIs
  - `withColumn`
  - column expressions
  - conditional transformations

These resources were used for learning and implementation guidance. The final workflow was verified against the project requirements and experiment results.

---

## 25. Limitations

The current project has some limitations:

- The dataset is relatively small compared with production-scale customer datasets.
- The inference demonstration uses a small sample of customer records.
- The final model has lower recall than precision, meaning some churners may not be detected.
- Month-to-month contract customers show a higher error rate than other contract groups.
- Probability-threshold tuning has not yet been explored.
- Additional customer-behaviour or temporal features could potentially improve performance if more suitable production data were available.

---

## 26. Conclusion

This project implements a complete customer churn prediction workflow, starting from raw customer data and ending with a reusable serialized machine learning Pipeline.

Feature engineering was used to create meaningful representations of customer spending, service engagement, tenure, contract risk, and charge distributions.

Logistic Regression was used as the baseline model, followed by Random Forest and XGBoost as tree-based models. Both tree-based models were tuned using cross-validation and evaluated using the same validation strategy.

XGBoost was selected as the final model because it achieved the strongest validation ROC-AUC among the evaluated models.

The final preprocessing steps, feature engineering, and XGBoost model were packaged into a single scikit-learn Pipeline and saved using Joblib. This allows the saved artifact to be loaded and used directly for prediction on raw customer data without retraining or manually rebuilding the preprocessing workflow.

A separate Spark notebook demonstrates how selected feature-engineering transformations can be implemented using PySpark DataFrame operations.

Overall, the project demonstrates an end-to-end and reproducible machine learning workflow covering:

```text
Data Understanding
      ↓
Evaluation Strategy
      ↓
Baseline
      ↓
Feature Engineering
      ↓
Preprocessing
      ↓
Model Training
      ↓
Cross-Validation & Tuning
      ↓
Model Comparison
      ↓
Final Test Evaluation
      ↓
Error Analysis
      ↓
Final Pipeline
      ↓
Joblib Serialization
      ↓
Inference
      ↓
PySpark Feature Engineering
```