
# Data Analysis: Revenue and Profit Trends by Region

## Overview
This project analyzes a financial dataset spanning three years (2020-2022), focusing on revenue, profit, and profit margins across different regions and products. The goal is to identify trends, patterns, and actionable insights.

## Key Findings
1. **Revenue Trends Over Time**:
   - Total revenue exhibits seasonal fluctuations.
   - Consistent growth is observed in certain periods, but no significant spikes are apparent.

2. **Regional Comparison**:
   - Total revenue and profit are distributed relatively evenly across regions.
   - Statistical tests (ANOVA and Kruskal-Wallis) confirmed no significant differences in revenue between regions.

3. **Profit Margins**:
   - Average profit margins show slight seasonal variations but remain relatively stable.

4. **Product Insights**:
   - Revenue distribution varies significantly between products, highlighting differences in performance.

## Statistical Analysis
### Tests Performed:
- **ANOVA**: No significant difference in mean revenue across regions (\(p = 0.63\)).
- **Kruskal-Wallis**: Supported ANOVA results, indicating no significant differences in median revenue across regions (\(p = 0.62\)).

### Assumptions:
- Data normality was not satisfied (tested using Shapiro-Wilk, \(p < 0.05\)).
- Variances were homogeneous (tested using Levene’s test, \(p = 0.98\)).

## Visualizations
1. **Total Revenue by Year and Region**:
   ![Revenue by Region](images/revenue_by_year_region.png)

2. **Revenue Distribution by Product**:
   ![Revenue by Product](images/revenue_by_product.png)

3. **Profit Margin Trends Over Time**:
   ![Profit Margin Trends](images/profit_margin_trends.png)

4. **Total Profit by Region**:
   ![Profit by Region](images/profit_by_region.png)

## Next Steps
- Extend the dataset to include more granular details, such as customer demographics or marketing campaigns.
- Investigate product-specific performance trends further to identify growth opportunities.

## How to Use
- The dataset (`financial_dashboard_data_extended.csv`) is included in the `data/` folder.
- Jupyter Notebook with the analysis code is available in the `notebooks/` folder.

## Dataset
The dataset includes:
- **Date**: Transaction date.
- **Region**: Geographic region (North, South, East, West).
- **Product**: Product categories (A, B, C, D).
- **Revenue**: Total revenue per transaction.
- **Cost**: Cost of goods sold per transaction.
- **Profit**: Revenue minus cost.
- **Profit Margin**: Profit as a percentage of revenue.

## Tools and Libraries
- **Python**: Pandas, Matplotlib, Seaborn, Scipy.
- **Tableau**: For interactive dashboards.

## Repository Structure
- `data/`: Contains the dataset used in this analysis.
- `notebooks/`: Jupyter notebooks with the analysis code.
- `images/`: Visualizations generated from the analysis.

---
**Disclaimer**: The data is synthetic and used for demonstration purposes only.
