# 计算器 实现一些基本操作  加减乘除 打印操作结果

# Code 3

# class Caculator:
#     __result = 0
#
#     @classmethod
#     def first_value(cls,v):
#         cls.__result = v
#
#     @classmethod
#     def jia(cls,n):
#         cls.__result += n
#
#     @classmethod
#     def jian(cls,n):
#         cls.__result -=n
#
#     @classmethod
#     def cheng(cls,n):
#         cls.__result *= n
#     @classmethod
#     def show(cls):
#         print("the result is %d" %(cls.__result))
#
#
# Caculator.first_value(2)
# Caculator.jia(6)
# Caculator.jian(4)
# Caculator.cheng(5)
# Caculator.show()

# Code 4
# what issue will Code 3 has ?
# 类只有一个 无法支持同时多次处理、操作 ， 同时只允许一个程序进行读写
# 想法 ： 改成一个对象 属性 这样就可以创建多个对象-实例

# class Caculator:
#
#     def __init__(self,num):
#         self.__result = num
#
#
#     def jia(self,n):
#         self.__result += n
#
#
#     def jian(self,n):
#         self.__result -=n
#
#
#     def cheng(self,n):
#         self.__result *= n
#
#     def show(self):
#         print("the result is %d" %(self.__result))
#
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()


# Code 5 针对code4 增加容错处理

# class Caculator:
#
#     def __init__(self,num):
#         # if not isinstance(num,int):
#         #         #     raise TypeError("this is not an INT type")
#         self.check_num(num)
#         self.__result = num
#
#
#     def jia(self,n):
#         self.check_num(n)
#         self.__result += n
#
#
#     def jian(self,n):
#         self.check_num(n)
#         self.__result -=n
#
#
#     def cheng(self,n):
#         self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print("the result is %d" %(self.__result))
#
#     def check_num(self,num):
#         if not isinstance(num,int):
#             raise TypeError("this is not an INT type")
#
#
# c1 = Caculator(3)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()


# Code 6  code5破坏了代码 目标 不破坏 jia jian cheng 等实例方法
# 用 Decorator！

# class Caculator:
#
#     def check_num_zsq(func):
#         def wrapper(self,num):
#             if not isinstance(num,int):
#                 raise TypeError("this is not an INT type")
#             return func(self,num)
#
#         return wrapper
#
#     @check_num_zsq
#     def __init__(self,num):
#         # if not isinstance(num,int):
#         #         #     raise TypeError("this is not an INT type")
#         # self.check_num(num)
#         self.__result = num
#
#     @check_num_zsq
#     def jia(self,n):
#         # self.check_num(n)
#         self.__result += n
#
#     @check_num_zsq
#     def jian(self,n):
#         # self.check_num(n)
#         self.__result -=n
#
#     @check_num_zsq
#     def cheng(self,n):
#         # self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print("the result is %d" %(self.__result))
#
#     # def check_num(self,num):
#     #     if not isinstance(num,int):
#     #         raise TypeError("this is not an INT type")
#
#
# c1 = Caculator(2)
# c1.jia("YZ")
# c1.jian(4)
# c1.cheng(5)
# c1.show()


# Code 7 any else improvement?
# class Caculator:
#
#
#     def __check_num_zsq(func):
#         def wrapper(self,num):
#             if not isinstance(num,int):
#                 raise TypeError("this is not an INT type")
#             return func(self,num)
#
#         return wrapper
#
#     @__check_num_zsq
#     def __init__(self,num):
#         # if not isinstance(num,int):
#         #         #     raise TypeError("this is not an INT type")
#         # self.check_num(num)
#         self.__result = num
#
#     @__check_num_zsq
#     def jia(self,n):
#         # self.check_num(n)
#         self.__result += n
#
#     @__check_num_zsq
#     def jian(self,n):
#         # self.check_num(n)
#         self.__result -=n
#
#     @__check_num_zsq
#     def cheng(self,n):
#         # self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print("the result is %d" %(self.__result))
#
#     # def check_num(self,num):
#     #     if not isinstance(num,int):
#     #         raise TypeError("this is not an INT type")
#
#
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()

def test_zsq(num):
    return num
#Caculator.check_num_zsq(test_zsq)
#为了避免外接调用zsq 可以将其私有化 private

# Code 8 新需求来啦 播报每个操作的值
#每次操作都print出来值

# 装饰器的嵌套 装饰器的运行顺序

