import numpy as np
import pandas as pd

df1=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/student.csv")
df2=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/result.csv")
print(df1,'\n\n',df2)
print('*'*24)

df3=pd.merge(df1,df2,on='roll',how='inner')
print(df3)
print('*'*24)

df4=df3.loc[df3['res']=='pass']
print(df4)
print('*'*24)