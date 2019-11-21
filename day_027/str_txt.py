x = str(123)

print(x)

print(type(x))

x = str(r'abc123')
print(x)

# Single and double quotes
print('123"abc')    # 123"abc

print("123'abc")    # 123'abc

# Triple quotes
x ="""This is
    a Python
    multiline string."""

'''
This is
    a Python
    multiline string.
'''

print(x)

# len to get the length of a string
print(len('abcdef'))

print(len('I love python!'))

# string concatenation
print('12''34''56')             # 123456
print('12' '34' '56')           # 123456
print('12' + '34' + '56')       # 123456

print('12' * 3)                 # 121212

# comma to split tuple
x = 'abc', 'edf'
print(x)
print(type(x))

# iterate a string
for a in 'abc':
    print(a)

print()
print('-'*7 + '\n')

# string sliding using index
x = 'abcdef'
print(x[0])
print(x[-1])

print(x[3])
print(x[-3])

print(x[-6])
# print(x[-7])              # error: index out of bound

# string sliding using: x[start: end]
x = 'abcdef'
print(x[1:4])               # bcd

print(x[1:])                # bcdef

print(x[:4])                # abcd, == x[0, 4] == x[0] x[1] x[2] x[3]

print(x[:-1])               # abcde, which means print out everything except the last one

print(x[:])                 # abcdef, dump out everything

# add steps to slide a string
x = '0123456789'
print(x[1:7:2])             # 135, from 1 to 6, step = 2

print(x[::2])               # 02468, print out everything where step = 2

print(x[7: 1: -2])          # 753, from 7 to 2, step = -2

print(x[::-1])              # 9876543210

# string transformation
print(str(123))             # 123
print(str(1.23))            # 1.23
print(str(2 + 4j))          # (2 + 4j)