Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #striding
>>> a = 'data science'
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> a[::3]
'dacn'
>>> 
>>> b = 'cloud computing'
>>> b[::4]
'cdmi'
>>> b[::2]
'codcmuig'
>>> b[::6]
'cci'
>>> 
>>> b[5:]
' computing'
>>> b[3:11]
'ud compu'
>>> a[:9]
'data scie'
>>> b[:9]
'cloud com'
>>> b[2:10:3]
'o m'
>>> b.count()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b.count()
TypeError: count() takes at least 1 argument (0 given)
>>> 
>>> c = 'machine learning'
>>> c[2:12:4]
'cea'
>>> c[3:15:6]
'he'
>>> c[1:14:3]
'ai ai'
>>> 
>>> #negative
>>> a = 'python course'
>>> a[-1:-9:-2]
'ero '
>>> a[-1:-10:-2]
'ero o'
a[-3:-12:-4]
'r t'
a[::-1]
'esruoc nohtyp'

x=""hello""
SyntaxError: invalid syntax
x=257
y=257
print(x is y)
False
