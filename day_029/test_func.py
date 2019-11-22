def my_python_func():
    print('Hello Python')

def add(a, b):
    return a + b

x = add

def f(a):
    a[0] = 'abc'



if __name__ == "__main__":
    my_python_func()

    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))

    print("sum =",add(a, b))
    #sum = 8

    print("x =", x(a, b))
    # x = 8

    print("concatenation:", add('hola ', 'amigo'))
    # concatenation: hola amigo

    print("Tuple Addition:", add((1, 2), (3, 4)))
    # Tuple Addition: (1, 2, 3, 4)

    print("List Addition:", add([1, 2], [3, 4]))
    # List Addition: [1, 2, 3, 4]

    print("Passing parameter:")
    print('a - b:', add(a='ab', b='cd'))
    # a - b: abcd

    print('b - a:', add(b='ab', a = 'cd'))
    # b - a: cdab

    x = [1, 2]
    print(f(x))
