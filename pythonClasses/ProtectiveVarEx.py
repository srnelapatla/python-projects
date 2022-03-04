#Protective by prefixing the name of the member/var by a single underscore “_”.
##this is also example of class writing multiple classes in a single file
class ProtectiveVarEx:
    def __init__(self):
        self.a = 2
        self._b = 3


class DerivedClass(ProtectiveVarEx):
    def __init__(self):
        ProtectiveVarEx.__init__(self)
        self._b = 4
p = ProtectiveVarEx()
print(p._b)
d = DerivedClass()
print(d._b)

