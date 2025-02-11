# Nested if: An if statement inside another if statement, allowing for multiple conditions to be checked.

# Syntax:
# if(condition1):
#     if(condition):
#         statement
#     elif(condition):
#         statement
#     else:
#         statement
# elif(condition2):
#     if(condition):
#         statement
#     elif(condition):
#         statement
#     else:
#         statement

# Example: Checking if a number is positive, negative, or zero, and then checking if it is even or odd
num = int(input("Enter a number: "))

if num > 0:  
    if num % 2 == 0:  # Nested condition to check if the positive number is even
        print("Positive and Even")
    else:  
        print("Positive and Odd")
elif num < 0:  
    if num % 2 == 0:  # Nested condition to check if the negative number is even
        print("Negative and Even")
    else:  
        print("Negative and Odd")
else:  
    print("Zero")
