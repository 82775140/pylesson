list1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if list1[j]<list1[j+1]:
            temp = list1[j+1]
            list1[j+1] = list1[j]
            list1[j] = temp
    print(list1)