class Person:

    def __init__(self, fname, lname, age, loc):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.loc = loc

    def printvalue(self):
        print("Firstname:",self.fname)
        print("Lastname:",self.lname)
        print("Age:",self.age)
        print("Location:",self.loc)

person1 = Person('Vinay','S',28,'Ernakulam')
person1.printvalue()

person2 = Person('Anu','K',26,'Thrissur')
person2.printvalue()