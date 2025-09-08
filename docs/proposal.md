# Loan Default Prediction Using Machine Learning
Prepared for UMBC Data Science Master Degree Capstone by **Dr. Chaojie (Jay) Wang**  
Author: **Reddy Sai Reddy Duggireddy**  
GitHub: *[Add link once repo is created]*  
LinkedIn: *[Add link]*  
PowerPoint: *[Add link]*  
YouTube: *[Add link]*  

---

## 1. Background  

Loan defaults create major challenges for financial institutions, leading to losses, slower loan processing, and reduced credit availability for borrowers. This project focuses on predicting loan default risk so lenders can make **faster, fairer, and more accurate decisions** while minimizing financial losses.  

By using **machine learning models**, large volumes of borrower data can be analyzed efficiently to find hidden patterns and predict default risk with high accuracy. This supports **automated and data-driven lending decisions**, helping banks manage risk while improving operational efficiency and financial inclusion.  

---

### Why It Matters  
Accurate loan default prediction enables banks and financial institutions to **reduce financial risk**, **speed up loan approvals**, and **ensure fair lending decisions**. It improves **efficiency** by automating risk assessments, minimizes **human bias**, and provides **data-driven insights** for responsible lending practices. Ultimately, this creates a **safer, faster, and more inclusive lending system** that benefits both lenders and borrowers.  

---

### Research Questions  
1. How can lenders **accurately identify high-risk borrowers** before loan approval to minimize default rates?  
2. What **demographic, financial, and credit-related factors** play the most significant role in predicting loan defaults?  
3. Can **automated risk prediction systems** enhance loan processing speed and efficiency while ensuring **profitability and reduced risk**?  

---

## 2. Data  

- **Source:** Loan Default Dataset (Kaggle/Public Lending Datasets)  
- **Size:** ~20 MB (255,347 rows × 18 columns)  
- **Time Period:** Latest financial data (not time-bound)  
- **Each Row Represents:** A single loan application  

---

### Data Dictionary  

| Column Name       | Data Type     | Description                                 | Example Values         |
|-------------------|---------------|---------------------------------------------|-------------------------|
| LoanID            | Categorical   | Unique loan identifier                      | L001, L002, L003         |
| Age               | Numeric       | Age of borrower                             | 25, 40, 65               |
| Income            | Numeric       | Annual income of borrower                   | 50,000, 120,000          |
| LoanAmount         | Numeric       | Loan amount requested                        | 10,000, 25,000           |
| CreditScore        | Numeric       | Credit score of borrower                     | 700, 650, 780            |
| MonthsEmployed     | Numeric       | Employment duration in months               | 12, 24, 60               |
| NumCreditLines     | Numeric       | Number of existing credit lines              | 2, 5, 10                 |
| InterestRate       | Numeric       | Interest rate (%) assigned to the loan       | 8.5, 12.0, 15.5          |
| LoanTerm           | Numeric       | Loan term in months                          | 36, 60, 120              |
| DTIRatio           | Numeric       | Debt-to-Income ratio                         | 0.2, 0.5, 0.7            |
| Education          | Categorical   | Education level                              | High School, Bachelor’s   |
| EmploymentType     | Categorical   | Employment type                              | Full-time, Self-employed  |
| MaritalStatus      | Categorical   | Marital status                               | Single, Married, Divorced |
| HasMortgage        | Categorical   | Mortgage status (Yes/No)                     | Yes, No                  |
| HasDependents      | Categorical   | Dependents status (Yes/No)                   | Yes, No                  |
| LoanPurpose        | Categorical   | Purpose of loan                              | Home, Auto, Education     |
| HasCoSigner        | Categorical   | Co-signer involved (Yes/No)                  | Yes, No                  |
| Default            | Binary (0/1)  | Target variable: 1 = Default, 0 = Repaid      | 1, 0                     |

---

### Target Variable  
- **Default** (1 = Default, 0 = Repaid)  

### Predictors  
- All other variables except `LoanID`  

---

## 3. Exploratory Data Analysis (EDA)  

We will perform:  
- **Distribution Analysis:** Default vs Repaid proportions  
- **Correlation Analysis:** Between Income, CreditScore, LoanAmount, and Default  
- **Visualization:** Box plots, heatmaps, bar charts for categorical features  
- **Data Quality Checks:** Missing values, duplicates, data consistency  

---

## 4. Model Training  

- **Models to Use:**  
  - Logistic Regression → Simple baseline model for interpretability  
  - Random Forest Classifier → Handles non-linear patterns & feature importance  
  - XGBoost Classifier → High-performance boosted trees for accuracy  

- **Train-Test Split:** 80% Training, 20% Testing  
- **Tools & Libraries:** scikit-learn, XGBoost, pandas, NumPy, Matplotlib, Seaborn, Plotly  
- **Metrics:** Accuracy, Precision, Recall, F1-Score, ROC-AUC  

---

## 5. Application of Trained Models  

- Build a **Streamlit Web App**:  
  - User inputs borrower details  
  - Model predicts probability of loan default  
  - Helps loan officers make informed decisions  

---

## 6. Conclusion  

- **Expected Outcomes:**  
  - Identify key factors contributing to loan defaults  
  - Provide lenders with a **risk prediction tool** for better decision-making  
- **Limitations:**  
  - External macroeconomic factors not included  
- **Future Work:**  
  - Integrate real-time economic indicators & credit bureau data for improved accuracy  

---

## 7. References  

- Kaggle Loan Default Dataset  
- Scikit-learn Documentation  
- XGBoost Documentation  
- Streamlit Documentation  

---
