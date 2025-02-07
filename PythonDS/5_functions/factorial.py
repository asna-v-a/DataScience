# Function to calculate factorial
#Method1
def factorial():
    limit=int(input("Enter the limit: "))
    fact=1
    for i in range(1,limit+1):
        fact*=i
    print("Factorial:",fact)

factorial()



#Method2
def factorial(limit):
    fact=1
    for i in range(1, limit+1):
        fact*=i
    print("Factorial:",fact)

limit=int(input("Enter the limit: "))
factorial(limit)

#Method3
def factorial(limit):
    fact = 1
    for i in range(1, limit + 1):
        fact *= i
    return fact

limit = int(input("Enter the limit: "))
factorial=factorial(limit)
print("Factorial:", factorial)



def factorial():
    limit = int(input("Enter the limit: "))
    fact = 1
    for i in range(1, limit + 1):
        fact *= i
    return fact


factorial=factorial()
print("Factorial:", factorial)
