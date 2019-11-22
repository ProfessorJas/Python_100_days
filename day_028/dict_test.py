# 1. normal way to create dictionary
dict0 = {}
print(dict0)
# {}

dict0['name'] = 'John'
dict0['age'] = 25
print(dict0)
# {'name': 'John', 'age': 25}

dict1 = {1:'a', 2:'b', 3:'c'}
print(dict1)
# {1: 'a', 2: 'b', 3: 'c'}

dict2 = {'1': 'a', '2': 'b', '3': 'c'}
print(dict2)
# {'1': 'a', '2': 'b', '3': 'c'}

dictbook = {'book': {'Python tutorial': 100, 'Java tutorial': 99}}      # embedded dictionary
print(dictbook)
# {'book': {'Python tutorial': 100, 'Java tutorial': 99}}

dict_num = {(1, 3, 5): 1, (2, 4, 6): 10}        # use the tuple as the key
print(dict_num)
# {(1, 3, 5): 1, (2, 4, 6): 10}
print('-'*10)

# 2. use the built-in function dict() to create the dictionary
print(dict())

dict3 = dict([(1, "a"), (2, "b"), (3, 'c')])        # list of (key, value)
print(dict3)
# {1: 'a', 2: 'b', 3: 'c'}

dict3 = dict(((1, "a"), (2, "b"), (3, "c")))        # tuple of (key, value)
print(dict3)
# {1: 'a', 2: 'b', 3: 'c'}

print(dict(name='john', age=25))        # 利用赋值格式的键值对创建字典

print(dict([('name', 'john'), ('age', 25)]))        # Use the list of tuple to create the dictionary

# 3. Use the built-in function fromkeys()
dict5 = {}.fromkeys((1, 2, 3), 'Person')            # assign the value to "person"
print(dict5)
# {1: 'Person', 2: 'Person', 3: 'Person'}

dict6 = {}.fromkeys((1, 2, 3))          # did not assign the value
print(dict6)
# {1: None, 2: None, 3: None}


print(dict.fromkeys(['name', 'age']))   # 创建无映射值的字典，默认值为None
# {'name': None, 'age': None}

print(dict.fromkeys('abc', 10))         # 使用字符串和映射值创建字典
# {'a': 10, 'b': 10, 'c': 10}

print('-'*10)
