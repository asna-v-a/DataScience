#Sum of odd numbers in a list

lst = []

for i in range(1, 101):
    if i%2==1:
        lst.append(i)

print(lst)
print("Sum: ",sum(lst))