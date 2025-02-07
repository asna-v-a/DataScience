# Program to Check if a Number is Prime

num = int(input("Enter the number: "))

if (num < 2):
    print(num,"is neither prime nor not prime")

for i in range(2, num):
    if (num % i == 0):
        print(num, "is not prime")
        break
    else:
        print(num, "is prime")
        break
else:
    print(num, "is not prime")

