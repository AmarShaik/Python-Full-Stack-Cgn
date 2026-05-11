#patterns
#7
'''n = int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==0 or (j==n-3 and i<=n-2) or (i==n-1 and j<n-3):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

#O/p:
5
* * * * *
    *
    *
* *       '''

#8
'''n = int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==n-3 or (j==0 and i<=n-3) or (j==n-1 and i>n-3):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

#o/p:
5
* * * * *
*
* * * * *
        *
* * * * *'''

#9
'''n = int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
#O/p:
5
*       *
*       *
*       *
*       *
* * * * *
'''

#10
'''n = int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==n-3 or (j==0 and i<=n-3) or (j==n-1 and i>=n-3):
            
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
#O/p:
5
*
*
* * * * *
        *
        *
'''

#11
'''n = int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==n-3 or (j==0 and i<=n-3) or (j==n-1 and i>=n-3) or (j==n-3 and i>=n-3):
            
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
#O/p:
5
*
*
* * * * *
    *   *
    *   *
'''

#12
'''n=4
for i in range(n,0,-1):
    for j in range(n-1,0,-1):
        if i==n-2 or j==n-3 or (i==0 and j>2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#O/p:
* *
  *
* * *
  *
'''

#13
'''n = 4
for i in range(4, 0, -1):
    for j in range(n-1, 0, -1):
        if (i==0 and j==3) or (i==3 and j==2) or (i==2 or j==1) or (i==1 and j==0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#O/p:
*
  *
    *
*
'''
