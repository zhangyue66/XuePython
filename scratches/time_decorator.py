# from decorators import decorator
#
# @decorator
# def yz_first_dec(name):
#     print("this is a server for %s and great!" %name)
#     for i in range(9):
#         print("yue loves Lingzi!")
#     return True
#
#
# yz_first_dec("Lingzi")

#
# import functools
# import time
# import os
# from random import randint
#
# def timer(func):
#
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         #sleep(randint(1,10))
#         time.sleep(randint(1,10))
#         end_time = time.time()
#         print("over!")
#         print("cost time is %d" %(end_time-start_time))
#     return wrapper
#
#
#
# @timer
# def function_running(name):
#     for i in range(name):
#         sum(i^2+i*i)
#
#
#
# function_running(10000)
import functools
import time

def timer(func):

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        yz = sum([i**2 for i in range(10000)])
    return yz*num_times

waste_some_time(2)
print(waste_some_time(10))

waste_some_time(4)
print(waste_some_time(1))