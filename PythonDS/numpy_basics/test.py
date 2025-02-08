"""
1.Write a NumPy program to test whether none of the elements of a given array are zero.
2. Write a NumPy program to create an array of integers from 30 to 70.
3.Write a NumPy program to create an array of all even integers from 30 to 70.
4. Get the common items between a and b
Input:
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
5. Reverse the columns of a 2D array arr.
# Input
arr = np.arange(9).reshape(3,3)
"""
import numpy as np

a= np.array([1, 2, 3, 4, 5])
print(np.all(a!=0))

a=np.arange(30,71)
print(a)

a=np.arange(30,71,2)
print(a)

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c=np.array([x for x in a if x in b])
u=np.unique(c)
print(u)
#or
print(np.intersect1d(a, b))



arr = np.arange(9).reshape(3,3)
print(arr[::-1,::-1])