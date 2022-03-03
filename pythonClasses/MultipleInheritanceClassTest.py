#Multiple inheritance example
# child class inherit the properties from more than one parent class
from pythonClasses.MultipleInheritanceChildClass import MultipleInheritanceChildClass


class MultipleInheritanceClassTest:
    ma1 = MultipleInheritanceChildClass()

    ma1.printFromChildClass() #this will print init values from ParentClassA ParentClassB

    ma1.classNameChg("hey changing class name A property value ")
    ma1.printFromChildClass()  #this will print changed value from parent classA
