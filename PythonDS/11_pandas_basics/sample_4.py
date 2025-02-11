import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/sample4.txt",sep=',',header=None)
#header_tag : file contains column name
#if there is no header_tag mention header=None, otherwise it will take 1st row as column names
df.columns=['id','fname','lname','age','phno','location']
print(df)

df1=df.sort_values(by='age',ascending=False)[['fname','lname','age','phno']].head(2)
print(df1)

df2=df.sort_values(by='age')[['fname','lname','age','phno']].head(1)
print(df2)

df3=df.loc[df['location']=='Chennai'].sort_values(by='age',ascending=False)\
    [['fname','lname','age','phno']].head(1)

print(df3)