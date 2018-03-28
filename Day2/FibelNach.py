def fibel(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return fibel(n-1)+fibel(n-2)


temp = int(input("请输入您的月数"))
result = fibel(temp)
print("%d月的兔子数为%d" % (temp, result))
