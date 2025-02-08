"""
OOPS Properties

1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction


1. Inheritance : A class extracting features of another class ,min 2 class : parent class and child class
                child-class inherit features of parent class

types:
1. single
2. multiple : child has more than 1 parent
3. multilevel : child has a parent and child at as a parent for another child class


"""

#Single Inheritance
class A:# parent class or base class
    def printa(self,num):
        self.num=num
        print("Inside class A",self.num)

class B(A):#child class or derived class
    def printb(self,num):
        self.num=num
        print("Inside class B",self.num)

obj1=B()
obj1.printa(40)
obj1.printb(30)
