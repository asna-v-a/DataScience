# Factorial of a number

num = int(input("Enter the limit: "))

i = 1
fact = 1

while (i <= num):
    fact *= i
    i += 1

print("Factorial of", num, "is", fact)