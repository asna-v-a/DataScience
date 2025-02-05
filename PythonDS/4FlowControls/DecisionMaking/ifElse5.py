#Bonus calculation
salary = int(input("Enter your salary: "))
year_exp = int(input("Enter year of experience: "))

if year_exp >= 5:
    bonus = salary*5/100
    print("Your Net bonus is",round(bonus))
else:
    print("Not eligible")