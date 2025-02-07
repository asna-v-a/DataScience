# Fibonacci Series

num = int(input("Enter the number: "))

fib1, fib2 = 0, 1
for i in range(num):
    print(fib1)
    fib1, fib2 = fib2, fib1 + fib2
