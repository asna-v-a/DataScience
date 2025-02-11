# Data Structure : is a specialized format for organizing, storing, and managing data

"""
Three types:
1. Series
2. Data Frame
3. Label


1. Series : 1D data. Eg: List,Tuple,dictionary,...
   One-dimensional labeled array that can hold any data type (integers, floats, strings, Python objects, etc.)

2. Data Frame : 2D data. Eg: Nested List, text, csv file, json,...
   Two-dimensional, size-mutable, and heterogeneous data structure.
   It is the most commonly used structure in Pandas and is similar to a table or spreadsheet.

3. Label : 3D
   refers to the index or column name used to access elements in a Series or DataFrame.
"""


import pandas as pd


# Creating a simple Series
a=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(a)

b=pd.Series((1,2,3,4,5,6,7,8,9,10))
print(b)

#In dictionary, the key value will act as the index
c=pd.Series({'id':101,'fname':'vinay','lname':'k','age':24,'prof':'marketing'})
print(c)


# Creating a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

print("Pandas DataFrame:")
print(df)
