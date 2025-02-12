import pandas as pd

df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/data.csv")  # Update the path as needed

# ---------------------- DISPLAY INITIAL DATA INSIGHTS ---------------------- #
print("🔹 First 5 Rows:\n", df.head())  # View first few rows
print("\n🔹 Last 5 Rows:\n", df.tail())  # View last few rows
print("\n🔹 Dataset Shape (Rows, Columns):", df.shape)  # Number of rows & columns
print("\n🔹 Data Types:\n", df.dtypes)  # Check column data types

# ---------------------- CHECK & HANDLE MISSING VALUES ---------------------- #
print("\n🔹 Missing Values Before Cleaning:\n", df.isnull().sum())

# Fill missing numerical values with column mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill missing categorical values with the mode (most frequent value)
for col in df.select_dtypes(include=["object"]).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# ---------------------- REMOVE DUPLICATES ---------------------- #
df.drop_duplicates(inplace=True)

# ---------------------- CONVERT DATA TYPES ---------------------- #
if "date" in df.columns:  # Check if 'date' column exists
    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)  # Convert to datetime format

# ---------------------- DISPLAY CLEANED DATA INFO ---------------------- #
print("\n🔹 Cleaned Data Overview:\n", df.info())

df.to_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/cleaned_data.csv", index=False)