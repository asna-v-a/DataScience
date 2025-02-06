# Pattern Problems


# Nested for loop
num = int(input("Enter the number: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i, end=" ")
    print()

print()

for i in range(0, num):
    for j in range(1, num + 1):
        print(j+i, end=" ")

    print()
print()
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()


#print() - newline
# i - num rows for (for i in range(1,num+1)
# j - num columns
#print(i) - same value
#print(j) - different value


#Top greater - smaller -> i for loop should be reverse (num,0,-1)
#Bottom greater - smaller -> j for loop should be reverse (num,0,-1)