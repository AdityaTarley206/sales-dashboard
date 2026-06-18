# Sales Performance Dashboard

## Objective
The goal of this project was to analyze over 50,000 sales records to identify key revenue trends, profit margins, and customer purchasing behaviors, and to visualize these findings in an interactive Power BI dashboard for management decision-making.

## Methodology
1. **Data Generation:** Used Python (Pandas) to generate a realistic, 50k+ row synthetic sales dataset. This dataset mimics a real-world electronics and office supply retailer, complete with regional data, varying discounts, and realistic profit margins.
2. **SQL Analysis:** Wrote complex SQL queries to aggregate the data, find the top 5 best-selling products, calculate lifetime customer value, and evaluate the impact of discount strategies on overall profitability.
3. **Data Visualization:** Built an interactive Power BI dashboard featuring dynamic slicers, revenue/profit trend lines, and KPI cards to summarize the findings.

## Files
- `sales_data.csv`: The raw dataset generated for analysis.
- `generate_sales_data.py`: The Python script used to synthesize the dataset.
- `sales_analysis.sql`: The SQL queries used to extract insights from the data.

## Key Findings
- **Discount Strategy:** Discounts higher than 15% significantly erode profit margins without driving enough additional volume to offset the cost.
- **Top Performers:** 'Standing Desk' and 'Laptop' categories drive the highest total revenue, while accessories yield the highest percentage profit margin.
