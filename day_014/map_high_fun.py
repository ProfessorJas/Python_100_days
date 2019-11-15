from math import factorial

def square(n):
    return n**2

# use the Python plug-in function
facmap = map(factorial, list(range(10)))
print(list(facmap))
# print out: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# use the self-defined function
squaremap = map(square, list(range(10)))
print(list(squaremap))
# print out: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# We can also use Labmda function
lamMap = map(lambda x: x * 2, list(range(10)))
print(list(lamMap))
# print out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Pass in multiple sequences
mutiMap = map(lambda x, y: {x: y}, list(range(10)), list(range(11, 15)))
print(list(mutiMap))
# print out: [11, 13, 15, 17]