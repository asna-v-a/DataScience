
f = open("C:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/customer.txt",'r')

#Dancer prof, fname, lname, age
"""
for i in f:
    data=i.rstrip('\n').split(',')
    prof = data[4]
    if prof=='Dancer':
        print(data[1:4])
"""

#age above 50 , fname, lname, age, prof
"""
for i in f:
    data=i.rstrip('\n').split(',')
    age = data[3]
    if age>'50':
        print(data[1:4])
"""

#age range 25 to 40 , fname, lname, age, prof
"""
for i in f:
    data=i.rstrip('\n').split(',')
    age = data[3]
    if age>'25' and age<'40':
        print(data[1:4])
"""

#India work , fname, lname, age, prof
"""
for i in f:
    data=i.rstrip('\n').split(',')
    location = data[-1]
    if location =='india':
        print(data[1:4])
"""

#India work and age above 50 , fname, lname, age
"""
for i in f:
    data=i.rstrip('\n').split(',')
    age = data[3]
    location = data[-1]
    if location =='india' and age>'50':
        print(data[1:4])
"""

#India work and prof dancer , fname, lname, age
"""
for i in f:
    data=i.rstrip('\n').split(',')
    age = data[3]
    prof = data[4]
    if prof =='Dancer' and age>'50':
        print(data[1:4])
"""

#Pilot prof,  fname, lname, age
"""
for i in f:
    data=i.rstrip('\n').split(',')
    prof = data[4]
    if prof =='Pilot':
        print(data[1:4])
"""

#Pilot prof and age above 40,  fname, lname, age
"""
for i in f:
    data=i.rstrip('\n').split(',')
    age = data[3]
    prof = data[4]
    if prof =='Pilot' and age>'40':
        print(data[1:4])
"""

#US work,  fname, lname, age
"""
for i in f:
    data=i.rstrip('\n').split(',')
    location = data[-1]
    if location=='us':
        print(data[1:4])
"""

#US work and age above 50,  fname, lname, age
"""
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    location = data[-1]
    if location=='us' and age>'50':
        print(data[1:4])
"""

#each location count
"""
dic = {}
data=''
lst=[]
for i in f:
    data=i.rstrip('\n').split(',')
    lst.append(data[-1])

for j in lst:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+= 1

print(dic)
"""
"""
dic = {}
for i in f:
    data=i.rstrip('\n').split(',')
    location = data[-1]
    if location not in dic:
        dic[location]=1
    else:
        dic[location]+= 1

print(dic)
"""

#each profession count
"""
dic = {}
data=''
lst=[]
for i in f:
    data=i.rstrip('\n').split(',')
    lst.append(data[4])

for j in lst:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+= 1

print(dic)
"""
"""
dic = {}
for i in f:
    data=i.rstrip('\n').split(',')
    prof = data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+= 1

print(dic)
"""

#each age count
"""
dic = {}
lst=[]
for i in f:
    data=i.rstrip('\n').split(',')
    lst.append(data[3])

for j in lst:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+= 1

print(dic)
"""
dic = {}
for i in f:
    data=i.rstrip('\n').split(',')
    age = data[3]
    if age not in dic:
        dic[age]=1
    else:
        dic[age]+= 1

print(dic,'\n')
print("Age : Count")

for k,v in dic.items():
    print(k," : ",v)