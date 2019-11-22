class Person(object):
    # Define class attribute and assign the value
    nation = 'China'
    city = 'Shanghai'

    def __init__(self, name, age):
        # define object attribute
        self.name = name
        self.age = age

p1 = Person('Joe Wang', 34)
p2 = Person('Javier Amgio', 25)

print('Visit the class attribute nation: %s, city: %s' % (Person.nation, Person.city))

print('Visit the class attribute through p1 object nation: %s, city: %s' % (p1.nation, p1.city))
print('Visit the class attribute through p2 object nation: %s, city: %s' % (p2.nation, p2.city))

print('Visit the object attribute through p1 object name: %s, age: %s' % (p1.name, p1.age))
print('Visit the object attribute thorugh p2 object name: %s, age: %s' % (p2.name, p2.age))

print('-' * 34)

# Add city attribute for class object p1 and p2
print('After add city attribute for p1 and p2')
p1.city = 'Blacksburg'
p2.city = 'Peru'

print('Visit the class attribute through class, nation: %s, city: %s' % (Person.nation, Person.city))

print('Visit the class attribute through p1 object, nation: %s, city: %s' % (p1.nation, p1.city))
print('Visit the class attribute through p2 object, nation: %s, city: %s' % (p2.nation, p2.city))

print('You cannot visit the object attribute through class')