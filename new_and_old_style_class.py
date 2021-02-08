class Person:
    pass

print(Person.__bases__)   #<class 'object'>  this is a new style class by default

class Person1(object):
    pass

print(Person1.__base__)



