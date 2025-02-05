# map and filter
"""
Map : used when every element in a list needs to do a task or function
      Reduce length of program
syntax: variable = list(map(function,iterable))

iterable: list name performing the function

Filter : filter the list by a condition
         Reduce length of program
syntax: variable = list(filter(function,iterable))
"""

# map
lst=[1,2,3,4,5,6,7,8,9,10]
"""
def square(num):
    return num**2
f=list(map(square,lst))
print(f)
"""
f=list(map(lambda num:num**2,lst))
print(f)

f1=list(map(lambda num:num**3,lst))
print(f1)

#filter
f3=list(filter(lambda num:num%2==0,lst))
print(f3)

f4=list(filter(lambda num:num%2,lst))
print(f4)