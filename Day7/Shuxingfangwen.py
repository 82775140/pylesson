class C:
    def __init__(self):
        self.x = "x_man"
c = C()
print(c.x)
getattr(c,"x")
s = getattr(c,"y","没有这个属性")
print(s)
class A:
    def __init__(self,size = 10):
        self.size =size
    def get_size(self):
        return self.size
    def set_size(self,value):
        self.size = value
    def del_size(self):
        del self.size
    x = property(get_size,set_size,del_size)
a = A()
print(a.x)
class B:
    def __init__(self):
        self.x = "x_man"
    def __getattribute__(self, item):
        print("getattribute")
        return super().__getattribute__(item)
    def __getattr__(self, item):
        print("getattr")
    def __setattr__(self, key, value):
        print("setattr")
        super().__setattr__(key,value)
    def __del__(self,name):
        print("delattr")
        super().__delattr__(name)
b = B()
print(b.x)
