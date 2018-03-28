class Demo:
    def __init__(self,size = 10):
        self.size = size
    def getsize(self):
        return self.size
    def set_size(self,value):
        self.size = value
    def del_size(self):
        del self.size
    x = property(getsize,set_size,del_size)
d = Demo()
print(d.x)
d.x = 20
print(d.x)