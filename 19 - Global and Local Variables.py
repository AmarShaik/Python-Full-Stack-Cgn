#Global and Local Variables
#variable outside and inside the function is called global and local variables
#A variable define above the functions and is accessible to the entire global space is called global variable
#A variable inside the function is called local variable

#first case of global variable
'''a = 3
def check1():
    print("inside value is", a)
check1()
print("outside value is", a)

#Output:
inside value is 3
outside value is 3'''

#second case of global variable
'''a = 4
def check2():
    a = 5
    a=a**2
    print("inside value is", a)
check2()
print("outside value is", a)

#Output:
inside value is 25
outside value is 4'''

#third case of both global and local variables
'''a = 5
b = 9
def check3():
    a = 7
    print("inside valus is", a)
    a = 10
    print("updated value is", a+5)
    b = 12 #local variable
    b = b + a
    print("value of b is", b)
check3()
print("a value is", a)
print("b value is", b)

#Output:
inside valus is 7
updated value is 15
value of b is 22
a value is 5
b value is 9'''

#usage of global keyword
#When user wants to access the global variable inside the function directly and carry forward the updated value even outside the function then we need to use global keyword
a = 5
b = 12
def final():
    global a, b
    print("inside value is", a)
    a = 10
    print("updated value is", a)
    b = 15
    b = b + a
    print("value of b is", b)
final()
print("a value is", a)
print("b value is", b)
