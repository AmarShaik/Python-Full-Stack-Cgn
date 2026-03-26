Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> a = 'codegnan'
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> 
>>> b = 'work until you succeed'
>>> b[:5]
'work '
>>> b[11:12]
'y'
>>> b[11:13]
'yo'
>>> b[11:14]
'you'
>>> b[5:9]
'unti'
>>> b[5:10]
'until'
>>> b[16:23]
'ucceed'
>>> b[15:23]
'succeed'
>>> 
>>> c= 'simple is better than complex'
>>> c[17:21]
'than'
>>> c[23:29]
'omplex'
>>> c[22:29]
'complex'
>>> c[10:16]
'better'
>>> c[:6]
'simple'
>>> 
>>> #negative
>>> a = 'codegnan it solutions'
>>> a[-1:-9]
''
>>> a[-9:-1]
'solution'
>>> a[-10:-1]
' solution'
a[-9:0]
''
a[-9:]
'solutions'
a[-12:-11]
'i'
a[-12:-10]
'it'
a[-21:-13]
'codegnan'

b = 'beautiful is better than ugly'
b[-4:]
'ugly'
b[-16:-11]
'bette'
b[-16:12]
''
b[-16:-10]
'better'
b[-29:-20]
'beautiful'
