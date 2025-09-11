# Loan Default Risk Prediction 
Prepared for UMBC Data Science Master Degree Capstone by **Dr. Chaojie (Jay) Wang**  
Author: **Reddy Sai Reddy Duggireddy**  
GitHub: *https://github.com/ReddySaiReddyDuggireddy*  
LinkedIn: *https://www.linkedin.com/in/reddy-sai-reddy-duggireddy/*  

---

## 1. Background  

Loan default poses a significant financial risk to banks, credit unions, and lending institutions worldwide. When borrowers fail to repay loans, it affects not only financial institutions but also economic stability and credit accessibility for future borrowers.  

This project aims to build a **data-driven solution** to predict the likelihood of loan default before loan approval using borrower demographics, financial indicators, and loan-related details. The ultimate goal is to help lenders **minimize risk**, **optimize credit policies**, and **make fair, data-informed lending decisions**.  

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

- **Source:** Loan Default Dataset (https://www.kaggle.com/datasets/nikhil1e9/loan-default)  
- **Size:** ~20 MB (255,347 rows × 18 columns)  
- **Time Period:** Latest financial data  
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

