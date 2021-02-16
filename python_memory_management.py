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
