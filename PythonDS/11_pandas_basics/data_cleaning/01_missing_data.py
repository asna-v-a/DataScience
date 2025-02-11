import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/missing_data.csv")

print(df)
print(df.dtypes)
print('*'*53)
print(df.isna().sum())

print('*'*53)
#replace missing value with a common value
"""
df.fillna(350,inplace=True)# replace each NaN with the value 300, inplace=True :  used to change same dataframe
print(df)
print('*'*53)
"""

#Fill missing values in specific columns
df['Calories'].fillna(300,inplace=True)# it shows warning, to avoid it use: 'df.method({col: value}, inplace=True)'
                                       # or df[col] = df[col].method(value)
print(df)
df['Date'].fillna('2020/12/22',inplace=True)
print(df)