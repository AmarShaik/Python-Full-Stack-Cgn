#Loops
#break, continue, pass
#the difference between break, continue and pass
'''break statement is used to terminate the entire loop
continue statement is used to skip the current iteration and rest of the code will continue
pass statement is a null statement, it does nothing but syntactically we need'''
#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(10):
    if i==4:
        break
    print(i)'''

'''a = 'codegnan'
for i in a:
    if i=='d':
        break
    print(i)'''

'''a = ['codegnan', 'python', 'course']
for i in a:
    if i=='python':
        break
    print(i)'''

#continue
'''a = 20
while a>2:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(30):
    if i==25 or i==26:
        continue
    print(i)'''

'''for i in range(30):
    if i=225:
        continue
    print(i)'''

'''a = 'python'
for i in a:
    if i == 'h':
        continue
    print(i)'''

#pass
'''a = 40
while a>10:
    print(a)
    a=a-1
    if a==20:
        pass'''

'''for i in range(15):
    if i==10:
        pass
    print(i)'''

#Task-1
while True:
    n = int(input('enter marks:'))
    if n in range(91,101):
        print('grade - A')
    elif n in range(81, 91):
        print('grade - B')
    elif n in range(71, 81):
        print('grade - C')
    elif n in range(50, 71):
        print('grade - D')
    else:
        print('Fail')
