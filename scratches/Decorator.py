class Person(object):
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

#Decorator property,setter,deleter


    @age.deleter
    def age(self):
        print("deleting values!")
        del self._age




    def play(self):
        if self._age <= 16:
            print("%s is playing chess!" %self._name)
        else:
            print("%s is palying adult game!" %self._name)


def main():
    person = Person("Yue",13)
    person.play()
    person.age = 30
    person.play()

    del person.age

    person.is_gay = False

    print(person.is_gay)

if __name__ == "__main__":
    main()

