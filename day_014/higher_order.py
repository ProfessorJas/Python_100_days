from math import factorial

def high_fun(f, arr):
    return [f(x) for x in arr]

def square(n):
    return n**2

# use the Python plug-in function
print(high_fun(factorial, list(range(10))))
# print out [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# use the self-defined function
print(high_fun(square, list(range(10))))
# print out [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]