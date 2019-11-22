class Methods(object):
    # Define a class

    # Define a public method
    def publicMethod(self):
        return 'Public method'

    # Define a private method
    def __privateMethod(self):
        return 'Prviate method'

m = Methods()
print('Use the object to call:', m.publicMethod())
print('Use the object to call:', m._Methods__privateMethod())

print('-' * 17)

print('Use the class to call:', Methods.publicMethod(m))
print('Use the class to call:', Methods._Methods__privateMethod(m))