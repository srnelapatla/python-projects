# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

c = 0
while True:
    try:
        guess = int(input("enter random number between [1-9] :"))
        number = random.randint(1, 9)
        if guess <= 9 or guess <= 1:
            c = c + 1
            if guess == number:
                print("hurray.... you guessed correct!!!")
                break
            elif guess < number:
                print("too low...try again")
            elif guess > number:
                print("too high..try again")
        else:
            print(" your guess should be between 1-9 ")
    except:
        print("it is not a valid option. only numbers are allowed ")

print("you guessed in ", c)
