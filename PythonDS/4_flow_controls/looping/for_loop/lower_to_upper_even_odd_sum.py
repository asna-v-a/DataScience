# Program to Calculate the Sum of Even and Odd Numbers in a Given Range

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

even_sum =0
odd_sum=0

for i in range(lower,upper+1):
    if(i%2==0):
        even_sum+=i
    elif(i%2==1):
        odd_sum+=i
    else:
        print("Invalid")

print("Odd sum: ",odd_sum)
print("Even sum: ",even_sum)