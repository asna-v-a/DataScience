"""
Using melt() and pivot()
"""
import pandas as pd

df = pd.DataFrame({"Name": ["Alice", "Bob"], "Math": [80, 90], "Science": [85, 95]})
melted = df.melt(id_vars=["Name"], var_name="Subject", value_name="Score")
print(melted)

# Reshape using pivot
reshaped = melted.pivot(index="Name", columns="Subject", values="Score")
print(reshaped)
