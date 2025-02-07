lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

"""
Incorrect Logic Example:

for i in range(lower,upper+1):
    for j in range(2,i):   
        if i%j ==0:
            break
        else:
            print(i,end=' ')
            break

print()

- The commented code has a flaw:
- If i = 2, the inner loop for j in range(2, i) will not execute.
- The if and else conditions will not run, affecting prime number detection.

"""

for i in range(lower, upper + 1):
    if i > 1:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print(i, end=' ')
