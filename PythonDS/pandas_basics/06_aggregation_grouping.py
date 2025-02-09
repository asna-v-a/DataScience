import pandas as pd

data = {'Department': ['HR', 'IT', 'HR', 'IT'], 'Salary': [5000, 7000, 5500, 7200]}
df = pd.DataFrame(data)

# Group by Department
grouped = df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:")
print(grouped)
