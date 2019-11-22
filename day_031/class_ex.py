class Person(object):
    # reload __init__ method
    def __init__(self, name, gender, age, nation):
        print('Calling init when create a Person object')

        self.name = name
        self.gender = gender
        self.age = age
        self.nation = nation
    
    # define setName method
    def setName(self, name):
        self.name = name

    # define setGender method
    def setGender(self, gender):
        self.gender = gender

    # define setAge method
    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def getNation(self):
        return self.nation

    def printMessage(self):
        return 'Name: %s, Gender: %s, Age: %s, Nation: %s' % (self.name, self.gender, self.age, self.nation)

if __name__ == "__main__":
    CNPerson = Person('Mr. Wang', 'M', 23, 'CHINA')
    USPerson = Person('James', 'M',23, 'US')
    GBPerson = Person('Johnson', 'M', 55, 'GB')

    print("Chinese Person:", CNPerson.printMessage())
    print('US Person:', USPerson.printMessage())
    print('GB Person:', GBPerson.printMessage())

    CNPerson.setAge('27')
    print('The age of the CN Person is:', CNPerson.getAge())

    CNPerson.setName('Jo Wang')
    print('The name of the CN Person is:', CNPerson.getName())