def bussness(x):
    if 0<x<=10:
        i = x*0.1
    elif 10<x<=20:
        j = x*0.075
        return j
    elif 20<x<=40:
        k = (x-20)*0.05
        return k
    elif 40<x<=60:
        a = (x-40)*0.03
        return a
    elif 60<x<=100:
        b = (x-60)*0.015
        return b
    elif x>100:
        i = (x-100)*0.01
money = int(input("请输入您的利润"))
bussness(money)
print(("利润为 %d w 时，应发放奖金数为 %d w 元")%(money,bussness(money)))