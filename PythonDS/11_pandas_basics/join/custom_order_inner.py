import numpy as np
import pandas as pd

df1=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/custom_windows.csv")
df2=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/order_windows.csv")
print(df1,'\n\n',df2)

df3=pd.merge(df1,df2,on='id',how='inner')
print(df3)

df4=df3.loc[df3['age']>23][['name','age','location','dat','amount']]
print(df4)

df5=df3.sort_values(by='age',ascending=False)\
    [['name','age','location','dat','amount']].head(2)
print(df5)

df6=df3.sort_values(by='dat',ascending=False)\
    [['name','age','location','dat','amount']].head(1)
print(df6)