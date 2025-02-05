tu = (10, 15, 20, 25, 30, 35, 40, 45, 50)
lst = list(tu)
print(lst)
for i in range(0, len(lst)):
    if lst[i] == 20:
        lst[i] = 55
        break
tu1 = tuple(lst)
print(tu1)
