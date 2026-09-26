import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Simulated Kenyan E-Commerce Data
np.random.seed(42)
n_rows = 10500

counties = ['Nairobi', 'Mombasa', 'Kiambu', 'Kisumu', 'Nakuru']
payments = ['M-Pesa', 'Credit Card', 'Bank Transfer']
categories = ['Electronics', 'Fashion', 'Groceries', 'Home & Living']

data = {
    'Transaction_ID': [f"TXN_{1000 + i}" for i in range(n_rows)],
    'County': np.random.choice(counties, n_rows, p=[0.50, 0.15, 0.15, 0.10, 0.10]),
    'Payment_Method': np.random.choice(payments, n_rows, p=[0.70, 0.20, 0.10]),
    'Category': np.random.choice(categories, n_rows),
    'Amount_KES': np.random.randint(500, 15000, n_rows),
    'Delivery_Status': np.random.choice(['Delivered', 'Delayed', 'Cancelled'], n_rows, p=[0.85, 0.10, 0.05])
}

df = pd.DataFrame(data)

# 2. Data Cleaning & Transformation Pipeline
df.loc[df.sample(frac=0.02).index, 'Amount_KES'] = np.nan
df['Amount_KES'] = df['Amount_KES'].fillna(df['Amount_KES'].median()) 

# 3. Aggregation: Revenue by County
county_revenue = df.groupby('County')['Amount_KES'].sum().sort_values(ascending=False)

# 4. Generate Portfolio Visualization
plt.figure(figsize=(10, 5))
county_revenue.plot(kind='bar', color='#0066cc')
plt.title('Total Revenue (KES) by Kenyan County')
plt.xlabel('County')
plt.ylabel('Total Sales (KES)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('county_revenue.png')
print("Successfully processed 10,500 rows. Portfolio visualization saved!")
