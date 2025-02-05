print("Problem 1")
lst=[15,20,25,30,35,40,50]
print(lst[-2]+lst[-0]+lst[1])
print()
print("Problem 2")
lst=[15,3,10,6,9,7]
result=sum(lst)
lst1=[]
for i in lst:
    lst1.append(result-i)
print(lst1)
print()
print("Problem 3")
lst=[1,3,8,6,5,3,2,4,6,8,9,7,5,4,8,9,12]
lst1=[]
for i in range(0,len(lst)-1):
    if(lst[i-1]<lst[i]>lst[i+1]) or (lst[i-1]>lst[i]<lst[i+1]):
        lst1.append(lst[i])
print(lst1)

