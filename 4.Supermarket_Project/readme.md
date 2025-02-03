# Supermarket Data Cleaning Project

## Overview

This project was aimed at cleaning and preparing a messy supermarket dataset to ensure it was consistent and ready for analysis. The dataset contained information about various products, including their names, prices, quantities, and categories. The primary goal was to clean up the data by handling inconsistencies, removing unnecessary characters, and dealing with missing or incorrect values.

## Objectives

1. **Clean product names**: Ensure all product names follow a consistent format with proper capitalization and no extra spaces.
2. **Standardize prices**: Remove any unwanted characters (like `$` symbols) and ensure all prices are in numeric format.
3. **Fix quantity values**: Handle missing or incorrect quantity values.
4. **Handle missing values**: Replace or correct missing data (such as missing prices or quantities).
5. **Standardize categories**: Clean up the product category names to ensure consistency.

## Data Issues Encountered

- **Inconsistent column names**: The dataset had column names with extra spaces, making them inconsistent for processing.
- **Irregular price formatting**: Prices included special characters like `$` and spaces, which could interfere with analysis.
- **Empty and missing values**: Some rows had missing or blank entries, particularly for the `Price` and `Quantity` columns.
- **Inconsistent product names**: Product names had variations in capitalization and unnecessary whitespace.
- **Inconsistent categories**: Some categories were not consistently formatted (e.g., `"fruit"` vs. `"Fruit"`).

## Commands Used

### 1. **Standardizing column names**
```python
df.columns = df.columns.str.strip().str.replace(' ', '_')
```
- Removed any leading or trailing spaces from column names.
- Replaced spaces with underscores to make column names more consistent and easier to access.

### 2. **Cleaning product names**
```python
df['Product_Name'] = df['Product_Name'].str.strip().str.title()
```
- Removed leading and trailing spaces from the `Product_Name` column.
- Ensured all product names are capitalized consistently.

### 3. **Cleaning prices and converting to numeric**
```python
df['Price'] = df['Price'].str.replace(r'[^0-9.]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
```
- Removed any non-numeric characters from the `Price` column (e.g., `$`, spaces).
- Converted the `Price` column to a numeric format, handling any invalid or missing values with `NaN`.

### 4. **Handling missing or invalid quantity values**
```python
df['Quantity'] = df['Quantity'].astype(str).str.strip()
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0).astype(int)
```
- Stripped whitespace from `Quantity` values and handled any invalid or missing values by filling them with `0`.
- Converted the `Quantity` column to an integer type.

### 5. **Standardizing categories**
```python
df['Category'] = df['Category'].str.strip().str.title()
```
- Trimmed any extra spaces in the `Category` column.
- Capitalized the first letter of each word to ensure consistency across category names.

## Issues Encountered

- **Missing values**: Many rows had missing values for the `Price` or `Quantity` columns. I handled these by using `pd.to_numeric` with the `errors='coerce'` option, which converts invalid entries to `NaN`, and then filled missing values with `0` where necessary.

- **Irregular date formats**: Originally, the dataset had a `Date_Purchased` column with inconsistent date formats. After removing this column and replacing it with a `Category` column, date-related issues were no longer a concern.

- **Inconsistent formatting**: Some product names and categories had different capitalization, extra spaces, or special characters. I used string operations (`str.strip()`, `str.title()`) to clean up these inconsistencies.

## Outcome

After cleaning the dataset, I now have a consistent and well-formatted supermarket product catalog. The final dataset is free of inconsistent data, malformed entries, and unnecessary characters. The cleaned dataset is now ready for further analysis or use in any data processing pipeline.

### Cleaned Dataset Columns:

- **ID**: Unique identifier for each product.
- **Product_Name**: Name of the product, properly capitalized and formatted.
- **Price**: Price of the product, in numeric format (with any special characters removed).
- **Quantity**: Quantity of the product, converted to integers with missing values filled as `0`.
- **Category**: The category of the product, consistently formatted.

This cleaned dataset is now ready for analysis, reporting, or any other downstream tasks.
