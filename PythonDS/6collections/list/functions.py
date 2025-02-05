list1 = [1,2,3,4,5,6,7,8,9,10]
sum1=0

for i in list1:
    sum1+=i

print("Sum using For loop:",sum1)

#List has in-build functions, sum()
print("Sum using Function:",sum(list1))

print("Largest element in list:",max(list1))

print("Smallest element in list:",min(list1))

print("Smallest element in list:",len(list1))

#Functions used in list
"""
1. sum(list) : Sum of elements in the list
2. max(list) : Largest element in the list
3. min(list) : Smallest element in the list
4. len(list) : Total length of the list

"""