class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_subject):
        print("%s is studying %s !" %(self.name,course_subject))


    def watch_movie(self):
        if self.age <18:
            print("%s can only watch cartoon" %(self.name))
        else:
            print(" %s can watch JAV !" %(self.name))







def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()