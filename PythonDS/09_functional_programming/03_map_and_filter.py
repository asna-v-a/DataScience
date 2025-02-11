"""
Map and Filter Functions

1. Map:
   - Used when every element in a list needs to be processed using a function.
   - Reduces the length of the program by applying the function to all elements.
   - Syntax: list(map(function, iterable))

2. Filter:
   - Used to filter elements from a list based on a condition.
   - Reduces the length of the program by selecting only elements that satisfy the condition.
   - Syntax: list(filter(function, iterable))
"""

# Sample list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map to calculate squares
squares = list(map(lambda num: num ** 2, lst))
print("Squares:", squares)

# Using map to calculate cubes
cubes = list(map(lambda num: num ** 3, lst))
print("Cubes:", cubes)

# Using filter to get even numbers
evens = list(filter(lambda num: num % 2 == 0, lst))
print("Even Numbers:", evens)

# Using filter to get odd numbers
odds = list(filter(lambda num: num % 2 != 0, lst))
print("Odd Numbers:", odds)
