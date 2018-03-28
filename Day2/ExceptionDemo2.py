try:
    sum = 1+'1'
    file = input("请输入您要打开的文件名")
    f = open(file)
    for each in f:
        print(each)
except FileNotFoundError as reason:
    print("文件未找到，错误的原因是"+str(reason))
except TypeError as reason:
    print("类型出错啦，错误的原因是" + str(reason))
finally:
    print("感谢使用")