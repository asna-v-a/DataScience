#Abstraction

"""

"""
from abc import ABC, abstractmethod


# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass  # Abstract method, must be implemented by subclasses


# Concrete Class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)


# Concrete Class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Concrete Class for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Instantiate and use the classes
shapes = [
    Circle(radius=5),
    Rectangle(length=10, width=4),
    Triangle(base=6, height=3)
]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.calculate_area()}")
