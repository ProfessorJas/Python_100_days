
def printing():
    for x in range(1, 10):
        print(' ' * (15 - x), end = '')
        n = x

        while (n >= 1):
            print(n, sep='', end='')
            n -= 1
        
        n += 2
        while n <= x:
            print(n, sep='', end='')
            n += 1

        print()

if __name__ == "__main__":
    printing()
