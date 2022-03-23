import pandas
d = {'a': 111, 'b': 222, 'c': 333}
ser = pandas.Series(data=d)
ser = pandas.Series(d)

# here ser is now work as a list
#print(ser[1:2])

#print(ser['c'])

print(ser[ser == 333 ])
#
# print(ser)
# ser = pandas.Series(data=d, index=['x', 'y', 'z'])
# print(ser)