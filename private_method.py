# class Person:
#     __age = 18
#
#     def __run(self):
#         print("run")
#
#
# p = Person()
# print(Person.__dict__)  # {'__module__': '__main__', '_Person__age': 18, '_Person__run': <function Person.__run at 0x035353D0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
#
# print(Person._Person__run(p))


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):#格式化方法
#         return "this Person is having attributes: %s %s " %(self.name,self.age)
#
#     def __repr__(self):#展示内存 类型等 面向开发者
#         return ""
#
#
# p1 = Person("yz",32)
# p2 = Person("yy",28)
# print(p1,p2)

# import datetime
#
# t = datetime.datetime.now()
# print(t)
# print(repr(t))
#
# tmp = repr(t)
# time = tmp
# print(eval(time))

# ------__call__ method ---------

# class Person:
#     def __call__(self, *args, **kwargs):
#         print("XXX call now")
#         print(args,kwargs)
# p = Person()
#
# p(123,456,name="sz")

#----------
#functools.partial

def create_pen(p_type,p_color):
    print("createing a pen which is %s type and %s color!" %(p_type,p_color))

create_pen("yz pen","red")
create_pen("yz pen","yellow")
create_pen("yz pen","black")

import functools
c_partial_pen = functools.partial(create_pen,p_type = "yz pen")

c_partial_pen(p_color ="white")


print("# -------------use _call_ to do it ------")

class PenFactory:
    def __init__(self,p_type):
        self.p_type = p_type


    def __call__(self, p_color):
        print("createing a pen which is %s type and %s color!" %(self.p_type,p_color))


penOne = PenFactory("yz pen")
penOne("red")
penOne("white")
penOne("black")


# class Test:
#     def __call__(self, *args, **kwargs):
#         print("yz")
#
# t = Test()
# t()


#-----------------索引操作------------------
print("-----------------------------index method-------------------")

class Person:
    def __init__(self):
        self.cache = {}
    def __setitem__(self, key, value):
        #print("setitem",key,value)
        self.cache[key] = value

    def __getitem__(self, item):
        print("getitem",item)
        return self.cache[item]

    def __delitem__(self, key):
        print("delitem",key)
        del self.cache[key]

p = Person()
p["name"] = "yuezhang"
print(p["name"])

del p["name"]

print(p.cache)



# -----------------------切片操作-----------------------------
print("------------------------now showing slice method-------------------- ")

class Person:
    def __setitem__(self, key, value):
        if isinstance(key,slice):
            print("slice")

p = Person()


# -----------------------比较操作----------------------------
print("------------------------now showing COMPARE method-------------------- ")

class Person:
    def __init__(self,age,height):
        self.age = age
        self.height = height

    # >, <, =, !=, >=, <=
    def __eq__(self, other):
        print(other)
        return self.age == other.age and self.height == other.height

    def __ne__(self, other):
        return "xxx not equal"

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

p1 = Person(18,170)
p2 = Person(18,178)

print(p1==p2)
print(p1 != p2)
print(p1 <= p2)
#print(a1 > a2) #TypeError: '>' not supported between instances of 'A' and 'A'

# ----------------上下文环境的布尔值---------------------------
print("-------------------now showing Boolean---------------------------------")

class Person:
    def __init__(self):
        self.age = 10

    def __bool__(self):
        return self.age >= 18


p = Person()
if p:
    print("XXX")

p2 = Person()
p2.age = 20
if p2:
    print("adult now!")


#------------遍历操作-------------
print("---------now showing iterator")
# class Person:
#     pass
#
# p = Person()
#
# for i in p:
#     print(i)  #_____TypeError: 'Person' object is not iterable

class Person:
    def __init__(self):
        self.result = 1

    def __getitem__(self, item):
        print("getitem")
        self.result += 1
        if self.result >= 6:
            raise StopIteration("stop the iteration")
        return self.result

    def __iter__(self):
        print("iter")

        return iter([1,2,3,4,5])


p = Person()
for i in p:
    print(i)


