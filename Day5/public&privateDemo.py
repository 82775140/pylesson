class Person:
    __person_name = "sss"
    def get_person_name(self):
        return self.__person_name
        print("my name is %s"%self.__person_name)
Person1 = Person()
Person1.get_person_name()
a=Person1._Person__person_name
print(a)