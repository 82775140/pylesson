dict1 = {}
dict2 = dict1.fromkeys(range(32), "nice")
for each in dict2.keys():
    print(each)
for eachvalues in dict2.values():
    print(eachvalues)
for eachItem in dict2.items():
    print(eachItem)
print(dict2.get(32))
print(31 in dict2)
print(32 in dict2)
dict3 = dict2.copy()
print(dict3)