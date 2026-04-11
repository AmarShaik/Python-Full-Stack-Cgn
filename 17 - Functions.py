#Functions
#a function is a block of organised, reusable code and that is used to perform a single or multiple tasks
#python use in-built functions like print, can make your function also, these are called user-defined functions
#function blocks beginning with the keyword def, followed by the function name paranthesis(())
'''a = 10
b = 20
print('sum is', a+b)
print('difference is', a-b)
print('product is' a*b)

a = 100
b = 200
print('sum is', a+b)
print('difference is', a-b)
print('product is' a*b)

a = 1000
b = 2000
print('sum is', a+b)
print('difference is', a-b)
print('product is' a*b)'''

'''def calculate(a,b):
    print('sum is', a+b)
    print('difference is', a-b)
    print('product is', a*b)
calculate(10, 20)
calculate(100, 200)
calculate(1000, 2000)'''

'''def calculate(a,b):
    print('division is', a//b)
    print('power is', a**b)
    print('modulus is', a%b)
calculate(6, 2)
calculate(6, 2)
calculate(6, 2)'''

'''def add(a,b):
    print(a+b)
add(4,5)'''

#run-time input
'''def cal():
    a = int(input())
    b = int(input())
    print(a+b)
cal()'''

'''def fullname():
    fname = input('')
    lname = input('')
    print((fname+lname).title())
fullname()'''

#print v/s return
#it just shows the user output in a console
#return is used to terminate a function and gives back a value form the function

'''def mul(a,b):
    print(a*b)
mul(4,5)'''

'''def mul(a,b):
    return a*b
print(mul(4,5))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,5)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c   #only prints the first return
    return d
    return e
print(cal(4,5))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(cal(4,5))'''

#Task-1
'''while True:
    def cal():
        a = int(input('enter a value:'))
        b = int(input('enter b value:'))
        option = int(input(choose a calculation:
                                1 - add
                                2 - sub
                                3 - mul))
        if option == 1:
            print(a+b)
        elif option == 2:
            print(a-b)
        elif option == 3:
            print(a*b)
        else:
            print('choose a correct option')
    print(cal())'''

#OR

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
a = int(input('a value:'))
b = int(input('b value:'))
option=int(input(choose an option
                                1. add
                                2. sub
                                3. mul))
if option == 1:
    add()
elif option == 2:
    sub()
elif option == 3:
    mul()'''

#Task-2
'''def split_bill():
    amount = int(input('enter the total amount:'))
    persons = int(input('enter total number of people:'))
    per_person = amount//persons
    print('Each person should pay:', per_person)
split_bill()'''

#OR

def split_bill():
    amount = int(input('enter the total amount:'))
    persons = int(input('enter total number of people:'))
    per_person = amount//persons
    print(f'Each person should pay: {per_person}')
split_bill()
