class supper:               # Define a parent class
    def __init__(self, a):
        self.supper_data = a

class sub(supper):          # sub class is the subclass of the class super
    def __init__(self, a, b):           # Constrcutor of the child class
        self.sub_data = a
        super(sub, self).__init__(b)    # Calling the constructor of parent class

x = sub(10, 20)

print('Supper Data:', x.supper_data)
print('Sub Data:', x.sub_data)