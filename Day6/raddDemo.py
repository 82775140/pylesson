class int(int):
    def __radd__(self, other):
        return int.__sub__(self,other)

a = int(1)
b = int(3)
print(1+b)