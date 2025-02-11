"""
List Comprehension

1. Reduces code length by writing operations in a single line.
2. Uses a compact syntax to create and manipulate lists efficiently.

Methods (Conceptual Understanding):

1. Creating a list with a range of elements.
   Syntax: var = [expression for item in range]

2. Creating a list based on a single condition.
   Syntax: var = [expression for item in range if condition]

3. Creating a list based on multiple conditions.
   Syntax: var = [expression1 if condition1 else expression2 for item in range]

   Note:
   - No `elif` in list comprehension.
   - Multiple conditions can be handled using nested `if-else` statements.

"""

# 1. Creating a list with a range of elements (numbers from 1 to 10)
lst1 = [num for num in range(1, 11)]
print(lst1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Creating a list of even numbers from 1 to 20
even_lst = [num for num in range(1, 21) if num % 2 == 0]
print(even_lst)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 3. Creating a list based on multiple conditions (odd numbers squared, even numbers halved)
new_lst = [num ** 2 if num % 2 else num // 2 for num in range(1, 11)]
print(new_lst)  # Output: [1, 1, 9, 2, 25, 3, 49, 4, 81, 5]
