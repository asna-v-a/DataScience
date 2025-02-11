"""
Working with MultiIndex
"""
import pandas as pd

arrays = [["A", "A", "B", "B"], [1, 2, 1, 2]]
index = pd.MultiIndex.from_arrays(arrays, names=("Letter", "Number"))
df = pd.DataFrame({"Values": [10, 20, 30, 40]}, index=index)
print(df)
print(df.loc["A"])  # Selecting MultiIndex
print(df.xs(1, level="Number"))  # Accessing specific level
