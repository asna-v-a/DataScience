# Dimensionality Reduction in EDA
# Reducing the complexity of datasets using PCA.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/data.csv")

# Select only numeric columns
df_numeric = df.select_dtypes(include=["number"])

# Handle missing values (Fill with median of numeric columns)
df_numeric = df_numeric.fillna(df_numeric.median(numeric_only=True))

# Standardize data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_numeric)

# Apply PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

# Print explained variance
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Convert PCA results to DataFrame
pca_df = pd.DataFrame(data=pca_result, columns=["PC1", "PC2"])

# Scatter plot to visualize PCA results
plt.figure(figsize=(8,6))
plt.scatter(pca_df["PC1"], pca_df["PC2"], alpha=0.5, c="blue")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Dimensionality Reduction")
plt.show()

