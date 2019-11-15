dict = {'Name': 'Mary', 'Age': 17}

print("Value: ", dict.values())

dict1 = {'One': '15', 'Two': '14', 'Three': '7'}

print(dict1.items())
for key,values in dict1.items():            # key and values must be str type
    print(key + ' is ' + values)