#-----------------------恢复迭代器初始值---------------------
print("------- iter and next ------")
class Person:

    def __init__(self):
        self.age = 1

    def __iter__(self):
        self.age = 1
        return self

    def __next__(self):
        self.age += 1
        if self.age >= 6:
            raise StopIteration("iteration stopped")

        return self.age

p = Person()

from collections import abc
print(isinstance(p,abc.Iterator))

for k in p:
    print(k)
print("---iter second time")
for k in p:
    print(k)

print("iterable %s" %(isinstance(p,abc.Iterable))) # Iterable is checking whether class is hving __iter__ method

#--------------------iter函数的使用---------------------------

print("------------now showing iter() how to use")

class Person:

    def __init__(self):
        self.age = 1

    def __iter__(self):
        self.age = 1
        return self

    def __next__(self):
        self.age += 1
        if self.age >= 6:
            raise StopIteration("iteration stopped")

        return self.age

    def __call__(self, *args, **kwargs):
        self.age += 1
        if self.age >= 6:
            raise StopIteration("iteration stopped")

        return self.age
        #return self.__next__()

p = Person()

#pt = iter(p,4) #TypeError: iter(v, w): v must be callable

#pt = iter(p.__next__,4) ->right

pt = iter(p,4) # add __call__ method,can comment out __next__

# i tried below method it is also working
# def __call__(self, *args, **kwargs):
#     # self.age += 1
#     # if self.age >= 6:
#     #     raise StopIteration("iteration stopped")
#     #
#     # return self.age
#     return self.__next__()


for i in pt:
    print(i)

#---------------------------描述其 定义方式1-----------------------------
print("------------now showing descriptor------------------")

class Person:
    def __init__(self):
        self.__age = range

    def get_age(self):
        return self.__age

    def set_age(self,value):
        if value < 0:
            value = 0
        self.__age = value

    def del_age(self):
        del self.__age

    age = property(set_age,get_age,del_age)

p = Person()
p.set_age(-10)
print(p.get_age())
p.del_age()
#print(p.get_age())
#help(Person)
# if we want to CRUD the attribute by similar way p.age = 10 , what should we do ?  check line 317 property(mthod1,method2,method3)

#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  age


#---------------------------描述其 定义方式2-----------------------------  重要
print("when there is multi classes , use property decorator will become very long. each class needs to use 3 method as set,get,del. use OOP to integrate these 3 ways ")

class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, key):
        print("delete")

class Person:
    age = Age()
    #利用__getattribute__实现描述器get方法
    def __getattribute__(self, item):
        print("方法拦截")

p = Person()
p.age = 10
print(p.age)
del p.age

#print(Person.age) #descriptor only work in new style class not in classic style class


#优先级
print("---------------描述器和实例属性同名时 优先级是？-------------")

#资料描述器 get set vs 非资料描述器 only get
# 资料》实例》非资料
class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, key):
        print("delete")

class Person:
    age = Age()
    def __init__(self):
        self.age = 10  #__dict__ =={}


# 描述器值得储存问题
print("------------------------------descriptor's value how to store?")

class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set",self,instance,value)

    def __delete__(self, key):
        print("delete")

class Person:
    age = Age()

p = Person()
p.age = 10

p2 = Person()
p2.age = 11

# set <__main__.Age object at 0x03FB1790> <__main__.Person object at 0x03FB1718> 10
# set <__main__.Age object at 0x03FB1790> <__main__.Person object at 0x03FB17A8> 11

# dont bind on self.value . bind it to instance.value



#--------------------------使用类 实现装饰器-----------------------------------------
print("------------now use Class to make decorator")

#normal way

def check(func):
    def wrapper():
        print("log in")
        func()
    return wrapper

@check
def say():
    print("say")


say()

#class method

class check:
    def __init__(self,func):
        self.f = func

    def __call__(self, *args, **kwargs):
        print("log2")
        self.f()

def say1():
    print("say1")

say1 = check(say1)

say1()



