# Single line swapping of 2 numbers

# Initial values of num1 and num2
num1 = 10
num2 = 20

# Print before swapping
print("Before swapping")
print("Number 1 is", num1)  # Prints the value of num1
print("Number 2 is", num2)  # Prints the value of num2

# Single line swap
num1, num2 = num2, num1  # Swap the values of num1 and num2

# Print after swapping
print("\nAfter swapping")
print("Number 1 is", num1)  # Prints the new value of num1 (which is the original num2)
print("Number 2 is", num2)  # Prints the new value of num2 (which is the original num1)
