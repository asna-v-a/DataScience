# Correlation Analysis in EDA
# Understanding relationships between numerical variables using heatmaps.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/data.csv")

# Select only numerical columns for correlation
df_numeric = df.select_dtypes(include=["number"])

# Handle missing values by filling with the median
df_numeric.fillna(df_numeric.median(), inplace=True)

# Compute correlation matrix
corr_matrix = df_numeric.corr()

# Heatmap visualization
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Matrix")
plt.show()
