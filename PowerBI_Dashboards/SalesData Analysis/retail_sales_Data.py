# Re-import necessary modules after kernel reset
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define lists for categorical data
regions = ['North', 'South', 'East', 'West', 'Central']
product_categories = ['Electronics', 'Apparel', 'Home & Kitchen', 'Toys', 'Books']
subcategories = {
    'Electronics': ['Smartphone', 'Laptop', 'Tablet'],
    'Apparel': ['T-shirt', 'Jeans', 'Jacket'],
    'Home & Kitchen': ['Blender', 'Cookware', 'Vacuum Cleaner'],
    'Toys': ['Board Game', 'Doll', 'Puzzle'],
    'Books': ['Fiction', 'Non-Fiction', 'Children']
}
payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash']
shipping_methods = ['Standard', 'Express', 'Overnight']
customer_segments = ['Retail', 'Corporate', 'Wholesale']

# Generate 1000 rows
n = 1000
data = []
for i in range(n):
    category = random.choice(product_categories)
    subcategory = random.choice(subcategories[category])
    order_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(10, 1000), 2)
    total_price = round(quantity * unit_price, 2)
    discount = round(random.uniform(0, 0.3), 2)
    discounted_price = round(total_price * (1 - discount), 2)
    profit = round(discounted_price * random.uniform(0.05, 0.25), 2)

    data.append([
        f'ORD{i:05d}',
        order_date.strftime('%Y-%m-%d'),
        random.choice(regions),
        category,
        subcategory,
        f'PROD{random.randint(1000,9999)}',
        quantity,
        unit_price,
        total_price,
        discount,
        discounted_price,
        profit,
        random.choice(payment_methods),
        random.choice(shipping_methods),
        random.choice(customer_segments)
    ])

columns = [
    'OrderID', 'OrderDate', 'Region', 'Category', 'Subcategory', 'ProductID',
    'Quantity', 'UnitPrice', 'TotalPrice', 'Discount', 'DiscountedPrice',
    'Profit', 'PaymentMethod', 'ShippingMethod', 'CustomerSegment'
]

df = pd.DataFrame(data, columns=columns)

# Save to CSV
csv_path = "C:/Users/sheer/Downloads/retail_sales_data.csv"
df.to_csv(csv_path, index=False)

csv_path
