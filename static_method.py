
#
# l =[1,4,3,2]
# list.sort(l)
# print(l)
# l.sort()

class Person:
    @staticmethod
    def jingtai():
        print("this is a static method")


Person.jingtai()

p = Person()

p.jingtai()

func = Person.jingtai

func()
