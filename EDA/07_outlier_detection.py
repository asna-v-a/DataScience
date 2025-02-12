# Outlier Detection in EDA
# Identifying and handling outliers using boxplots and the Z-score method.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/data.csv")

# Handling missing values (important before Z-score computation)
df["salary"].fillna(df["salary"].median(), inplace=True)  

# Z-score method for detecting outliers
df["Z_Score"] = (df["salary"] - df["salary"].mean()) / df["salary"].std()
outliers = df[df["Z_Score"].abs() > 3]  # Identifies values beyond 3 standard deviations

# Display detected outliers
print("Outliers:\n", outliers)

# Boxplot visualization
plt.figure(figsize=(8, 4))
sns.boxplot(x=df["salary"])
plt.title("Boxplot of Salary (Outlier Detection)")
plt.show()

# Drop the temporary Z-score column after analysis
df.drop(columns=["Z_Score"], inplace=True)
