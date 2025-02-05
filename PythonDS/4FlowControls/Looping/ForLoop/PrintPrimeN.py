lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

"""
for i in range(lower,upper+1):
    for j in range(2,i):   if i=2 if and else condition wont work
        if i%j ==0:
            break
        else:
            print(i,end=' ')
            break

print()
"""

for i in range(lower, upper + 1):
    if i > 1:
        flag = 1
        for j in range(2, i):
            if i % 2 == 0:
                flag = 0
                break
        if flag == 1:
            print(i, end=' ')
print()


for i in range(lower, upper + 1):
    if i > 1:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print(i, end=' ')
