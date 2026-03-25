Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String Methods
>>> #len()
>>> a = "codegnan"
>>> len(a)
8
>>> b = "python course"
>>> len(b)
13
>>> c = ""
>>> len(c)
0
>>> d = " "
>>> len(d)
1
>>> 
>>> #count
>>> #def - no. of repeated characters
>>> a = "twinkle twinkle little star"
>>> a.count("t")
5
>>> a.count(" ")
3
>>> a.count("twinkle")
2
>>> a.count("Twinkle")
0
>>> 
>>> #find a string
>>> a = "python code"
>>> a.find("c")
7
>>> a.find("code")
7
>>> a.find("o")
4
>>> a.find("d")
9
>>> 
>>> #escape sequences
>>> #\n -> new line
>>> #\t -> tab space
>>> a = "name\nmobileno\temail\ncity"
>>> print(a)
name
mobileno	email
city
>>> b = "name:shaik amar\nmobileno:9895623147\tmailid:shaikamamr@gmail.com\ncity:vja"
>>> print(b)
name:shaik amar
mobileno:9895623147	mailid:shaikamamr@gmail.com
city:vja

#replace
a = "wait until you succeed"
a.replace("wait", "work")
'work until you succeed'
b = "wait wiat until you succeed"
c = "wait wait until you succeed"
c.replace("wait", "work")
'work work until you succeed'
c.replace("wait", "work", 1)
'work wait until you succeed'

#upper()
a = "hello"
a.upper()
'HELLO'
b = "WELCOME"
b.lower()
'welcome'
c = "python"
c.capitalize()
'Python'
d = "i am in class"
d.title()
'I Am In Class'
d.capitalize()
'I am in class'

#conditions
a = "python"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
a.startswith("p")
True
a.endswith("n")
True
b = "python course"
b.isalpha()
False
c = 78945
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c = "78945"
c.isdigit()
True
a = "amar"
a.isalnum()
True
a = "amar123"
a.isalnum()
True
b = "amar@123"
b.isalnum()
False

#strip
#lstrip(), rstrip()
a = "   amar    "
a.strip()
'amar'
a.lstrip()
'amar    '
a.rstrip()
'   amar'

#split()
a = "python java c cpp"
a.split()
['python', 'java', 'c', 'cpp']
a = "i am learning python course"
a.split()
['i', 'am', 'learning', 'python', 'course']


#join()
a = 'html', 'css', 'js', 'bs'
''.join(a)
'htmlcssjsbs'
' '.join(a)
'html css js bs'
'k'.join(a)
'htmlkcsskjskbs'

#concatenation
a = "python"
b = "course"
print(a+b)
pythoncourse
print(a + " " + b)
python course
fname = "amar"
lname = "shaik"
print(fname+lname)
amarshaik
print(fname+ " " +lname)
amar shaik
print(fname.title()+" "+lname.title())
Amar Shaik
print((fname+" "+lname).title())
Amar Shaik

#formatting
a=6
b=8
print(a+b)
14
print("the sum is", a+b)
the sum is 14
name = "shaik amar"
print("my name is", name)
my name is shaik amar
city = "vijayawada"
print("i live in", city)
i live in vijayawada

a = "motu"
b = "patlu"
print("hello {}{}".format(a, b))
hello motupatlu
print("hello {} {}".format(a, b))
hello motu patlu
print("hello {} and {}".format(a, b))
hello motu and patlu
print("hello {} hello {}".format(a, b))
hello motu hello patlu
print("hello {} \nhello {}".format(a, b))
hello motu 
hello patlu

#fstring (formatting string)
a =
SyntaxError: invalid syntax
a = "tony"
b = "stark"
print(f"hello {a} {b}")
hello tony stark

a = 3
b = 5
print(a*b)
15
print("product is {}".format(a*b))
product is 15
print("product is {}".format(c))
product is 78945
c = a * b
print("product is {}".format(c))
product is 15
print(f"product is {c}")
product is 15
