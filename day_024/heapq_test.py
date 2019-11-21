from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

# heapify the data array
heapify(data)
print(data)

heappush(data, -5)
print(data)

arr = [heappop(data) for i in range(3)]

print(arr)