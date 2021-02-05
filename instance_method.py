class Person:
    def eat(self,food):
        print("eating noodles",food)
        print(self)

    def eat2(self,dick):
        print("yi yang eating my dick",dick)

# p = Person()
# print(p)
# p.eat("hot pot")

# <__main__.Person object at 0x036D2F10>
# eating noodles hot pot
# <__main__.Person object at 0x036D2F10>

#其他调用 使用类调用 知道细节即可
# print(Person.eat)
# Person.eat(123,"abc")

# func = Person.eat
# func(123,"nhh")

p = Person()
p.eat2("yuedick")