def biggest_odd(num):
    lst=[]
    for i in num:
        if int(i)%2==1:
            lst.append(i)
    lst.sort(reverse=True)
    return lst[0]

number =input("Enter the number: ")
result=biggest_odd(number)
print(result)