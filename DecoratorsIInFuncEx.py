"""
Decorators are used wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
"""

def lowerCase(str):
    return str.lower()

def upperCase(str):
    return str.upper()

def convertCase(convertCase,str):
    convertedString = convertCase(str)
    print(convertedString)


convertCase(lowerCase, "SANTOSH")
