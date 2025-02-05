# Dictionary : Key-value pair

#1. Define Dictionary
dic={} # Empty Dictionary

list2 = list() # list using function, used to change other collections to list --> list(set_name)

dic1={'id':101,'fname':'vinay','lname':'k','age':28,'profession':'bigdata'}
print(dic1)

#2. Heterogeneous data
#3. It doesn't support duplicate keys but support duplicate values - last entered value will be taken if there are duplicate keys
#4. Insertion order is preserved
#5. It's Mutable
dic1['age']=10
print(dic1)

#Index : no index, access elements using keys
print(dic1['id'])


