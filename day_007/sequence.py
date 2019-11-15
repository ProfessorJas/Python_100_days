# define a student sequence
stuinfo = ['amigo', 'jaja', 17]
print(stuinfo)

stuname = ['amigo', 'Xavi', 'Javier']
stuage = [17, 18, 19]
database = [stuname, stuage]

print("My database: %s" % database)
print("Names in my database: %s" % database[0])
print("ages in my datbase: %s" % database[1])
#-------------------------------

str = 'Amigo'
print("Character at index 0 is: %s" % str[0])
print("Character at index 1 is: %s" % str[1])
print("Character at index -1 is %s" % str[-1])
print("Character at index -2 is %s" % str[-2])

# sliding 分片
tag = ['https://www.cnblogs.com/yangyuqig/p/10101663.html']
print("The content which the underscore is from 0 - 24: %s" % tag[0][0:24])

#--------------------------------
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Number from 3 to 10 is: %s" % num[3: 10])

print("The first three numbers are: %s" % num[0:3])


# numbers between 0 and 6 where step is 2
print("Numbers between 0 and 6 where step is 2: %s" % num[0:6:2])

print("Sliding of negative number: %s" % num[7:-1])

print("Negative sliding: %s" %num[-9:-1])

# Get number in the first 6 elements where the step is 2
print("Get number in the first 6 elements where the step is 2: %s" % num[:6:2])

## Sequence Addition

a = 'Hola'
b = ' world!'
print("The result of a + b is : %s" % (a + b))

# Sequence multiplication
a = 'Hola Amigo! '
b = a * 3
print("The result of the multiplication is: %s" % b)


# the element in the Sequence
str = 'hello'
print('h' in str)

print('x' in str)

print('el' in str)

print('low' in str)

print('hello' in str)

# the length, maximum, minimum of the sequence
print(len([11, 22, 33]))        # 3

print(max([11, 23, 7]))         # 23

print(min([11, 23, 7]))         # 7