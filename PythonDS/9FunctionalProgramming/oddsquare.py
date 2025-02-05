lst=[1,2,3,4,5,6,7,8,9,10]
f1=list(filter(lambda num:num%2,lst))
f2=list(map(lambda num:num**2,f1))
print(f2)

f=list(map(lambda num:num**2,list(filter(lambda num:num%2,lst))))
print(f)

