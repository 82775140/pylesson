import pickle
import os
mylist = [3.14159, "xxi", 5689]
pickle_file = open("mylist.pkl", "wb")
pickle.dump(mylist, pickle_file)
pickle_file.close()
print(os.getcwd())

pickle_file = open("mylist.pkl", "rb")
mylist2 = pickle.load(pickle_file)
print(mylist2)