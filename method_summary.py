class Person:
    age = 0
    def shilifangfa(self):
        print(self)
        print(self.age)
        print(self.num)

    @classmethod
    def leifangfa(cls):
        print(cls)
        print(cls.age)
        #print(cls.number)  ->AttributeError: type object 'Person' has no attribute 'number'

    @staticmethod
    def jingtaifangfa():
        print(Person.age)

p = Person()
p.num = 10


p.leifangfa()
Person.leifangfa() # class method can not visit instance's attribute

Person.jingtaifangfa()

# p.shilifangfa()
# # 类属性
# print(Person.age)
# print(p.age)
# #实例属性
# print(p.num)
#print(Person.num)   -> AttributeError: type object 'Person' has no attribute 'num'