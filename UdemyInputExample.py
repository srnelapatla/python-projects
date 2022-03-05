# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import date

name = str(input("Enter the name : "))
age = int(input("Enter the age : "))

while True:
    if age <= 0:
        print("Enter age greater than 0")
        age = int(input("Enter the age :"))
    else:
        break

# creating the date object of today's date
todays_date = date.today()

#calculateYear = ((todays_date.year) - age) + 100
#
#print(name, ", you will be 100 in the year", calculateYear)

calculateYear = str((((todays_date.year) - age) + 100))
print(name + ", will be 100 years old in the year " + calculateYear)
