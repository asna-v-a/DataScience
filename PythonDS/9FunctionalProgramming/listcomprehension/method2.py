#method2
#1-50 even numbers
lst=[i for i in range(1,51) if i%2==0]
print(lst)

#1-30 divisible by 5
lst=[i for i in range(1,31) if i%5==0]
print(lst)

#1-25 odd numbers square
lst=[(i,i**2) for i in range(1,26) if i%2]
print(lst)

#1-50 divisible by 2 and 5
lst=[i for i in range(1,51) if i%2==0 and i%5==0]
print(lst)

