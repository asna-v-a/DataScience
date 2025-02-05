class Student:
    college = 'CUSAT' #statc variable
    def studentdetails(self,id,fname,lname,age):
        self.id=id#instance variable
        self.fname=fname
        self.lname=lname
        self.age=age


    def printdetails(self):
        print("Student Id:",self.id)
        print("First Name:",self.fname)
        print("Last Name:",self.lname)
        print("Age:",self.age)
        print("College:",Student.college)#calling static variable
        print()

student1=Student()
student1.studentdetails(101,'Asna','V A','23')
student1.printdetails()

student2=Student()
student2.studentdetails(102,'Sreyas','A','25')
student2.printdetails()

student3=Student()
student3.studentdetails(103,'Khajol','Manuel','23')
student3.printdetails()

student4=Student()
student4.studentdetails(104,'Anand','K V','25',)
student4.printdetails()

student5=Student()
student5.studentdetails(105,'Salman','A S','24')
student5.printdetails()