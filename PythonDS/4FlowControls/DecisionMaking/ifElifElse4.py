#Grade Calculation
sub1 = int(input("Enter the subject1 marks: "))
sub2 = int(input("Enter the subject2 marks: "))
sub3 = int(input("Enter the subject3 marks: "))
sub4 = int(input("Enter the subject4 marks: "))

total = sub1 + sub2 + sub3 + sub4
print("Total marks:",total)

if total >= 180:
    print("Grade : A+")
elif (total >= 160) & (total <=179):
    print("Grade : A")
elif (total >= 140) & (total <=159):
    print("Grade : B+")
elif (total >= 120) & (total <=139):
    print("Grade : B")
elif (total >= 100) & (total <=119):
    print("Grade : C+")
elif (total >= 80) & (total <=99):
    print("Grade : C")
else:
    print("Failed")