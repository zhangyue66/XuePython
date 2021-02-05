#私有化属性 x _y __z

#类的内部  子类内部  模块其他位置  模块外部位置

class Animal:
    x = 10
    def test(self):
        print(Animal.x)
        print(self.x)

class Dog(Animal):
    def test2(self):
        print(Dog.x)
        print(self.x)
    pass


# #testing code
#
# a = Animal()
# # a.test()
# #
# d = Dog()
# # d.test2()
#
# print(Animal.x)
# print(Dog.x)
# print(a.x)
# print(d.x)

a = 666