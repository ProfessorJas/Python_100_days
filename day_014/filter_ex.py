def boy(n):
    if n % 2 == 0:
        return True

    return False

# self-defined function
filterList = filter(boy, list(range(20)))

print(list(filterList))
# print out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

filterList2 = filter(lambda n: n % 2 == 0, list(range(20)))


print(*filterList2)
# print out: 0 2 4 6 8 10 12 14 16 18

list01 = [5, -1, 3, 6, -7, 8, -11, 2]
list02 = ['apple', 'pig', 'monkey', 'money']

print(sorted(list01))
# print out: [-11, -7, -1, 2, 3, 5, 6, 8]

print(sorted(list01, key=abs))
# print out: [-1, 2, 3, 5, 6, -7, 8, -11]

# default ascending
print(sorted(list02))
# print out: ['apple', 'money', 'monkey', 'pig']

# descending order
print(sorted(list02, reverse=True))
# print out: ['pig', 'monkey', 'money', 'apple']

# reverse anonymous function
print(sorted(list02, key=lambda x: len(x), reverse=True))
# print out: ['monkey', 'apple', 'money', 'pig']
