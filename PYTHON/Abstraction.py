#Abstraction
#The process of handling complexity by hiding unnecessary information from a user is called abstraction

#abstract method
#if the method is declared without implementation is called abstract method

#abstract class
#if a class contain one or more than one abstract method then the class is called abstract class


'''class A():
    def method(self):
        pass
obj1=A()
obj1.method()'''

'''class A():
    def method(self):
        print("data")
obj1=A()
obj1.method()'''

'''from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is impelmented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''

#BMI Calculator
'''height = float(input("Enter height: "))
weight = float(input("Enter weight: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.5:
    print("You have a normal weight.")
elif 24.5 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")'''

'''#Email automation
#simple otp
import random
import math
import smtplib
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
email = input("Enter the mail to send OTP: ")
msg = OTP
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("shaikamar907@gmail.com", "yqlh iwfx otmi pamw")
user = "shaikamar907@gmail.com"
s.sendmail(user, email, msg)
while True:
    otp = input("Enter the OTP: ")
    if otp == OTP:
        print("Login successful")
        break
    else:
        print("Incorrect OTP")
'''
