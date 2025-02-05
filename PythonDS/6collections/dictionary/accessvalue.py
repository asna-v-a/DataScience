dic={'id':101,'fname':'vinay','lname':'k','age':28,'profession':'bigdata'}

print(dic['fname'])
print(dic['lname'])
print(dic['age'])
print()


for i in dic:
    print(i,":",dic[i])

#update value
dic['age']=10
print(dic)

dic['age']+=10
print(dic)

# to add new key-value pair
dic['marks']=100
print(dic)

print('age' in dic)
print('age' not in dic)
print('fname' in dic)
print('lname' not in dic)
print('location' not in dic)

#delete key-value pair
del dic['id']
print(dic)