#
# class Caculator:
#
#     def __say(self,word):
#         print("saying %d" %word)
#
#     def __say_zsq(func):
#         def wrapper(self,num):
#             print("saying %d" %num)
#             return func(self,num)
#         return wrapper
#
#     def __check_num_zsq(func):
#         def wrapper(self,num):
#             if not isinstance(num,int):
#                 raise TypeError("this is not an INT type")
#             return func(self,num)
#
#         return wrapper
#
#     @__check_num_zsq
#     @__say_zsq
#     def __init__(self,num):
#         # if not isinstance(num,int):
#         #         #     raise TypeError("this is not an INT type")
#         # self.check_num(num)
#         #self.__say(num)
#         self.__result = num
#
#     @__check_num_zsq
#     @__say_zsq
#     def jia(self,n):
#         # self.check_num(n)
#         self.__result += n
#
#     @__check_num_zsq
#     @__say_zsq
#     def jian(self,n):
#         # self.check_num(n)
#         self.__result -=n
#
#     @__check_num_zsq
#     @__say_zsq
#     def cheng(self,n):
#         # self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print("the result is %d" %(self.__result))
#
#     # def check_num(self,num):
#     #     if not isinstance(num,int):
#     #         raise TypeError("this is not an INT type")
#
#
# c1 = Caculator(1)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()


# 如何使得装饰器返回不同的内容
# 定义一个方法 方法可以传入参数 然后返回一个装饰器  -》def create_say_zsq(operation=""):
#
#
# class Caculator:
#
#     def __say(self,word):
#         print("saying %d" %word)
#
#
#
#     def __check_num_zsq(func):
#         def wrapper(self,num):
#             if not isinstance(num,int):
#                 raise TypeError("this is not an INT type")
#             return func(self,num)
#
#         return wrapper
#
#     def create_say_zsq(operation=""):
#         def __say_zsq(func):
#             def wrapper(self,num):
#                 print(operation +" saying %d" %num)
#                 return func(self,num)
#             return wrapper
#         return __say_zsq
#
#     @__check_num_zsq
#     @create_say_zsq("Ini")
#     def __init__(self,num):
#         # if not isinstance(num,int):
#         #         #     raise TypeError("this is not an INT type")
#         # self.check_num(num)
#         #self.__say(num)
#         self.__result = num
#
#     @__check_num_zsq
#     @create_say_zsq("Add")
#     def jia(self,n):
#         # self.check_num(n)
#         self.__result += n
#
#     @__check_num_zsq
#     @create_say_zsq("Deduct")
#     def jian(self,n):
#         # self.check_num(n)
#         self.__result -=n
#
#     @__check_num_zsq
#     @create_say_zsq("Times")
#     def cheng(self,n):
#         # self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print("the result is %d" %(self.__result))
#
#     # def check_num(self,num):
#     #     if not isinstance(num,int):
#     #         raise TypeError("this is not an INT type")
#
#
#     #用描述器
#     @property
#     def result(self):
#         return self.__result
#
# c1 = Caculator(1)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()
# print(c1.result)


# 现在我想用装饰器装饰 show 方法 因为 show只传入一个参数 ， 而不是传入self和num两个参数， 我能怎么修改呢？

# 我想将私有属性__result传给一个未知的函数或者变量 我可以在class内部设置一个方法 这个方法返回————result 更好的就是用描述器 set attribute的方法


#继续优化

class Caculator:

    def __say(self,word):
        print("saying %d" %word)



    def __check_num_zsq(func):
        def wrapper(self,num):
            if not isinstance(num,int):
                raise TypeError("this is not an INT type")
            return func(self,num)

        return wrapper

    def create_say_zsq(operation=""):
        def __say_zsq(func):
            def wrapper(self,num):
                print(operation +" saying %d" %num)
                return func(self,num)
            return wrapper
        return __say_zsq

    @__check_num_zsq
    @create_say_zsq("Ini")
    def __init__(self,num):
        # if not isinstance(num,int):
        #         #     raise TypeError("this is not an INT type")
        # self.check_num(num)
        #self.__say(num)
        self.__result = num


    @__check_num_zsq
    @create_say_zsq("Add")
    def jia(self,n):
        # self.check_num(n)
        self.__result += n
        return self

    @__check_num_zsq
    @create_say_zsq("Deduct")
    def jian(self,n):
        # self.check_num(n)
        self.__result -=n
        return self

    @__check_num_zsq
    @create_say_zsq("Times")
    def cheng(self,n):
        # self.check_num(n)
        self.__result *= n
        return self

    def show(self):
        print("the result is %d" %(self.__result))
        return self

    # def check_num(self,num):
    #     if not isinstance(num,int):
    #         raise TypeError("this is not an INT type")

    def clear(self):
        self.__result = 0
        return self
    #用描述器
    @property
    def result(self):
        return self.__result

c1 = Caculator(1)
#c1.jia(6).jian(4).cheng(5).show()   #链式编程 此时我引入一个方法clear 在一次运算之后重置__result 这样就可以利用一个实例 实现两次运算
c1.jia(6).jian(4).cheng(5).show().clear().jia(555).cheng(56).jian(999).show()
print(c1.result)