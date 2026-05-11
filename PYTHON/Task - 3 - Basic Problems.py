# armstrong number
# prime number
# fibonocci
# palindrome
# anagram
# 8-digits password - Uppercase, lowercase, digit, special character
#reverse a number without converting into string
#patterns - diamond, bow-arrow, increasing order or numbers, alphabets


#armstrong number
'''
num = int(input("Enter a number: "))
sum = 0
digits = len(str(num))
for i in str(num):
   sum += int(i) ** digits
if num == sum:
   print(num, "is an armstrong number")
else:
   print(num, "is not an armstrong number")'''


#prime number
'''
n = int(input("Enter a number: "))
if n > 1:
   for i in range(2, n):
       if n % i == 0:
           print(n, "is not a prime number")
           break
   else:
       print(n, "is a prime number")'''

#fibonocci
'''
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    print("Fibonacci sequence:")
    for i in range(n):
        print(a)
        a, b = b, a + b'''

#palindrome
'''
text = input("Enter a string: ")
rev = ""
for i in text:
    rev = i + rev
if text == rev:
    print("It is palindrome")
else:
    print("Not a palindrome")'''

#anagram
'''
str1 = input("Enter string1: ")
str2 = input("Enter a string2: ")
if sorted(str1) == sorted(str2):
    print("It is an anagram")
else:
    print("Not an anagram")'''

#8-digits password - Uppercase, lowercase, digit, special character

pwd = input("Enter a password: ")
if len(pwd) == 8:
   if (any(char.isupper() for char in pwd) and any(char.islower() for char in pwd) and 
       any(char.isdigit() for char in pwd) and any(char in "!@#$%&-_'\",.<>?/" for char in pwd)):
       print("Valid password") 
else:
    print("Invalid password")