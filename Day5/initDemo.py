class Ball:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print("我是%s,谁踢我"% self.name)
b = Ball("土豆")
b.kick()

class Person:
    name = "小甲鱼"
p = Person()
a = p.name
print(a)