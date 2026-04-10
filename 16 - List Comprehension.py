#List Comprehension
#Every list comprehension can be re-written as a for loop but every for loop cannot be re-wirtten in list comprehension
'''a = ['codegnan', 'python', 'course']'''
#Output - ['CODEGNAN', 'PYTHON', 'COURSE']

#SYNTAX
# a = [exprn for var in collection/range]

'''a = [i.upper() for i in a]
print(a)'''


'''b = ['vja', 'hyd', 'vzg']
b = [i.title() for i in b]
print(b)'''

'''c = [1, 2, 3, 5, 6, 8, 12, 13]
c = [i*i for i in c]
print(c)'''

#if-usage in list comprehension
'''a = [i for i in range(16) if i%2==0]
print(a)'''

'''a = [i*i for i in range(21) if i%2==0]
print(a)'''

'''fruit = ['apple', 'grape', 'mango', 'berry', 'kiwi', 'dragon']
b = [i for i in fruit if 'a' in i]
print(b)
#Output - ['apple', 'grape', 'mango', 'dragon']'''

#no elif usage in list comprehension

#if-else usage in list comprehesion
'''a = [i*i if i % 2 == 0 else i*5 for i in range(31)]
print(a)'''

'''a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [a[i]+b[i] for i in range(len(a)] #or [a[i]+b[i] for i in range(5)]
print(c)'''
#Output = [6,6,6,6,6]

#Patterns
'''n = int(input())
for i in range(1, n+1):
    print('*' * i)

#Output
5
*
**
***
****
*****'''

#2
'''n = int(input())
for i in range(1, n+1):
    print('*' * n)

#Output
5
*****
*****
*****
*****
*****'''

#3
n = int(input())
for i in range(n):
    print('*' * (n-i))

#Output

