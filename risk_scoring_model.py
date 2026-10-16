"""
Tata Financial Delinquency Prediction & Risk Profiling Model
System: Geldium AI Collections Platform
Author: Prashant Kumar
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, precision_recall_fscore_support

def generate_financial_dataset(n=5000):
    np.random.seed(101)
    data = {
        'credit_score': np.random.normal(680, 50, n).clip(300, 850),
        'debt_to_income': np.random.uniform(0.1, 0.65, n),
        'past_delinquencies': np.random.poisson(0.8, n),
        'credit_utilization': np.random.uniform(0.05, 0.95, n),
        'monthly_income': np.random.normal(5500, 1500, n).clip(1200, 20000),
        'loan_amount': np.random.normal(15000, 6000, n).clip(2000, 60000),
        'payment_history_score': np.random.uniform(0.4, 1.0, n)
    }
    df = pd.DataFrame(data)
    # Delinquency logit
    logit = (
        -0.008 * df['credit_score'] +
        3.2 * df['debt_to_income'] +
        0.5 * df['past_delinquencies'] +
        2.5 * df['credit_utilization'] -
        2.1 * df['payment_history_score']
    )
    prob = 1 / (1 + np.exp(-logit))
    df['is_delinquent'] = (prob > 0.45).astype(int)
    return df

def train_risk_engine():
    print("[+] Loading Geldium Financial Intelligence Dataset...")
    df = generate_financial_dataset(8000)
    X = df.drop('is_delinquent', axis=1)
    y = df['is_delinquent']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.08, max_depth=4, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    probas = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, probas)

    print(f"[+] Model ROC-AUC Score: {auc:.4f}")
    return model, X_test, y_test

if __name__ == "__main__":
    train_risk_engine()
