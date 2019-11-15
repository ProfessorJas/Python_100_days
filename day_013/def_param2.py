def f(a, l=None):
    if l is None:
        l = []
    
    l.append(a)

    return l

if __name__ == "__main__":
    print(f(1))         # [1]
    print(f(2))         # [2]
    print(f(3))         # [3]

    list = ['hey yo']

    print(f(1, list))   # ['hey yo', 1]
    print(f(2, list))   # ['hey yo', 1, 2]
    print(f(3, list))   # ['hey yo', 1, 2, 3]