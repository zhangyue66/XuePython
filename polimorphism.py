#--------------多态  ----------------

#
#
# class Animal:
#     def jiao(self):
#         pass
#
# class Dog(Animal):
#     def jiao(self):
#         print("wangwang")
#
# class Cat(Animal):
#     def jiao(self):
#         print("miaomiao")
#
# def test(obj):
#     obj.jiao()
# d = Dog()
# c = Cat()
# # c.jiao()
# # d.jiao()
# test(c)

# 什么是鸭子类型 duck typing -- 关注是行为和属性，并不关心int boolean还是其他类型


#抽象类 抽象方法

import abc

class Animal(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def jiao(self):
        pass

    @abc.abstractclassmethod
    def test(self):
        pass

class Dog(Animal):
    def jiao(self):
        print("wangwang")

    def test(self):
        print("method test")

class Cat(Animal):
    def jiao(self):
        print("miaomiao")

def test(obj):
    obj.jiao()


#a = Animal()

# -> TypeError: Can't instantiate abstract class Animal with abstract methods jiao

d = Dog()
d.test()  #TypeError: Can't instantiate abstract class Dog with abstract methods test

#在Dog自己实现这个方法来消除这个错误