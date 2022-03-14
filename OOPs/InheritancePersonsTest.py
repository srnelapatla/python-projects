from pythonClasses.InheritancePersonB import InheritancePersonB
from pythonClasses.InheritancePersonA import InheritancePersonA

class InheritencePersonsTest:
    pa = InheritancePersonA("Parent")
    pa.setDetails("male", 50)
    pa.getDetails()

    p1 = InheritancePersonB("child")
    p1.setDetails("female", 10)
    #p1.getDetails()
    p1.setOccupation("whatever")
    p1.getDetails()

