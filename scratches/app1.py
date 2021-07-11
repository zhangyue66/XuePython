from Student import Student

student1 = Student("Jim","Business",3.6,False)
student2 = Student("Pam","Art",2.5,True)

print(student1.name,student1.gpa)
print(student2.is_on_probation)

print(student1.on_honor_roll())

class ChineseStuent(Student):
    def make_special_dish(self):
        print("The chef makes orange chickern!")

