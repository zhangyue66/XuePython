class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("Last name"+self.last_name)
        print("eye color" + self.eye_color)


class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Childer constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

   # def show_info(self):
        #print("Last name" + self.last_name)
        #print("eye color" + self.eye_color)
        #print("number of toys is "+ str(self.number_of_toys))




#biley_cyrus = Parent("Cyrus","balck")
miley_cyrus = Child("Cyrus","black",5)
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()