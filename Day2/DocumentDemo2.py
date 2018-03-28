file = open("D:\\迅雷下载\MusouOrochiZ.Green.Edition-ALI213\MusouOrochiZ.Green.Edition-ALI213\MusouOrochiZ\Readme.txt")
print(file.tell())
for each in file:
    print(each)
file.close()
file1 = open("D:\\test.txt", 'w')
file1.write("你好")
file1.close()
with open("D:\\test.txt") as f:
    print(f.read())