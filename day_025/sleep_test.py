import time

for i in range(3):
    print('one')
    print(time.time())
    time.sleep(2)

    print('two')
    print(time.time())
    time.sleep(2)

print('Finish')