#Encapsulation
"""
bind properties and methods together
Protect data from unauthorised access
increase security
cant be edited
encapsulation is implemented using:( access modifiers)
1. public members: accessible from anywhere
2.protected members : indicate with single underscore _ , can only access within the class or its subclass
3.private members :  indicate with double underscore __ , cant access directly from outside the class
"""
#private member
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def getbalance(self):
        return self.__balance
account=BankAccount(1000)
account.deposit(1000)
print(account.getbalance())
#public members
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def getname(self):
        return self.__name
person=Person('Asna',23)
