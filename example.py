# class Dog:
#     def __init__(self,name,age=1):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "name is {},age {} dog ".format(self.name,self.age)
#
#     def eat(self):
#         print("%s is eating" % self)
#
#     def play(self):
#         print("%s is playing" % self)
#
#     def sleep(self):
#         print("%s is sleeping" % self)
#
#     def watch(self):
#         print("%s is watching" % self)
#
#
# class Cat:
#     def __init__(self,name,age=1):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "name is {},age {} cat ".format(self.name,self.age)
#
#     def eat(self):
#         print("%s is eating" % self)
#
#     def play(self):
#         print("%s is playing" % self)
#
#     def sleep(self):
#         print("%s is sleeping" % self)
#
#     def catch(self):
#         print("%s is catching mouse" % self)
#
#
# class Person:
#     def __init__(self,name,pets,age=1):
#         self.name = name
#         self.age = age
#         self.pets = pets
#
#     def __str__(self):
#         return "name is {},age {} person ".format(self.name,self.age)
#
#     def eat(self):
#         print("%s is eating" % self)
#
#     def play(self):
#         print("%s is playing" % self)
#
#     def sleep(self):
#         print("%s is sleeping" % self)
#
#     def watch(self):
#         print("%s is watching" % self)
#
#     def yangPets(self):
#         for pet in self.pets:
#             pet.eat()
#             pet.play()
#             pet.sleep()
#
#     def make_pets_work(self):
#         for pet in self.pets:
#             #pet.watch() #小猫没有watch方法 怎么处理 第一种方案 用isinstance()判定实例和类别
#             if isinstance(pet,Dog):
#                 pet.watch()
#             else:
#                 pet.catch()
#
#
# d = Dog("blacky",18)
# print(d.__dict__)  # {'name': 'blacky', 'age': 1} {'name': 'blacky', 'age': 18}
# d.eat()
# d.play()
# d.watch()
#
#
# c = Cat("Mimi",20)
# c.catch()
#
# p = Person("yue",[d,c],32)
# p.yangPets()
# p.make_pets_work()

#-------------- Code 3--------------------------------------
class Animal:
    def __init__(self,name,age=1):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating" % self)

    def play(self):
        print("%s is playing" % self)

    def sleep(self):
        print("%s is sleeping" % self)

class Dog(Animal):

    def __str__(self):
        return "name is {},age {} dog ".format(self.name,self.age)

    def work(self):
        print("%s is watching" % self)


class Cat(Animal):

    def __str__(self):
        return "name is {},age {} cat ".format(self.name,self.age)


    def work(self):
        print("%s is catching mouse" % self)


class Person(Animal):
    def __init__(self,name,pets,age=1):
        super(Person,self).__init__(name,age)
        self.pets = pets

    def __str__(self):
        return "name is {},age {} person ".format(self.name,self.age)


    def watch(self):
        print("%s is watching" % self)

    def yangPets(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def make_pets_work(self):
        for pet in self.pets:
            #pet.watch() #小猫没有watch方法 怎么处理 第一种方案 用isinstance()判定实例和类别
            # if isinstance(pet,Dog):
            #     pet.w()
            # else:
            #     pet.catch()
            pet.work()
# p = Person("YZ",pets=[1,2],age=18)
# print(p.__dict__)

d = Dog("blacky",18)
c = Cat("redy",2)
p = Person("YZ",[d,c],32)
p.yangPets()
p.make_pets_work()

# d = Dog("blacky",18)
# print(d.__dict__)  # {'name': 'blacky', 'age': 1} {'name': 'blacky', 'age': 18}
# d.eat()
# d.play()
# d.watch()
#
#
# c = Cat("Mimi",20)
# c.catch()
#
# p = Person("yue",[d,c],32)
# p.yangPets()
# p.make_pets_work()
"""
name is blacky,age 18 dog  is eating
name is blacky,age 18 dog  is playing
name is blacky,age 18 dog  is sleeping
name is redy,age 2 cat  is eating
name is redy,age 2 cat  is playing
name is redy,age 2 cat  is sleeping
name is blacky,age 18 dog  is watching
name is redy,age 2 cat  is catching mouse
"""