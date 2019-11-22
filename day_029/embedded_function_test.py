def add(a, b):
    def getsum(x):      # 在函数内部定义函数，将字符串转换为ASCII码求和
        s = 0

        for n in x:
            s += ord(n)

        return s

    return getsum(a) + getsum(b)        # call getsum function getsum()

if __name__ == "__main__":
    print(add('12', '34'))