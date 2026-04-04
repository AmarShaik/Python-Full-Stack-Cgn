#Task-1
'''age = int(input('enter your age:'))
if age >= 18:
    print('You are eligible for voting')
else:
    print('You are not eligible for voting')'''

#Task-2
'''n = int(input('enter a number:'))
if n % 2 == 0:
    print('it is even')
else:
    print('it is odd')'''

#Task-3
'''n = int(input('enter year:'))
if(n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print('it is leap year')
else:
    print('it is not leap year')'''

#Task-4
'''name = input("enter your name:")
if name == 'amar':
    print('welcome amar')
else:
    print('welcome guest')'''

#Task-5
'''vow = ['a', 'e', 'i', 'o', 'u']
letter = input('enter a letter:').lower()
if letter in vow:
    print('it is vowel')
else:
    print('it is consonant')'''

#Task-6
'''names = ['amar', 'tony', 'steve', 'stark', 'rogers']
name = input('enter your name:').lower()
if name in names:
    print(f'welcome {name}')
else:
    print('welcome guest')'''

#Task-7
#multiple if
'''uname = input('enter your username:')
password = int(input('enter your password:'))
if uname == 'amar' and password == 1234:
    print('login successful')'''


#if-else
'''uname = input('enter your username:')
password = int(input('enter your password:'))
if uname == 'amar' and password == 1234:
    print('login successful')
else:
    print('does not match')'''

#Task-8
#if-elif-else:
'''cake price 1200 - redvelvet cake
1000 - chocolate cake
800 - cheese cake
600 - butterscotch
remaining all prices - sorry cake is not available'''

'''n = int(input("enter cake price:"))
if n==1200:
    print('redvelvet cake')
elif n==1000:
    print('chocolate cake')
elif n==800:
    print('cheese cake')
elif n==600:
    print('butterscotch')
else:
    print('sorry cake is not available')'''

items = ['crispy chicken pizza', 'paneer pizza', 'corn pizza', 'french fries and coke']
print(items)
n = input('enter food:')
if n == 'crispy chicken pizza':
    print('prize is 800')
elif n == 'paneer pizza':
    print('prize is 600')
elif n == 'corn pizza':
    print('prize is 400')
elif n == 'french fries and coke':
    print('prize is 200')
else:
    print(f'sorry {n} is not available')
