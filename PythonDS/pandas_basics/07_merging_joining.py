import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Salary': [5000, 6000, 7000]})

# Merging on ID column
merged_df = pd.merge(df1, df2, on='ID', how='inner')

print("Merged DataFrame:")
print(merged_df)
