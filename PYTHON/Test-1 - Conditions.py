#10/4/26
#1. Classify numbers as small/medium/large
# n = int(input("Enter a number: "))
# if n<10:
#     print("Small")
# elif n in range(10, 999):
#     print("Medium")
# elif n>=1000:
#     print("Large")

#2. Loan eligibility - salary>=30000 and age between 21 and 60
# while True:
#     salary = int(input("Enter salary: "))
#     if salary >= 30000:
#         print("Sufficient Salary")
#         age = int(input("Enter your age: "))
#         if age in range(21, 61):
#             print("Eligible for Loan")
#         else:
#             print("Not Eligible")
#     else:
#         print("Not Eligible")

#3. Frequency type
'''input_string = input("Enter a string: ")
input_char = input("Enter the character to count: ")
count = input_string.count(input_char)
if count in range(3):
    print(count)
    print("Low Frequency")
elif count in range(3, 4):
    print(count)
    print("Medium Frequency")
elif count>=5:
    print(count)
    print("High Frequency")
else:
    print("No frequency found")'''

#4. Validate Email Format(Contains '@' and '.')
'''mail = input("Enter mailid: ")
if '@' and '.' in mail:
    print("Valid Email")
else:
    print("Not Valid")'''

#5. Anagrams
'''a = input("Enter string a: ")
b = input("Enter string b: ")
if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("Not an Anagram")'''

#6. Mobile Number is valid(10 digits & starts with 6 or 7 or 8 or 9)
'''a = input("Enter mobile number: ")
if len(a)==10 and a[0] in "6789":
    print("Valid Mobile Number")
else:
    print("Not Valid")'''

#7. Prime Number and Count
'''n = int(input("Enter a number: "))
count = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i%j==0:
            break
    else:
        count+=1
        print(i)
print("The no.of primes is",count)'''

#8. uppercase, lowercase, digit, srecial characters
'''n = input("Enter a string: ")
if n.isupper():
    print("Uppercase Letter")
elif n.islower():
    print("Lowercase Letter")
elif n.isdigit():
    print("Digit")
else:
    print("Special Character")'''

#9. contains 'a'
'''n = input("Enter a string: ")
if 'a' in n:
    print("Contains 'a'")
else:
    print("Does not contain 'a'")'''

#10. Smallest of 2 numbers
'''a = int(input("a: "))
b = int(input("b: "))
if a>b:
    print(f"{b} is smaller")
elif a<b:
    print(f"{a} is smaller")
else:
    print("Both are equal")'''
