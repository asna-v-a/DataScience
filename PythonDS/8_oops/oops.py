# Object Oriented Programming

"""
class : A base model or blueprint
object : Used to build the base model
reference : Operations done over the objects

example:
class: mobile phone
object: iphone, samsung, oppo, realme, vivo, nothing,.........
reference: call, photo, video, text,............

constructor : initializing variables while creating objects

function in a class is called method, variables defined in a method will be instance variables
class name starts with uppercase
self(can also use this instead) is an instance keyword: to create an instance variable (can be used in other methods in the class)
(instance: value different)
static variable : constant value, static variable is called using class name Eg: Student.college
(Student: class, college: static variable)



Key OOP Concepts:

1. Class - A blueprint or template for creating objects.
2. Object - An instance of a class.
3. Reference - Used to perform operations on an object.
4. Method - A function inside a class.
5. Instance Variables - Variables that belong to an object (different for each object).
6. Static Variables - Shared variables across all instances of a class.
7. Constructor (__init__) - Initializes instance variables when an object is created.
"""

class A:
    # Static variable (shared by all instances)
    category = "Book"  # This remains constant for all objects of class A

    def printA(self):
        print(f"Reading a {A.category}")

    def printB(self):
        print(f"Writing a {A.category}")

# Creating objects (instances of class A)
obj1 = A()
obj1.printA()
obj1.printB()

obj2 = A()
obj2.printA()
obj2.printB()

# Accessing the static variable
print("Static Variable:", A.category)

"""
Explanation:

1. Class A is defined with a static variable category = "Book".
2. Methods printA and printB print reading and writing messages.
3. Objects obj1 and obj2 are created from class A.
4. Static Variable A.category is accessed using the class name.
5. The output remains the same across instances since static variables are shared.

"""