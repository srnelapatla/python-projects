# Write a Python program to get the frequency of the elements in a list.
# input
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

import collections

my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

print("original list is  ", my_list)

ctr = collections.Counter(my_list)

print("frequency of each element in the list is ", ctr)
