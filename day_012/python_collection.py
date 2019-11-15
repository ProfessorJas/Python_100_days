dict = {}

print(type(dict))

s = set(('Hello', 'World'))

print(s)

## add can add a new element
s.add('!')

print('Set after adding the character', s)

## update can also add new elements, and parameters can be lists, tuple, or dictionary
# add list
s.update([1, 3], [2, 4])
print('The newest collection is:', s)

# add tuple
s.update(('h', 'j'))
print('The newest collection is:,', s)

# remove an element from dictionary
s.remove(2)
print("After remove 2: ", s)

# if remove a non-existed element in dictionary, it will throw and error
# s.remove('hi')
# print('After remvoe hi: ', s)           # It will throw and error


# discard can also remove element and it will not throw and error if there did not exist that element
thisset = set(('Google', 'Amazon', 'Facebook', 'MicroSoft'))
thisset.discard('jaja')
print(thisset)

thisset.discard('Amazon')
print(thisset)

# pop() method can randomly delete an element
print(s)

s.pop()
print(s)

# len() will return the number of element
print("The length of the set is:", len(s))

# clear() will clear the set
s.clear()
print("After clear the set:", s)

# x in s can check whether s exists x
s = {'hello', 'word'}
print('hello' in s)
print('world' in s)

# collection operations
a = set('afjkskdjf kadjknvkds jcjmfadjadsivnfa')
b = set('resg fsdfvewafadsafbsdf')

print(a)
print(b)

# elements in a but not in b
print(a - b)

# elements in  a or b
print(a | b)

# elements in both a and b
print(a & b)

# elements in either a and b
print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# difference
x = {'apple', 'google', 'facebook'}
y = {'google', 'amazon', 'Facebook'}
z = x.difference(y)
print(z)

x1 = {1, 2, 3, 4}
y1 = {1, 2, 3}

x1.difference_update(y1)
print(x1)

# intersection
x = {"apple", "banana", "cherry"}
y = {"google", "amazon", "apple"}
z = x.intersection(y)

print(z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)

# intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "amazon", "apple"}
x.intersection_update(y)
print(x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)

print(x)

# union will merge collections, and duplicate items will only appear once
x = {"google", "facebook", "apple"}
y = {"apple", "cherry", "banana"}
z = x.union(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)
print(result)

# isdisjoint check is there exists the same elements in both set, return true if not, false otherwise
x = {"google", 'banana', "cherry"}
y = {"apple", "amazon", "google"}
z = x.isdisjoint(y)
print(z)

x = {'a', 'b', 'c'}
y = {'d', 'e', 'ff'}
z = x.isdisjoint(y)
print(z)

# issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(z)

# issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)
print(z)

# symmetric_difference will return the same element
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.symmetric_difference(y)

print(z)

# symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

x.symmetric_difference_update(y)

print(x)