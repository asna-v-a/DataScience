import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/pandas_basics/files/sample4.txt",sep=',',header=None)
df.columns=['id','fname','lname','age','phno','location']
print(df)

dfc=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/pandas_basics/files/customer.csv")
print(dfc)

#max()
"""
newDF=oldDF.groupby('colname')['colname'].max()
"""

df1=dfc.groupby('prof')['age'].max().sort_values(ascending=False)
print(df1)

#min()
"""
newDF=oldDF.groupby('colname')['colname'].min()
"""

df2=dfc.groupby('prof')['age'].min().sort_values(ascending=False)
print(df2)
