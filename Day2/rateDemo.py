def rate(price, rates):
    fina_price =price*rates
    old_price = 50
    print("修改后变量的值为1", old_price)
    return fina_price


old_price = float(input("请输入原价"))
rates = float(input("请输入折扣率"))
new_price=float(rate(old_price, rates))
print("修改后变量的值为2", old_price)
print(new_price)