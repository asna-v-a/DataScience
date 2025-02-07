#Nested list : list inside a list

lst =[[101,'vinay','k',28,'bigdata',1000]
    ,[102,'arjun','p',30,'python',1500]
    ,[103,'vimal','p',27,'bigdata',2000]
    ,[104,'vineeth','s',31,'testing',1750]
    ,[105,'naveen','r',29,'python',1800]]
print(lst)
print()

for i in lst:
    print(i)
print()

for i in lst:
    if i[3]>28:
            print(i)

print()
print(lst[0])

print()
for i in lst:
    if i[3]==30:
            print(i[1:5])

print()
for i in lst:
    if i[4]=='bigdata':
            print(i[1::2])

print()
for i in lst:
    if i[3]>28 and i[4]=='python': # in some case & won't support int and str together , use 'and' instead.
            print(i[1:4])

print()
total=0
for i in lst:
    total+=i[-1]
print("Total salary:",total)