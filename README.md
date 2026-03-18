# 🏦 Bank Customer Churn Analysis (EDA Project)

## 📘 Overview
This project performs **Exploratory Data Analysis (EDA)** on the **BankChurners dataset** to understand customer behavior, identify churn patterns, and discover the main factors that drive customer retention.

It includes data cleaning, visualization, correlation analysis, and statistical testing — providing clear **business insights and managerial recommendations**.

---

## 🎯 Objectives
- Analyze how many customers are active vs churned  
- Study demographic influence (age, gender, education, marital status) on churn  
- Examine financial factors like income and credit limit  
- Explore transaction behavior and engagement level  
- Find top numerical features correlated with churn  
- Draw actionable insights for churn reduction

---

## 📊 Dataset Details
**File:** `BankChurners.csv`  
**Records:** 10,127  
**Key Columns:**
- `Attrition_Flag` → Active / Attrited Customer  
- `Customer_Age`, `Gender`, `Education_Level`, `Income_Category`  
- `Credit_Limit`, `Total_Revolving_Bal`, `Total_Trans_Ct`, `Total_Trans_Amt`  
- `Months_on_book`, `Total_Relationship_Count`, `Contacts_Count_12_mon`

---

## ⚙️ Tools & Libraries
| Category | Libraries/Tools |
|-----------|----------------|
| Language | Python |
| Data Handling | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Statistical Test | scipy.stats |
| IDE | Jupyter Notebook / VS Code / PyCharm |

---

## 🧩 Project Structure
# 🏦 Bank Customer Churn Analysis (EDA Project)

## 📘 Overview
This project performs **Exploratory Data Analysis (EDA)** on the **BankChurners dataset** to explore customer behavior, detect churn patterns, and identify key factors that influence customer retention.

The analysis includes **data cleaning, visualization, correlation analysis, and hypothesis testing** to uncover insights that can guide business decisions for improving customer retention.

---

## 🎯 Objectives
- Compare the number of active vs churned customers  
- Study the effect of age, gender, and education on churn  
- Examine how income and credit limits affect churn  
- Analyze transaction count and amount to measure engagement  
- Find which numeric features correlate most with churn  
- Generate actionable managerial insights  

---

## 📊 Dataset Details
**Dataset:** [Bank Customer Churn Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)

**Dataset:** `BankChurners.csv`  
**Records:** 10,127  
**Key Columns:**
- `Attrition_Flag` — Customer status (Active / Attrited)  
- `Customer_Age`, `Gender`, `Education_Level`, `Marital_Status`  
- `Income_Category`, `Credit_Limit`, `Total_Revolving_Bal`, `Total_Trans_Ct`  
- `Total_Trans_Amt`, `Months_on_book`, `Total_Relationship_Count`, `Contacts_Count_12_mon`

---

## ⚙️ Tools & Libraries Used
| Category | Libraries/Tools |
|-----------|----------------|
| **Programming Language** | Python |
| **Data Handling** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Statistical Testing** | scipy.stats |
| **IDE / Environment** | Jupyter Notebook / VS Code / PyCharm |

---

## 🧩 Project Structure


=============================================
# 💻 How to Push Your Project to GitHub
=============================================

Follow these steps to upload your **Bank Customer Churn Analysis** project:

---

## Step 1: Create a GitHub Account
1. Go to [GitHub](https://github.com/) and **sign up** if you don’t have an account.
2. Log in to your account.

---

## Step 2: Create a New Repository
1. Click on **+ → New Repository**.
2. Give it a name, e.g., `BANK-CUSTOMER-CHURN-ANALYSIS`.
3. Optionally, add a **description**, like:
   *Exploratory Data Analysis project on bank customer churn.*
4. Keep it **Public** or **Private**.
5. **Do not** initialize with README.
6. Click **Create Repository**.

---

## Step 3: Push Your Project from VS Code

Open **VS Code terminal** in your project folder and run:

```bash
# Initialize Git repository
git init

# Add all files
git add .

# Commit the files
git commit -m "First commit"

# Rename default branch to main
git branch -M main

# Add remote repository (replace URL with your GitHub repo URL)
git remote add origin https://github.com/your-git-handle/BANK-CUSTOMER-CHURN-ANALYSIS.git

# Push files to GitHub
git push -u origin main

