a = int('12')

def outFunc():
    print("Call the outFunc() function")

    a = 4
    b = 3

    def inFunc():
        print('Call inFunc() function')

        b = 5
        c = a + b

        print('Call inFunc will return:', c)
        # 4 + 5 = 9

        return c

    e = b + inFunc()

    print('Call outFunc will return:', e)
    # 3 + (4 + 5) = 12

outFunc()