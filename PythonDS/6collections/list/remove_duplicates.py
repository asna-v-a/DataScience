# Removing duplicates from a list

lst=[1,4,30, 5,5,5,10,40,40,30,5,6,13,25,50]
lst2=[]

for i in lst:
    if i not in lst2:
        lst2.append(i)

print(lst2)