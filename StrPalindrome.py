# String palinddrome is the word which reads the same from front and backward
# example ABBA, LIRIL
from Tools.scripts.fixcid import Reverse

str1 = input("enter the palindrome : ")
str2 = str1[len(str1)::-1]  ## or str1[::-1]
if str1 == str2:
    print(str1, "is a Palindrome ")
else:
    print(str1, "is not a Palindrome ")
"""
following is the another method to find if the string is a palindrome or not
thisList = list(str1)
# print(thisList)
newlist = thisList[::-1]
# print(newlist)

if "".join(thisList) == "".join(newlist):
    print(str1, "is a Palindrome ")
else:
    print(str1, "is not a Palindrome ")
"""