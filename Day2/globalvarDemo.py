def my_fun():
    global count
    count = 10
    print(count)


my_fun()
print(count)


def fun_1():
    print("fun_1正在被调用")
    def fun_2():
        print("fun_2正在被调用")
    fun_2()


fun_1()


def fun_x(x):
    def fun_y(y):
        return x*y
    return fun_y


i = fun_x(8)(5)
print(i)


def funo():
    x = 5
    def funs():
        nonlocal x
        x *= x
        return x
    return funs()


print(funo())
