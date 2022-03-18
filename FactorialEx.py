# this is the  example of factorial table
# 4! is 4 * 3 * 2 * 1 = 24

def findFactorial(n):
    f = 1

    for i in range(1, n + 1):
        f *= i
    return f


x = 4

print(findFactorial(int(x)))
