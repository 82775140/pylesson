import random
direction_x = [0, 10]
direction_y = [0, 10]
class Little_Turtle:
    move_ability = random.randint(1, 2)
    max_health = 100
    @staticmethod
    def __init__(self):
        self.health = 100
        self.move_direction_x=random.randint(direction_x,direction_y)
    def move(self):
        new
    @staticmethod
    def health_point(self):
        max_health = 100
        if max_health>100:
            return 100
class Fish:
    move_direction_x = random.randint(1,11)
    move_direction_y = random.randint(1,11)
    def move(self):
        move_ability = 1
        x = random.randint(0,11)
        y = random.randint(0,11)
        if x<0 or x>10 or y<0 or y>10:
            print("小鱼撞到边界啦")
turtle = Little_Turtle()
turtle.move(turtle)
for i in range (10):
    fish = Fish()
if turtle.move(turtle):
    turtle.max_health -= 1
while turtle.move_direction_x  == fish.move_direction and fish.move_direction_y == fish.move_direction_y:
    print("小鱼被乌龟吃掉啦！")
    fish -=1
    print("还剩%d只鱼"%fish)
    turtle.max_health += 20
if turtle.max_health == 0:
    print("Game Over")