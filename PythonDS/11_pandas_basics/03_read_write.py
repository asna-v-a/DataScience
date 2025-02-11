import pandas as pd

# Reading CSV file
df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/sample.csv")
print("Data from CSV:")
print(df.head())

# Writing to CSV
df.to_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/output.csv", index=False)

#Use pip or conda to install openpyxl
# Reading & Writing Excel
df = pd.read_excel("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/sample.xlsx")
df.to_excel("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/output.xlsx", index=False)
