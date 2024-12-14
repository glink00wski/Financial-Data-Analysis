import pandas as pd
import numpy as np
from faker import Faker
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, shapiro, levene

# Initialize Faker for realistic data
fake = Faker()

# Parameters for the dataset
n_records = 500
regions = ["North", "South", "East", "West"]
products = ["Product A", "Product B", "Product C", "Product D"]

# Generate data
np.random.seed(42)
data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-12-31", periods=n_records),
    "Region": np.random.choice(regions, size=n_records),
    "Product": np.random.choice(products, size=n_records),
    "Revenue": np.random.uniform(500, 5000, size=n_records).round(2),
    "Cost": np.random.uniform(300, 4000, size=n_records).round(2),
    "Salesperson": [fake.name() for _ in range(n_records)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate Profit and Profit Margin
df["Profit"] = (df["Revenue"] - df["Cost"]).round(2)
df["Profit Margin (%)"] = ((df["Profit"] / df["Revenue"]) * 100).round(2)

# Save dataset
file_path = "C:\\Users\\grzeg\\OneDrive\\Pulpit\\GitHub - project\\Financial Data Analysis\\financial_dashboard_data.csv"
df.to_csv(file_path, index=False)



# Extend dataset to multiple years for deeper analysis
n_years = 3  # Generate data for 3 years
n_records_per_year = 500

all_data = []
for year in range(2020, 2020 + n_years):
    np.random.seed(year)  # For reproducibility
    year_data = {
        "Date": pd.date_range(start=f"{year}-01-01", end=f"{year}-12-31", periods=n_records_per_year),
        "Region": np.random.choice(regions, size=n_records_per_year),
        "Product": np.random.choice(products, size=n_records_per_year),
        "Revenue": np.random.uniform(500, 5000, size=n_records_per_year).round(2),
        "Cost": np.random.uniform(300, 4000, size=n_records_per_year).round(2),
        "Salesperson": [fake.name() for _ in range(n_records_per_year)]
    }
    df_year = pd.DataFrame(year_data)
    df_year["Profit"] = (df_year["Revenue"] - df_year["Cost"]).round(2)
    df_year["Profit Margin (%)"] = ((df_year["Profit"] / df_year["Revenue"]) * 100).round(2)
    all_data.append(df_year)

# Combine all years into one dataset
df_extended = pd.concat(all_data, ignore_index=True)

# Save the extended dataset for use
file_path_extended = "C:\\Users\\grzeg\\OneDrive\\Pulpit\\GitHub - project\\Financial Data Analysis\\financial_dashboard_data_extended.csv"
df_extended.to_csv(file_path_extended, index=False)

# Summary of dataset for analysis
df_extended.head(), df_extended.info(), file_path_extended

# Configure matplotlib for better visuals
plt.rcParams.update({
    "figure.figsize": (10, 6),
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
})

# 1. Revenue trends over time
df_extended["YearMonth"] = df_extended["Date"].dt.to_period("M")
revenue_trends = df_extended.groupby("YearMonth")["Revenue"].sum()

plt.plot(revenue_trends.index.astype(str), revenue_trends.values)
plt.title("Total Revenue Over Time")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# 2. Average Revenue by Region
avg_revenue_region = df_extended.groupby("Region")["Revenue"].mean().sort_values()

sns.barplot(x=avg_revenue_region.index, y=avg_revenue_region.values)
plt.title("Average Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Average Revenue")
plt.grid(axis="y", alpha=0.5)
plt.tight_layout()
plt.show()

# 3. Heatmap of correlations
corr_matrix = df_extended[["Revenue", "Cost", "Profit", "Profit Margin (%)"]].corr()

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 4. Boxplot of Revenue by Region
sns.boxplot(data=df_extended, x="Region", y="Revenue")
plt.title("Distribution of Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.grid(axis="y", alpha=0.5)
plt.tight_layout()
plt.show()


# Recreate the 'YearMonth' column for time-based grouping
df_extended["YearMonth"] = df_extended["Date"].dt.to_period("M")

# 5. Profit Margin Trends Over Time
profit_margin_trends = df_extended.groupby("YearMonth")["Profit Margin (%)"].mean()

plt.figure(figsize=(12, 6))
plt.plot(profit_margin_trends.index.astype(str), profit_margin_trends.values, marker="o")
plt.title("Average Profit Margin Over Time")
plt.xlabel("Month")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=45)
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# Total Profit by Region (re-run to confirm data)
total_profit_region = df_extended.groupby("Region")["Profit"].sum()

sns.barplot(x=total_profit_region.index, y=total_profit_region.values, palette="viridis")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.grid(axis="y", alpha=0.5)
plt.tight_layout()
plt.show()




# Test Anova to check if the means revenues in all the regions are equal, H0 - all mean revenues are equal in the regions

# Group the data by region
groups = [df_extended.loc[df_extended["Region"] == region, "Revenue"] for region in df_extended["Region"].unique()]

# 1. Shapiro-Wilk test to test normality for each group
normality_results = {region: shapiro(data) for region, data in zip(df_extended["Region"].unique(), groups)}

# 2. Levene's test to assess the equality of variances in the groups
levene_result = levene(*groups)

# 3. Test ANOVA
anova_result = f_oneway(*groups)

normality_results # p_value < 0.05 indicates that data does not have normal distribution in groups, therefore one of the assumptions to the Anova test is not met but we can continue but being carefull
levene_result # p_value > 0.05 indicates that variances in groups are equal
anova_result # P_value > 0.05 there are no diffrences in the mean revenues in the groups

