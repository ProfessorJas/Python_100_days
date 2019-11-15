def f(a, l=[]):
    l.append(a)

    return l

if __name__ == "__main__":
    print(f(1))     # [1]
    print(f(2))     # [1, 2]
    print(f(3))     # [1, 2, 3]