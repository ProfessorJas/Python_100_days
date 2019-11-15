# 1. str.format() example
# 1)
print('{} Website: "{}!"'.format('Python技术', 'www.justdopython.com'))

# 2)
print('{0} and {1}'.format('Hello', 'Python'))
print('{0} {1}'.format('Hello', 'Python'))
print('{1} {0}'.format('Hello', 'Python'))

# 3)
print('{name} Website: {site}'.format(name='Pyton Tech', site='www.justdopython.com'))

# 4)
print('Online Shopping Website: {0}, {1}, {other}.'.format('Taobao', 'JD', other='PDD'))

# 5)
print("repr() shows quotes: {!a}; str() doesn't: {!s}".format('test1', 'test2'))

# 6)
import math

print('The value of PI is approximately {0:.3f}.'.format(math.pi))

# 7)
table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789}
for name, phone in table.items():print('{0:10} ==> {1:10}'.format(name, phone))

# 8)
table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789789789789}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# 2
str = input("Please input something: ")
print('What you said:', str)

# 3
# read
f = open('tmp.txt', 'r')
str = f.read(16)

print(str)
f.close()

# readline()
f = open('tmp.txt', 'r')
str = f.readline()
print(str)
f.close()

# readlines()
f = open('tmp.txt', 'r')
str = f.readlines(1)

print(str)
f.close()

# write()
f = open('tmp.txt', 'w')
hola = f.write('Hola World!')
print(hola)

f.close()

# seek()
f = open('tmp.txt', 'rb+')
f.write(b'0123456789abcdef')

# move the pointer
f.seek(5)
print(f.read())

# tell()
f = open('tmp.txt', 'r')
f.seek(5)
print(f.tell())

# close()
with open('tmp.txt', 'r') as f:
    read_data = f.read()
    print('Data is:', read_data)
print(f.closed)

# with()
with open('tmp.txt', 'r') as f:
    read_data = f.read()
    
print(f.closed)

# json operation
import json

data = {'id': '1', 'name': 'john', 'age': 12}
with open('t.json', 'w') as f:
    json.dump(data, f)

with open("t.json", 'r') as f:
    d = json.load(f)

print(d)
