"""
Introduction to Exploratory Data Analysis (EDA)
EDA helps understand data distribution, patterns, and anomalies before applying machine learning models.
"""

import pandas as pd

# Load a sample dataset
df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/sample.csv")

# Display dataset shape
print(f"Dataset Shape: {df.shape} (Rows, Columns)\n")

# Display basic dataset info
print("Dataset Overview:")
print(df.info())

# Display first five rows
print("\nFirst five rows of the dataset:")
print(df.head())

# Display last five rows
print("\nLast five rows of the dataset:")
print(df.tail())

# Display types of each column
print("\nTypes of each column:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Summary statistics for categorical columns
print("\nCategorical Data Overview:")
print(df.describe(include=['object']))
