#the number is a palindrome if the reverse of that equal to the actual number
number=int(input("enter the number to check if it ia a palindrome or not : "))
temp = number
reverseNbr = 0
while(temp > 0):
    reminder = int(temp % 10)
    reverseNbr = int(reverseNbr * 10 + reminder)
    temp = int(temp /10)
if (reverseNbr==number):
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")