#Generating a List within a Given Range

lst = []

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

for i in range(lower, upper+1):
    lst.append(i)

print(lst)