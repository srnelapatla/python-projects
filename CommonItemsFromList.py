# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}

lst1 = ["Red", "Green", "Orange", "White"]
lst2 = ["Black", "Green", "White", "Pink"]
print(set(lst1) & set(lst2))
print(set(lst1).union(set(lst2)))
#print(set(lst1).difference(set(lst2)))
