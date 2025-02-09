import pandas as pd
import matplotlib.pyplot as plt

data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Plot a bar chart
df.plot(x='Category', y='Values', kind='bar', legend=False)
plt.title("Category Values")
plt.show()
