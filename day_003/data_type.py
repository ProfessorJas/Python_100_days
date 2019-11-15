# Number
'''
    Python supports 3 different data type
    1. Int: 
    2. Float: 2.5e2 = 2.5 * 10 ^ 2 = 250
    3. Complex: a + bj, complex(a, b)
'''
print(5 + 4)
print(4.3 - 2)
print(3 * 7)
print(3 * 7.0)
print(2 / 4)        # division, get 0.5
print(2 // 4)       # division, get 0
print(17 % 3)
print(2 ** 5)       # 2 ^ 5

# String
s = "Learn Python"
print(s[0])
print(s[-1])
print(s[6:])
print(s[::-1])      # reverse the string

print(s.replace('Python', 'Java'))

## searching using: find(), index(), rfind(), rindex()
print(s.find('6'))
print(s.find('n', 6))       # find 'n' starting from 6
print(s.find('java'))       # cannot find the string 'java' return -1

print(s.index('P'))
# print(s.index('p'))       # throw error if not find

print(s.upper())            # all caps
print(s.lower())            # all lowercase
print(s.swapcase())         # switch caps and non-caps
print(s.istitle())          # return whether all the first letter of a word is capatalized or not
print(s.islower())
# get rid of the space using: strip(), lstrip(), rstrip()

## formatting
s1 = '%s %s %s' % ('Hola', 'Amigo', 123)
print(s1)

s2 = '{} {}'.format(21, 'KG')
print(s2)

s2 = '{1}{0} {1}'.format(21, 'KG')
print(s2)

s3 = '{name} : {age}'.format(age = 21, name = 'KG')
print(s3)

l = ['2019', '10', '19', '23:23']
s5 = '-'.join(l)
print(s5)

s5 = s5.split('-')
print(s5)               # 2019-10-19-23:23
print(s5[-1][::-1])     # 32:32

# List
Weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
print(Weekday[0])       # Monday
print(Weekday[-1])      # Friday

print(Weekday.index('Tuesday'))

Weekday.append('Amigo')
print(Weekday)

Weekday.remove('Amigo')
print(Weekday)

# Tuple
letters = (('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5))
print(letters[0])
print(letters[0:3])
print()
# Set
a_set = {1, 2, 3, 4}
print(a_set)

a_set.add(5)
print(a_set)

a_set.discard(4)        # remove element 4
print(a_set)

jaja = a_set.__contains__(5)
print(jaja)

jaja = a_set.__contains__(6)
print(jaja)

# Dictionary
Logo_code = {
    'BIDU': 'Baidu',
    'Glge': 'Google',
    'SINA': 'Sina',
    'YOKU': 'Youku'
}

print(Logo_code)

print(Logo_code['SINA'])
print(Logo_code.keys())
print(Logo_code.values())
print(len(Logo_code))