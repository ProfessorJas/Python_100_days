class Car(object):
    # Define an object

    sales_price = 150000            # Public class attribute
    __manufacture_price = 120000    # Private class attribute

    def __init__(self, brand, serial):
        self.brand = brand          # Public object attribute
        self.__serial = serial      # Private object attribute

print('Visit the public class attribute:', Car.sales_price)
print('Visit the private class attribute:', Car._Car__manufacture_price)    

c = Car('VW', 'Golf')
print('Visit the public object attribute of c, brand:', c.brand)
print('Visit the private object attribur tof c, serial:', c._Car__serial)