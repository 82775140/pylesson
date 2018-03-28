try:
    with open("text.txt","r") as  f:
        for each in f:
            print(each)
except IOError as reason:
    print("出错"+str(reason))


