#count() : used to calculate each column wise count (value)
"""
1.Each column wise count

syntax:
newDF=oldDF.groupby('colname')['colname'].count()
"""
import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/pandas_basics/files/sample4.txt",sep=',',header=None)
df.columns=['id','fname','lname','age','phno','location']
print(df)

dfc=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/pandas_basics/files/customer.csv")
print(dfc)

df1=df.groupby('location')['location'].count()
print(df1)

df2=df.groupby('location')['location'].count()\
    .sort_values(ascending=False)
print(df2)

df2=df.groupby('age')['age'].count()\
    .sort_values(ascending=False)
print(df2)

dfc1=dfc.groupby('prof')['prof'].count()\
    .sort_values()
print(dfc1)

dfc2=dfc.loc[dfc['loc']=='india'].groupby('prof')['prof'].count()\
    .sort_values(ascending=False)
print(dfc2)

dfc2=dfc.loc[(dfc['loc']=='india')&(dfc['age']>40)].groupby('prof')['prof'].count()\
    .sort_values(ascending=False)
print(dfc2)