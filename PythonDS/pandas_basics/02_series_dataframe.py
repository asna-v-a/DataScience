import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Pandas Series:")
print(s)


# Creating a List Series
a=pd.Series([5,8,6,4,1,0,3,10])
print(a)

#shape: in 1d, it gives no of elements
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)

#head() : first 5 values in 1d, first 5 rows in 2d(data frame)
print(a.head())
print(a.head(3))#number inside () gives that number of elements
print(a.head(7))

#tail() : last 5 values in 1d, last 5 rows in 2d(data frame)
print(a.tail())
print(a.tail(3))#number inside () gives that number of elements
print(a.tail(7))

a=pd.Series([5,8,6,4,1,0,3,10],index=[3,0,2,6,4,1,5,7])
print(a)



# Creating a Dictionary Series
a=pd.Series({'id':101,'fname':'vinay','lname':'k','age':24,'prof':'bigdata'})
print(a)

b=pd.Series({'id':101,'fname':'vinay','lname':'k','age':24,'prof':'bigdata'},index=['age','prof','fname','lname','id'])
print(b)



# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)


#Operations in series
a=pd.Series([5,8,6,4,1,0,3,10])
b=pd.Series([1,2,3,4,5,6,7,8])

c=a.add(b)
print(c)

c=a.subtract(b)
print(c)

c=a.multiply(b)
print(c)

c=a.divide(b)
print(c)




#Nested list (Data Frame)
lst=[[101,'vinay','k',28,'bigdata',3000],
     [102,'arun','p',30,'python',1500],
     [103,'vimal','w',27,'bigdata',6000],
     [104,'vineeth','q',31,'testing',1750],
     [105,'naveen','n',29,'python',1800],
     [106,'abay','n',30,'bigdata',6000],
     [107,'anand','k',25,'testing',1850],
     [106,'abay','n',30,'bigdata',6000]]

df=pd.DataFrame(lst)
print(df)
print()

df.columns=['id','fname','lname','age','prof','salary']
print(df)

print(df.shape)
print(df.dtypes)# in dataframe datatype of each column will be shown
print(df.head(3))
print(df.tail(1))


#Describe() : Detailed description of each column in table, only numerical columns will be shown
print(df.describe())
print(df.describe(include='O'))#object data will be described (Object - O)
#top: most first repeated value, if not take 1st column value
#freq: no of repeated values of top

print(df.describe(include='all'))#both numerical and object data will be described
#NaN : Not a Number

#Add new column
df['gender']=['m','m','m','m','m','m','m','m']
print(df)

#Drop a column
df1=df.drop(['prof'],axis=1)
print(df1)

#drop_duplicates() : to drop duplicate rows
df2=df.drop_duplicates()
print(df2)




#Nested Dictionay (Data Frame)
dict={'id':[101,102,103,104,105],
      'fname':['vinay','arun','vimal','vineeth','naveen'],
      'lname':['k','p','r','s','t'],
      'sub1':[38,30,37,31,39],
      'sub2':[35,31,39,40,36],
      'sub3':[28,30,35,38,32],
      'location':['Thrissur','Ernakulam','Kannur','Alappuzha','Kozhikode']
      }
print(dict)
df=pd.DataFrame(dict)
print(df)

df['gender']=['m','m','m','m','m']#add new column
print(df)


