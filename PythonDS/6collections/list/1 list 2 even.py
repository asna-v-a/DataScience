lst=[]
even_list=[]
odd_list=[]

for i in range(1,101):
    lst.append(i)
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(lst)
print(even_list)
print(odd_list)

print("List sum:",sum(lst))
print("Even list sum:",sum(even_list))
print("Odd list sum:",sum(odd_list))