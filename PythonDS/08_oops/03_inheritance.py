"""

Inheritance:
- A class extracts features from another class, min 2 class : parent class and child class.
- The class being inherited from is the Parent Class.
- The class that inherits is the Child Class.


Types of Inheritance:
1. Single Inheritance - One parent, one child.
2. Multiple Inheritance - One child, multiple parents.
3. Multilevel Inheritance - A class inherits from another child class.
4. Hierarchical Inheritance - One parent, multiple children.
5. Hybrid Inheritance - A combination of two or more types of inheritance.

"""

# 1. SINGLE INHERITANCE (One Parent, One Child)

print("\n--- Single Inheritance ---")

class Animal:  # Parent Class
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Child Class inheriting from Animal
    def bark(self):
        print("Dog barks")

# Object of Child Class
dog1 = Dog()
dog1.speak()  # Calling parent class method
dog1.bark()   # Calling child class method



# 2. MULTIPLE INHERITANCE (One Child, Multiple Parents)

print("\n--- Multiple Inheritance ---")

class Parent1:
    def feature1(self):
        print("Feature from Parent1")

class Parent2:
    def feature2(self):
        print("Feature from Parent2")

class Child(Parent1, Parent2):  # Child class inheriting from multiple parents
    def feature3(self):
        print("Feature from Child")

# Object of Child Class
child1 = Child()
child1.feature1()  # Access Parent1 method
child1.feature2()  # Access Parent2 method
child1.feature3()  # Access Child method


# 3. MULTILEVEL INHERITANCE (Grandparent → Parent → Child)

print("\n--- Multilevel Inheritance ---")

class Grandparent:
    def grand_method(self):
        print("Grandparent method")

class Parent(Grandparent):  # Inherits from Grandparent
    def parent_method(self):
        print("Parent method")

class Child(Parent):  # Inherits from Parent (which already inherited Grandparent)
    def child_method(self):
        print("Child method")

# Object of Child Class
child2 = Child()
child2.grand_method()  # Grandparent method
child2.parent_method()  # Parent method
child2.child_method()  # Child method



# 4. HIERARCHICAL INHERITANCE (One Parent, Multiple Children)

print("\n--- Hierarchical Inheritance ---")

class Vehicle:  # Parent Class
    def start(self):
        print("Vehicle started")

class Car(Vehicle):  # Child 1
    def car_feature(self):
        print("Car has 4 wheels")

class Bike(Vehicle):  # Child 2
    def bike_feature(self):
        print("Bike has 2 wheels")

# Objects of Child Classes
car1 = Car()
bike1 = Bike()

car1.start()       # Inherited from Vehicle
car1.car_feature()

bike1.start()      # Inherited from Vehicle
bike1.bike_feature()



# 5. HYBRID INHERITANCE (Combination of Multiple Inheritance Types)

print("\n--- Hybrid Inheritance ---")

class Engine:
    def engine_type(self):
        print("Engine Type: Diesel")

class Car(Vehicle, Engine):  # Car inherits from Vehicle and Engine (Multiple Inheritance)
    def car_details(self):
        print("Car Model: SUV")

# Object of Hybrid Class
car2 = Car()
car2.start()       # From Vehicle
car2.engine_type() # From Engine
car2.car_details() # Own Method

"""
OUTPUT:

--- Single Inheritance ---
Animal makes a sound
Dog barks

--- Multiple Inheritance ---
Feature from Parent1
Feature from Parent2
Feature from Child

--- Multilevel Inheritance ---
Grandparent method
Parent method
Child method

--- Hierarchical Inheritance ---
Vehicle started
Car has 4 wheels
Vehicle started
Bike has 2 wheels

--- Hybrid Inheritance ---
Vehicle started
Engine Type: Diesel
Car Model: SUV

"""