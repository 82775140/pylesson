class int(int):
    def __itruediv__(self, other):
        return int.__add__(self,other)
i = int(20)
j = int(6)
print(i/j)