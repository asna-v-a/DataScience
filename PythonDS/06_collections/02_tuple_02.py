#Modifying a Tuple by Converting it to a List

tu = (10, 15, 20, 25, 30, 35, 40, 45, 50)  # Original tuple
lst = list(tu)  # Convert tuple to list
print(lst) 

# Modify the element
for i in range(0, len(lst)):
    if lst[i] == 20:
        lst[i] = 55
        break

tu1 = tuple(lst)  # Convert list back to tuple
print(tu1) 
