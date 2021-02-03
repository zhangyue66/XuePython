

def eat():
    print(1)
    print(2)
    print(3)

#eat()

class Person:
    def eat2(self):#  METHOD
        print("this is a instance mehod",self)


    @classmethod
    def leifangfa(cls):
        print("this is a class method",cls)

    @staticmethod
    def jingtaifangfa():
        print("this is a static method")

p = Person()
print(p.__dict__)
print(Person.__dict__)

def run():
    print("run")

p.age = run

print(p.__dict__)
#p = Person()
# print(p)
# p.eat2()

#Person.leifangfa()

Person.jingtaifangfa()

