# Feature Engineering Concepts

## One-Hot Encoding

**What it does:**  
One-Hot Encoding converts categorical variables into numerical binary columns so machine learning models can process them.

**When useful:**  
Useful for nominal categorical variables where categories do not have any natural order, such as Contract Type, Payment Method, or Internet Service.

**Limitation/Risk:**  
It can create a large number of features when a column contains many unique categories.

---

## Ordinal / Label Encoding

**What it does:**  
Ordinal encoding assigns numerical values to categories based on their order.

**When useful:**  
Useful when categories have a meaningful ranking, such as Low, Medium, and High.

**Limitation/Risk:**  
Using it on unordered categories may create false relationships because the model may interpret numbers as having a mathematical meaning.

---

## Target / Mean Encoding

**What it does:**  
Target encoding replaces categories with the average target value associated with each category.

**When useful:**  
Useful for high-cardinality categorical features where One-Hot Encoding creates too many columns.

**Limitation/Risk:**  
It can cause target leakage if calculated using information from validation or test data.

---

## Scaling / Standardization

**What it does:**  
Scaling transforms numerical features into a similar range, commonly using StandardScaler.

**When useful:**  
Useful for models affected by feature magnitude, such as Logistic Regression, SVM, and KNN.

**Limitation/Risk:**  
Scaling is usually unnecessary for tree-based models because they split data using thresholds.

---

## Missing-value Imputation

**What it does:**  
Imputation replaces missing values with estimated values.

**When useful:**  
Used when datasets contain incomplete information.

**Common approaches:**
- Median imputation for numerical variables
- Most-frequent imputation for categorical variables

**Limitation/Risk:**  
Poor imputation choices can introduce bias into the dataset.

---

## Binning

**What it does:**  
Binning converts continuous numerical values into groups or ranges.

**When useful:**  
Useful when ranges are more meaningful than exact values.

Example:
- Age → Young, Adult, Senior

**Limitation/Risk:**  
Too many bins can increase complexity, while too few bins may remove useful information.

---

## Interaction Features

**What it does:**  
Interaction features combine two or more variables to capture relationships between them.

**When useful:**  
Useful when the effect of one feature depends on another feature.

Example:
- Income × Spending

**Limitation/Risk:**  
Creating too many interactions can increase model complexity and overfitting.

---

## Ratio Features

**What it does:**  
Ratio features create relationships between numerical variables.

**When useful:**  
Useful when relative values are more meaningful than absolute values.

Example:
- Total Charges / Tenure Months → Average Monthly Spend

**Limitation/Risk:**  
Division by zero and unstable ratios need to be handled carefully.

---

## Date / Time Features

**What it does:**  
Date information can be converted into useful features such as year, month, day, or duration.

**When useful:**  
Useful when time patterns influence the target.

Example:
- Customer signup month
- Days since registration

**Limitation/Risk:**  
Future information must not be used during prediction.

---

## Target Leakage

**What it does:**  
Target leakage occurs when information unavailable at prediction time is included in training data.

**When useful:**  
Leakage is not a feature engineering technique but a check performed to ensure reliable models.

**Risk:**  
It produces unrealistically high performance and poor real-world results.

Example:
Using Churn Reason to predict Churn.