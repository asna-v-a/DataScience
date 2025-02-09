"""
Speeding up Pandas Operations
"""
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(1000000, 2), columns=["A", "B"])
df["Sum"] = df.eval("A + B")  # Faster than df["A"] + df["B"]
print(df.head())

# Using .query() for efficient filtering
filtered_df = df.query("A > 0.5 and B > 0.5")
print(filtered_df.head())
