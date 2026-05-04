#Email automation
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
        
