"""
lamda is the function without a name
"""

## add two number with function



def addTwoNumber(a,b):
    return a + b

print(addTwoNumber(1,5)) #this returns 6

#now with lamda
sum = lambda  x, y : x + y

print(sum(1,5))


#now with lamda
operations = lambda  x, y : (x + y , x -y , x * y)


print(operations(1,5))

