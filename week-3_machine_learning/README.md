# Student Performance Prediction using Machine Learning

## 📌 Project Overview

This project focuses on predicting students' final performance scores using Machine Learning. The project implements a complete machine learning workflow starting from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, and prediction.

A **Linear Regression** model is used to learn the relationship between different student-related factors and their final scores.

---

##  Objective

The main objectives of this project are:

- Analyze the factors affecting student performance.
- Perform data cleaning and exploratory data analysis.
- Build a machine learning regression model.
- Evaluate model performance using different evaluation metrics.
- Predict student scores using the trained model.

---

##  Dataset Description

The dataset contains information related to students' academic and lifestyle factors.

### Input Features:

- Study Hours
- Attendance
- Previous Score
- Assignments Completed
- Sleep Hours
- Internet Usage Hours
- Extra Classes

### Target Variable:

- **Final Score**

The target variable represents the final academic performance score of the student.

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Pickle

---

##  Machine Learning Workflow

The project follows the following pipeline:

1. Importing Required Libraries
2. Loading Dataset
3. Data Exploration
4. Data Cleaning
5. Exploratory Data Analysis (EDA)
6. Feature Selection and Preprocessing
7. Splitting Dataset
8. Model Training
9. Model Evaluation
10. Saving Trained Model
11. Making Predictions

---

##  Data Preprocessing

The following preprocessing steps were performed:

- Checking missing values
- Handling duplicate records
- Treating outliers
- Converting data into suitable format for model training

Outlier analysis was performed using the **IQR method**.

---

##  Exploratory Data Analysis (EDA)

EDA was performed to understand relationships and patterns within the dataset.

The analysis included:

- Data distribution analysis
- Boxplot analysis for outliers
- Correlation analysis
- Feature relationship visualization

Important relationships studied:

- Study Hours vs Final Score
- Attendance vs Final Score
- Previous Score vs Final Score
- Assignment Completion vs Performance

---

##  Machine Learning Model

### Linear Regression

Linear Regression was used because the target variable (**Final Score**) is continuous.

The model estimates the relationship:

```
Final Score = f(Student Features)
```

and predicts student performance based on given inputs.

---

##  Model Evaluation

The model performance was evaluated using:

### Evaluation Metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

##  Train-Test Split Evaluation

Dataset was divided into:

- Training Data: 80%
- Testing Data: 20%

Performance:

```
MAE  : 3.75
RMSE : 4.40
R² Score : 0.86
```

---

##  Train-Validation-Test Evaluation

Dataset was divided into:

- Training Data: 70%
- Validation Data: 15%
- Testing Data: 15%

Performance:

```
Validation R² Score : 0.85

Testing R² Score : 0.86
```

The similar validation and testing performance shows that the model generalizes well on unseen data.

---

##  Visualization

The project includes visualizations such as:

- Actual vs Predicted Values Plot
- Residual Analysis
- Feature Relationship Graphs
- Correlation Heatmap

These visualizations help understand model performance and data patterns.

---

##  Model Saving

The trained Linear Regression model is saved using Pickle.

Saved model file:

```
linear_regression_model.pkl
```

The saved model can be reused for making predictions without retraining.

---

##  Prediction

The trained model can predict student final scores by providing new student information.

Example inputs:

- Study Hours
- Attendance
- Previous Score
- Assignment Completion
- Sleep Hours
- Internet Usage
- Extra Classes

---




## ✅ Conclusion

This project successfully demonstrates the implementation of a complete Machine Learning regression pipeline for predicting student performance.

The Linear Regression model achieved an R² score of approximately **0.86**, showing good predictive performance.

The project covers:

- Data preprocessing
- Exploratory Data Analysis
- Machine Learning model development
- Model evaluation
- Prediction workflow

---

