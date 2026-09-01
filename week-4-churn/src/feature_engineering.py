import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class FeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        leakage_columns = [
            "Churn Label",
            "Churn Score",
            "Churn Reason"
        ]

        X = X.drop(
            columns=leakage_columns,
            errors="ignore"
        )

        X["Total Charges"] = pd.to_numeric(
            X["Total Charges"],
            errors="coerce"
        )

        X["Avg_Monthly_Spend"] = (
            X["Total Charges"] /
            X["Tenure Months"].replace(0, np.nan)
        )

        X["Total_Services"] = (
            (X["Phone Service"] == "Yes").astype(int)
            + (X["Internet Service"] != "No").astype(int)
            + (X["Online Security"] == "Yes").astype(int)
            + (X["Tech Support"] == "Yes").astype(int)
        )

        X["Tenure_Category"] = pd.cut(
            X["Tenure Months"],
            bins=[0, 12, 36, 72],
            labels=["New", "Medium", "Long"]
        )

        X["Contract_Risk"] = np.where(
            X["Contract"] == "Month-to-month",
            "High",
            "Low"
        )

        X["Log_Total_Charges"] = np.log1p(
            X["Total Charges"]
        )

        return X