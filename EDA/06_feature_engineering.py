# Feature Engineering in EDA
# Creating new features to enhance predictive models and improve data insights.

import pandas as pd
import numpy as np  # Importing NumPy for mathematical operations

# Load dataset
df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/feature_engineered_data.csv")  # Replace with the actual file path

# Handling missing values by filling numerical columns with their median
df.fillna(df.median(numeric_only=True), inplace=True)  

# Ensure height is in meters
# If height values are in centimeters (greater than 3 meters), convert them to meters
if df["height"].max() > 3:
    df["height"] = df["height"] / 100  

# Create new features

# 1. Body Mass Index (BMI) Calculation: BMI = weight (kg) / height² (m²)
df["BMI"] = df["weight"] / (df["height"]**2)

# 2. Age Grouping: Categorizing individuals into age groups
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 30, 45, 60, 100], 
                         labels=["Teen", "Young Adult", "Adult", "Middle-Aged", "Senior"])

# 3. Weight-to-Height Ratio: Useful for analyzing body structure characteristics
df["Weight_Height_Ratio"] = df["weight"] / df["height"]

# 4. Log Transformation of Weight: Helps reduce skewness in weight distribution
df["log_weight"] = np.log(df["weight"] + 1)  # Adding 1 to avoid log(0)

# Display the first few rows of the modified dataset
print("First 5 Rows with New Features:\n", df.head())

# Save the updated dataset
df.to_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/feature_engineered_cleaned_data.csv", index=False)
print("Feature Engineering Completed! Data saved as 'feature_engineered_data.csv'.")
