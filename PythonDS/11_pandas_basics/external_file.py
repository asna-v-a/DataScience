import numpy as np
import pandas as pd

#loc/filter -> order -> cols -> rows (head/tail/iloc)

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/sample4.txt",sep=',',header=None)
#header_tag : file contains column name
#if there is no header_tag mention header=None, otherwise it will take 1st row as column names
print(df)

print('*'*60)
df.columns=['id','fname','lname','age','phno','location']
print(df)

df1=df.iloc[4]
print(df1)

df1=df.iloc[3:7]
print(df1)

df1=df.iloc[3:7:2]
print(df1)

#loc : to pass condition(like where)
#newDF=oldDF.loc[oldDF[colname]condition]

df2=df.loc[df['age']>23]
print(df2)


df3=df.loc[df['age']==21][['fname','lname','age','phno']]
print(df3)

df4=df.loc[df['age']==23][['fname','lname','age','phno']]
print(df4)

df5=df.loc[df['location']=='Chennai'][['fname','lname','age','phno']]
print(df5)

df6=df.loc[df['age']<23][['fname','lname','age']]
print(df6)

#more than 1 condition syntax
#newDF=oldDF.loc[(oldDF[colname]condition)&(oldDF[colname]condition)]

df7=df.loc[(df['age']>23)&(df['location']=='Chennai')][['fname','lname','age']]
print(df7)

#sort --> order by
#sort_values()
#newDF=oldDF.sort_values(by='colname')
#newDF=oldDF.sort_values(by='colname',ascending=False)

df8=df.sort_values(by='age')
print(df8)

df9=df.sort_values(by='age',ascending=False)
print(df9)

