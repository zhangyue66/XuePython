# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
#
#
# @log
# def now():
#     print("yue zhang is good!")
#
# now()


import time,functools


def metric(func):
    def wrapper(*args,**kwargs):
        print("%s executed in %s ms " %(func.__name__,"10.24"))
        return func(*args,**kwargs)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

fast_furios = fast(11, 22)
print(":what?")
#s = slow(11, 22, 33)
if fast_furios == 33:
    print('测试失败!')
#elif s != 7986:
   # print('测试失败!')