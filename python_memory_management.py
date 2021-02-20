class Person:
    pass

p = Person()
print(p)
print(id(p))
print(hex(id(p)))

# 比较常用 不用改变的变量 不会创建对象 而是用缓存 字符，短小字符
# 比如说1,2,3,4

num1 = 1
num2 = 1
print(id(num1),id(num2))

#----------------引用计数器----------------------

import sys
class Person:
    pass

p1 = Person() #1
print(sys.getrefcount(p1)) # 2 主义：会大一 ，因为函数有传递

p2 = p1
print(sys.getrefcount(p1))# 3
del p2
print(sys.getrefcount(p1))#2
del p1  #如果计数器变为0，说明这个内存没有被引用，可以被当做垃圾处理
#print(sys.getrefcount(p1))  #NameError: name 'p1' is not defined . gabbage and got recycled


#----------------------------------------------------

#内存管理机制
#当一个对象 如果被引用 +1 删除一个引用-1 如果计数器是0 被释放

#例子 ： 两个对象互相引用 内存泄漏 永远无法删除

import objgraph

#objgraph.count() 垃圾回收器的个数
class Person:
    pass

class Dog:
    pass

p = Person()
d = Dog()

print(objgraph.count("Person"))
print(objgraph.count("Dog"))
p.pet = d
d.master=p

#删除p,d之后 对象是否释放？

del p
del d

print(objgraph.count("Person"))
print(objgraph.count("Dog"))

#1
#1   not zero anymore

print("python的内存管理机制就是 引用计数器 + 垃圾回收器")

print("经过引用计数器机制任然没有被释放的对象中，找到循环引用，干掉相关对象")


#------------------如何检测“循环引用”---------------------------------------

class Person:
    pass

p = Person()
l=[p]
t = (p)
# container object


# 分代回收 若一个对象检测十次都没有被干掉 那么就减少检测频率 因为他很长寿。
import gc
print(gc.get_threshold())   # (700, 10, 10)
gc.set_threshold(200,5,5)

#开启 关闭 判断垃圾回收机制
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()


#手动回收

class Person:
    pass

class Dog:
    pass

p = Person()
d = Dog()

p.pet = d
d.master = p
#手工产生循环引用

del p
del d

gc.collect() #manual collect garbage here

print(objgraph.count("Person"))
print(objgraph.count("Dog"))
#  两种垃圾回收机制 相辅相成


