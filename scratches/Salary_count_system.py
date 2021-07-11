#design a salary system use abc.ABCMeta and abstractmethod

#Manager 15000,Developer 200/hour ,Salesman 1800 base + 5% sale count

from abc import ABCMeta,abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        #how to get salary depending on different people
        pass



class Manager(Employee):
    def get_salary(self):
        return 15000.0


class Developer(Employee):

    def __init__(self,name,working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)


    def get_salary(self):
        return 200.0*self.working_hour


class Salesman(Employee):
    def __init__(self,name,sale_amount,base_salary=1990.0):

        self.base_salary = base_salary
        self.sale_amount = sale_amount
        super().__init__(name)

    def get_salary(self):
        return self.base_salary+self.sale_amount*0.05



class EmployeeFactory():
    @staticmethod
    def create(emp_type,*args,**kwargs):
        emp_type = emp_type.upper()
        emp= None
        if emp_type == "M":
            emp = Manager(*args,**kwargs)
        elif emp_type == "D":
            emp = Developer(*args,**kwargs)
        elif emp_type == "S":
            emp = Salesman(*args,**kwargs)
        return emp




def main():
    emp = [
        EmployeeFactory.create("M","Yue"),
        EmployeeFactory.create("D","Lingzi",100),
        EmployeeFactory.create("D","Lingwa",60),
        EmployeeFactory.create("S","Fangfang",1800000,1990)
    ]
    for emp1 in emp:
        print("%s:%.2f dollar" %(emp1.name,emp1.get_salary()))


if __name__ == "__main__":
    main()