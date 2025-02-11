#Handle wrong data/outliers(ML)

"""
The data which has huge difference from other data
In machine learning, it is said to be outliers

outliers uses loc for removing data
"""

import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/missing_data.csv")
print(df)

"""
#manuel method
df.loc[7,'Duration']=45
print(df)
"""

x=df['Duration'].mode()[0]
print("*"*55)
df.loc[7,'Duration']=x
print(df)

y=df['Calories'].mean()
print(y)
for i in df.index:
    if df.loc[i,'Calories']>400:
        df.loc[i,'Calories']=y
print(df)


