# Model Comparison and Selection

## 1. Objective

The objective of this experiment was to compare a simple baseline model with two tree-based ensemble models and select the most suitable final model for customer churn prediction.

The models evaluated were:

- Logistic Regression — baseline model
- Random Forest — bagging-based ensemble
- XGBoost — gradient-boosting model

ROC-AUC was selected as the primary evaluation metric, while F1-score was used as a supporting metric.

## 2. Validation Comparison

All three models were evaluated using the same validation dataset and the same evaluation methodology.

| Model | Validation ROC-AUC | Validation F1 |
|---|---:|---:|
| Logistic Regression | 0.8349 | 0.5836 |
| Tuned Random Forest | 0.8417 | 0.3164 |
| Tuned XGBoost | 0.8535 | 0.5841 |

ROC-AUC was prioritized because it evaluates the model's ability to distinguish between churned and non-churned customers across different classification thresholds.

F1-score was used as a supporting metric because the churn dataset contains class imbalance and both precision and recall are relevant.

## 3. Hyperparameter Tuning

Both Random Forest and XGBoost were tuned using `GridSearchCV` with three-fold cross-validation.

### Random Forest

Best configuration:

`max_depth = 10`  
`min_samples_split = 5`  
`n_estimators = 200`

Best cross-validated ROC-AUC:

`0.84998`

### XGBoost

Best configuration:

`learning_rate = 0.05`  
`max_depth = 3`  
`n_estimators = 100`

Best cross-validated ROC-AUC:

`0.86274`

The held-out test set was not used during hyperparameter tuning or model selection.

## 4. Model Selection

Tuned XGBoost was selected as the final model because it achieved the highest validation ROC-AUC among the three evaluated models.

Validation ROC-AUC ranking:

| Rank | Model | Validation ROC-AUC |
|---|---|---:|
| 1 | Tuned XGBoost | 0.8535 |
| 2 | Tuned Random Forest | 0.8417 |
| 3 | Logistic Regression | 0.8349 |

XGBoost therefore provided the strongest discrimination between churned and non-churned customers according to the project's primary evaluation metric.

XGBoost also achieved an F1-score of 0.5841, which was slightly higher than the Logistic Regression baseline F1-score of 0.5836 and substantially higher than the tuned Random Forest F1-score of 0.3164.

## 5. Performance vs Simplicity

Logistic Regression is the simplest of the three models and provides a useful interpretable baseline.

Random Forest provides a more flexible non-linear model, but in this experiment its F1-score was considerably lower than both Logistic Regression and XGBoost.

XGBoost is more complex than Logistic Regression, but the additional complexity was justified by its stronger validation ROC-AUC and slightly better F1-score.

The selected XGBoost configuration also uses a moderate tree depth of 3, which helps control model complexity.

## 6. Why XGBoost Was Selected

XGBoost was selected because:

- It achieved the highest validation ROC-AUC.
- It achieved the highest F1-score among the three evaluated models.
- It can capture non-linear relationships.
- It can model interactions between customer features.
- Its tuned configuration provided strong cross-validated performance.
- The increase in complexity was considered justified by the improvement in predictive performance.

## 7. Final Decision

**Final Model: Tuned XGBoost**

Selected configuration:

`n_estimators = 100`  
`learning_rate = 0.05`  
`max_depth = 3`

The selected model was then evaluated on the untouched test set.

The test set was not used for model training, hyperparameter tuning, or model selection.

## 8. Final Test Evaluation

The final model was evaluated on the held-out test set only after model selection.

Final test results:

| Metric | Score |
|---|---:|
| Accuracy | 0.8013 |
| Precision | 0.6715 |
| Recall | 0.4947 |
| F1-score | 0.5697 |
| ROC-AUC | 0.8585 |

The final test ROC-AUC was compared with the validation ROC-AUC to assess generalization performance.

The test ROC-AUC of 0.8585 was slightly higher than the validation ROC-AUC of 0.8535, indicating that the model maintained similar discriminatory performance on the held-out test set.

## 9. Conclusion

The comparison shows that the tuned XGBoost model was the strongest overall choice for this project.

Logistic Regression provided a simple and competitive baseline, while Random Forest provided a more flexible tree-based alternative. XGBoost achieved the highest validation ROC-AUC and a slightly higher F1-score than the baseline.

Based on the primary evaluation metric, supporting metric, cross-validation results, and the trade-off between performance and complexity, tuned XGBoost was selected as the final model.

The final XGBoost model was incorporated into a complete preprocessing and feature-engineering Pipeline and saved using Joblib for reproducible inference.