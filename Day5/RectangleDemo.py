class Rectangle:
    __length = int(input("请输入您的长"))
    __wide   = int(input("请输入您的宽"))
    def getsize(self):
        print(self.__length*self.__wide)



rectangle = Rectangle()
rectangle.getsize()