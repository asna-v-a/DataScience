import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/pandas_basics/files/missing_data.csv")

x=df['Calories'].mean()# can also use median
print(x)

df['Calories'].fillna(x,inplace=True)
print(df)

y=df['Date'].mode()[0]#if datatype is object, use mode()
print(y)

df['Date'].fillna(y,inplace=True)
print(df)