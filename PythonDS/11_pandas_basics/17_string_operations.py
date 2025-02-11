"""
Advanced String Manipulations
"""
import pandas as pd

df = pd.DataFrame({"Names": ["Alice Johnson", "Bob Smith"]})
df["Uppercase"] = df["Names"].str.upper()
df["Last Name"] = df["Names"].str.split().str[-1]
print(df)
