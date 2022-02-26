#the rule that each number (called a Fibonacci number) is equal to the sum of the preceding two numbers. ...
#F (0) = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...


startNumber = 0
nextNumber = 1
#printing 20 fibonacci number
print(startNumber, end=',')

for i in range(20):
    sumOfPrevTwoNumbers = startNumber + nextNumber
    print(sumOfPrevTwoNumbers, end=',')
    nextNumber = startNumber
    startNumber = sumOfPrevTwoNumbers



