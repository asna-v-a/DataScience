class Employee:
    prof='Developer'
    company_name='IBM'
    def employeedetails(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age

    def printdetails(self):
        print("Employee ID:",self.id)
        print("First name:",self.fname)
        print("Last name:",self.lname)
        print("Age:",self.age)
        print("Profession:",Employee.prof)
        print("Company name:",Employee.company_name)
        print()



employee1=Employee()
employee1.employeedetails(101,'Asna','V A','23')
employee1.printdetails()

employee2=Employee()
employee2.employeedetails(102,'Sreyas','A','25')
employee2.printdetails()

employee3=Employee()
employee3.employeedetails(103,'Khajol','Manuel','23')
employee3.printdetails()

employee4=Employee()
employee4.employeedetails(104,'Anand','K V','25',)
employee4.printdetails()

employee5=Employee()
employee5.employeedetails(105,'Salman','A S','24')
employee5.printdetails()