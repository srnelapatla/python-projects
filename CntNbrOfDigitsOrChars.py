# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2

str = "this is the string 3.0"
d=c=1
for char in str:
    if char.isdigit():
        d += 1
    elif char.isalpha():
        c += 1
    else:
        pass
print("number of digits in a given string is",d )

print("number of char in a given string is", c )
