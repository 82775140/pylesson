class Parent:
    pass
class Child(Parent):
    pass
a=issubclass(Child,Parent)
print(a)
b = Child()
c = isinstance(b,Child)
print(c)
class Nice:
    def __init__(self):
        self.x = "你好"
n = Nice()
d = hasattr(n,"x")
print(d)