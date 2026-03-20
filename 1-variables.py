Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#variables
#variables are containers which stores data in a particular memory location
#it is case-ssensitive so 'A' is not same as 'a'
#it cannot be assigned as numbers such as '2=34', only 'a=32'
a=10
print(a)
10
a=2
b=20
print(a+b)
22
C=23
print(c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(c)
NameError: name 'c' is not defined. Did you mean: 'C'?
name = "amar"
print(name)
amar
place = "vijayawada"
print(place)
vijayawada
course = "python full-stack"
print(course)
python full-stack
#Rule-2: do not start variable names with keywords, such as if, elif....
a=4, b=6
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4; b=7
print(a*b)
28
a, b = 6, 7
print(a*b)
42
>>> #a=4, b=3 - it will give an error
>>> #can be written as a, b = 4, 5 (or) a=3; b=4
>>> a, b = "python", "course"
>>> print(a+b)
pythoncourse
>>> print(a+" "+b)
python course
>>> fname = "amar"
>>> lanme = "shaik"
>>> print(fname+" "+lname)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(fname+" "+lname)
NameError: name 'lname' is not defined. Did you mean: 'name'?
>>> print(fname+" "+lanme)
amar shaik
>>> lname  = "shaik"
>>> print(fname+" "+lname)
amar shaik
>>> 
>>> #Rule-3: it doesn't allow any special characters except underscore "_"
>>> _ = 20
>>> print(_)
20
>>> first name = "amar"
SyntaxError: invalid syntax
>>> firstname = "amar"
>>> print(firstname)
amar
>>> first_name = "amar"
>>> print(first_name)
amar
>>> lname = "shaik"
>>> lname_ = "shaik"
>>> print(lname)
shaik
>>> print(lname_)
shaik
>>> a = 12
>>> print(a)
12
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> #error as a is not defined because we used 'del' keyword to delete a variable
