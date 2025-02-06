#Calculate Electricity bill

unit = int(input("Enter the units used: "))

if(unit <= 100):
    bill = 0
elif(unit >= 101) & (unit <= 200):
    bill = (unit - 100) * 5
else:
    bill = 500 + (unit - 200) * 10

print("Bill amount:",bill)