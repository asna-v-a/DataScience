# Input Function - input()

# Prompt the user for input and store the values in variables
num1 = input("Enter number 1: ")  # Taking input as string
num2 = input("Enter number 2: ")  # Taking input as string

# If you want to perform mathematical operations, convert the inputs to integers
num1 = int(num1)  # Convert num1 to integer
num2 = int(num2)  # Convert num2 to integer

# Display the entered numbers
print("Entered number 1:", num1)
print("Entered number 2:", num2)

# Example of a mathematical operation
sum_numbers = num1 + num2
print("Sum of the numbers:", sum_numbers)
