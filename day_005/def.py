# define a function
def hello():
    print("Hello World")

# call function
hello()

#--------------------------

# define a function
def helloN(name):
    print("Hello World: ", name)

# call function
helloN('Amigo')

#--------------------------

# define a function
def add(a, b):
    return a + b

def reduce(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# call function
print(add(1, 2))            # 1 + 2 = 3
print(reduce(1, 2))         # 1 - 2 = -1
print(multiply(1, 2))       # 1 * 2 = 2
print(divide(4, 1))         # 4 / 1 = 4
#-------------------------

# Return multiple value is also supported in Python
def more(x, y):
    nx = x + 2
    ny = y - 2

    return nx, ny

# call function
x, y = more(10, 10)
print(x, y)
#---------------------------

# recursion
def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n - 1)

print(fact(5))