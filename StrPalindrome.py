# String palinddrome is the word which reads the same from front and backward
# example ABBA, LIRIL
from Tools.scripts.fixcid import Reverse

str1 = input("enter the palindrome : ")
thisList = list(str1)
# print(thisList)
newlist = thisList[::-1]
# print(newlist)

if "".join(thisList) == "".join(newlist):
    print(str1, "is a Palindrome ")
else:
    print(str1, "is not a Palindrome ")
