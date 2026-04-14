#positional and keyword arguments
#id - positional, 10 - keyword
'''def Details(id, name, mailid):
    id = 10
    name = 'amar'
    mailid = 'amar@gmail.com'
    print(id, name, mailid)
Details(id = 'id', name = 'name', mailid = 'mailid')'''

'''def Details(id, name, mailid):
    print(id, name, mailid)
Details(id='id', name='name', mailid='mailid')
Details(id=20, name='anwar', mailid='anwar@gmail.com')
Details(id=30, name='yash', mailid='yash@gmail.com')
Details(40, 'tony', mailid='tony@gmail.com')
Details('stark', 50, 's@gmail.com')'''

#default arguments
'''def Grocery(item, price):
    print('item is %s' %item)
    print('price is %d' %price)
Grocery('sugar', 100)'''

'''def Grocery(item='rice', price=1500):
    print('item is %s' %item)
    print('price is %d' %price)
Grocery()'''

'''def Grocery(item, price=200):
    print('item is %s' %item)
    print('price is %d' %price)
Grocery('dal')'''

'''def Grocery(item='ghee', price):
    #ERROR - non default arg follows defaults arg, so  always non def or both non def or both def arg should be passed
    print('item is %s' %item)
    print('price is %d' %price)
Grocery(500)'''

'''def Cake(cakename, cakeprice, cakeqty):
    print(cakename, cakeprice, cakeqty)
Cake('blackforest', 1500, 1000)'''

# * arguments -> * is used to unpack the elements
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)
print(type(a))''' #list

'''a = (2,3,4,5,6,7,8)
print(a)
print(*a)
print(type(a))'''  #tuple

'''a = {2,3,4,5,6,7,8}
print(a)
print(*a)
print(type(a))'''   #<class 'set'>

'''a={"year":2026, "month":4}
print(a)
print(*a)
print(type(a))'''   #<class 'dict'>

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c = 3,4,5
print(a)
print(b)
print(c)'''

'''a,b,c = 2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)'''  #ValueError

'''a,*b,c = 2,3,4,5,6,7,8,9
print(a)    #2
print(*b)   #3 4 5 6 7 8
print(c)''' #9

'''a,b,c = "pyt"
print(a)
print(b)
print(c)'''

#variable length arguments -> they are automatically stored in tuple and we use * arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b = [3,4,5,6,7]
check(*b)
c = (2,3,4,5,6,7)
check(*c)
d = {6,7,8,9,10}
check(*d)
e = {"name":"amar", "year":2026}
check(*e)'''

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int, float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4.5,6.8)
check1(2,3,6,3.4,7.1,"amar",5+8j, True, False)'''

#kwargs(**)
'''def check(**a):
    print(a)
    print(type(a))    #dict
check()
d = {"idnos":[10,20,30],
     "names":["amar", "stark", "steve"],
     "status":["p","a","p"]
     }
check(**d)'''

'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i, a[i])
    for i in a.items():
        print(i)
check()
d = {"idnos":[10,20,30],
     "names":["amar", "stark", "steve"],
     "status":["p","a","p"]
     }
check(**d)'''

#both * and ** usage
'''def final(*a, **b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+1
        print(d)
    for i, j in b.items():
        print("key is", i)
        print("value is", j)
final()
data = (2,3,4,5,6.4,3.5)
final(*data)
details = {"names":["banner", "phill"],
           "places":["vja", "hyd"]}
final(**details)
final(*data, **details)'''

#max(), min(), sum()
'''print(max(4,5,6,7,8,9,10,12))
print(min(4,5,6,7,8,9,10,12))
a = (3,4,2,5,6,8,9)
print(sum(a))'''

