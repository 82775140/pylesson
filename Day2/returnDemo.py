def returnd(x):
    if(x==1):
        return 1
    else:
        return x*returnd(x-1)


temp = int(input("请输入您的数字"))
result = returnd(temp)
print("您输入的数字为%d,阶乘为%d" % (temp, result))
