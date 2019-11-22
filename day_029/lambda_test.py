add = lambda a, b: a + b

print(add(1, 2))
# 3

print(add('ab', 'ad'))
# abad

add = lambda a, b: ord(a) + ord(b)
print(add('1','2'))