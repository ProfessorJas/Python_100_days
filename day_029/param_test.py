# Parameter前面加上*号，说明可以接受任意个数的参数
def f(a, *b):
    s = a

    for x in b:
        s += x
    return s

def add(a, *b, c):
    s = a + c

    for x in b:
        s += x

    return s

if __name__ == "__main__":
    print(f(1, 2))

    print(f(1, 2, 3))

    print(f(1, 2, 3, 4, 5))
    print('-' * 10)

    print(add(1, 2, c = 3))
    # 6

    print(add(1, c = 3))
    # 3

    print(add(1, 1, 2, 3, 4, 5, c = 3))
    # 19