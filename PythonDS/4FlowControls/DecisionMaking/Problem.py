# input
"""
1.Current year
2.Current month - number
3.Current date
4.Birth year
5.Birth month
6.Birth date

age = ?

check year, month and date
eg: 2024 10 29
"""

current_year = int(input("Enter the current year: "))
current_month = int(input("Enter the current month: "))
current_date = int(input("Enter the current date: "))

birth_year = int(input("Enter the birth year: "))
birth_month = int(input("Enter the birth month: "))
birth_date = int(input("Enter the birth date: "))

if (current_year == birth_year):
    age = 0
elif (current_year > birth_year):
    if (current_month == birth_month):
        if (current_date >= birth_date):
            age = current_year - birth_year
        else:
            age = current_year - birth_year - 1
    elif (current_month > birth_month):
        age = current_year - birth_year
    else:
        age = current_year - birth_year - 1
else:
    age = "Invalid"
print("Age:", age)
