#this is the example about private variable.
#private variable is defined using "__variableName"
class PrivateVariableEx:
    def __init__(self):
        self.var = "something"
        #declare private variable using double underscrore
        self.__privateVar = "PrivateVar"

pve = PrivateVariableEx()

print(pve.var)
###print(pve.privateVar)
"""uncommenting private variable access retunrs an error"""
