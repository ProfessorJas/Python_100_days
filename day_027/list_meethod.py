print([])               # create an empty list object
# []

print(list())           # create an empty list object
# []

print([1, 2, 4])        # list with the same type

print([1, 2, 3, ('a', 'bc', 'defg'), [12, 34, 'amigo']])        # list with different type

print(list('abcd'))     # listify an iterative object       # ['a', 'b', 'c', 'd']

print(list((1, 22, 333)))   # [1, 22, 333]      listify a tuple

# get the length
print(len([]))          # 0

print(len([1, 2, ('a', 'abc'), [12, 34]]))      # 4

# merge a list
print([1, 2] + ['abc', 20])     # [1, 2, 'abc', 20]

# repetition
print([1, 2] * 3)
# [1, 2, 1, 2, 1, 2]

print('----------\n')
# iteration
x = [1, 2, ('a', 'b'), ['ab', 'cd', 'efg']]
for amigo in x:
    print(amigo)

print(2 in [1, 2, 3])           # True

print('a' in [1, 2, 3])         # False

x = [1, 2, ['a', 'b']]
print(x[0])                     # 1

print(x[2])                     # ['a', 'b']

print(x[-1])                    # ['a', 'b']

x[2] = 200                      # modify the second list object
print(x)

print(x + list(range(10)))      # [1, 2, 200, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[2: 5])                  # [200]

x = x + list(range(10))
print(x[2:5])                   # [200, 0, 1]

print(x[2:])                    # [200, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(x[:5])                    # [1, 2, 200, 0, 1]

print(x[2:7:2])                 # [200, 1, 3]

print(x[7:2:-2])                # [4, 2, 0]

x[2: 5] = 'abc'
print(x)                        # [1, 2, 'a', 'b', 'c', 2, 3, 4, 5, 6, 7, 8, 9]

# Matrix
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(x)

print(x[0])

print(x[0][0])

# visit, sort, and reverse the list

# append adds an element at the end of the list
x = [1, 2]
x.append('amigo')
print(x)                # [1, 2, 'amigo']

# extend adds several object at the end of the list
x = [1, 2]
x.extend(['a', 'b'])
print(x)                # [1, 2, 'a', 'b']

x.append('ab')
print(x)                # [1, 2, 'a', 'b', 'ab']

x = [1, 2, 3]
x.insert(1, 'abc')      # insert the element at the specific position
print(x)                # [1, 'abc', 2, 3]

x = [9, 8, 7, 7]
x.remove(7)             # remove will delete the specific object, if it has duplicate, remove the first
print(x)

x = [1, 2, 3, 4]
print(x.pop())      # 4
print(x)            # [1, 2, 3]

print(x.pop(1))     # 2  # pop delete the item at index 1
print(x)            # [1, 3]


x = [10, 2, 30, 5]
x.sort()
print(x)            # [2, 5, 10, 30]


x = ['bbc', 'abc', 'abc', 'BBC', 'Abc']
x.sort()
print(x)                    # ['Abc', 'BBC', 'abc', 'abc', 'bbc']

x = [1, 2, 3]
x.reverse()
print(x)                    # [3, 2, 1]


