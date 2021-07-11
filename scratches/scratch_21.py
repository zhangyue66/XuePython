'''
class Person(object):

    __slots__ = ('_name','_age','_gender')


    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age
person = Person("Ming",48)
#person.is_agy = False
print("%s is %d years old!" % (person.name,person.age))
'''

from math import sqrt

class Triangle(object):

    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
        #self.is_good = False



    @staticmethod
    def is_valid(a,b,c):
        if a+b>c and b+c>a and a+c>b:
            return True
        else:
            return False



    def tri_length(self):
        return self._a+self._b+self._c


    def tri_area(self):
        p = self.tri_length()/2

        return sqrt(p*(p-self._a)*(p-self._b)*(p-self._c))

def main():
    a,b,c = 1,5,9



    if Triangle.is_valid(a,b,c):
        tri = Triangle(a, b, c)

        print(tri.tri_length())
        print(tri.tri_area())
    else:
        print("not a triangle!")



if __name__ == "__main__":
    main()

