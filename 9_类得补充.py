
num = 10

print(num.__class__)

s = "abc"

print(s.__class__)

class Person:
    pass

p = Person()
print(p.__class__)


print("-"*20)

print(int.__class__)

print(str.__class__)

print(Person.__class__)

# <class 'type'>   -> Metaclass type实例化int  int实例化10
# <class 'type'>
# <class 'type'>



#创建类得方法
def run(self):
    print(self)
xxx = type("dog",(),{"count":0,"run":run})
print(xxx)   #<class '__main__.dog'>

print(xxx.__dict__)


d = xxx()
print(d) #<__main__.dog object at 0x03FA2FB8>

d.run()


