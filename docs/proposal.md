# Cost of Living Analysis & Prediction  

**Prepared for:** UMBC Data Science Master Degree Capstone  
**Professor:** Dr. Chaojie (Jay) Wang  
**Author:** Reddy Sai Reddy Duggireddy  
**GitHub:** https://github.com/ReddySaiReddyDuggireddy  
**LinkedIn:** https://www.linkedin.com/in/reddy-sai-reddy-duggireddy/
---

## 1. Background  

### What is it about?  
This project aims to analyze and predict the **total cost of living** across U.S. states using regression models. The dataset covers key cost components such as **housing, food, healthcare, childcare, transportation, and taxes** for multiple family sizes and regions (metro vs rural).  

Our goal is to identify **cost drivers**, perform **regional comparisons**, and build a **predictive model** for better insights into affordability trends.  

---

### Why does it matter?  
- **Families:** Helps understand affordability before relocation or budgeting decisions.  
- **Policymakers:** Identifies high-cost regions for potential subsidies or tax relief.  
- **Researchers:** Provides data-driven insights into cost-of-living variations.  

With rising expenses across the U.S., such analysis enables **informed decision-making** for households and governments alike.  

---

## 2. Research Questions  

1. Which U.S. states and family types face the **highest cost burdens**?  
2. What **key factors** (housing, childcare, healthcare, etc.) contribute most to total living costs?  
3. Can regression models accurately **predict total cost of living** based on regional and demographic features?  
4. How do **metro vs rural areas** differ in cost-of-living patterns?  

---

## 3. Dataset  

- **Source:** U.S. Cost of Living Dataset  
- **Data Size:** 31,430 rows × 15 columns  
- **Geographic Coverage:** All 50 states + D.C.  
- **Time Period:** 2023 cross-sectional data  

### Key Features:  
- `housing_cost`  
- `food_cost`  
- `transportation_cost`  
- `healthcare_cost`  
- `childcare_cost`  
- `taxes`  
- `isMetro` (Metro vs Rural)  
- `family_member_count`  

**Target Variable:**  
- `total_cost` → Total annual cost of living for a given region & family type  

---

## 4. Methodology  

1. **Data Preprocessing:** Handle missing values, outliers, and normalization.  
2. **Feature Engineering:** Create affordability indices, regional cost ratios, and family-size adjustments.  
3. **Exploratory Data Analysis (EDA):**  
   - Regional comparisons (state-wise, metro vs rural)  
   - Cost breakdown visualizations  
4. **Regression Modeling:**  
   - **Linear Regression:** Baseline prediction  
   - **Random Forest Regressor:** Captures non-linear patterns & feature importance  
   - **Gradient Boosting Regressor:** Improves accuracy with sequential learning  
5. **Evaluation Metrics:**  
   - RMSE (Root Mean Squared Error)  
   - R² (Explained Variance)  

---

## 5. Expected Outcomes  

- A **predictive model** to estimate cost of living accurately across U.S. regions.  
- **Key insights** into major cost drivers like housing & childcare.  
- **State-wise affordability rankings** and **metro vs rural comparisons**.  
- **Interactive visualizations** for policymakers & families.  

---

## 6. References  

- U.S. Cost of Living Dataset (Kaggle / Public Data Repositories)  
- Studies on **cost-of-living indices** and **economic affordability research**  
- Machine learning techniques for **regression modeling**  
