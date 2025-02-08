"""
Functional Programming

Functional programming aims to make code more concise, readable, and efficient by using functions as first-class citizens.

Advantages:
- Improves reusability and readability.
- Reduces the length of code.
- Encourages declarative programming (focus on what to do, not how to do it).

4 Key Functional Programming Concepts in Python:
1. Lambda Functions (Anonymous functions)
2. Map Function (Applies a function to all elements in an iterable)
3. Filter Function (Filters elements based on a condition)
4. List Comprehension (Concise way to create lists)
"""


# 1. Lambda Function (Anonymous, Single-line function)
# Syntax: lambda arguments: expression

add = lambda a, b: a + b
print("Sum:", add(5, 10))  # Output: 15


# 2. Map Function (Applies a function to all elements in an iterable)
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers:", squared_numbers)  
# Output: [1, 4, 9, 16, 25]


# 3. Filter Function (Filters elements based on a condition)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)  
# Output: [2, 4]


# 4. List Comprehension (Concise way to create lists)
# Syntax: [expression for item in iterable if condition]

squares = [x ** 2 for x in numbers]
print("Squares using List Comprehension:", squares)  
# Output: [1, 4, 9, 16, 25]

even_numbers_lc = [x for x in numbers if x % 2 == 0]
print("Even Numbers using List Comprehension:", even_numbers_lc)  
# Output: [2, 4]


"""
Key Takeaways:
- Lambda: One-liner function, no def keyword.
- Map: Applies a function to an entire list.
- Filter: Extracts elements that satisfy a condition.
- List Comprehension: Shorter way to generate lists.
"""

