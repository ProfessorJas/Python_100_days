tup1 = ('google', 'amigo', 17, 7)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", 'c', 'd', 'E'
tup4 = ()

print(tup1)

print("Element type in tup3 is %s" % type(tup3))

TupNum = (34)           # int class
print(type(TupNum))

TupNum = (34, )         # tuple class
print(type(TupNum))

# visiting the element in the tuple
tup1 = ('google', 'facebook', 'amazon', 1, 7, 17)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("The first element in tup1 is: %s" % tup1[0])
print("Range 1 - 5 in tup2 is: ", tup2[1:5])

# modify tuple
tup1 = ('Google', 'Facebook', 'Amazon', 'MicroSoft')
tup2 = (1, 2, 3, 4, 5, 6, 7)

print(tup1 + tup2)

# delete tuple
tup1 = ('Google', 'Facebook', 'Amazon', 'MicroSoft')
print(tup1)

# del tup1
# print("After delete tup1: ")

# print(tup1)               # it will run into an error saying tup1 is not defined

#----------------------------
tup1 = ('Google', 'Facebook', 'Amazon', 'MicroSoft', 'Apple')
print('The length of tup1 is : ', len(tup1))

# tuple concatenation
tup1 = (1, 2, 3)
tup2 = ('Facebook', 'Google', 'MicroSoft', 'Amazon')
tup3 = ("Hola", "Amigo", "jaja")

joined_tuple = tup1 + tup2 + tup3
print(joined_tuple)

# copy tuple
tup1 = ('Duplicate amigo| ')
print(tup1 * 7)

# visit the specific element
content = ('hello', 'world', '!!')
print(content)

print(content[1:])
print(content[:2])

print(content[-1])

print(content[-2])

# built-in function of tuple
tup1 = (21, 3, 44, 56, 3, 10)

# get the number of element in the tuple
print("The number of element in tup1 is: ", len(tup1))

# get the maximum element in the tuple
print("Max element is : ", max(tup1))

# get the minimum element in the tuple
print("Min element is : ", min(tup1))

# list <-> tuple
print(list(tup1))
list(tup1)
print(tuple(tup1))














