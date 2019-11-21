import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]

bisect.insort(scores, (300, 'Ruby'))

print(scores)

bisect.insort_right(scores, (700, 'Go'))

print(scores)

bisect.insort_left(scores, (000, 'C'))

print(scores)