#Test - 4
#1 
'''class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length*self.width
        return area
a = Rectangle(5,4)
print(a.area())'''

#2
'''class Father():
    def skill(self):
        print("Driving")
class Mother():
    def skill(self):
        print("Cooking")
class Child(Father, Mother):
    def skill(self):
        print("Driving+Cooking")
a = Father()
a.skill()
b = Mother()
b.skill()
c = Child()
c.skill()'''

#3
'''class Dog():
    def speak(self):
        print("Bow Bow")
class Cat():
    def speak(self):
        print("Meow")
class Cow():
    def speak(self):
        print("Maaa")
a = Dog()
a.speak()
b = Cat()
b.speak()
c = Cow()
c.speak()'''

#4
'''class Calculator():
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b
calc = Calculator()
print(calc.add(10, 20)) 
print(calc.add(10, 20, 30)) '''

#5
class Bank():
    def roi(self):
        return "5%"
class SBI():
    def roi(self):
        return "6%"
a = Bank()
print(a.roi())
b = SBI()
print(b.roi())
