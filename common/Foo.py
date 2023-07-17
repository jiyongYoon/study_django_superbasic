class Foo:
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

    def setfirst(self, first):
        self.first = first

    def setsecond(self, second):
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def func1():
        print("function 1")

    def func2(self):
        print(id(self))
        print("function 2")


f = Foo()
# f.func1()
f.func2()

Foo.func1()
Foo.func2(f)

# f.setdata('첫번째', '두번째')
print(f.first)
print(f.second)


f2 = Foo(1, 3)
print(f2.first)
print(f2.second)
f2.setfirst(2)
print(f2.first)

