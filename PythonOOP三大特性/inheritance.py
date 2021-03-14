class Animal:
    pass
#单继承
class Dog(Animal):
    pass

#多继承

class XXX:
    pass

class Cat(Animal,XXX):
    pass

print(Cat.__bases__)  #(<class '__main__.Animal'>, <class '__main__.XXX'>)
print(Animal.__bases__)  #(<class 'object'>,)


print(int.__bases__)
print(float.__bases__)
print(bool.__bases__)

# (<class 'object'>,)
# (<class 'object'>,)
# (<class 'int'>,)

d = Dog()
print(d.__class__)
print(object.__class__)



#----------------继承 资源---------------------


class Animal:
    #属性方法
    #设置不同的权限和属性和方法，继承中看看
    #子类可否访问

    a=1
    _b = 2
    __c = 3

    def t1(self):
        print("t1")

    def _t2(self):
        print("t2")

    def __t3(self):
        print("t3")

    def __init__(self):
        print("init of Animal")

class Person(Animal):
    def test(self):
        print(self.a)
        print(self._b)
        #print(self.__c)   ->AttributeError: 'Person' object has no attribute '_Person__c'

        self.t1()
        self._t2()
        #self.__t3()  ->AttributeError: 'Person' object has no attribute '_Person__t3'
        self.__init__()

p = Person()
p.test()

Animal.a =666
p.test()


# 三种继承形态 单继承 无重叠多继承 有重叠多继承  （资源的使用）