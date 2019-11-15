# define the class
class Car:
    pass

# instantiate an Car object
c = Car()

class Car:
    name = 'BMW'

# calling the class method
# 1. use @classmethod
# 2. Use cls pass the object, don't need to instantiate
class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    @classmethod
    def run(cls, speed):
        print(cls.name, speed, 'km/s')

# Calling method 1
c = Car('VW Golf')
c.run(100)

# Calling method 2
Car.run(120)

# static method
# 1. use 'staticmethod' decorator and without self
class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def run(speed):
        print(Car.name, speed, 'km/s')

# calling method 1
c = Car('BMW')
c.run(100)

# calling method 2
Car.run(120)

##
# instance method       ***
##
class Car(object):
    # name = 'BMW'

    def __init__(self, name):
        self.name = name

    def run(self, speed):
        print(self.name, speed, "km/s")

c = Car('VW Golf')
c.run(100)

# Class inheritance
# parent class
class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name

    def run(self, speed):
        print(self.name, speed, 'km/s')

# child class
class BMWcar(Car):
    conf = "Eco Model"
    pass

# calling run method in the parent Car class
bc = BMWcar("Eco BMW car")
bc.run(99)

# Polymophism
# parent class
class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    def run(self, speed):
        print('Car --> ', self.name, speed, 'km/s')

# child class 1
class BMWcar(Car):
    def run(self, speed):
        print('BMW --> ', self.name, speed, 'km/s')

# child class 2
class VWcar(Car):
    def run(self, speed):
        print('VW -- > ', self.name, speed, 'km/s')

# calling parent constructor
c = Car("Car")
c.run(120)

c = BMWcar("BMW")
c.run(150)

c = VWcar("VW")
c.run("144")