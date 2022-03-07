# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output

def is_sublist(lst, subLst):
    lst = list(set(lst))  # this will remove the duplicates from the list and convert set back to list again.

    sub_set = False
    if subLst == []:   # this check  if list is empty or not.
        sub_set = True
    elif subLst == lst:  # this checks if both  lists are same element by element
        sub_set = True
    elif len(subLst) > len(lst):  # if sublist is larger than main list there is no need to check further if both lists are same or not.
        sub_set = False
    else:
        n = 0
        for i in range(len(lst)):
             for j in range(len(subLst)):
                 if lst[i] == subLst[j]:
                     n = n +1
        if n == len(subLst):
            sub_set = True

    return sub_set


a = [2, 4,7, 3, 5, 7]
b = [4, 3]
c = [3, 7]
d = [3, 9]
print(is_sublist(a, b))
print(is_sublist(a, c))
print(is_sublist(a, d))