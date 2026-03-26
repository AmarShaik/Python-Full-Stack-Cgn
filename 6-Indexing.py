Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #indexing
>>> a = 'vijayawada'
>>> a[1]
'i'
>>> a[5]
'a'
>>> a[0]
'v'
>>> a[3]
'a'
>>> 
>>> b = 'i am in class'
>>> b[7]
' '
>>> b[1]
' '
>>> b[4]
' '
>>> b[1]+b[4]
'  '
>>> b[1]+b[4]+b[7]
'   '
>>> b[12]
's'
>>> b[13]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b[13]
IndexError: string index out of range
>>> #error - string index out of range
>>> b[3]
'm'
>>> b[8]+b[9]
'cl'
>>> b[8]+b[9]+b[19+0]+b[11]+b[12]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b[8]+b[9]+b[19+0]+b[11]+b[12]
IndexError: string index out of range
>>> b[8]+b[9]+b[10]+b[11]+b[12]
'class'
>>> 
>>> x = 10
>>> print(type(x))
<class 'int'>
>>> x=10
>>> print(type(x))
<class 'int'>

c = 'time is very precious'
c[]
SyntaxError: invalid syntax
c[0]
't'
c[8]+c[9]+c[10]+c[11]
'very'
c[13]+c[14]+c[15]+c[16]+c[17]+c[18]+c[19]+c[20]
'precious'
c[0]+c[1]+c[2]+c[3]
'time'

d = ''vijayawada is
SyntaxError: invalid syntax
d = 'vijayawada is a royal city'
d[15]+d[16]+d[17]+d[18]+d[19]
' roya'
d[16]+d[17]+d[18]+d[19]+d[20]
'royal'
d[21]+d[22]+d[23]+d[24]
' cit'
d[22]+d[23]+d[24]+d[25]
'city'
d[0]+d[2]+d[3]+d[4]+d[5]+d[6]+d[7]+d[8]+d[9]
'vjayawada'
e = 'i am learning python course'
e[14]+e[15]+e[16]+e[17]+e[18]+e[19]+[20]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    e[14]+e[15]+e[16]+e[17]+e[18]+e[19]+[20]
TypeError: can only concatenate str (not "list") to str
e[14]+e[15]+e[16]+e[17]+e[18]+e[19]
'python'

#negative
a = 'i love python'
a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]
'nohtyp'
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a-[11]+a[-10]+a[-9]+a[-8]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a-[11]+a[-10]+a[-9]+a[-8]
TypeError: unsupported operand type(s) for -: 'str' and 'list'
a[-11]+a[-10]+a[-9]+a[-8]
'love'
b = 'vizag is a city of destiny'
b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'estiny'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
