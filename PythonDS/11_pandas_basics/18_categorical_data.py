"""
Working with Categorical Data
"""
import pandas as pd

df = pd.DataFrame({"Category": ["A", "B", "A", "C", "B"]})
df["Category"] = df["Category"].astype("category")
print(df.dtypes)

# Setting category order
df["Category"] = df["Category"].cat.set_categories(["C", "B", "A"], ordered=True)
print(df.sort_values("Category"))
