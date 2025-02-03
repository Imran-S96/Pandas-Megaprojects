import pandas as pd

df = pd.read_csv('supermarket.csv')

# 1. Trim whitespace and standardize column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

# 2. Clean up 'Product_Name' and fix capitalization
df['Product_Name'] = df['Product_Name'].str.strip().str.title()


# 3. Remove special characters, handle empty strings with None, and convert 'Price' to numeric
df['Price'] = df['Price'].str.replace(r'[^0-9.]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Strip whitespace in 'Quantity', convert to numeric, and fill missing values
df['Quantity'] = df['Quantity'].astype(str).str.strip()  # Remove spaces
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0).astype(int)

# 5. Standardize 'Category' names (e.g., capitalize first letters)
df['Category'] = df['Category'].str.strip().str.title()

print(df.to_string())

df.to_csv('cleaned_supermarket.csv', index=False)

