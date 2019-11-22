class test:
    data = 100
    __data2 = 200           # Pseudo private variable

    def add(a, b):
        return a + b
    
    def __sub(a, b):
        return a - b

print(test.data)

print(test._test__data2)

print(test.add(2, 5))

print(test._test__sub(9, 2))