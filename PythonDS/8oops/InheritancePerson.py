class Person:
    def getdetails(self,fname,lname,age,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc

class Employee(Person):
    def professionaldetails(self,id,prof,exp,salary):
        self.id=id
        self.prof=prof
        self.exp=exp
        self.salary=salary

    def printdetails(self):
        print("Employee ID: ",self.id)
        print("First name: ",self.fname)
        print("Last name: ",self.lname)
        print("Age: ",self.age)
        print("Profession: ",self.prof)
        print("Salary: ",self.salary)
        print("Experience: ",self.exp)
        print("Location: ",self.loc)
        print()


employee1=Employee()
employee1.getdetails('Arun','VA',23,'Thrissur')
employee1.professionaldetails(101,'Developer',3,50000)
employee1.printdetails()

employee1=Employee()
employee1.getdetails('Varun','K',25,'Ernakulam')
employee1.professionaldetails(102,'Software Engineer',5,80000)
employee1.printdetails()

employee1=Employee()
employee1.getdetails('Arya','T',30,'Palakkad')
employee1.professionaldetails(103,'HR',8,100000)
employee1.printdetails()
