
class Person:
    """
    this is a Class for Person
    """
    age = 19

    def __init__(self):
        self.name = "yz"

    def run(self):
        print("run")

Test = Person

t = Test()
print(Person.__dict__)
print(Person.__bases__)
print(Person.__doc__)

print(Person.__name__)
print(Person.__module__)


#实例属性

p = Person()
print(p.__class__)
