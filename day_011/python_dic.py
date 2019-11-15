# define a dictionary and assign some values
MyDog = {'size': 'big', 'color': 'white', 'character': 'gentle'}

# get the value from the key
print(MyDog['size'])

print('My dog has ' + MyDog['color'] + ' fur.\n' + 'It has a ' + MyDog['character'] + ' character.')

# dict data type
MyCon = {12: 'big', 0: 'white', 354: 'gentle', 1: 'good'}

# difference bewteen dictionary and list
list1 = ['amigo', 23, 'Shanghai']
list2 = [23, 'Shanghai', 'amigo']
print(list1 == list2)               # False

dic1 = {'name': 'Amigo', 'age': 23, 'address': 'Shanghai'}
dic2 = {'age': 23, 'name': 'Amigo', 'address': 'Shanghai'}
print(dic1 == dic2)                 # True

# values will overwrite the duplicate key
dic1 = {'name': 'jaja', 'age': 23, 'address': 'Shanghai', 'name': 'Amigo'}
print(dic1)

print(dic1['name'])

dict = {'Alice': '123', 'Bob': '234', 'Ceci': '456', ('a', 'b'): (12, 34)}
dict = {'Name': 'Frandy', 'Age': 20, 'Class': 'One'}

dict['Age'] = 19

# add new key, value pair
dict['School'] = 'Duke University'

print(dict)

# clear the dictionary
dict.clear()

print(dict)