import numpy as np
import pandas as pd

dict1={'id':[101,102,103,104,105],
      'fname':['vinay','arun','vimal','vineeth','naveen'],
      'lname':['k','p','r','s','t'],
      'age':[38,26,37,31,39],
       }
dict2={'prof':['bigdata','python','testing','bigdata','python'],
       'id':[102,103,105,106,108],
       'location':['Thrissur','Ernakulam','Kannur','Alappuzha','Kozhikode'],
       'salary':[38000,30000,37000,31000,40000]
      }
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)

print(df1,"\n\n",df2)

df3=pd.merge(df1,df2,on='id',how='left')
print(df3)