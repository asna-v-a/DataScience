import pandas as pd
import numpy as np
import scipy.stats as stats

np.random.seed(42)  # For reproducibility

# Generate sample data
data = {
    "age": np.random.randint(18, 60, 100),
    "height": np.random.uniform(150, 200, 100),
    "weight": np.random.uniform(50, 100, 100),
    "group_A": np.random.normal(70, 10, 100),
    "group_B": np.random.normal(75, 12, 100),
    "gender": np.random.choice(["Male", "Female"], 100),
    "category": np.random.choice(["A", "B", "C"], 100)
}

# Convert into a DataFrame
df = pd.DataFrame(data)

# Introduce some missing values randomly
df.loc[np.random.choice(df.index, 5), "age"] = np.nan
df.loc[np.random.choice(df.index, 3), "gender"] = np.nan

# Save dataset to CSV (optional)
df.to_csv("data.csv", index=False)

df = pd.read_csv("data.csv")  # Load dataset from file

print("🔹 Dataset Overview:")
print(df.head(), "\n")  # Display first few rows
print(df.info(), "\n")  # Check data types and missing values
print("Missing Values:\n", df.isnull().sum(), "\n")  # Check missing values

# ---------------------- HANDLING MISSING DATA ---------------------- #
# Fill missing numerical values with the median
df.fillna(df.median(numeric_only=True), inplace=True)

# Fill missing categorical values with the mode
for col in df.select_dtypes(include=["object"]).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("✅ Missing values handled using median (numeric) & mode (categorical).\n")

# ---------------------- DESCRIPTIVE STATISTICS ---------------------- #
print("🔹 Descriptive Statistics:")
print(df.describe(), "\n")  # Mean, median, std deviation, min, max, etc.

# ---------------------- NORMALITY CHECK (SHAPIRO-WILK TEST) ---------------------- #
if "age" in df.columns and df["age"].notnull().sum() > 3:
    shapiro_stat, shapiro_p = stats.shapiro(df["age"].dropna())
    print(f"🔹 Normality Test (Shapiro-Wilk): Statistic={shapiro_stat:.4f}, P-Value={shapiro_p:.4f}\n")
else:
    print("⚠️ Normality test skipped (insufficient numeric data in 'age').\n")

# ---------------------- HYPOTHESIS TESTING (T-TEST) ---------------------- #
if "group_A" in df.columns and "group_B" in df.columns:
    t_stat, p_val = stats.ttest_ind(df["group_A"].dropna(), df["group_B"].dropna())
    print(f"🔹 T-Test Results: T-Statistic={t_stat:.4f}, P-Value={p_val:.4f}\n")
else:
    print("⚠️ T-Test skipped (missing required columns).\n")

# ---------------------- CORRELATION ANALYSIS ---------------------- #
print("🔹 Feature Correlation Matrix:")
print(df.corr(numeric_only=True), "\n")

# ---------------------- CHI-SQUARE TEST (For Categorical Data) ---------------------- #
if "category" in df.columns and "gender" in df.columns:
    contingency = pd.crosstab(df["category"], df["gender"])
    chi2, p, _, _ = stats.chi2_contingency(contingency)
    print(f"🔹 Chi-Square Test: Chi2={chi2:.4f}, P-Value={p:.4f}\n")
else:
    print("⚠️ Chi-Square Test skipped (missing categorical columns).\n")

# ---------------------- OUTLIER DETECTION (Z-SCORE METHOD) ---------------------- #
if "age" in df.columns:
    df["z_score"] = np.abs(stats.zscore(df["age"].dropna()))
    outliers = df[df["z_score"] > 3]  # Identifies values beyond 3 standard deviations
    print("🔹 Outliers Detected in 'Age':")
    print(outliers[["age", "z_score"]], "\n")

# Remove temporary z-score column
df.drop(columns=["z_score"], errors="ignore", inplace=True)

