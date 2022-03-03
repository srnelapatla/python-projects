#Multiple inheritance example
# child class inherit the properties from more than one parent class

class MultipleInheritanceParentClassA:
    def __init__(self):
        self.classNameA = "MultipleInheritanceParentClassA"
    def classNameChg(self,classNM):
        self.classNameA=classNM
