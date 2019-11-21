for i in range(1, 10):
    str = ""

    for j in range(1, i + 1):
        str = str + '%d * %d = %-2d ' % (j, i, j * i)

    print(str)
    print()