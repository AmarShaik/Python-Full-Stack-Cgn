#Run-time input()
#general 3 types of add
'''
a = 3
b = 4
print(a+b)

a = 3
b = 4
c = a+b
print(c)

print(3+4)
'''

#int
'''a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
print(a+b)'''

#float
'''a = float(input("enter value of a:"))
b = float(input("enter value of b:"))
print(a+b)'''

#str
'''a = str(input("enter value of a:"))
b = str(input("enter value of b:"))
print(a+b)

(or)

a = input("enter value of a:")
b = input("enter value of b:")
print(a+b)'''

#complex
'''a = complex(input("enter value of a:"))
b = complex(input("enter value of b:"))
print(a+b)'''

#Boolean
'''a = bool(input("enter value of a:")) #True
b = bool(input("enter value of b:"))    #False
c = bool(input("enter value of c:"))    #True
print(a+b+c) #Output - 3  -- This is based on no.of inputs'''

'''a = int(input())
b = int(input())
print(a+b)'''

'''a = input()
b = input()
print(a+b)'''

'''fname = input("enter fname:")
lname = input("enter lname:")
print(fname + " " + lname)'''

#Task
a = [9,1,5,2,8,4,6,3,7,0]
#output - [7,6,4,3,0,9,8,5,2,1] - using list methods
first_half = a[:5]
second_half = a[5:]
first_half.sort()
second_half.sort()
first_half.reverse()
second_half.reverse()
result = second_half + first_half
print(result)









