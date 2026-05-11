#inheritance
#3 - types - single, multiple, multilevel

#single inheritance
'''class RBI():    #parent class
    cash = 100000
    def available_cash(cls):
        print("available cash is", cls.cash)
        print("available cash is", RBI.cash)
class SBI(RBI):  #child class-1
    pass
class HDFC(RBI):
    cash = 50000
    def new_cash(cls):
        print("new cash is", cls.cash+cls.cash)
        print("new cash is", cls.cash+RBI.cash)
a = HDFC()
a.available_cash()
a.new_cash()'''

#multiple inheritance
'''class Father():
    height = 170
    def f_height(self):
        print("Father height: ", self.height)
class Mother():
    weight = 60
    def w_weight(self):
        print("Mother weight: ", self.weight)
class Kid(Father, Mother):
    dob = "29-Feb-2004"
    def k_dob(self):
        print("DOB: ", self.dob)
k = Kid()
k.f_height()
k.w_weight()
k.k_dob()'''

#multi-level inheritance
'''class grandparent():
    def land(self):
        print("Grandparents have acres of land")
class parent(grandparent):
    def house(self):
        print("Parents own a house")
class child(parent):
    def vehicle(self):
        print("Child owns a car")
c = child()
c.land()
c.house()
c.vehicle()'''

# multi-level inheritance for dog breeds
'''class Dog:
    def traits(self):
        print("Dogs are loyal and friendly animals")
class Rottweiler(Dog):
    def breed(self):
        print("Ferocious and strong dogs")
class Greyhound(Dog):
    def breed(self):
        print("Greyhounds are fast dogs")
class Doberman(Greyhound, Rottweiler):
    def breed_trait(self):
        print("Doberman is frocious, quick and loyal dog")
d = Doberman()
d.traits()
d.breed()
d.breed_trait()'''

#super()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent class is implemented")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child class is implemented")
a=child("amar",21)
print(a.name)
print(a.age)'''

#encapsulation
#having multiple concepts into a single one is called encapsulation
#3 - types - publicdata(), __privatedata(), _protecteddata()

#publicdata()
'''class parent():
    publicdata=10
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj=child()
obj.method1()
obj.method2()
print(obj.publicdata)'''

#_protecteddata()
'''class parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj=child()
obj.method1()
obj.method2()'''

#__privatedata()
'''class parent():
    __privatedata="amar"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj=child()
obj.method1()
obj.method2()'''
