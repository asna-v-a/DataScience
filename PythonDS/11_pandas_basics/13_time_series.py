"""
Handling Time-Based Data
"""
import pandas as pd

dates = pd.date_range(start="2024-01-01", periods=5, freq="D")
df = pd.DataFrame({"Date": dates, "Value": [10, 20, 30, 40, 50]})
df.set_index("Date", inplace=True)
print(df)

# Resampling time series data
print(df.resample("2D").sum())  # Summing every 2 days
