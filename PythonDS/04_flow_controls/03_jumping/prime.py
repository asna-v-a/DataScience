# Check if a number is prime
# A prime number is only divisible by 1 and itself, so we check for factors from 2 to num-1.

num = int(input("Enter the number: "))  # Take input for the number to check if it's prime

flag = 0  # Indicating the number is prime unless proven otherwise

for i in range(2, num):  
    if num % i == 0:  # If num is divisible by i, it's not a prime number
        flag = 1  # Indicating num is not prime
        break  # Exit the loop early since we found a factor

# If flag is still 0, the number is prime, otherwise, it's not prime
if flag == 0:
    print(num, "is prime")  
else:
    print(num, "is not prime")  
