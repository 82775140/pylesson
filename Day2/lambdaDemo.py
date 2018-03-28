def x(x):
    return 2*x+1


print(x(5))


g = lambda x: x*2+5
print(g(3))


def x(i, j):
    return i*j+1


print(x(3, 5))


resoure = lambda x,y: x*y+1
print(resoure(6, 7))


print(list(filter(None, [1, 0, True, False])))


def odds (x):
    if x % 2 != 0:
        return x


print(list(filter(odds, range(10))))

print(list(map(lambda a: a*3+2, range(10))))