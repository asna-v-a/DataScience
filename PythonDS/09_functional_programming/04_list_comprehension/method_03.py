"""
Method 3: Multiple Conditions in List Comprehension

1. Uses multiple conditions to modify elements differently.
2. The "if-else" structure applies different logic based on conditions.
3. No "elif" in list comprehension; nesting "else if" is required.

Syntax:
lst = [expression1 if condition1 else expression2 if condition2 else expression3 for item in range]

Examples:
"""

# Even numbers are squared, odd numbers are cubed (1-50)
lst = [(i, i**2) if i % 2 == 0 else (i, i**3) for i in range(1, 51)]
print(lst)

# Numbers from 1 to 30 labeled as "Even" or "Odd"
lst = [(i, "Even") if i % 2 == 0 else (i, "Odd") for i in range(1, 31)]
print(lst)

# Numbers categorized as "Small" (1-15), "Medium" (16-35), "Large" (36-50)
lst = [(i, "Small") if i <= 15 else (i, "Medium") if i <= 35 else (i, "Large") for i in range(1, 51)]
print(lst)
