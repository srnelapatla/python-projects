# Multiple inheritance example
# child class inherit the properties from more than one parent class
from pythonClasses.MultipleInheritanceParentClassA import MultipleInheritanceParentClassA
from pythonClasses.MultipleInheritanceParentClassB import MultipleInheritanceParentClassB


class MultipleInheritanceChildClass(MultipleInheritanceParentClassA, MultipleInheritanceParentClassB):
    def __init__(self):
        print("this is from MultipleInheritanceChildClass")
        MultipleInheritanceParentClassA.__init__(self)
        MultipleInheritanceParentClassB.__init__(self)

    def printFromChildClass(self):
        print(self.classNameA, " and ", self.classNameB)
