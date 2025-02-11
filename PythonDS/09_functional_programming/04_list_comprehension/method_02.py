"""
Method 2: Creating Lists with Conditions Using List Comprehension

1. Generates a list by iterating through a range.
2. Adds elements based on a single condition.

Syntax:
lst = [expression for item in range if condition]

Examples:
"""

# List of even numbers from 1 to 50
lst = [i for i in range(1, 51) if i % 2 == 0]
print(lst)

# List of numbers from 1 to 30 that are divisible by 5
lst = [i for i in range(1, 31) if i % 5 == 0]
print(lst)

# List of odd numbers from 1 to 25 along with their squares
lst = [(i, i**2) for i in range(1, 26) if i % 2]
print(lst)

# List of numbers from 1 to 50 that are divisible by both 2 and 5
lst = [i for i in range(1, 51) if i % 2 == 0 and i % 5 == 0]
print(lst)
