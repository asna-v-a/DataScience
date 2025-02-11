#Factorial of number

limit = int(input("Enter the limit: "))
factorial = 1
for i in range(1,limit+1):
    factorial *= i

print("Factorial of",limit,"is",factorial)