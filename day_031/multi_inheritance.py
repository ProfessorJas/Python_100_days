class P1(object):           # Base class 1
    def f(self):
        print('Calling f in P1')

class P2(object):           # Base class 2
    def f(self):
        print('Calling f in P2')

    def g(self):
        print('Calling g in P2')

class C1(P1, P2):           # Level 1 subclass from P1 and P2
    def h(self):
        print('Calling h in C1')

class C2(P1, P2):           # Level 1 subclass from P1 and P2
    def g(self):
        print('Calling g in C2')

class GC(C1, C2):           # Level 2 subclass from C1 and C2
    pass

gc = GC()

gc.f()
# Calling f in P1

gc.g()
# Calling g in C2

gc.h()
# Calling h in C1