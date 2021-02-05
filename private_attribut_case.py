class Person():
    # 主要作用，创建好一个实例之后，初始化这些属性给这个实例
    def __init__(self,age):
        self.__age = age

    def setAge(self,value):
        if isinstance(value,int) and 0<value<200:

            self.__age = value
        else:
            print("input error")

    def getAge(self):
        print(self.__age)

p1 = Person(18)
#print(p1.age)
p1.getAge()
p1.setAge(21)
p1.getAge()

# p2 = Person(67)
# print(p2.age)