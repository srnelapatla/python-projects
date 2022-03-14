from pythonClasses.InheritancePersonA import InheritancePersonA


class InheritancePersonB(InheritancePersonA):
    def setOccupation(self, occ):
        self.occ = occ

    def getDetails(self):
        print(self.name, self.age, self.sex, self.occ)