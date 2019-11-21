import math
n = int(input("Enter a number which is greater than 3: "))

i = 2

while (i <= math.sqrt(n)):
    r = n % i

    if (r == 0):
        print(n, " is not an odd number")
        break
    else:
        i += 1
    
    print(n, " is an odd number.")