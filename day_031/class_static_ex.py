class Methods(object):          # Define a Methods class
    # Use @classmethod to define public class method
    @classmethod
    def publicClassMethod(cls):
        return cls

    # Use @classmethod to define private class method
    @classmethod
    def __privateClassMethod(cls):
        return cls

    # Use @staticmethod to define public method
    @staticmethod
    def publicStaticMethod():
        return 'Public static method'

    # Use @staticmethod to define private method
    @staticmethod
    def __privateStaticMethod():
        return 'Private static method'

    # define public class
    def publicMethod(self):
        print('Call publicMethod')

    # Define private method
    def __privateMethod(self):
        print('Call privateMethod')

    # Use the built-in method, classmethod, to transfer public method publicMethod to class method
    publicMethodToClassMethod = classmethod(publicMethod)

    # Use the built-in method, classmeethod, to transfer private method privateMethod to class method
    privateMethodToClassMethod = classmethod(__privateMethod)

    # Use the built-in method staticmethod to transfer publicMethod to static method
    publicMethodToStaticMethod = staticmethod(publicMethod)

    # Use the built-in method staticmethod to transfer privateMethod to static method
    privateMethodToStaticMethod = staticmethod(__privateMethod)

m = Methods()

print('Use the class method, define public class method using @classmethod!', Methods.publicClassMethod())

print('Use the object method, define public class method using @classmethod!', m.publicClassMethod())

print('Use the class method, define private class method using @classmethod!', Methods._Methods__privateClassMethod())

print('Use the object method, define private class method using @classmethod!', m._Methods__privateClassMethod())


print('-' * 17)

print(Methods.publicClassMethod())
print(m.publicClassMethod())
print(Methods._Methods__privateClassMethod())
print(m._Methods__privateClassMethod())

print('-' * 17)

print(Methods.publicStaticMethod())
print(m.publicStaticMethod())

print(Methods._Methods__privateStaticMethod())
print(m._Methods__privateStaticMethod())

print('-' * 17)

print(Methods.publicMethodToClassMethod())
print(m.publicMethodToClassMethod())

print(Methods.privateMethodToClassMethod())
print(m.privateMethodToClassMethod())

print('-' * 17)

print(Methods.publicMethodToStaticMethod(m))
print(m.publicMethodToStaticMethod(m))

print(Methods.privateMethodToStaticMethod(m))
print(m.privateMethodToStaticMethod(m))