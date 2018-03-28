class Rectangle:
    def __init__(self,length=0,width=0):
        self. length = length
        self.width = width
    def __setattr__(self, key, value):
        if key =="square":
            self.width = value
            self.length = value
        else:
            super().__setattr__(key,value)
    def getarea(self):
        return self.width*self.length
r = Rectangle()
r.square = 10
x = r.getarea()
print(x)