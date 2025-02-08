"""
Lambda Function

A lambda function is an anonymous function (a function without a name).
It is useful for writing small, one-line functions that do not require a full function definition.

Advantages:
- Reduces the length of the code.
- Can be used as an argument inside functions like map(), filter(), and sorted().

Syntax:
variable = lambda arguments: expression
"""

# Add two numbers using lambda
add = lambda num1, num2: num1 + num2
print("Addition:", add(10, 20))  # Output: 30

# Multiply three numbers using lambda
mul = lambda num1, num2, num3: num1 * num2 * num3
print("Multiplication:", mul(10, 2, 3))  # Output: 60

# Find the cube of a number using lambda
cube = lambda num: num ** 3
print("Cube:", cube(3))  # Output: 27
