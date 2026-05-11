#generators
#no tuple comprehension in above cases if we remove those braces and keep paranthesis and then the outcome is generator

#ex - list comprehension
'''a = [i for i in range(16)]
print(a)
print(type(a))

#Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
<class 'list'>'''

'''a = (i for i in range(16))
print(*a) #should use '*' to print if it is in generator
print(type(a))

#Output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
<class 'generator'>'''

'''a = (i for i in range(16))
#print(*a)
#print(list(a))
#op: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(tuple(a))
#op: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

#print(set(a))
#op: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}'''

#A generator is also a function which can be used as an iterator(loop) by producing group of values, where we use yield keyword
#yield v/s return
#return will terminate the function whereas yield can pass the function and go on with every successive iteration

'''a, b = [int(x) for x in input("enter the values").split(",")]
def check(a, b):
    while a<b:
        yield a
        a = a + 1
        yield a
print(*check(a, b))

#op: 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10'''

'''a, b = [int(x) for x in input("enter the values").split(",")]
def check(a, b):
    while a<b:
        yield a
        a = a + 1
        #yield a
print(*check(a, b))

#op: enter the values2, 10
#2 3 4 5 6 7 8 9'''


'''a, b = [int(x) for x in input("enter the values").split(",")]
def check(a, b):
    while a<b:
        #yield a
        a = a + 1
        yield a
print(*check(a, b))

#op: enter the values2, 10
#3 4 5 6 7 8 9 10'''

'''a, b = [int(x) for x in input("enter the values").split(",")]
def check(a, b):
    while a<b:
        a=a+1
        return a
print(check(a, b))

#op: enter the values2, 10
#3'''

'''a, b = [int(x) for x in input("enter the values").split(",")]
def check(a, b):
    while a<b:
        a=a+1
    return a
print(check(a, b))

#op: enter the values2, 10
#10'''

#yield v/s return
'''def mygen():
    return "python"
    return "java"
    return "ds"
    return "python", "java", "ds"
print(*mygen())'''

def mygen():
    yield "vja"
    yield "hyd"
    yield "vzg"
print(*mygen())

#op: vja hyd vzg

#next() - to print one by one
d = mygen()
print(next(d))
print(next(d))
print(next(d))
