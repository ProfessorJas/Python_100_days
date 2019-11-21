print(())               # create an empty tuple

print(tuple())          # create an empty tuple

print((2, ))            # create a single element tuple. Comma cannot be ignored
# (2,)

print((1, 2.5, 'abc', [1, 2]))      # tuple with elements of different types
# (1, 2.5, 'abc', [1, 2])

print((1, 2, ('a', 'b')))           # tuple can embedded with tuple
# (1, 2, ('a', 'b'))

print(tuple('abcd'))                # create tuple with string
# ('a', 'b', 'c', 'd')

print(tuple(['1', '2', '3']))         # create tuple with list
# ('1', '2', '3')

print(tuple(x * 2 for x in range(5)))
# (0, 2, 4, 6, 8)

print('-------')
# iterate each element in the tuple
for x in (1, 2.5, 'abc', [1, 2]):
    print(x)

print()
x = tuple(range(10))
print(x)
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(x[1])         # 1

print(x[-1])        # 9

print(x[2:5])       # (2, 3, 4)

print(x[2:])        # (2, 3, 4, 5, 6, 7, 8, 9)

print(x[:5])        # (0, 1, 2, 3, 4)

print(x[1:7:2])     # (1, 3, 5)

print(x[7:1:-2])    # (7, 5, 3)

x = (1, 2, 3) * 3
print(x)            # (1, 2, 3, 1, 2, 3, 1, 2, 3)

print(x.index(2))   # 1
print(x.index(1))   # 0

print(x.index(2, 2))    # 4
print(x.index(2, 2, 7))     # 4 search from the position 2 to 7 where the value is 2

# print(x.index(5))         # it will run into an error statement

# the length of tuple
print(len((1, 2, 3, 4)))        # 4


# merge tuple
print((1, 2) + ('ab', 'cd') + (2.45,))

# tuple repetition
print((1, 2) * 3)

print(2 in (1, 2))
print(7 in (1, 2))

x = ((1, 2, 3), (4, 5, 6,), (7, 8, 9))
print(x)

x = (1, 2) * 3
print(x)