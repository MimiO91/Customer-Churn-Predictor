import pandas as pd
import numpy as np

def generate_customer_data(n_customers=500, seed=42):
    np.random.seed(seed)
    df = pd.DataFrame({
        "CustomerID": range(1001, 1001 + n_customers),
        "Industry": np.random.choice(["Tech", "Retail", "Healthcare", "Finance", "Education"], n_customers),
        "TenureMonths": np.random.randint(1, 60, n_customers),
        "LastLoginDaysAgo": np.random.randint(0, 60, n_customers),
        "SupportTickets": np.random.poisson(2, n_customers),
        "AvgUsage": np.round(np.random.uniform(30, 100, n_customers), 2),
        "UsageDropPct": np.round(np.random.uniform(0, 80, n_customers), 2),
        "ContractEndsIn": np.random.randint(0, 24, n_customers)
    })

    # Simulated churn label
    df["Churned"] = df.apply(
        lambda row: 1 if (row["UsageDropPct"] > 50 and row["LastLoginDaysAgo"] > 30 and row["SupportTickets"] >= 3) else 0,
        axis=1
    )
    return df

def assign_retention_action(prob):
    if prob > 0.6:
        return "Call & Retain"
    elif prob > 0.3:
        return "Send Promo"
    else:
        return "No Action"
