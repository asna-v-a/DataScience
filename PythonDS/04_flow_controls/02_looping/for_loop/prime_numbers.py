# Program to Check if a Number is Prime

num = int(input("Enter the number: "))

if (num < 2):
    print(num, "is neither prime nor not prime")
else:
    flag = 0

for i in range(2, num):
    if (num % i == 0):
        flag = 1
        break
if (flag == 0):  # if(flag>0):
    print(num, "is prime")
else:
    print(num, "is not prime")
