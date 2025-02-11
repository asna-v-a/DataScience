import numpy as np
import pandas as pd

# Load dataset
missing_data_file = "C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/missing_data.csv"
heart_data_file = "C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/heart.csv"
df = pd.read_csv(missing_data_file)

# 1. Find Total Number of Missing Values
print("Original Data:")
print(df)
print("\nData Types:")
print(df.dtypes)
print("\nTotal Missing Values in Each Column:")
print(df.isna().sum())
print("*" * 53)

# 2. Fill Missing Values Using Mean, Median, and Mode
print("\nFilling Missing Values...")
df.fillna(350, inplace=True)  # Replace NaN with 350
df['Calories'].fillna(df['Calories'].mean(), inplace=True)
df['Date'].fillna(df['Date'].mode()[0], inplace=True)
print(df)

# 3. Drop Missing Values
df = pd.read_csv(missing_data_file)
df.dropna(inplace=True, ignore_index=True)
df.dropna(subset=['Calories'], inplace=True, ignore_index=True)
df.dropna(subset=['Date'], inplace=True, ignore_index=True)
print("\nData After Dropping Missing Values:")
print(df)

# 4. Handling Wrong Format Data
print("\nHandling Wrong Format Data...")
df.loc[7, 'Duration'] = df['Duration'].mode()[0]
print(df)

# 5. Handle Wrong Data/Outliers
print("\nHandling Outliers...")
calories_mean = df['Calories'].mean()
for i in df.index:
    if df.loc[i, 'Calories'] > 400:
        df.loc[i, 'Calories'] = calories_mean
print(df)

# Handling incorrect thalach values in heart dataset
df_heart = pd.read_csv(heart_data_file)
thalach_mean = df_heart['thalach'].mean()
for i in df_heart.index:
    if df_heart.loc[i, 'thalach'] > 180:
        df_heart.loc[i, 'thalach'] = thalach_mean
print("\nHeart Dataset After Handling Thalach Outliers:")
print(df_heart)

# Save cleaned data
df.to_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/missing_data_cleaned.csv", index=False)
df_heart.to_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/heart_cleaned.csv", index=False)
print("\nData cleaning complete. Cleaned files saved.")
