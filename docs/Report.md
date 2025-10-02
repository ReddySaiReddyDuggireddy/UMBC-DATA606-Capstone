## 4. Exploratory Data Analysis (EDA)

The purpose of this section is to explore the loan default dataset in detail, identify patterns and trends, and prepare the data for predictive modeling. This includes data cleaning, summary statistics, and visualizations to understand the relationship between features and the target variable.

---

### 4.1 Data Preparation
- **Target Variable:** `Default` (0 = Repaid, 1 = Defaulted)  
- **Features Used:** All columns except `LoanID` (dropped as it is only an identifier and does not provide predictive information).  

---

### 4.2 Data Quality Check
- **Missing Values:** No missing values found.  
- **Duplicate Rows:** No duplicate rows present.  
✅ The dataset is clean and ready for analysis.  

---

### 4.3 Summary Statistics
Key insights from numerical features:
- **Average Age:** ~44 years  
- **Average Loan Amount:** ~127,000  
- **Average Credit Score:** ~574  
- **Average Income:** ~85,000  
- **DTI Ratio:** Median around 0.5 (50% of income goes to debt payments).  

These statistics highlight that borrowers generally have mid-level incomes and moderate credit scores.

---

### 4.4 Target Variable Distribution
- Most loans are repaid (`Default = 0`).  
- Only a smaller portion of borrowers defaulted (`Default = 1`).  
- This indicates a **class imbalance**, which needs to be considered during model training (SMOTE).  

---

### 4.5 Correlation Analysis
- Loan Default shows weak but visible correlations with:
  - **Credit Score** (negative correlation)  
  - **Income** (negative correlation)  
  - **Interest Rate** (positive correlation)  
  - **Loan-to-Income Ratio** (positive correlation)  
- No strong multicollinearity issues among predictors.  

---

### 4.6 Feature vs Target Visualizations and Interpretations
- **Income vs Loan Default:** Borrowers who defaulted generally have lower incomes compared to those who repaid. Higher-income borrowers are less likely to default.  
- **Credit Score vs Loan Default:** Defaulters tend to have lower credit scores. Credit Score is a strong indicator of repayment ability.  
- **Loan Amount vs Loan Default:** Defaulters often took slightly higher loan amounts, suggesting larger loans may increase financial stress.  
- **Interest Rate vs Loan Default:** Defaulters usually face higher interest rates, showing that borrowing costs impact repayment.  
- **Debt-to-Income Ratio vs Loan Default:** Borrowers with higher DTI ratios are more likely to


