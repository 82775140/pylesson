class Ball:
    def set_name(self,name):
        self.name=name
    def kick(self):
        print("我叫%s,谁踢我"%self.name)
A = Ball()
A.set_name("球A")
B = Ball()
B.set_name("球B")
C = Ball()
C.set_name("土豆")
C.kick()