f = open("C:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/temper.txt", 'r')

dic = {}
data=''

for i in f:
    data = i.rstrip('\n').split(',')
    location=data[0]
    temp=data[-1] # Convert to integer for correct comparison
    if location not in dic:
        dic[location]=temp
    else:
        old=dic[location]
        if old<temp:
            dic[location]= temp

print("District : Temperature")

for k,v in dic.items():
    print(k," : ",v)

