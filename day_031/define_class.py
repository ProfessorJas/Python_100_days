class class1:
    data = 100

    def setPdata(self, value):
        self.pdata = value
        print('Finish setting')

    def showPdata(self):
        print('self.pdata: ', self.pdata)

    print('Finish')

x = class1()
x.setPdata('amigo')
x.showPdata()
print('-' * 7)

x.setPdata(123)
x.showPdata()