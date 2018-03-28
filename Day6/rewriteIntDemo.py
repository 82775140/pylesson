class int(int):
    def __add__(self, other):
        return int.__sub__(self,other)
i = int("2")
j = int("5")
print(i+j)