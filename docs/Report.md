# Loan Default Risk Prediction  

**Prepared for:** UMBC Data Science Master Degree Capstone by **Dr. Chaojie (Jay) Wang**  
**Author:** **Reddy Sai Reddy Duggireddy**  
**GitHub:** *https://github.com/ReddySaiReddyDuggireddy*  
**LinkedIn:** *https://www.linkedin.com/in/reddy-sai-reddy-duggireddy/*  
**PowerPoint Presentation:** *https://github.com/ReddySaiReddyDuggireddy/UMBC-DATA606-Capstone/blob/main/docs/Data606_CapstonePresentations1.pptx*  
**YouTube Video:** *https://youtu.be/TucyWCtsC4Y*

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

## **5. Model Training**

Three machine learning models were used to train and test the **Loan Default Prediction** dataset:

* **Random Forest Classifier:** An ensemble learning model that builds multiple decision trees and averages their results to improve accuracy and reduce overfitting.  
* **Decision Tree Classifier:** A simple and interpretable model that splits data based on key variables to predict default or repayment outcomes.  
* **XGBoost Classifier:** A gradient boosting algorithm known for its efficiency, regularization, and ability to handle complex feature relationships.

### **Training Process**

* The dataset was divided into **training (80%)** and **testing (20%)** sets using the `train_test_split()` method.   
* Numerical features were **scaled** and categorical features were **encoded** using **Pipelines** to streamline preprocessing.  
* **Hyperparameter tuning** was performed using `GridSearchCV` to find the best-performing parameters for each model.  
* Libraries used included `scikit-learn`, `xgboost` for model development and evaluation.  
* The development and testing were carried out in **Jupyter Notebook** on a **macOS environment**.

### **Model Evaluation**

* Models were evaluated using key metrics such as  **Precision**, **Recall**, and **F1-score**.  
* **Confusion matrices** and **classification reports** were generated to assess prediction performance.  
* Feature importance scores helped identify which engineered features most strongly influenced loan default prediction.  
* Among the models tested, **XGBoost** provided the best trade-off between recall and precision, followed by **Random Forest** and **Decision Tree**.

---

## **6. Application of the Trained Model**

A **Streamlit web application** was developed to make the trained model interactive and user-friendly.  
The app allows users to input loan-related details — including **demographic, financial, and engineered features** — and instantly receive predictions about whether a loan is likely to be **repaid or defaulted**.

### **Key Features:**
* Real-time loan default prediction using the trained XGBoost model.  
* Clean form-based interface for entering applicant details.  
* Automatic calculation of engineered financial metrics such as:  
  - `Loan_to_Income_Ratio`  
  - `Debt_Service_Ratio`  
  - `FinancialStress`  
  - `EmploymentStability`  
  - `CombinedIncome`  
* Instant output message displaying the loan prediction result (Defaulted or Repaid).  

---

## **7. Conclusion**

This project demonstrates the use of **machine learning algorithms** to predict loan default risk based on borrower and financial attributes.  
By applying **feature engineering**, **scaling**, and **model tuning**, predictive accuracy and interpretability were improved without requiring data resampling methods.

### **Key Insights:**
* The **XGBoost model** outperformed other models in terms of precision and recall balance.  
* **Feature engineering** (e.g., Loan-to-Income Ratio, Debt Service Ratio, Credit Exposure Ratio) played a key role in enhancing model understanding.  
* Ensemble models like **Random Forest** proved effective at reducing overfitting and capturing complex relationships.  

### **Limitations:**
* Class imbalance slightly affected recall for minority cases (loan defaults).  
* Some engineered features relied on assumptions (e.g., co-signer income impact).  
* Results depend on dataset quality and may vary for different institutions or markets.

### **Future Work:**
* Incorporate **additional data sources** (e.g., credit utilization, payment history) for improved accuracy.   
* Deploy the Streamlit app with continuous model updates using live financial data.  


