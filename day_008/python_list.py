# list function
ll = list('hello python list')
print(ll)
print(ll[2])
print(ll[2:4])  # [2:4] => [2, 4) => 2, 3

# len function
list1 = ['Google', 'Amigo', 123, 77]
print(len(list1))

# max function
list_num = [1, 7, 17, 25, 34, 77]

print(max(list_num))

# min function
print(min(list_num))

## list method
# append
list_append = [1, 2, 3, 4]
list_append.append(5)       # append can only add a single element at last
print(list_append)


# count
num = [1, 2, 4, 7, 7, 7, 7, 7, 7, 7, 9]
print(num.count(7))     # 7
print(num.count(10))    # 0

name = ['a', 'a', ' ark', 'ash', 'amgio']
print(name.count('a'))      # 2

# extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)         # extend function can only take a collection like a list
print(a)

# index
# index can find the index where the element first appear

content = ['I', 'am', 'the', 'best', 'best', 'in', 'the', 'whole', 'world']
#           0    1      2       3       4      5     6       7        8
print(content.index('the'))        # 2
print(content.index('best'))       # 3

#------------------------
# insert
num = [1, 2, 5, 6, 7]
num.insert(2, 3)
print(num)

num.insert(3, 4)
print(num)

# pop
x = [1, 2, 3]
print(x)
print("The element being popped is: %s" % x.pop())
print("The new list is: %s" % x)
print("The element being popped is: %s" % x.pop())
print("The new list is: %s" % x)

x = [1, 2, 3]

print(x)
x.append(x.pop())

print(x)

# remove
# it remove the first element that matchs the query string
content = ['where', 'who', 'lisi', 'cotent', 'who', 'who']
print(content)
content.remove('who')
print(content)

# reverse
# it would reverse the element in the list
x = [1, 2, 3]
print("x: %s" % x)
x.reverse()
print("the reversed x: %s" % x)

# sort
x = [2, 3, 5, 7, 1, 4, 8, 6, 10]
x.sort()
print(x)

# clear
list1 = ['google', 'Amigo', 17, 34]
print(list1)
list1.clear()       # clear out the content in the list
print(list1)

# copy
list1 = ['google', 'Amigo', 17, 34]
list2 = list1.copy()
print(list2)

## List operations
x = [1, 2, 3, 4, 5]
print(x)

x[3] = 7

print(x)

del x[4]

print(x)

# sliding assignment
name = list('Pyther')
name[4:] = 'on'

print(name)

num = [1, 4, 5]
num[1:1] = [2, 3]
print(num)

num = [1, 2, 3, 4, 5]
num[1:3] = []

print(num)

num[-1: -1] = [5, 5, 5]
print(num)



