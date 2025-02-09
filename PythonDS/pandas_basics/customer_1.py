import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/pandas_basics/files/customer.csv")
#header_tag : file contains column name
#if there is no header_tag mention header=None, otherwise it will take 1st row as column names

print(df)

df1=df.head(50)
print(df1)

df2=df[['fname','lname','age','prof']].tail(30)#pass columns query first and then rows query
print(df2)

df3=df[['fname','lname','age','prof']].iloc[9:50]
print(df3)

x=df.iloc[:,:-1] # columns separation
print(x)

y=df.iloc[:,-1:]
print(y)

#Total number of missing values
print(df.isna().sum())

#Handle missing values
#fillna() : used to fill missing values

df4=df.fillna('India')
print(df4)
print(df4.isna().sum())