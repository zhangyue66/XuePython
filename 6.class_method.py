class Person:
    @classmethod
    def run(cls,a):
        print("this is a class method",cls,a)

Person.run(123)

p = Person()

p.run(666)

# this is a class method <class '__main__.Person'> 123
# this is a class method <class '__main__.Person'> 666  -> check official bulletin of classmethod

func = Person.run

func(111)

#derived class

class A(Person):
    pass

A.run(888)

#this is a class method <class '__main__.A'> 888