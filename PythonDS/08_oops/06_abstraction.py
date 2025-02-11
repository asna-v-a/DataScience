# Abstraction

"""
1. - Hiding implementation details and showing only essential features.
   - Achieved using abstract classes and abstract methods.
   - Prevents object instantiation of abstract classes.
   - Must be implemented by child classes.

Example:  
Consider a `Shape` class, which has a `calculate_area()` method.  
We don’t define how the area is calculated but ensure that every specific shape (like Circle, Rectangle, or Triangle)
must provide its own implementation.
"""

from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):  
    @abstractmethod
    def calculate_area(self):
        """Abstract method that must be implemented by subclasses"""
        pass  

# Concrete Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

# Concrete Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Concrete Class: Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Object Creation and Calculation
shapes = [
    Circle(radius=5),
    Rectangle(length=10, width=4),
    Triangle(base=6, height=3)
]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.calculate_area()}")
