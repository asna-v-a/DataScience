#Attendance

class_held = int(input("Enter the number of class held: "))
class_attended = int(input("Enter the number of class attended: "))

attendance_per = class_attended/class_held * 100
print("Attendance percentage :",round(attendance_per),"%")

if attendance_per >= 75:
    print("You are eligible for exam")
else:
    print("You are not eligible for exam")