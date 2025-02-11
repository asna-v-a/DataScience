import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice'], 'Age': [25, None, 35, 25]}
df = pd.DataFrame(data)

# Handling missing values
df.fillna(df['Age'].mean(), inplace=True)

# Removing duplicates
df.drop_duplicates(inplace=True)

print("Cleaned DataFrame:")
print(df)
