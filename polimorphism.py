#--------------多态  ----------------



class Animal:
    def jiao(self):
        pass

class Dog(Animal):
    def jiao(self):
        print("wangwang")

class Cat(Animal):
    def jiao(self):
        print("miaomiao")

def test(obj):
    obj.jiao()
d = Dog()
c = Cat()
# c.jiao()
# d.jiao()
test(c)

# 什么是鸭子类型 duck typing -- 关注是行为和属性，并不关心int boolean还是其他类型