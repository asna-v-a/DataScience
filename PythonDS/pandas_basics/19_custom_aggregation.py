"""
Defining Custom Aggregation Functions
"""
import pandas as pd

df = pd.DataFrame({"Team": ["A", "B", "A", "B"], "Score": [10, 20, 15, 25]})
agg = df.groupby("Team").agg(Custom_Sum=("Score", lambda x: sum(x) + 5))
print(agg)

# Using multiple custom aggregations
agg2 = df.groupby("Team").agg(
    Total_Score=("Score", sum),
    Adjusted_Score=("Score", lambda x: sum(x) + 10)
)
print(agg2)
