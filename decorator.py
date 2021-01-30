# def now():
#     print("2021-01-29")
# f = now
# print(now.__name__,f.__name__)

def log(func):
    def wrapper(*args,**kwargs):
        print("call %s():" % func.__name__)
        return func(*args,**kwargs)

    return wrapper




@log
def  now():

    print("2021-01-29")

now()

