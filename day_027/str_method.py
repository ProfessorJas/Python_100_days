str = 'abcabcabc'

print(str.count('ab'))      # count 'ab' in the str

print(str.count('ab', 2))   # count 'ab' in the str from index 2

print(str.endswith('bc'))   # endwith check with the string end with some string
                            # true

print(str.endswith('b'))    # false

print(str.startswith('ab')) # check whether string starts with some string
                            # True

print(str.startswith('b'))  # False

print(str.find('ab'))       # 0

print(str.find('ab', 2))    # find start from the second character, 3

print(str.find('ba'))       # -1

str = 'My name is {0}, and I am {1} years old.'.format('Amigo', 12)
print(str)
# My name is Amigo, and I am 12 years old.

str = 'My name is {1}, and I am {0} years old.'.format('Amigo', 12)
print(str)
# My name is 12, and I am Amigo years old.

str = "The %s's price id is %4.2f" % ('Amigio', 2.5)
print(str)

str = '%s %s %s' % (123, 1.23, 'jaja amigo')
print(str)
# 123 1.23 jaja amigo

str = '%r %r %r' % (123, 1.23, 'jaja amigo')
print(str)
# 123 1.23 'jaja amigo'

str = '123 %c %c' % ('a', 65)
print(str)
# 123 a A

str = '123 {0} {1}'.format('a', '65')
print(str)
# 123 a 65

str = '%d%d' % (123, 1.56)
print(str)
# 1231

str= '%d %d' % (123, 1.56)
print(str)
# 123 1

str = '%6d' % 123           # specify the width, filling in space by default
print(str)
#    123

str = '%6d' % 123456789
print(str)
# 123456789


str = '%-6d' % 123
print(str)
# '123   '


str = '%06d' % 123
print(str)
# 000123

x = 12.3456789
print('%e %f %g' % (x, x, x))
# 1.234568e+01 12.345679 12.3457

x = 1.234e10
print('%E %F %G' % (x, x, x))
# 1.234000E+10 12340000000.000000 1.234E+10

str = '\n\r    abc      \n\r'.strip()       # strip method would remove all the space, tab, and new line character
print(str)
# abc

str = 'www.xhu.edu.cn'.strip('wcn')         # delete the specified characters
print(str)
# .xhu.edu.

str = 'ab12' * 4
print(str)
print(str.replace('ab', 'amigo'))        # replace the specific characters with other characters

print(str.replace('ab', 'amigo', 2))

str = "this is string example....wow!!!"
print (str.replace("is", "was", 3))



str = 'ab cd ef'
print(str.split())
# ['ab', 'cd', 'ef']

str = 'ab,cd,ef'
print(str.split(','))
# ['ab', 'cd', 'ef']

str = 'ab,cd,ed'
print(str.split(',', 1))
# ['ab', 'cd,ed']

