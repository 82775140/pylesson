dict1 = {1: "one", 2: "two", 3: "three"}
dict2 = dict1.setdefault(4, "four")
dict3 = {5: "five", 6: "six"}
dict4 = dict1.update(dict3)
print(dict1)
