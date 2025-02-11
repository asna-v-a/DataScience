#Encapsulation

"""
   - Binding properties (variables) and methods (functions) together in a class.  
   - Protects data from unauthorized access.  
   - Increases security by restricting modifications.  

Access Modifiers in Python:  
   1. Public Members: Accessible from anywhere (no underscore).  
   2. Protected Members: Indicated with a single underscore `_`, accessible only within the class and its subclasses.  
   3. Private Members: Indicated with double underscores `__`, not accessible directly from outside the class.  

Example:  
A BankAccount class where balance should not be modified directly but only through deposit and withdrawal methods.
"""

# Private Members (Encapsulation in a BankAccount)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        """Retrieve account balance"""
        return self.__balance

# Object Creation
account = BankAccount(1000)
account.deposit(1000)  
print("Current Balance:", account.get_balance())  # Accessing private variable using a method

# Public Members (Accessible from anywhere)
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.age = age  # Public attribute

    def get_name(self):
        """Retrieve private name attribute"""
        return self.__name

# Object Creation
person = Person("Asna", 23)
print("Person Name:", person.get_name())  # Accessing private variable using a method
print("Person Age:", person.age)  # Public attribute can be accessed directly
