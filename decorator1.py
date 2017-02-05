#装饰器

# def now():
#     print("2016-12-27")
#
# f = now
#
# f()
#
# print(now.__name__)
#
# print(f.__name__)

# def log(func):
#     def wrapper(*args,**kwargs):
#         print("call %s():"% func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# @log
# def now():
#     print("2016-12-27")
#
# now()
#高阶版本
# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             print("%s %s():"%(text,func.__name__))
#             return func(*args,**kwargs)
#         return wrapper
#     return decorator
#
# @log("execute")
# def now():
#     print("2016-12-27")
#
# now()
# print(now.__name__)

# import functools
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("call %s():" %func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# a = log("execute")
#
# print(a.__name__)

# def log(func):
#     def wrapper(*args,**kwargs):
#         print("this is before wrapper")
#         c = func(*args,**kwargs)
#         print("this is after wrapper")
#         return c
#     return wrapper
#
# @log("execute")
# def f():
#     print("this is f()")
#
# print(f())

# import functools
#
# def log(par = None):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             if par:
#                 print('-----%s %s-----' % (par, func.__name__))
#             else:
#                 print('-----begin call-----')
#             func(*args,**kwargs)
#             print('-----end call-----')
#         return wrapper
#     return decorator
#
# @log("execute")
# def now1():
#     print("2016-12-27")
#
# @log()
# def now2():
#     print("2016-12-26")
#
# print(now1())
# print(now2())

import functools

def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                print("begin call %s %s():"%(text,func.__name__))
                func(*args,**kwargs)
                print("end call %s %s():"%(text,func.__name__))
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args,**kwargs):
            print("begin call %s():",text())
            text(*args,**kwargs)
            print("end call %s():",text())
        return wrapper

@log("execute")
def f1():
    print("this is f1()")

@log
def f2():
    print("this is f2()")

print(f1())
print(f2())



















