# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, -1])
# output
# -2

def second_smallest_nbr(list1):
    list1.sort(reverse=True)
    # a1, a2 = float('inf'), float('inf')
    temp1 = temp2 = 0
    for i in list1:
        if i < temp1:
            temp2 = temp1  # this step is for 2nd smallest
            temp1 = i
        else:
            continue
    return temp2  # temp1 returns the smallest

# print(second_smallest_nbr([1, 1, 1]))  this returns 0 even though it is not in the list

print(second_smallest_nbr([1, 2, -8, -8, -2, -100, -10, -100]))
