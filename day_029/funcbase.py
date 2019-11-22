def pascal(n):
    if not str(n).isdecimal() or n < 2 or n > 25:
        print('Parameter must be greater than 2 and less than 25')
        return False

    x = []          # result

    # 初始化不规则Pascal Triangle
    for i in range(1, n + 1):
        x.append([1] * i)
    
    # Calculate other values of Pascal Triangle
    for i in range(2, n):
        for j in range(1, i):
            x[i][j] = x[i - 1][j - 1] + x[i - 1][j]
    
    # Print out Pascal Triangle
    for i in range(n):
        if n <= 10:
            print('' * (40 - 4 * i), end='')

        for j in range(i + 1):
            print('%-8d' % x[i][j], end = '')

        print()

if __name__ == "__main__":
    print("Test")

    print(pascal(2))

    print(pascal(10))