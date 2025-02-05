f = open('wordcount', 'r')
dic = {}
data=''
for i in f:
    data = i.rstrip('\n').split(' ')

    for j in data:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+= 1

print(dic)
print(sum(dic.values()))