def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()

# ask function to return function

# def parent(num):
#     def first_child():
#         return "Hi,I am yz1!"
#
#     def second_child():
#         return "Hi,i am yz2!"
#
#     if num ==1:
#         return first_child
#     else:
#         return second_child
#
#
# print(parent(2))
#
# first = parent(1)
# second = parent(2)
#
# print(first())

# def my_decorator(func):
#     def wrapper():
#         print("before!")
#         func()
#         print("after!")
#     return wrapper
#
# def say_whee():
#     print("WHEE!")
#
# say_whee = my_decorator(say_whee)
#
# say_whee()

#
# from datetime import datetime
#
# def not_during_night(func):
#     def wrapper(*args, **kwargs):
#         if 7 <= datetime.now().hour < 12:
#             func()
#
#         else:
#             print("silent!shhhhh")
#             pass
#     return wrapper
#
# @not_during_night
# def say_whee(name):
#     print("Whee!!!")
#
#
# # say_whee = not_during_night(say_whee)
# #
# # say_whee()
#
#
# say_whee("yz")


import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

#a = return_greeting("admin")

#print(a)

return_greeting

return_greeting.__name__

help(return_greeting)


