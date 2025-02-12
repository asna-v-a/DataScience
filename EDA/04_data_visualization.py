# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/visualization_data.csv")  # Replace with your dataset path

# Display basic dataset info
print("Dataset Overview:")
print(df.head(), "\n")
print(df.info(), "\n")
print(df.describe(), "\n")

# ---------------------- HISTOGRAM ---------------------- #
plt.figure(figsize=(8, 5))
sns.histplot(df["age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# ---------------------- SCATTER PLOT ---------------------- #
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["age"], y=df["salary"], hue=df["gender"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# ---------------------- BOX PLOT ---------------------- #
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["age"])
plt.title("Boxplot of Age")
plt.show()

# ---------------------- COUNT PLOT (CATEGORICAL) ---------------------- #
plt.figure(figsize=(8, 5))
sns.countplot(x="gender", hue="gender", data=df, palette="pastel", legend=False)  # Fixed warning
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# ---------------------- LINE PLOT (TIME SERIES) ---------------------- #
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])  # Convert to datetime format
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="date", y="sales", data=df)
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()

# ---------------------- PIE CHART ---------------------- #
plt.figure(figsize=(6, 6))
df["gender"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["lightblue", "pink"])
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# ---------------------- PAIR PLOT ---------------------- #
# Exclude non-numeric columns to avoid errors
numeric_columns = df.select_dtypes(include=["number"])
sns.pairplot(numeric_columns)  # No hue to prevent categorical issues
plt.show()

# ---------------------- CORRELATION HEATMAP ---------------------- #
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_columns.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
