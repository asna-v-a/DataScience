# Object Oriented Programming

"""
class : A base model or blueprint

object : Used to build the base model

reference : Operations done over the objects

example:

class: mobile phone
object: iphone, samsung, oppo, realme, vivo, nothing,.........
reference: call, photo, video, text,............


constructor : initialising variables while creating objects
Eg in person



"""

#function in a class is called method, variables defined in a method will be instance variable
#class name starts with uppercase
#self(can also use this instead) is an instance keyword: to create an instance variable (can be used in other methods in the class)
# (instance: value different)
#static variable : constant value , static variable is called using class name Eg:Student.college
# (Student: class, college: static variable)

class A:
    def printA(self):
        print("Reading a book")

    def printB(self):
        print("Writing a book")

ohj1=A()
ohj1.printA()
ohj1.printB()

ohj2=A()
ohj2.printA()
ohj2.printB()
