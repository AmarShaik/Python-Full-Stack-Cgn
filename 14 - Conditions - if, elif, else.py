#Conditions
#if, elif, else
#if condition by using comparison operator
#<, >, <=, >=, !=, ==
'''a = 4
b = 8
if a<b:
    print('true')'''

'''a = 4
b = 8
if a>b:
    print('true')'''

'''a = 4
b = 8
if a<=b:
    print('less')'''

'''a = 4
b = 8
if a>=b:
    print('true')'''

'''a = 4
b = 8
if a!=b:
    print('true')'''

'''a = 4
b = 8
if a==b:
    print('true')'''

'''n = int(input())
if n>12:
    print('greater')'''

'''a = int(input('enter a value:'))
b = int(input('enter b value:'))
if a<b:
    print("less")'''

'''a = 'python'
if a == 'python':
    print('true')'''

'''a = input('enter a name:')
if a == 'amar':
    print('true')'''

#if condition by using logical operators
#and, or, not
'''a = 3
b = 8
if a<b and b>a:
    print('true')'''

'''a = 3
b = 8
if a<=b and b>=a:
    print('true')'''

'''a = 3
b = 8
if a!=b and b==a:
    print('true')'''

'''a = 5
b = 10
if a<b or b>a:
    print('true')'''

'''a = 5
b = 10
if a<=b or b>=a:
    print('true')'''

'''a = 5
b = 10
if a!=b or b==a:
    print('true')'''

'''a = 12
b = 15
if not a>b:
    print('less')'''

'''a = 12
b = 15
if not a<b:
    print('less')'''

'''a = int(input('a value'))
b = int(input('b value'))
if a<b and b>a:
    print('less')'''

'''a = int(input('a value'))
if a!=9 or a==6:
    print('true')'''

'''a = input('enter the data')
if a='python' or a=='java':
    print('true')'''

#if conditions using identity operators
#is, is not
'''a = 8
if type(a) is int:
    print('it is int')'''

'''a = 8
if type(a) is not int:
    print('it is int')'''

'''a = int(input('a value'))
if type(a) is int:
    print('true')'''

'''a = 8.6
if type(a) is float:
    print('it is float')'''

'''a = 8.6
if type(a) is not float:
    print('it is float')'''

'''a = float(input('a value'))
if type(a) is float:
    print('true')'''

'''a = 'amar'
if type(a) is str:
    print('it is str')'''

'''a = 'name'
if type(a) is not str:
    print('it is str')'''

'''a = input('enter a value')
if type(a) is str:
    print('true')'''

'''a = 5+6j
if type(a) is complex:
    print('it is complex')'''

'''a = 5+6j
if type(a) is not complex:
    print('it is complex')'''

'''a = complex(input('enter a value'))
if type(a) is complex:
    print('it is complex')'''

'''a = True
if type(a) is bool:
    print('bool')'''

'''a = True
if type(a) is not bool:
    print('bool')'''

'''a = bool(input('enter a value'))
if type(a) is bool:
    print('it is bool')'''

#if condition by using membership operators
#in, not in
'''a = [2,3,4,5,6,7,8,9]
if 4 in a:
    print('true')'''

'''a = [2,3,4,5,6,7,8,9]
if 4 not in a:
    print('true')'''

'''a = int(input('a value'))
if 10 in a:
    print('true')''' #error

'''a = [10,20,30,40,50]
b = int(inpu('enter b value'))
if b in a:
    print('true')'''


#if-else conditions by using comparison

'''a = 4
b = 9
if a<b:
    print("less")
else:
    print('true')'''

'''a = 4
b = 9
if a<b:
    print('less')
else:
    print('true')'''

'''a=4
b=9
if a==b:
    print('both are equal')
else:
    print('it is not equal')'''

'''a=4
b=6
if a!=b:
    print('both are not equal')
else:
    print('both are equal')'''

'''a = 4
b = 9
if a<=b:
    print('less')
else:
    print('true')'''

'''a = 4
b = 9
if a>=b:
    print('less')
else:
    print('true')'''

#if-elif conditions by using comparison

'''a=2
b=4
if a<b:
    print('less')
elif a>b:
    print('greater')'''

'''a=2
b=4
if a==b:
    print('equal')
elif a!=b:
    print('not equal')'''

'''a=2
b=4
if a<b:
    print('less')
else a>b:
    print('greater')
elif a!=b:
    print('not equal')'''

#if-elif-else conditions

'''a = 5
b = 7
if a<b:
    print('less')
elif b>a:
    print('greater')
else:
    print('true')'''

'''a = 5
b = 7
if a>b:
    print('less')
elif b>a:
    print('greater')
else:
    print('true')'''

'''a = 5
b = 7
if a==b:
    print('less')
elif b<a:
    print('greater')
elif a!=b:
    print('not equal')'''

#multiple-if conditions

'''a=8
b=12
if a<b:
    print('less')
if b>a:
    print('greater')
if a!=b:
    print('not equal')'''

'''a=8
b=12
if a==b:
    print('less')
if b>a:
    print('greater')
if a!=b:
    print('not equal')'''

#nested-if

'''a = 10
b = 20
if a<b:
    print('less')
    if b>a:
        print('greater')'''

'''a = 10
b = 20
if a>b:
    print('less')
    if b>a:
        print('greater')'''

'''a = 10
b = 20
if a<b:
    print('less')
    if b==a:
        print('greater')
    else:
    print('true')'''

'''a = 10
b = 20
if a==b:
    print('less')
    if b>a:
        print('greater')
else:
    print('false')'''

'''a = 10
b = 20
if a==b:
    print('less')
    if b<a:
        print('greater')
    else:
        print('true')
else:
    print('false')'''

'''a = 6
b = 9
if a!=b:
    print('not equal')
    if b<a:
        print('less')
    elif a>b:
        print('true')
    else:
        print('false')'''

