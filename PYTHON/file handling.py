#file handling
#write()
'''a=open("amar.txt","w")
a.write("codegnan it solutions")
a.close()

#append()
a=open("amar.txt","a")
a.write("python")
a.close()'''

'''a=open("amar.txt","w")
b=input("enter the data")
a.write(b)
a.close()'''

#readlines()
'''a=open("amar.txt")
print(a.read())#it will display entire content
print(a.readline())#it will display first line
print(a.readlines())#it will display with \n
print(a.read(9))#it will display no. of characters'''

#writelines() -> it makes every object side by side
'''a=open("python.txt", "w")
b=['amar', 'praveen', 'rakesh', 'manohar', 'jashua']
a.write('\n'.join(b))
a.close()'''

'''a=open("python.txt")
print(a.read())'''


a=open("C:\\Users\\shaik\\codegn\\file handling.py")
print(a.read())
