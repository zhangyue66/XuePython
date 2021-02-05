class Person:
    """
    关于类的描述，类的作用，类的构造函数等等
    """
    #这是人的个数
    count = 1

    def run(self,distance,step):
        """
        这个方法的作用效果
        :param distance: 类型int，default = 0
        :param step: 类型int，default = 1
        :return: float类型
        """
        print("a man is running ")
        return distance*step

help(Person)

"""
class Person(builtins.object)
 |  关于类的描述，类的作用，类的构造函数等等
 |  
 |  Methods defined here:
 |  
 |  run(self, distance, step)
 |      这个方法的作用效果
 |      :param distance: 类型int，default = 0
 |      :param step: 类型int，default = 1
 |      :return: float类型
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  count = 1

"""

def xxx(a,b,c):
    """

    :param a:
    :param b:
    :param c:
    :return:  int , sum of a b c
    """
    return a*b+c
"""
python3 -m pydoc 类的描述 -h
python3 -m pydoc -k 类 搜索含有类的module
python3 -m pydoc -p 1234 #open port 1234 as http server ,including documents
python3 -m pydoc -w decorator.html # write out to .html file
"""