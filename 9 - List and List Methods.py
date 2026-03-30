Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List
>>> #list[]
>>> #It is a built-in, MUTABLE and ORDERED collection of items used to store multiple values in a single variable
>>> a = [5, 6.7, 'amar', 5+6j, True, False]
>>> print(a)
[5, 6.7, 'amar', (5+6j), True, False]
>>> type(a)
<class 'list'>
>>> b = 60
>>> type(b)
<class 'int'>
>>> c=[60]
>>> type(c)
<class 'list'>
>>> 
>>> #append - to insert single value
>>> a = ['python', 'java', 'c', 'c++']
>>> a.append('html')
>>> print(a)
['python', 'java', 'c', 'c++', 'html']
>>> a.append('css', 'js')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append('css', 'js')
TypeError: list.append() takes exactly one argument (2 given)
>>> a.apppend(['css', 'js'])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.apppend(['css', 'js'])
AttributeError: 'list' object has no attribute 'apppend'. Did you mean: 'append'?
>>> a.append(['css', 'js'])
>>> print(a)
['python', 'java', 'c', 'c++', 'html', ['css', 'js']]
>>> 
>>> #extend
>>> b = ['apple', 'banana', 'cherry', 'mango']
>>> b.extend(['grapes', 'kiwi'])
>>> print(b)
['apple', 'banana', 'cherry', 'mango', 'grapes', 'kiwi']
>>> b.index(1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b.index(1)
ValueError: 1 is not in list
>>> b.index('banana')
1
>>> b.insert(1, 'berry')
>>> print(b)
['apple', 'berry', 'banana', 'cherry', 'mango', 'grapes', 'kiwi']

#sort
#sort()
a = ['white', 'red', 'black']
a.sort()
a
['black', 'red', 'white']

b = ['hyd', 'vja', 'bng']
b.sort()
b
['bng', 'hyd', 'vja']
c = [1, 5, 87, 9, 0, 24]
c.sort()
c
[0, 1, 5, 9, 24, 87]

#reverse
a = ['white', 'red', 'black']
a.reverse()
a
['black', 'red', 'white']
b.reverse()
b
['vja', 'hyd', 'bng']
c.reverse()
c
[87, 24, 9, 5, 1, 0]
#reverse just reverses the value, if you want desc order then you have to use sort() then reverse()

#pop()
#deletes a specific value
a = ['html', 'css', 'js', 'bs', 'react']
a.pop()
'react'
a.pop('js') #error
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.pop('js') #error
TypeError: 'str' object cannot be interpreted as an integer
a.pop(2)
'js'

#remove - permanently deletes a value
a.remove()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
a.remove('css')
a
['html', 'bs']

#clear - deletes full list
b = ['c', 'cpp', 'c#', 'java']
b.clear()
b
[]
b.append('pyhton')
b
['pyhton']

#copy()
a = ['hi', 'hello', 'how']
a.copy()
['hi', 'hello', 'how']
b = a.copy()
b
['hi', 'hello', 'how']

#count()
c = 'hello'
len(c)
5
d = ['hello']
len(d)
1
a.count('hello')
1
len(a)
3
