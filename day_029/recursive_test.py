def add(a, b):
    return a + b

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

print(fac(5))       # 5 * 4 * 3 * 2 * 1
# 120

d = [lambda a, b: a + b, lambda a, b: a * b]
print(d[0](1, 3))

print(d[1](1, 3))

d = [add, fac]      # Create a function list
print(d[0](1, 2))
# 3

print(d[1](5))
# 120

d = (add, fac)      # Create a function tuple
print(d[0](2, 3))
# 5

print(d[1](5))
# 120

d = {'sum': add, 'factorial': fac}
print(d['sum'](1, 2))

print(d['factorial'](5))