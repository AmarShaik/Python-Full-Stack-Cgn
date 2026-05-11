'''program to find the maximum element without keywords'''
#1D - Array
# arr = list(map(int, input("Enter the array elements: ").split()))
# max_element = arr[0]
# for i in arr:
#     if i > max_element:
#         max_element = i
# print("The maximum element is", max_element)

#2D - Array
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter the elements of row {i+1}: ").split()))
    matrix.append(row)
max_element = matrix[0][0]
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > max_element:
            max_element = matrix[i][j]
print("The maximum element is", max_element)

'''write a program to traverse an array and 
print all the even values and odd values seperately'''
# arr = list(map(int, input("Enter the values: ").split()))
# even = []
# odd = []
# for i in arr:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even numbers are:", even)
# print("Odd numbers are:", odd)

'''write a code to sort a list of strings based on 
the len and print the sorted array without using keywords'''
# arr = input("Enter the strings: ").split()
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if len(arr[i]) > len(arr[j]):
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)

'''write a program to count the repeated elements and print the count'''
# arr = list(map(int, input("Enter the array elements: ").split()))
# unique = {}
# for i in arr:
#     if i in unique:
#         unique[i] += 1
#     else:
#         unique[i] = 1
# count = 0
# for value in unique.values():
#     if value > 1:
#         count += 1
# print(count)

# Dry Run
# 1 2 2 3 1 4 2
# num = 1{1:1}
# num = 2{1:1, 2:1}
# num = 3{1:2, 2:1, 3:1}
# num = 4{1:2, 2:2, 3:1, 4:1}
# num = 5{1:2, 2:3, 3:1, 4:1}

# count = 0
# value 2 > 1 count = 1
# value 3 > 1 count = 2
# value 1 skip
# value 1
# 2