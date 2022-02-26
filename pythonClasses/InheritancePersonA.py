class InheritancePersonA:
    def __init__(self, name):
        self.name = name

    def setDetails(self, sex, age):
        self.sex = sex
        self.age = age

    def getDetails(self):
        print(self.name, self.age, self.sex)
