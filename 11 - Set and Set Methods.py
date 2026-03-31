Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Sets
#sets()
#It is an UNORDERED and MUTABLE(semi mutable) collection of unique and hashable elements
#denoted by '{}'
a = (5, 6.7, 'python', 5+6j, True, False)
a = {5, 6.7, 'python', 5+6j, True, False}
type(a)
<class 'set'>

a
{False, True, 5, 6.7, (5+6j), 'python'}

#add()
a = {4, 5, 6,7 12, 13}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a = {4, 5, 6,7, 12, 13}
a.add(100)
a
{4, 5, 6, 7, 100, 12, 13}
a
{4, 5, 6, 7, 100, 12, 13}

#issubset()
a = {1,2, 3, 4, 5, 6,7, 8}
b = {2, 3, 6, 7}
b.issubset(a)
True
a.issubset(b)
False
a.issuperset(b)
True

#superset()
#-^

#union()
a = {1,2,3,4,5,6}
b = {5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#intersection()
a = {3,4,5,6,7,8,9}
b = {1,2,6,7,3,10}
a.intercetion(b)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.intercetion(b)
AttributeError: 'set' object has no attribute 'intercetion'. Did you mean: 'intersection'?
a.intersection(b)
{3, 6, 7}

#diifference()
a = {2,4,6,8,10,12}
b = {10, 12, 14, 16, 18}
a.difference(b)
{8, 2, 4, 6}
b.difference(a)
{16, 18, 14}

#update(0
a = {1,3,5,7,9,11,13}
b = {5,6,7,8,9,10}
a.update(b)
a
{1, 3, 5, 6, 7, 8, 9, 10, 11, 13}

#symmetric_difference()
a = {1,2,3,4,5,6,7,8,9}
b = {4,5,6,7,8,10}
a.symmetric_difference(b)
{1, 2, 3, 9, 10}

#difference_update()
a = {1,2,3,4,5,6,7,10,12,14}
b = {4,5,6,7,2,10,14,16}
a.difference_update(b)
a
{1, 3, 12}
b.difference_update(a)
b
{2, 4, 5, 6, 7, 10, 14, 16}

a = {3,4,5,6,7,8,9,10,11,12}
b = {4,5,6,7,8,9,10,11,12,13,14}
a.symmetric_difference_update(b)
a
{3, 13, 14}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
b
{3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
a = {3,4,5,6,7,8,9,10,11,12}
b = {4,5,6,7,8,9,10,11,12,13,14}
a.intersection_update(b)
a
{4, 5, 6, 7, 8, 9, 10, 11, 12}
b.intersection_update(a)
b
{4, 5, 6, 7, 8, 9, 10, 11, 12}
>>> a = {2,3,4,5,6,7}
>>> b = {1,2,3,4,5,6,8}
>>> a.copy(b)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.copy(b)
TypeError: set.copy() takes no arguments (1 given)
>>> a.copy
<built-in method copy of set object at 0x000001A41C66CAC0>
>>> a.copy()
{2, 3, 4, 5, 6, 7}
>>> a.clear()
>>> a
set()
>>> a = {3,4,5,6,7,8,9}
>>> a.pop()
3
>>> a
{4, 5, 6, 7, 8, 9}
>>> a.pop(4)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.pop(4)
TypeError: set.pop() takes no arguments (1 given)
>>> #error
>>> a.remove(4)
>>> a
{5, 6, 7, 8, 9}
>>> a = {2,3,4,5,6,7,8}
>>> b = {7,8,9,10,11,13}
>>> a.isdisjoint(b)
False
>>> b.isdisjoint(a)
False
>>> a = {4,5,6,7,8}
>>> b = {1,2,3,9,10}
>>> a.isdisjoint(b)
True
>>> len(a)
5
>>> a.count(4)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.count(4)
AttributeError: 'set' object has no attribute 'count'
>>> a.discard(7)
>>> a
{4, 5, 6, 8}
