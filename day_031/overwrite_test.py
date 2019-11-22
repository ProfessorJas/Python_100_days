class supper:           # Define supper class
    data1 = 10
    data2 = 20

    def show1(self):
        print('Show1() in the parent class')

    def show2(self):
        print('Show2() in the parent lass')

class sub(supper):      # Define child class
    data1 = 100

    def show1(self):
        print('Show1() in the child class')

x = sub()
print(x.data1)      # 100, from child class
print(x.data2)      # 20, from parent class

x.show1()           # Show1() in the child class

x.show2()           # Show2() in the parent lass