class Person:
    def __init__(self):
        self.__age = 18

    #主要作用 是可以使用属性的方式 来使用这个方法
    @property
    def getAge(self):
        return self.__age

p1 =Person()
print(p1.getAge)

p1.getAge = 66

#
# p1.getAge = 66
# AttributeError: can't set attribut