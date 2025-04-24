# 🏥 Health Insurance Data Analysis (Germany)

This project analyzes a synthetic dataset of health insurance policyholders in Germany. It demonstrates key skills in **data wrangling**, **visualization**, and **cost trend analysis** — relevant to roles in healthcare, finance, and data science.

---

## 📌 Project Objectives

- Explore how personal and lifestyle factors affect annual health insurance charges.
- Visualize relationships between features like age, BMI, smoking status, and charges.
- (Optional) Build a simple predictive model using linear regression.

---

## 📂 Dataset Overview

The dataset `health_insurance_data.csv` includes 1,000 policyholders with the following fields:

| Column     | Description                          |
|------------|--------------------------------------|
| age        | Age of the insured person (18–65)    |
| gender     | Gender (male/female)                 |
| bmi        | Body Mass Index                      |
| children   | Number of children covered           |
| smoker     | Smoker status (yes/no)               |
| region     | Region in Germany                    |
| charges    | Annual insurance cost in euros (€)   |

---

## 🔍 Analysis Highlights

- **Smokers** pay significantly higher premiums than non-smokers.
- Higher **BMI** and **age** are correlated with higher charges.
- Certain regions show slightly elevated average costs.
- Boxplots and scatterplots reveal strong distribution patterns.

---

## 📊 Visualizations

- 📦 Boxplot: Charges by smoker status
- 📉 Scatterplot: BMI vs. Charges
- 📊 Bar chart: Average charges by region

---

## 🤖 Bonus: Predictive Modeling

A simple **Linear Regression** model is built using:
- Features: Age, BMI, Children, Smoker
- Output: Predicted Charges (€)
- Evaluation: R² score on test set

---

## 🛠️ Tools Used

- Python 3
- pandas
- matplotlib / seaborn
- scikit-learn (optional model)
- Jupyter Notebook

---

## 🧑‍💻 Author

**Sherry Dhingra**  
📍 Stuttgart, Germany  
🔗 [LinkedIn](https://www.linkedin.com/in/sherry-dhingra)  
📬 sherrydhingra2022@gmail.com

---

📁 *Project folder:* `Python_Projects/health_insurance_analysis/`
