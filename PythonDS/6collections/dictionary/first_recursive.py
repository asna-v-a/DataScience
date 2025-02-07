#Find first recurring character

pattern = 'ABDFGBASDFGTFVB'

dic={}
dic2={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print(i,"is first recursive")
        break

print(pattern)
for i in pattern:
    if i in dic2:
        dic2[i]+=1
    else:
        dic2[i]=1
print(dic2)