import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/missing_data.csv")
print(df)

"""
#drop missing value
#dropna()

df.dropna(inplace=True,ignore_index=True)#ignore_index will give consecutive index
print(df)

"""
df.dropna(subset='Calories',inplace=True,ignore_index=True)
print(df)

df.dropna(subset='Date',inplace=True,ignore_index=True)
print(df)