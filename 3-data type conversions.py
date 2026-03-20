Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#data type conversions

#int
int(8)
8
int(8.8)
8
int("amar")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("amar")
ValueError: invalid literal for int() with base 10: 'amar'
#error
int(2+3j)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(2+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#error


int(True)
1
int(False)
0

#float
float(2)
2.0
float(2.5)
2.5
float("amar")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float("amar")
ValueError: could not convert string to float: 'amar'
#error
float(2+3j)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    float(2+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
#error
float(True)
1.0
>>> float(False)
0.0
>>> 
>>> 
>>> #str
>>> str(2)
'2'
>>> str(4.5)
'4.5'
>>> str("amar")
'amar'
>>> str(2+3j)
'(2+3j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> #complex
>>> complex(6)
(6+0j)
>>> complex(7.8)
(7.8+0j)
>>> complex("amar")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    complex("amar")
ValueError: complex() arg is a malformed string
>>> #error
>>> complex(2j+3)
(3+2j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #bool
>>> bool(3)
True
>>> bool(5.7)
True
>>> bool('amar')
True
>>> bool(2+3j)
True
>>> bool(True)
True
>>> bool(False)
False
