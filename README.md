# 🧠 Customer Churn Predictor

This project simulates CRM data and uses logistic regression to predict which customers are at risk of churning. Based on each customer's churn probability, it recommends clear retention actions such as **"Call & Retain"** or **"Send Promo"** — helping CRM teams act before it's too late.

---

## 📌 Project Highlights

- 🔁 Simulated CRM dataset (500 customers)
- 🎯 Predicts churn likelihood with logistic regression
- 🧠 Uses behavioral patterns like usage drop, login recency, and support activity
- 💬 Suggests human-friendly retention actions based on churn risk
- 📊 Visual insights: churn distribution, top churn drivers, risk segmentation

---

## 🛠️ Tech Stack

- Python (`pandas`, `numpy`)
- Machine Learning: `scikit-learn`
- Visualization: `seaborn`, `matplotlib`
- Modular Code: `utils/churn_helpers.py`
- Google Colab or Jupyter/VS Code

---

## 🗂️ Project Structure

Customer-Churn-Predictor/
├── churn_predictor.ipynb ← Main notebook
├── churn_predictions.csv ← Final churn scores + recommendations
├── utils/
│ ├── init.py
│ └── churn_helpers.py ← Functions for data generation + retention logic
└── README.md

---

## 🧠 Example Output

| CustomerID | ChurnProbability | RecommendedAction |
|------------|------------------|-------------------|
| 1043       | 84.7%            | Call & Retain     |
| 1111       | 43.2%            | Send Promo        |

---

## 👩‍💼 Why It Matters

Most CRM tools show raw data — but this project turns that data into **prioritized actions** that sales or account managers can take right now.

It’s not just code. It’s real insight, ready to use.

---

## 👋 About the Author

**Reem Bouqueau**  
[LinkedIn Profile →](https://www.linkedin.com/in/reem-bouqueau)  
Helping CRM and business teams turn messy data into clear decisions.

---

## 💡 Ideas to Extend

- Replace simulated data with real CRM exports  
- Add Streamlit dashboard for interactive exploration  
- Expand retention strategies by industry or region
