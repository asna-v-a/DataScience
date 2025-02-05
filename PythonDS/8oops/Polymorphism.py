#Polymorphism : 'poly' means many and 'morphism' means forms

"""
single method, which acts in multiple ways

2 types
1.Overloading : same method name, different no of parameters ( work the largest numbered parameters)
2.Overriding :

python doesn't support overloading
"""
class Drinks:
    def temp(self):
        print("Temperature is 25 degrees")

class Soup:
    def temp(self):
        print("Temperature is 50 degrees")

d=Drinks()
s=Soup()
d.temp()
s.temp()

