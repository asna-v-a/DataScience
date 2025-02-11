import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Selecting specific columns
print(df['Name'])

# Selecting rows by label
print(df.loc['b'])

# Selecting rows by position
print(df.iloc[1])
