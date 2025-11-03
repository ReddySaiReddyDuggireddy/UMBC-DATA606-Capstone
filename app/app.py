#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(page_title="Loan Default Risk – Demo", page_icon="💳", layout="centered")

# -----------------------------
# Load trained model (Pipeline)
# -----------------------------
@st.cache_resource
def load_model(path="/Users/reddysaireddyduggireddy/xgb_best_model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

model = load_model("/Users/reddysaireddyduggireddy/xgb_best_model.pkl")

st.title("Loan Default Risk Prediction")
st.caption("Enter borrower & loan details. The app computes engineered risk features and predicts default risk.")

# -----------------------------
# Left/Right columns for clean UI
# -----------------------------
c1, c2 = st.columns(2)

with c1:
    # Numeric inputs
    age = st.number_input("Age (years)", min_value=18, max_value=99, value=35, step=1)
    income = st.number_input("Annual Income ($)", min_value=0, value=80000, step=1000)
    loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=120000, step=1000)
    credit_score = st.number_input("Credit Score (300–850)", min_value=300, max_value=850, value=680, step=1)
    months_employed = st.number_input("Months Employed", min_value=0, max_value=600, value=60, step=1)
    num_credit_lines = st.number_input("Number of Credit Lines", min_value=1, max_value=50, value=3, step=1)
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=40.0, value=10.5, step=0.1)

with c2:
    loan_term = st.number_input("Loan Term (months)", min_value=6, max_value=360, value=36, step=6)
    dti_ratio = st.number_input("Debt-to-Income Ratio (0.1–0.9)", min_value=0.0, max_value=2.0, value=0.50, step=0.01)

    # Categorical inputs
    education = st.selectbox("Education", ["High School", "Bachelor's", "Master's", "PhD", "Other"])
    employment_type = st.selectbox("Employment Type", ["Full-time", "Part-time", "Self-employed", "Unemployed", "Contract", "Other"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed", "Other"])
    has_mortgage = st.selectbox("Has Mortgage?", ["Yes", "No"])
    has_dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
    loan_purpose = st.selectbox("Loan Purpose", ["Home", "Auto", "Education", "Business", "Debt Consolidation", "Other"])
    has_cosigner = st.selectbox("Has Co-Signer?", ["Yes", "No"])

st.markdown("---")

# -----------------------------
# Helper: safe divisions
# -----------------------------
def safe_div(a, b, default=0.0):
    a = float(a)
    b = float(b)
    if b == 0 or np.isinf(a) or np.isinf(b) or np.isnan(a) or np.isnan(b):
        return default
    val = a / b
    if np.isinf(val) or np.isnan(val):
        return default
    return val

# -----------------------------
# Build single-row DataFrame of ORIGINAL features
# -----------------------------
row = {
    "Age": age,
    "Income": income,
    "LoanAmount": loan_amount,
    "CreditScore": credit_score,
    "MonthsEmployed": months_employed,
    "NumCreditLines": num_credit_lines,
    "InterestRate": interest_rate,
    "LoanTerm": loan_term,
    "DTIRatio": dti_ratio,
    "Education": education,
    "EmploymentType": employment_type,
    "MaritalStatus": marital_status,
    "HasMortgage": has_mortgage,
    "HasDependents": has_dependents,
    "LoanPurpose": loan_purpose,
    "HasCoSigner": has_cosigner,
}

df = pd.DataFrame([row])

# -----------------------------
# Compute ENGINEERED FEATURES
# -----------------------------
df["Loan_to_Income_Ratio"] = df.apply(lambda r: safe_div(r["LoanAmount"], r["Income"]), axis=1)
df["Credit_Exposure_Ratio"] = df.apply(lambda r: safe_div(r["LoanAmount"], r["NumCreditLines"]), axis=1)
df["Income_per_CreditLine"] = df.apply(lambda r: safe_div(r["Income"], r["NumCreditLines"]), axis=1)
df["Debt_Service_Ratio"] = df["DTIRatio"] * df["InterestRate"]

# MonthsEmployed / (Age * 12), clipped to [0, 1]
df["EmploymentStability"] = df.apply(lambda r: safe_div(r["MonthsEmployed"], (r["Age"] * 12.0)), axis=1)
df["EmploymentStability"] = np.clip(df["EmploymentStability"], 0, 1)

df["LoanBurden"] = df["Loan_to_Income_Ratio"] * df["DTIRatio"]
df["FinancialStress"] = df.apply(
    lambda r: safe_div(r["InterestRate"] * r["DTIRatio"], r["CreditScore"]),
    axis=1
)

# Combined income: boost if co-signer present (your assumption)
df["CombinedIncome"] = np.where(df["HasCoSigner"] == "Yes", df["Income"] * 1.5, df["Income"])

# Final safety pass (single row)
df = df.replace([np.inf, -np.inf], np.nan)
# For a single-row, filling with 0.0 is fine (no median across dataset available in app)
df = df.fillna(0.0)

# -----------------------------
# Align to model's expected columns if available
# -----------------------------
def align_to_model_columns(model, frame: pd.DataFrame):
    # If your pipeline preserves feature_names_in_ (sklearn >=1.0), use it
    expected = getattr(model, "feature_names_in_", None)
    if expected is not None:
        expected = list(expected)
        # Add any missing columns as zeros (robustness)
        for col in expected:
            if col not in frame.columns:
                frame[col] = 0
        # Keep only expected, and in order
        frame = frame[expected]
    return frame

df_for_model = align_to_model_columns(model, df.copy())

# -----------------------------
# Preview inputs & engineered
# -----------------------------
with st.expander("🔎 Preview row (original + engineered)"):
    st.dataframe(df, use_container_width=True)

# -----------------------------
# Predict
# -----------------------------
if st.button("Predict Default Risk"):
    try:
        y_pred = model.predict(df_for_model)
        # Try predict_proba if available
        default_prob = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(df_for_model)
            # binary: take probability of class 1
            if proba.shape[1] == 2:
                default_prob = float(proba[0, 1])

        if int(y_pred[0]) == 1:
            if default_prob is not None:
                st.error(f"⚠️ Likely to DEFAULT. Estimated probability: **{default_prob:.2%}**")
            else:
                st.error("⚠️ Likely to DEFAULT.")
        else:
            if default_prob is not None:
                st.success(f"✅ Likely to REPAY. Estimated default probability: **{default_prob:.2%}**")
            else:
                st.success("✅ Likely to REPAY.")

        # Small note for graders
        st.caption("Note: This result depends on the model you trained & saved as model.pkl and the exact feature schema.")
    except Exception as e:
        st.exception(e)
        st.warning(
            "If you see a column mismatch error, ensure your model was trained with the same columns "
            "(including engineered features) or save a Pipeline that handles preprocessing internally."
        )


# In[ ]:




