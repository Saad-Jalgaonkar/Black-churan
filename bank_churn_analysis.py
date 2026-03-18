# ======================================================
#                 BANK CUSTOMER CHURN ANALYSIS
# ======================================================

# -----------------------------
# Import Required Libraries
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("BankChurners.csv")
df = pd.DataFrame(data)

# =====================================================
#               EXPLORATORY DATA ANALYSIS (EDA)
# =====================================================
# print(df.head())
# print(df.columns)
# print(df.dtypes)
# print(df.isnull().sum())
# print(df.describe())
# print(df.duplicated().sum())

# =====================================================
#                  DATA CLEANING
# Note: The dataset is mostly clean; we’ll just drop
# irrelevant columns for a cleaner analysis.
# =====================================================
df.drop(
    columns=[
        "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
        "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2",
    ],
    inplace=True,
)

# =====================================================
#                  OUTLIER DETECTION
# =====================================================
plt.figure(figsize=(12, 8))
sns.boxplot(df)
plt.title("Outlier Detection")
plt.xticks(fontsize=5, fontweight="bold")
plt.tight_layout()
# plt.save("Outlier Detection.png",dpi=300)
plt.show()

# =====================================================
#                  DATA VISUALIZATION
# =====================================================

# -----------------------------
# CUSTOMER OVERVIEW
# -----------------------------

# Q1. How many customers are active vs churned?
active_churn_counts = df["Attrition_Flag"].value_counts().reset_index()
sns.countplot(x="Attrition_Flag", data=df, hue="Attrition_Flag", palette="Accent", width=0.4)
plt.legend(labels=["Active", "Churned"])
plt.xlabel("Attrition Flag")
plt.title("Number of Active and Churned Customers")
# plt.savefig("Active_vs_churned_count.png", dpi=300)
plt.show()

# Q2. What is the overall churn percentage?
plt.pie(
    active_churn_counts["count"],
    labels=active_churn_counts["Attrition_Flag"],
    autopct="%1.1f%%",
    startangle=180,
    explode=[0, 0.2],
    wedgeprops={"edgecolor": "black", "linewidth": 1.5},
)
plt.title("Overall Churn Percentage")
plt.legend()
# plt.savefig("Overall_Churn_Percentage.png", dpi=300)
plt.show()

# -----------------------------
# DEMOGRAPHIC ANALYSIS
# -----------------------------

# Q3. Does age group influence customer attrition?
bins = [0, 30, 50, 100]
labels = ["Young (0-30)", "Middle (31-50)", "Senior (51+)"]
df["Age_Group"] = pd.cut(df["Customer_Age"], bins=bins, labels=labels)

sns.countplot(x="Age_Group", data=df, hue="Attrition_Flag")
plt.title("Customer Attrition by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")
# plt.savefig("Customer_attr_by_age.png", dpi=300)
plt.show()

# Q4. Is there any gender difference in churn behavior?
sns.countplot(x="Gender", data=df, hue="Attrition_Flag", width=0.3, palette="Set2")
plt.title("Gender vs Customer Attrition", fontsize=13)
plt.xlabel("Gender")
plt.ylabel("Count")
# plt.savefig("gen_vs_cust_attrition.png", dpi=300)
plt.show()

# Q5. Which education or marital status group has the highest churn rate?
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
sns.countplot(x="Education_Level", hue="Attrition_Flag", data=df, ax=ax[0], palette="Set2")
ax[0].set_title("Churn by Education Level")
sns.countplot(x="Marital_Status", hue="Attrition_Flag", data=df, ax=ax[1], palette="Set2")
ax[1].set_title("Churn by Marital Status")
plt.tight_layout()
# plt.savefig("edu_marital_vs_churn_subplot.png", dpi=300)
plt.show()

# -----------------------------
# FINANCIAL BEHAVIOR
# -----------------------------

# Q6. How does income category relate to churn?
df["Income_Category"] = (
    df["Income_Category"]
    .str.replace(" - ", "–")
    .str.replace("-", "–")
    .str.strip()
)
order = ["Less than $40K", "$40K–$60K", "$60K–$80K", "$80K–$120K", "$120K +", "Unknown"]

sns.countplot(
    x="Income_Category",
    data=df,
    hue="Attrition_Flag",
    order=order,
    palette="pastel",
    edgecolor="black",
)
plt.xlabel("Income Category")
plt.title("Income Category vs Churn")
# plt.savefig("Income_category_relate_churn.png", dpi=300)
plt.show()

# Q7. Do customers with higher credit limits churn less?
sns.boxplot(x="Attrition_Flag", y="Credit_Limit", data=df, palette="Set2")
plt.title("Credit Limit vs Customer Churn")
plt.xlabel("Attrition Flag")
plt.ylabel("Credit Limit")
# plt.savefig("Credit_Lmt_vs_Cust_Churn.png", dpi=300)
plt.show()

# Conducting T-test
existing = df[df["Attrition_Flag"] == "Existing Customer"]["Credit_Limit"]
attrited = df[df["Attrition_Flag"] == "Attrited Customer"]["Credit_Limit"]

t_stat, p_value = ttest_ind(existing, attrited, equal_var=False)

if p_value < 0.05:
    print(f"T-statistic: {t_stat:.3f}")
    print(f"P-value: {p_value:.4f}")
    print("Since P-value < 0.05, the difference in average Credit Limit between Existing and Attrited customers is statistically significant.")
    print("This means customers with higher credit limits are significantly less likely to churn.")
else:
    print(f"T-statistic: {t_stat:.3f}")
    print(f"P-value: {p_value:.4f}")
    print("Since P-value >= 0.05, there is no statistically significant difference in average Credit Limit between the two groups.")

# Q8. Is there a relationship between Total Revolving Balance and churn?
sns.boxplot(x="Attrition_Flag", y="Total_Revolving_Bal", data=df, hue="Attrition_Flag", palette="Set2")
plt.title("Total Revolving Balance vs Customer Churn")
plt.xlabel("Attrition Flag")
plt.ylabel("Total Revolving Balance")
# plt.savefig("rel_total_revolving_bal_and_churn.png", dpi=300)
plt.show()

# -----------------------------
# CARD & USAGE PATTERNS
# -----------------------------

# Q9. Which card category has the highest churn rate?
churn_rate = (
    df.groupby("Card_Category")["Attrition_Flag"]
    .apply(lambda x: (x == "Attrited Customer").mean() * 100)
    .reset_index(name="Churn_Rate")
)
sns.barplot(x="Card_Category", y="Churn_Rate", data=churn_rate, hue="Card_Category", palette="Set2", width=0.4)
plt.title("Churn Rate by Card Category (%)")
plt.xlabel("Card Category")
plt.ylabel("Churn Rate (%)")
# plt.savefig("Churn_Rate_by_Card_Category.png", dpi=300)
plt.show()

# Q10. Do customers with fewer total transactions tend to leave more?
sns.boxplot(x="Attrition_Flag", y="Total_Trans_Ct", data=df, hue="Attrition_Flag", palette="Accent")
plt.title("Do Customers with Fewer Transactions Churn More?")
plt.xlabel("Attrition Flag")
plt.ylabel("Total Transaction Count")
# plt.savefig("total_transactions_churn.png", dpi=300)
plt.show()

# Q11. What is the relation between Total Transaction Amount and churn?
sns.boxplot(x="Attrition_Flag", y="Total_Trans_Amt", data=df, palette="Accent")
plt.title("Impact of Total Transaction Amount on Customer Churn")
plt.xlabel("Attrition Flag")
plt.ylabel("Total Transaction Amount")
# plt.savefig("total_trans_amt_churn.png", dpi=300)
plt.show()

# -----------------------------
# CORRELATION ANALYSIS
# -----------------------------

# Q12. Which numerical variables are most correlated with churn?
df.drop(columns=["CLIENTNUM"], inplace=True)
df["Attrition_Flag"] = df["Attrition_Flag"].map({"Attrited Customer": 0, "Existing Customer": 1})

numeric_df = df.select_dtypes(include=["number"])
plt.figure(figsize=(6, 5))
sns.heatmap(
    numeric_df.corr()[["Attrition_Flag"]].sort_values(by="Attrition_Flag", ascending=False),
    annot=True, cmap="coolwarm", fmt=".2f"
)
plt.title("Features Most Correlated with Customer Churn")
plt.xlabel("Attrition Flag")
plt.tight_layout()
# plt.savefig("correlation_with_churn.png")
plt.show()

# Q13. Any noticeable relationship between Total Relationship Count, Months on Book, and churn?
rel_df = df[["Attrition_Flag", "Total_Relationship_Count", "Months_on_book"]]
sns.heatmap(
    rel_df.corr()[["Attrition_Flag"]].sort_values(by="Attrition_Flag", ascending=False),
    annot=True, cmap="coolwarm", fmt=".2f"
)
plt.title("Correlation Between Customer Tenure, Relationship Count, and Churn")
plt.savefig("correlation_btw_total_rel_count_months_on_book_and_churn.png")
plt.show()

print("✅ EDA Completed Successfully!")
