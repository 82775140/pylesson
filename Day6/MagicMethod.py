class New_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
i = New_int(2)
j = New_int(3)
print(i+j)
