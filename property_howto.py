# # class Person(object):
# # #     def __init__(self):
# # #         self.__age = 18
# # #
# # #
# # #     def get_age(self):
# # #         return self.__age
# # #
# # #
# # #     def set_age(self,value):
# # #         self.__age = value
# # #
# # #     age = property(get_age,set_age)
# # #
# # #
# # #
# # # # First usage in new style class
# # #
# # # p = Person()
# # #
# # # print(p.age)
# # #
# # # p.age = 99
# # #
# # # print(p.age)
#
# print(p.__dict__)
#
# # 18
# # 99
# # {'_Person__age': 99}



# Second Usage in new style class


class Person(object):
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        print("---- get")
        return self.__age

    @age.setter
    def age(self,value):
        print("---- set")
        self.__age = value


p = Person()
print(p.age)

p.age = 10
print(p.age)