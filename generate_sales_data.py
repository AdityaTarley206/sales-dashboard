import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

print("Generating 50,000+ sales records...")

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Parameters
num_records = 52000
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate Dates
date_range = (end_date - start_date).days
dates = [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(num_records)]

# Product Data
products = {
    'Laptop': {'category': 'Electronics', 'price': 1200, 'cost': 800},
    'Smartphone': {'category': 'Electronics', 'price': 800, 'cost': 500},
    'Tablet': {'category': 'Electronics', 'price': 400, 'cost': 250},
    'Headphones': {'category': 'Accessories', 'price': 150, 'cost': 80},
    'Monitor': {'category': 'Electronics', 'price': 300, 'cost': 200},
    'Keyboard': {'category': 'Accessories', 'price': 100, 'cost': 40},
    'Mouse': {'category': 'Accessories', 'price': 50, 'cost': 20},
    'Desk Chair': {'category': 'Furniture', 'price': 250, 'cost': 150},
    'Standing Desk': {'category': 'Furniture', 'price': 500, 'cost': 350}
}

product_names = list(products.keys())
selected_products = [random.choice(product_names) for _ in range(num_records)]

# Customers and Geography
regions = ['North', 'South', 'East', 'West', 'Central']
cities = {
    'North': ['New York', 'Boston', 'Philadelphia'],
    'South': ['Atlanta', 'Miami', 'Dallas'],
    'East': ['Washington DC', 'Baltimore', 'Richmond'],
    'West': ['Los Angeles', 'San Francisco', 'Seattle'],
    'Central': ['Chicago', 'Detroit', 'St. Louis']
}

customer_ids = [f'CUST-{random.randint(1000, 9999)}' for _ in range(num_records)]
selected_regions = [random.choice(regions) for _ in range(num_records)]
selected_cities = [random.choice(cities[r]) for r in selected_regions]

# Quantities and Discounts
quantities = [random.randint(1, 5) for _ in range(num_records)]
# Add some bulk orders
for i in range(0, num_records, 100):
    quantities[i] = random.randint(10, 50)

discounts = [random.choice([0, 0, 0, 0.05, 0.1, 0.15, 0.2]) for _ in range(num_records)]

# Build the DataFrame
data = []
for i in range(num_records):
    prod = selected_products[i]
    qty = quantities[i]
    discount = discounts[i]
    
    base_price = products[prod]['price']
    unit_cost = products[prod]['cost']
    
    # Introduce some random price variance (+/- 5%)
    variance = random.uniform(0.95, 1.05)
    selling_price = base_price * variance
    
    revenue = selling_price * qty * (1 - discount)
    total_cost = unit_cost * qty
    profit = revenue - total_cost
    
    data.append([
        f'ORD-{100000 + i}',
        dates[i].strftime('%Y-%m-%d'),
        customer_ids[i],
        selected_regions[i],
        selected_cities[i],
        prod,
        products[prod]['category'],
        qty,
        round(selling_price, 2),
        discount,
        round(revenue, 2),
        round(total_cost, 2),
        round(profit, 2)
    ])

df = pd.DataFrame(data, columns=[
    'OrderID', 'OrderDate', 'CustomerID', 'Region', 'City', 
    'Product', 'Category', 'Quantity', 'UnitPrice', 'Discount', 
    'Revenue', 'TotalCost', 'Profit'
])

# Sort by Date
df = df.sort_values(by='OrderDate').reset_index(drop=True)

# Save to CSV
output_path = 'sales_data.csv'
df.to_csv(output_path, index=False)

print(f"Successfully generated {len(df)} records!")
print(f"Data saved to {os.path.abspath(output_path)}")
