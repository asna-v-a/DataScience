#Squaring elements and filtering even numbers

lst = [1, 4, 6, 7, 8, 9, 15, 20]
lst2 = []
lst3 = []
for i in lst:
    lst2.append(i ** 2)
    if i % 2 == 0:
        lst3.append(i)

print(lst)
print(lst2)
print(lst3)
