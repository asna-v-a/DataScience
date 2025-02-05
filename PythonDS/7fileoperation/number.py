f=open('number','r')
lst=[]
for i in f:
    data=i.rstrip('/n')
    lst.append(int(data))

print(lst)
print(sum(lst))