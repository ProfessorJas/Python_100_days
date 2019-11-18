class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        pass

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1

        return self.data[self.index]

if __name__ == "__main__":
    rev = Reverse("Amigo")
    
    while rev != None:
        print(next(rev))