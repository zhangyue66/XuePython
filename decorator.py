# def now():
#     print("2021-01-29")
# f = now
# print(now.__name__,f.__name__)

# def log(func):
#     def wrapper(*args,**kwargs):
#         print("call %s():" % func.__name__)
#         return func(*args,**kwargs)
#
#     return wrapper
#
#
#
#
# @log
# def  now():
#
#     print("2021-01-29")
#
# now()

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print("%s %s():" % (text,func.__name__))
            return func(*args,**kwargs)

        return wrapper
    return decorator

@log("execute")
def now():
    print("2020-01-30")

now()
print(now.__name__)  # function now's name changed to wrapper . not now anymore . introduce fucntools.wraps

#before

# execute now():
# 2020-01-30
# wrapper

# after introduce wraps(func)

# execute now():
# 2020-01-30
# now


#########Exercise#######################


