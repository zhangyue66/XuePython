#私有化属性 x _y __z

#类的内部  子类内部  模块其他位置  模块外部位置

class Animal:
    _x = 10
    def test(self):
        print(Animal._x)
        print(self._x)

class Dog(Animal):
    def test2(self):
        print(Dog._x)
        print(self._x)
    pass


# #testing code
#
a = Animal()
a.test()
# #
d = Dog()
d.test2()
#
print(Animal._x)
print(Dog._x)
print(a._x)
print(d._x)

__all__ = ["_a"]
_a = 666


# __z d的本质就是 name mangling __z  -> _Class__z
#private attribute