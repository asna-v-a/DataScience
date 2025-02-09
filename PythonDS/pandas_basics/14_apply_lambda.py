"""
Using .apply() and Lambda Functions
"""
import pandas as pd

df = pd.DataFrame({"Numbers": [1, 2, 3, 4, 5]})
df["Squared"] = df["Numbers"].apply(lambda x: x**2)
df["Even"] = df["Numbers"].apply(lambda x: "Yes" if x % 2 == 0 else "No")
print(df)
