import random
class Turtle:
    def __init__(self):
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)
    def move(self):
        print("我的位置是%d,%d"%(self.x,self.y))
turtle = Turtle()
turtle.move()
