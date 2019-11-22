# Create variable set
#1.  Normal way to create a set
s_set = {'Hola', 'Amigo', 'Jaja'}

print(s_set)

s_set.add('Hola')
print(s_set)

s_set.add('amigo')
print(s_set)

# 2. Use set() method to create
s2_set = set(['Amigo', 'Amigo', 'Rudy', 'Hola'])
print(s2_set)
# {'Hola', 'Rudy', 'Amigo'}

# Create an empty set
es = set()
print(es)

# 2. Create unchangeable set
s3_set = frozenset(['Hola', 'Amigo', "Jaja"])
print(s3_set)
# frozenset({'Hola', 'Jaja', 'Amigo'})

print('-' * 10)

### Visit the set
# iterate through the set
s_set = {'A', 'B', 'C'}
print('the element in the set: ')
for e in s_set:
    print(e)

### Update the set
# 1. add a new element
s1_set = {'A', 'B'}
s2_set = {'C', 'D', 'E'}

print('The default s1_set is:', s1_set)
# The default s1_set is: {'A', 'B'}

s1_set.add('F')
print('After adding F to s1_set:', s1_set)
# After adding F to s1_set: {'A', 'B', 'F'}

s1_set.update(s2_set)       # Add a set to a set
print("Use update method to add a set to a set: ", s1_set)
# Use update method to add a set to a set:  {'F', 'C', 'A', 'D', 'B', 'E'}

x = {1, 2}
x.update({10, 20})
print(x)
# {1, 2, 10, 20}

#
### Set is unchangeable, therefore you cannot add changeable object to the set.
### You cannot add set, list, dictionary object to a set
### You can add a tuple object to a set
#
x.add((1, 2, 3))
print(x)
# {1, 2, 10, (1, 2, 3), 20}

# delete elements
s_set = {'a', 'b', 'c'}
print('The default s_set is:', s_set)

# 1. Use remove method to delete  'a'
s_set.remove('a')

print(s_set)
# {'c', 'b'}

obj = s_set.pop()
print("The popped item is:", obj)

if obj == 'c':
    s_set.discard('b')
    print('After "b" being deleted:', s_set)
else:
    s_set.discard('c')
    print('After "c" being deleted:', s_set)

s_set = {'aa', 'vv', 'kk'}
print('After reassigning:', s_set)

s_set.clear()
print("After being cleared:", s_set)

print('-' * 10)

# set operation
x = {1, 2, 'a', 'bc'}
y = {1, 'a', 5}
print(len(x))


print('a' in x)
# True

print(x - y)
# {2, 'bc'}

print(x | y)
# {'bc', 1, 2, 5, 'a'}

print(x & y)
# {1, 'a'}

print(x ^ y)
# {2, 5, 'bc'}

print(x < y)
# False

print({1, 2} < x)
# True
