import random
times = 3
guess = 0
print("猜猜我想的数字是哪个")
while times > 0 and random.randint(1,10)!=guess:
    temp = input("请输入数字1-10")
    times -= 1
    while temp.isdigit():
        num = int(temp)
        if num == random.randint(1,10):
                print("猜对啦！")
                print("Game Over")
        else:
            if  num > random.randint(1,10):
                print("猜大啦")
            else:
                if num < random.randint(1,10):
                    print("猜小啦")
    else:
        print("类型有误")