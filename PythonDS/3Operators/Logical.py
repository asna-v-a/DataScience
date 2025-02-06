#Logical Operators

"""
Logical operators are used to perform logical operations on boolean values or expressions.
There are three main logical operators:

1. AND - & (Ampersand)
   - The AND operator returns True only when both conditions are True.
   - Truth Table:
     Input   Output
      0 0      0
      0 1      0
      1 0      0
      1 1      1

2. OR - | (Pipe Symbol)
   - The OR operator returns True if at least one condition is True.
   - Truth Table:
     Input   Output
      0 0      0
      0 1      1
      1 0      1
      1 1      1

3. XOR - ^ (Caret Symbol)
   - The XOR operator returns True when exactly one of the conditions is True (i.e., they are different).
   - Truth Table:
     Input   Output
      0 0      0
      0 1      1
      1 0      1
      1 1      0
"""

# Binary Logical Operations using AND, OR, XOR

num1 = 2  # Binary: 10
num2 = 4  # Binary: 100
print("num1 & num2 =", num1 & num2)  # AND operation (Binary AND) - Output will be 0

num3 = 4  # Binary: 100
num4 = 4  # Binary: 100
print("num3 & num4 =", num3 & num4)  # AND operation (Binary AND) - Output will be 4

# Logical Operators with Boolean values
a = True
b = False

# AND operator
print("a and b:", a and b)  # True AND False -> False

# OR operator
print("a or b:", a or b)  # True OR False -> True

# NOT operator
print("not a:", not a)  # NOT True -> False

# XOR operator - Outputs True if both values are different
print("a ^ b:", a ^ b)  # True XOR False -> True

# Demonstrating XOR with True and True, output should be False
c = True
print("c ^ a:", c ^ a)  # True XOR True -> False
