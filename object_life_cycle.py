#---------------------python的对象生命周期 和周期方法--------------------------
print("----------------- object life cycle -----------------")


class Person():
    # def __new__(cls, *args, **kwargs):
    #     print("create a object but interupted by me")
    def __init__(self):
        print("初始化方法")
        self.name = "yuezhang"
        self.wife = "yiyang"

    def __del__(self):
        print("对象释放被调用")

p = Person()
print(p)
print(p.wife)


#----对象生命周期的方法 实例--------------------

#创建一个实例 计数+1 释放 -1
personCnt = 0
class Person:
    def __init__(self):
        global personCnt
        print("cnt +1")
        personCnt += 1

    def __del__(self):
        global personCnt
        print("cnt -1")
        personCnt -= 1

p1 = Person()
p2 = Person()
print("cnt now is %d" %(personCnt))
del p1
print("cnt now is %d" %(personCnt))

#-------can you optimize print?--------

# i want to use static method to optimize


#----opt 1-----------


class Person:
    personCnt=0
    def __init__(self):
        print("cnt +1")
        Person.personCnt +=1

    def __del__(self):
        print("cnt -1")
        Person.personCnt -=1

    @classmethod
    def log(cls):
        print("now %d" %(Person.personCnt))

p3 = Person()
p4 = Person()
Person.log()
del p3
del p4
Person.log()
