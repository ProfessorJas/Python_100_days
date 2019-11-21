import time

def calculateTime():
    item = 1
    
    for i in range(1, 100000):
        item = item + i

    return item

startTime = time.time()
result = calculateTime()
endTime = time.time()

print("Cal result: ", str(result))

print("Cal timing: ", str(endTime - startTime))