import reprlib

a = [1, 2, 3, [4, 5], 6, 7]

reprlib.aRepr.maxlevel = 1

print(reprlib.repr(a))
# [1, 2, 3, [...], 6, 7]