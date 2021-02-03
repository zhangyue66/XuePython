# class Person:
#     pass
#
#
# p1 = Person()
# p2 = Person()
#
# #add attribute
# # p.age = 18
# # p.height = 180
# # p.age = 123
# # #verify if age added
# # print(p.age)
# # #print(p.__dict__)
# # print(p.sex)
#
# # p.pets = ["cat","dog"]
# # print(p.pets,id(p.pets))
# #
# # p.pets.append("snake")
# # del p.pets
# # print(p.pets,id(p.pets))
#
# p1.age = 18
# p2.address = "seattle"
# print(p1.address)


# class Money:
#     age = 18
#     count = 1
#     num = 666
#
# one = Money()
# two = Money()
#
# print(one.age)
# print(two.age)
#
# Money.age = 20
#
# print(one.age)
# print(two.age)
#
# # del Money.age
# del one.age
# print(Money.age)
# print(one.age)


# class Person:
#     age = 10
# # Person.age = 19
# # Person.age = 11
# # del Person.age
# # Person.age
# #
# #
# p = Person()
# # p.age = 18
# # p.age = 11
# # del p.age
# # p.age
# p.age += 5
# print(Person.age)
# print(p.age)


class Person:
    __slots__ = ["age"]
    pass

p1 = Person()
p1.age = 1

print(p1.age)
p1.num = 2
print(p1.num)


p2 = Person()