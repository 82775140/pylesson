def tower(n, x, y, z):
    if(n==1):
        print(x, "-->", z)
    else:
        tower(n-1, x, z, y)
        """将前n-1个盘子移动到y上"""
        print(x, "-->",z)
        """将最下面的盘子移动到z上"""
        tower(n-1, y, x, z)


temp = int(input("请输入汉诺塔层数"))
result=tower(temp,'x', 'y', 'z')
