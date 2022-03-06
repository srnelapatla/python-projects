# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least one upper case letter between [A-Z].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password

def passwordValidation(password):
    special_characters = "$#@"
    if len(password) < 6:
        return "Minimum length 6 characters"
    elif len(password) > 16:
        return "Maximum length 16 characters"
    elif password.isdigit():
        return "At least 1 letter between [a-z] and 1 letter between [A-Z]"
    elif password.isalpha():
        return "At least 1 number between [0-9]"
    elif not any(char.isupper() for char in password):
        return "At least 1 letter must be upperCase"
    elif not any(char.islower() for char in password):
        return "At least 1 letter must be lowercase"
    elif not any(char in special_characters for char in password):
        return "At least 1 character from [$#@]"
    else:
        return "password is valid"


passwd = input("Input your password : ")
print(passwordValidation(passwd))
