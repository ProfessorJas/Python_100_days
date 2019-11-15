seq = ('name', 'age', 'class')

dict = dict.fromkeys(seq)

print("New dict is: ", str(dict))

dict = dict.fromkeys(seq, 10)
print("New dict is: ", str(dict))

dict = dict.fromkeys(seq, ('zzy', 7, 'Two'))
print("New dict is: ", str(dict))