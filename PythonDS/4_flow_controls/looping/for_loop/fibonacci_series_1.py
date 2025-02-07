# Fibonacci Series

num = int(input("Enter the number: "))

fib1 =0
fib2 = 1

if(num == 1):
    print(fib1)
elif(num==2):
    print(fib1)
    print(fib2)
elif(num>2):
    print(fib1)
    print(fib2)
    for i in range(2,num):
        fib3=fib1+fib2
        print(fib3)
        fib1=fib2
        fib2=fib3
else:
    print("Invalid")

