class test:
    def __init__(self, value):
        self.data = value
        print("Finish Constructing!")

    def __del__(self):
        del self.data

        print("Finish Destructing!")

x = test(100)
print(x.data)

del x

# print(x.data)     # error, x is destroyed