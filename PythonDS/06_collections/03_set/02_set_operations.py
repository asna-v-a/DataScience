#Set Operations

"""
1. Union
2. Intersection
3. Difference

"""
str1={1,2,3,4,5,6,7,8,9,10}
str2={5,6,7,8,9,10,11,12,13,14,15}

# Union : all elements from both sets without duplicates
str3=str1.union(str2)
print(str3)

# Intersection : common elements wil be taken
str4=str1.intersection(str2)
print(str4)

# Difference
str5=str1.difference(str2)
print(str5)

str6=str2.difference(str1)
print(str6)