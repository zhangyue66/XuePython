'''
x = 80
is_on=True
while is_on==True:
    if x >= 5:
        print("yes!")
        break
    else:
        is_on = False
        print("No!")
'''

'''
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
'''


'''
def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
    print("main function is " ,__name__)
'''



def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100







def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200

def yue_zhang():
    yz_name = 'Yue Zhang'
    print(yz_name)
    return yz_name


if __name__ == "__main":
    yue_zhang()


