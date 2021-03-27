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

Animal.a = 666
p.test()


# 三种继承形态 单继承 无重叠多继承 有重叠多继承  （资源的使用）

# 继承标准方案的演化 python3.X之后 MRO DFS BFS

# 继承资源的访问顺序

#单继承
class C:
    age = "c"

class B(C):
    #age = "b"
    pass

class A(B):
    #age = "a"
    pass

print(A.age)

#无重叠多继承

#A -B -C -D- E


#有重叠多继承 如果再用dfs 会产生顺序错误 违背了重写可用的原则（python2.X）

# import inspect
# print(inspect.getmro(A))


#python 2.2 MRO 原则 1.经典类 dfs 2.新式类 dfs改进 并不是bfs、


# 此方法无法侦测有问题的继承 所以新式类引入C3算法

#--------python 2.3 - 2.7的C3 linearization algorithm

class D:
    pass

class B(D):
    pass

class C(D):
    pass

class A(B,C):
    pass

import inspect
print(inspect.getmro(A))
print("yz")


#------python3.X之后没有经典类 只有C3 算法


#------继承  资源的覆盖 -----


class D:
    pass

class C(D):

    age = "c"
    pass

class B(D):
    age = "b"
    def test(self):
        print(self)

    @classmethod
    def test2(cls):
        print(cls)
    pass

class A(B,C):
    pass

print(A.mro())
print(A.__mro__)
print(A.age)  #优先调用优先级高的类里面  属性的覆盖 方法的重写

A.test2() #<class '__main__.A'>

a = A()
a.test() #<__main__.A object at 0x0314F5C8>


# 资源累加的场景  子类比父类多一些自己特有的资源


class B:
    a = 1

    def __init__(self):
        self.b = 2

    def t1(self):
        print("t1")

    @classmethod
    def t2(cls):
        print("t2")

    @staticmethod
    def t3():
        print("t3")

class A(B):
    c= 3
    pass

a_obj = A()

print(A.a)
print(a_obj.b)
A.t2()
print(B.t3() == A.t3())
print(A.c)

a_obj.d = "xxx"
print(a_obj.d)



#------资源累加的弊端



class D:
    def __init__(self):
        print("d")

class B(D):
    def __init__(self):
        print("b")

class C(D):
    def __init__(self):
        print("c")

class A(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("a")


B()
C()
print("bad thing ")
A()  #重复调用


# 所以引用 super调用高优先类的方法 super只能在新式类中使用

class D:
    def __init__(self):
        print("d")

class B(D):
    def __init__(self):
        super().__init__()
        print("b")

class C(D):
    def __init__(self):
        super().__init__()
        print("c")

class A(B,C):
    def __init__(self):
        # B.__init__(self)
        # C.__init__(self)
        super().__init__()
        print("a")

print("enhance with super()")
D()
B()
C()
print("bad thing ")
A()  #没有重复使用