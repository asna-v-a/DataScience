x=0
for i in range(10):
    for j in range(-1,-10,-1):
        x+=1
print(x)
print()



a,b = 5,12
c = -1
if c:# if condition gives number(non zero) greater than or less than 0 , it'll be true always(False when 0)
    print("Hello")
else:
    print("hai")

print()

x=0
a=0 #a=0,b=-5 -> 2, a=5,b=5 -> 3, a=
b=-5
if a>0:
    if b<0:
        x+= 5
    elif a>5:
        x+=4
    else:
        x+=3
else:
    x+=2
print(x)
print()