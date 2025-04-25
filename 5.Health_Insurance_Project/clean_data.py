import pandas as pd
import numpy as np
from word2number import w2n

def parse_age(value):
    try:
        # If it's already a number, convert it
        return float(value)
    except:
        try:
            # Try converting words to numbers
            return w2n.word_to_num(str(value))
        except:
            return np.nan  # If all else fails, return NaN

# Read CSV file in Pandas
df = pd.read_csv('insurance_data.csv')

# Drop rows with no customer_id
df = df.dropna(subset = ["customer_id"])

# Change all missing name values to NULL 
df = df.fillna({'name':'NULL'})
     
# Apply conversion to age column
df['age'] = df['age'].apply(parse_age)

# Calculate BMI
df['bmi'] = (df['weight_kg'] / (df['height_m'] ** 2)).round(1)

# Standardize the 'smoker' column to lowercase strings
df['smoker'] = df['smoker'].str.lower().map({
    'yes': True, 'y': True, 'true': True,
    'no': False, 'n': False, 'false': False
})



print(df)