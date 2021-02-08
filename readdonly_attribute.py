# python name mangling , so there is no real Private attribute. use the __dict__ method to change the value

#p.__dict__["_Person__age""] = 999 can change the value easily

# now introduce the 2nd usage of read only attribute


class Person:

    def __setattr__(self, key, value):
        print(key,value)

        if key == "age" and key in self.__dict__.keys():
            print("this attribute is readonly, can not set value")
        else:
            #self.key = value  -> this is wrong. will cause inf loop
            self.__dict__[key] = value

p1 = Person()
p1.age = 18
p1.name = "sz"
p1.age = 999
print(p1.age)
print(p1.__dict__)