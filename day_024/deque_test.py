from collections import deque

d = deque(["test1", "test2", "test3"])

d.append("task4")

print(d)

print(d.popleft())

print(d)

print(d.append("test amigo"))

print(d)

print(d.appendleft("hola test"))

print(d)