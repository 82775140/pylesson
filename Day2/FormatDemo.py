print("My name is %(name)s,I am %(age)d years old" % {'name':'sss', 'age':21})
print("%+7x" % 10)
print(("%-5d" % 5))
print('{:0>8}'.format('70'))
print('{:.2f}'.format(3.1415926))
print('{:,}'.format(1234567890))
print('%+d' % 7)
print('%#x' % 17)
a = list()
print(a)    #生成空列表

b = "I love you"
b = list(b)
print(b)

c = (1, 1, 2, 3, 5, 8)
c = list(c)
print(c)

d = "I love you"
d = tuple(d)
print(d)

print(len(d))

b.append('next')
print(b)
max_num = max(b)
print(max_num)

tuple2 = (3.1, 2.2,4.5)
sum_tuple2 = sum(tuple2, 1)
print(sum_tuple2)

print(tuple(reversed(sorted(tuple2))))

a = (1,2,3,4,5)
b = (2,3,4,5)
print(list(zip(a,b)))
