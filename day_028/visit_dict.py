dict_1 = {1: "a", 2: 'b', 3: 'c'}

print("Looping dict_1: ", dict_1)

for key in dict_1:
    print("dict_1[%s] = " % key, dict_1[key])
'''
dict_1[1] =  a
dict_1[2] =  b
dict_1[3] =  c
'''

for (key, value) in dict_1.items():
    print("dict_1[%s] = " % key, value)
'''
dict_1[1] =  a
dict_1[2] =  b
dict_1[3] =  c
'''

x = {'name': 'John', 'age': 25}
y = x.keys()
print(y)
# dict_keys(['name', 'age'])

print(x['age'])
# 25

print(x.values())
# dict_values(['John', 25])

### update the dictionary
print('-' * 10)
# define a dictionary with 3 elements
s_dict = {1001: "Mr. Wong", 1002: "Mr. Clarke", 1003: "Mr. Taylor"}
print("There are", str(len(s_dict)), "students")

print("Here comes another student Amigo, and we assign 1004 to him: ")
s_dict[1004] = 'Mr. Amigo'
print("There are", str(len(s_dict)), "students. They are: ")

for key in s_dict:
    print("s_dict[%s] = " % key, s_dict[key])

print("Here comes another student Big Amigo, and we assign 1004 to him: ")
s_dict[1004] = 'Big Amigo'
print("There are", str(len(s_dict)), "students. They are: ")

for key in s_dict:
    print("s_dict[%s] = " % key, s_dict[key])

print('-' * 10)

x = {'name': 'John', 'age': 25}
print(x.setdefault('name'))         # 返回指定值的映射值
# John

# Use setdefault to add an element to dictionary
print(x.setdefault('sex'))          # 键不存在，为字典添加键值对，映射值默认为None
# None

print(x)
# {'name': 'John', 'age': 25, 'sex': None}

x.setdefault('phone', 123456)       # add KV pair
print(x)
# {'name': 'John', 'age': 25, 'sex': None, 'phone': 123456}

x['phone'] = '654321'               # modify the KV pair by assigning the value to the key
print(x)

print('-' * 10)

### delete the elementi

# use del keyword
del(x['phone'])
print(x)

print(x.pop('age', "Age does not exist"))
# 25

print(x.pop('age', "Age does not exist"))
# Age does not exist

print(x)

print('-' * 10)

## delete demo
s_dict = {1:'amigo', 2:'hola', 3:'jaja'}
print('The dict:', s_dict)

# 1. Use del() function to delete the element
del(s_dict[1])

print('After using del method to delete key 1: ', s_dict)

# 2.1 Use pop() function to delete the element which does not exist
print(s_dict.pop(1, "The item does not exist"))

# 2.2 Use pop() function to delete the element which does exist
print(s_dict.pop(2, "The item does not exist"))

# Use del to delete the element
del s_dict[3]
print(s_dict)
# {}


### Methods of dictionary
#1. get length
# Use len()
x = dict(zip(['name', 'age'], ['John', '25']))
print(x)
# {'name': 'John', 'age': '25'}

print(len(x))
# 2

# 2. 关系判断
print('name' in x)
# True

print('sex' in x)
# False

# 3. clear(): are used to clear the dictionary
x = dict(name = 'John', age = 25)
print(x)
# {'name': 'John', 'age': 25}

x.clear()
print(x)
# {}

# 4. copy(): are used to copy dictionary object
x = {'name': 'John', 'age': 25}
y = x                               # 直接赋值，x和y refer to the same dictionary object

print(y)

x['name'] = 'Jaja'

print(x, y)
# {'name': 'Jaja', 'age': 25} {'name': 'Jaja', 'age': 25}

print(y is x)   # True

y = x.copy()

y['name'] = 'Adios'

print(x, y)
# {'name': 'Jaja', 'age': 25} {'name': 'Adios', 'age': 25}

print(y is x)
# False

print('-' * 10)

## 4. get(key[,default])
print(x.get('name'))
print(y.get('name'))

print(x.get('sex'))
# None

print(x.get('sex', 'xxx'))          # similar to Java map.getOrDefault
# xxx

x = {'a': 1, 'b': 2}
kx = x.keys()
print(kx)
# dict_keys(['a', 'b'])

y = {'b': 3, 'c': 4}
ky = y.keys()
print(ky)

print(kx - ky)
# {'a'}

print(ky - kx)
# {'c'}

print(kx & ky)
# {'b'}

print(kx | ky)
# {'a', 'c', 'b'}

print(kx ^ ky)
# {'a', 'c'}







