a = 10              # a is a global value

def add(b):         # parameter b is the local variable of add
    c = a + b       # c is the local variable of the add function, a is the global variable outside

    return c

print(add(5))       # function call


a = 10

def show():
    a = 100

    print('In show(): a =', a)

show()
print('Globally: a =', a)

a = 10

def show():
    global a                # global用于在函数内部申明全局变量 
    print('a =', a)
    # a = 10

    a = 100
    print('a =', a)
    # a = 100
show()
print('a =', a)
# a = 100

print('-' * 10)

def test():
    a = 10

    def show():
        nonlocal a          # 申明a是test函数的本地变量
        a = 100             # 修改test函数的本地变量a
        print('In show(): a =', a)

    show()
    print('In test(): a =', a)

test()
'''
In show(): a = 100
In test(): a = 100
'''
