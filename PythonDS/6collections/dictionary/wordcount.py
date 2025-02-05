# count of each words in a sentence

line='cat rat bat rat bat cat rat rat bat rat'
dic={}

data=line.split(' ')
print(data)

for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
