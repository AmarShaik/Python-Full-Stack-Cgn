#method overloading
'''class new():
    def sum(self, a = None, b = None, c = None):
        if a!=None and b!=None and c!=None:
            print("The sum is", a+b+c)
        elif a!=None and b!=None:
            print("Product is", a*b)
        else:
            print("Program ends..."ArithmeticError)
a = new()
a.sum()
a.sum(2,4,5)
a.sum(5,6)'''

#method overriding
'''class Animal():
    def speak(self):
        print("Animal can make sounds")
class Dog():
    def speak(self):
        print("Dog barks")
a = Animal()
b = Dog()
a.speak()
b.speak()'''

#Task
class Vehicle():
    def travel(self):
        print("Vehicles is used for transport")
class Car():
    def travel(self):
        print("Car is used to travel on roads")
class Ship():
    def travel(self):
        print("Ship is used to travel on seaways")
class Plane():
    def travel(self):
        print("Planes is used to travel on air")
a = Vehicle()
b = Car()
c = Ship()
d = Plane()
a.travel()
b.travel()
c.travel()
d.travel()
