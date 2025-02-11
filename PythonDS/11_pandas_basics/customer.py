import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/11_pandas_basics/files/customer.csv")
print(df)
print('*'*73)
print(df.isna().sum())
print('*'*73)

#1. Fill the missing value using india
df1=df.fillna('india')
print(df1.isna().sum())
print('*'*73)

#2. fname,lname,age,prof,loc
df2=df1[['fname','lname','age','prof','loc']]
print(df2)
print('*'*73)

#3. Age mxm 5 emp fname,lname,age,prof
df3=df1.sort_values(by='age',ascending=False)[['fname','lname','age','prof']].head(5)
print(df3)
print('*'*73)

#4. Age minimum 3 emp fname,lname,age,prof
df4=df1.sort_values(by='age')[['fname','lname','age','prof']].head(3)
print(df4)
print('*'*73)

#5. Age above 50 fname,lname,age
df5=df1.loc[df1['age']>50][['fname','lname','age']]
print(df5)
print('*'*73)

#6. Age less than 30 fname,lname,age,prof,loc
df6=df1.loc[df1['age']<30][['fname','lname','age','prof','loc']]
print(df6)
print('*'*73)

#7. india work fname,lname,age,prof
df7=df1.loc[df1['loc']=='india'][['fname','lname','age','prof']]
print(df7)
print('*'*73)

#8. india work and age above 50 fname,lname,age
df8=df1.loc[(df1['age']>50)&(df1['loc']=='india')][['fname','lname','age','prof']]
print(df8)
print('*'*73)

#9. uk work fname,lname,age,prof
df9=df1.loc[df1['loc']=='uk'][['fname','lname','age','prof']]
print(df9)
print('*'*73)

#10. india work and prof Doctor fname,lname,age
df10=df1.loc[(df1['prof']=='Doctor')&(df1['loc']=='india')][['fname','lname','age']]
print(df10)
print('*'*73)

#11. india work, age mxm 3 employee fname,lname,age
df11=df1.loc[df1['loc']=='india'].sort_values(by='age',ascending=False)[['fname','lname','age']].head(3)
print(df11)
print('*'*73)

#12. india wok ,age min 2 emp fname,lname,age
df12=df1.loc[df1['loc']=='india'].sort_values(by='age')[['fname','lname','age']].head(2)
print(df12)
print('*'*73)

#13. Pilot prof, age mxm 1 emp fname,lname,age,location
df13=df1.loc[df1['prof']=='Pilot'].sort_values(by='age',ascending=False)[['fname','lname','age','loc']].head(1)
print(df13)
print('*'*73)

#14. Pilot prof, age minim 3 emp fname,lname,age
df14=df1.loc[df1['prof']=='Pilot'].sort_values(by='age')[['fname','lname','age']].head(3)
print(df14)
print('*'*73)

#15. uk work ,age min 10 emp fname,lname,prof
df15=df1.loc[df1['loc']=='uk'].sort_values(by='age')[['fname','lname','prof']].head(10)
print(df15)
print('*'*73)