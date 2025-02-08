"""
Method 1: Creating Lists Using List Comprehension

1. Generates a list by iterating through a range.
2. Performs operations on each element while iterating.

Syntax: 
lst = [expression for item in range]

Examples:
"""

# Creating a list of numbers from 1 to 50
lst = [i for i in range(1, 51)]
print(lst)

# Creating a list of numbers from 1 to 25
lst = [i for i in range(1, 26)]
print(lst)

# Creating a list of squares of numbers from 1 to 10
lst = [i**2 for i in range(1, 11)]
print(lst)

# Adding 5 to each element of an existing list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1 = [i + 5 for i in lst]
print(lst1)
