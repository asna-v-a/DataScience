#Polymorphism

"""
- 'Poly' means many, and 'Morphism' means forms.
- A single method can behave differently in multiple classes.

Types of Polymorphism:
   1 Method Overloading: 
     - Same method name but different number of parameters.
     - Python does not support method overloading directly.
     - Can be achieved using default arguments or variable-length arguments.

   2 Method Overriding: 
     - A child class provides a different implementation of a method from the parent class.

Example:
A Drinks class and a Soup class both have a `temp()` method, but each provides a different implementation.
"""

# Method Overriding Example
class Drinks:
    def temp(self):
        print("Drinks: Temperature is 25 degrees")

class Soup:
    def temp(self):
        print("Soup: Temperature is 50 degrees")

# Object Creation
d = Drinks()
s = Soup()

# Calling the same method but different outputs (Polymorphism)
d.temp()
s.temp()

"""
Output:
Drinks: Temperature is 25 degrees
Soup: Temperature is 50 degrees
"""


# Method Overloading (Achieved using Default Arguments)
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Object Creation
calc = Calculator()
print("Sum (2 numbers):", calc.add(5, 10))       # 2 parameters
print("Sum (3 numbers):", calc.add(5, 10, 15))   # 3 parameters

"""
Output:
Sum (2 numbers): 15
Sum (3 numbers): 30
"""

# Method Overriding Example
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

# Object Creation
a = Animal()
dog = Dog()
cat = Cat()

# Calling overridden method
a.make_sound()  # Output: Animal makes a sound
dog.make_sound()  # Output: Dog barks
cat.make_sound()  # Output: Cat meows
