Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Operators
#Arithmetic Operators -> +, -, *, //, /, **, %
#Assignment Operators -> +=, -=, *=, //=, /=, **=, %=
#Comparioson Operators -> <, >, <=, >=, !=, ==
#Logical Operators -> and, or, not
#Identity Operators -> is, is not
#Membership Operators -> in, not in
#Bitwise Operators -> &, |, ~, ^, <<, >>

#Arithmetic
a = 3
b = 6
print(a+b)
9
print(a-b)
-3
print(a*b)
18
print(a//b)
0
print(a/b)
0.5
printa(a**b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    printa(a**b)
NameError: name 'printa' is not defined. Did you mean: 'print'?
print(a**)
SyntaxError: invalid syntax
print(a**b)
729
a%b
3

#Assignment
a=4
b=6
a
4
b
6
a+=b
b
6
b+=a
b
16
b-=a
b
6
b*=a
b
60
b//=a
b
6
b**=a
b
60466176
b/=a
b
6046617.6

#Comparison
a = 4
b = 6
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a<=b
True
b>=a
True
a>=b
False
b<=a
False
a = 7
b = 7
a==b
True
a!=b
False

#Logical
a = 4
b = 2
a<b and b>a
False
a<b and b<a
False
a>b and b<a
True
a>=b and b<=a
True
a<=b and b>=a
False
a!=b and a==b
False
a>b or a<b
True
a!=b or a==b
True
not True
False
not False
True

#Identity
a = 7
if type(a) is int:
    print("true")

    
true
if type(a) is not int:
    print("true")

    

#Output won't be generated
    
b = 7.8
if type(a) is float:
    print("it is float")

    
if type(b) is float:
    print("it is float")

    
it is float

#Membership
a = 3, 4, 5, 6, 7, 8, 9, 10
if 10 in a:
    print(10)

    
10
>>> if 10 in a:
...     print("it is")
... 
...     
it is
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> IF 20 not in a:
...     
SyntaxError: invalid syntax
>>> if 20 not in a:
...     print("is is not present")
... 
...     
is is not present
>>> print(3 in a)
True
>>> print(2 in a)
False
>>> print(2 not in a)
True
>>> 
>>> #Bitwise
>>> a = 3
>>> b = 5
>>> a&b
1
>>> bin(3)
'0b11'
>>> bin(5)
'0b101'
>>> c = 7
>>> d = 11
>>> a&b
1
>>> c&d
3
>>> bin(7)
'0b111'
>>> bin(11)
'0b1011'
>>> bin(15)
'0b1111'
>>> bin(4)
'0b100'
