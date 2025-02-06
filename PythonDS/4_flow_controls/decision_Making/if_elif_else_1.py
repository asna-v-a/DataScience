# Positive/Negative/Zero Check

num = int(input("Enter the number: "))

# Checking if the number is less than 0 (negative)
if num < 0:
    print(num, "is Negative")  # If condition is true, print that the number is negative

# Checking if the number is greater than 0 (positive)
elif num > 0:
    print(num, "is Positive")  # If condition is true, print that the number is positive

# If the number is neither negative nor positive, it must be zero
else:
    print("The number is Zero")  # If both previous conditions are false, print that the number is zero
