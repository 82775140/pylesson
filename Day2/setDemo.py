num1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
num2 = []
for each in num1:
    if each not in num2:
        num2.append(each)
print(num2)
set1 = list(set(num1))
print(set1)
set2 = frozenset([1, 2, 3, 423, 555])
set3 = {789, 456, 222}
set3.add(2)
print(set3)