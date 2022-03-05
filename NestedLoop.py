# Write a Python program to construct the following pattern, using a nested loop number.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

n = int(input("Enter the number to print the number in repeated form : "))
n +=1
for i in range(n):
    for j in range(i):
        print(i, end=" ")
    print(end="\n")

#another way....
for i in range(n):
    print(str(i) * i )
