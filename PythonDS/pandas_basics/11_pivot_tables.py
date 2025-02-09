"""
Creating and Using Pivot Tables
"""
import pandas as pd

df = pd.DataFrame({"Category": ["A", "B", "A", "B"], "Score": [10, 20, 30, 40]})
pivot = df.pivot_table(values="Score", index="Category", aggfunc="mean")
print(pivot)

# Pivot with multiple aggregation functions
pivot2 = df.pivot_table(values="Score", index="Category", aggfunc=["sum", "count"])
print(pivot2)
