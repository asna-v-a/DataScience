f = open("C:/Users/asnav/Desktop/Task/temper.txt", 'r')
dic = {}
data=''
for i in f:
    data = i.rstrip('\n').split(',')
    location=data[0]
    temp=data[-1]
    if location not in dic:
        dic[location]=temp
    else:
        old=dic[location]
        if old<temp:
            dic[location]= temp
print("District : Temperature")
for k,v in dic.items():
    print(k," : ",v)

