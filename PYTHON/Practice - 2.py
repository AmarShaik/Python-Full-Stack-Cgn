# ticket = input("Ticket - 'Yes' or 'No'").upper()
# rain = input("Rain - 'Yes' or 'No'").upper()
# if ticket == "YES" and rain == "NO":
#     print("Going for a movie")
# elif ticket == "YES" and rain == "YES":
#     print("Not going for a movie")
# elif ticket == "NO" and rain == "YES":
#     print("Not going for a movie")
# elif ticket == "NO" and rain == "NO":
#     print("Not going for a movie")
# else:
#     print("Enter 'YES' or 'NO'")

'''program to remove duplicates from a string'''
# word = input("Enter string: ")
# box = ""
# for i in word:
#     if i not in box:
#         box += i
# print(box)

# word = input("Enter string: ")
# box = ""
# for i in range(len(word)):
#     if word[i] not in box:
#         box += word[i]
# print(box)

# word = input("Enter string: ")
# box = ""
# while word:
#    if word[0] not in box:
#       box += word[0]
#    word = word[1:]
# print(box)

'''program to repeatedly add the digits of a number until we get a single digit'''
n = int(input())
while n>=10:
   sum = 0
   while n!=0:
      rem = n%10
      sum = sum + rem
      n = n//10
   n = sum
print(n)