# Swapping 2 numbers using a third variable

# Initial values of num1 and num2
num1 = 10
num2 = 20

# Print before swapping
print("Before swapping")
print("Number1 is", num1)  
print("Number2 is", num2)  

# Swap logic using a third variable (temp)
temp = num1  # Store the value of num1 in temp
num1 = num2  # Assign the value of num2 to num1
num2 = temp  # Assign the value stored in temp (original num1) to num2

# Print after swapping
print("\nAfter swapping")
print("Number1 is", num1) 
print("Number2 is", num2)  
