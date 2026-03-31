Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Dictionary
#dict - {}
#collection of key value pairs, MUTABLE and ORDERED
a = {'name':'amar', 'year':2026,'month':3}
a
{'name': 'amar', 'year': 2026, 'month': 3}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['amar', 2026, 3])
a.items()
dict_items([('name', 'amar'), ('year', 2026), ('month', 3)])
a.update{'date':31}
SyntaxError: invalid syntax
a.update({'date':31})
a
{'name': 'amar', 'year': 2026, 'month': 3, 'date': 31}
a.update({'city':'vja'}, {'state':'andhra pradesh'})
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.update({'city':'vja'}, {'state':'andhra pradesh'})
TypeError: update expected at most 1 argument, got 2
#error - for multilpe inputs, it should be in single {}
a.update({'city':'vja', 'state':'andhra pradesh'})
a
{'name': 'amar', 'year': 2026, 'month': 3, 'date': 31, 'city': 'vja', 'state': 'andhra pradesh'}
b = {'mailid':'shaikamar907@gmail.com'}
b
{'mailid': 'shaikamar907@gmail.com'}
b.setdefault('name', 'amar')
'amar'
b
{'mailid': 'shaikamar907@gmail.com', 'name': 'amar'}
a.pop()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
b.pop('name')
'amar'
b
{'mailid': 'shaikamar907@gmail.com'}
a.pop(2026)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.pop(2026)
KeyError: 2026
>>> b.copy()
{'mailid': 'shaikamar907@gmail.com'}
>>> b.clear()
>>> b
{}
>>> b = {}
>>> b
{}
>>> b.update({'day':'tuesday'})
>>> b
{'day': 'tuesday'}
>>> a.get('state')
'andhra pradesh'
>>> a['city']
'vja'
>>> a.popitem()
('state', 'andhra pradesh')
>>> a
{'name': 'amar', 'year': 2026, 'month': 3, 'date': 31, 'city': 'vja'}
>>> c = {'idnos':[10,20,30], 'names':['manohar','krishna','amar']}
>>> c
{'idnos': [10, 20, 30], 'names': ['manohar', 'krishna', 'amar']}
>>> c.keys()
dict_keys(['idnos', 'names'])
>>> c.values()
dict_values([[10, 20, 30], ['manohar', 'krishna', 'amar']])
>>> d = {
...     'name':'amar',
...     'city':'vja',
...     'country':'india'
...     }
>>> d
{'name': 'amar', 'city': 'vja', 'country': 'india'}
>>> e = {'name':'amar', 'city':'vja', 'name':'amar'}
>>> e
{'name': 'amar', 'city': 'vja'}
>>> #dict doesn't allow duplicates
>>> e = {'name':'amar', 'city':'vja', 'name':'anwar'}
>>> e
{'name': 'anwar', 'city': 'vja'}
>>> #latest/last key value is considered
>>> e = {'name':'amar', 'city':'vja', 'name1':'amar'}
>>> e
{'name': 'amar', 'city': 'vja', 'name1': 'amar'}
>>> #keys should be different
