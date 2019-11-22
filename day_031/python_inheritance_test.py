class Student(object):              # Define a Student class
    baseClassData = 123

    def __init__(self, num, name, gender):
        self.num = num
        self.name = name
        self.gender = gender

    def printInformation(self):
        print('Num: %d, Name: %s, Gender: %s' % (self.num, self.name, self.gender))


class Student1(Student):            # Declare that the parent class is Student
    def __init__(self, num, name, gender, age, address):
        Student.__init__(self, num, name, gender)
        self.age = age
        self.address = address

    def printInformation1(self):
        Student.printInformation(self)      # Call the printInformation() from the parent class

        print('Age: %d, Address: %s' % (self.age, self.address))

s = Student1(123, 'Amigo', 'M', 25, 'Shanghai')
s.printInformation1()

print('=='*25)
print('baseClassData from the parent class:', s.baseClassData)