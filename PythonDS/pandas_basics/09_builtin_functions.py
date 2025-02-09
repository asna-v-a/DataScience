import pandas as pd

data = {'A': [10, 20, 30, 40], 'B': [5, 10, 15, 20]}
df = pd.DataFrame(data)

# Descriptive statistics
print("Describe:")
print(df.describe())

# Summation
print("Sum of A:", df['A'].sum())

# Mean
print("Mean of B:", df['B'].mean())

# Sorting
print("\nSorted DataFrame:")
print(df.sort_values(by='A', ascending=False))
