-- =======================================================================
-- Project 1: Sales Performance Analysis
-- Description: SQL queries to analyze revenue trends, customer purchasing
--              behavior, and product performance.
-- Database: Designed for standard SQL (PostgreSQL, SQL Server, SQLite)
-- =======================================================================

-- 1. Total Revenue, Profit, and Order Count
SELECT 
    COUNT(DISTINCT OrderID) AS TotalOrders,
    ROUND(SUM(Revenue), 2) AS TotalRevenue,
    ROUND(SUM(Profit), 2) AS TotalProfit,
    ROUND(SUM(Profit) / SUM(Revenue) * 100, 2) AS ProfitMarginPercentage
FROM sales_data;

-- 2. Revenue Trends Over Time (Monthly)
SELECT 
    SUBSTR(OrderDate, 1, 7) AS Month,
    ROUND(SUM(Revenue), 2) AS MonthlyRevenue,
    ROUND(SUM(Profit), 2) AS MonthlyProfit,
    COUNT(OrderID) AS OrdersCount
FROM sales_data
GROUP BY SUBSTR(OrderDate, 1, 7)
ORDER BY Month ASC;

-- 3. Top 5 Best-Selling Products by Revenue
SELECT 
    Product,
    Category,
    SUM(Quantity) AS TotalUnitsSold,
    ROUND(SUM(Revenue), 2) AS TotalRevenue
FROM sales_data
GROUP BY Product, Category
ORDER BY TotalRevenue DESC
LIMIT 5;

-- 4. Customer Purchasing Behavior (Top 10 Customers by Lifetime Value)
SELECT 
    CustomerID,
    COUNT(OrderID) AS NumberOfOrders,
    ROUND(SUM(Revenue), 2) AS LifetimeValue,
    ROUND(AVG(Revenue), 2) AS AverageOrderValue
FROM sales_data
GROUP BY CustomerID
ORDER BY LifetimeValue DESC
LIMIT 10;

-- 5. Regional Performance Analysis
SELECT 
    Region,
    ROUND(SUM(Revenue), 2) AS RegionalRevenue,
    ROUND(SUM(Profit), 2) AS RegionalProfit,
    ROUND(SUM(Profit) / SUM(Revenue) * 100, 2) AS RegionalProfitMargin
FROM sales_data
GROUP BY Region
ORDER BY RegionalRevenue DESC;

-- 6. Discount Impact on Profitability
SELECT 
    Discount,
    COUNT(OrderID) AS TotalOrders,
    SUM(Quantity) AS TotalUnitsSold,
    ROUND(SUM(Revenue), 2) AS TotalRevenue,
    ROUND(SUM(Profit), 2) AS TotalProfit,
    ROUND(SUM(Profit) / SUM(Revenue) * 100, 2) AS ProfitMargin
FROM sales_data
GROUP BY Discount
ORDER BY Discount ASC;
